import requests
import hashlib
from typing import Union
from bisect import bisect, bisect_left, bisect_right
from matplotlib import pyplot


class StorageNode:
    def __init__(self, name=None, host=None) -> None:
        self.name = name
        self.host = host

    def fetch_file(self, path):
        return requests.get(f'https://{self.host}:1231/{path}').text

    def put_file(self, path):
        with open(path, 'r') as fp:
            content = fp.read()
            return requests.post(f'https://{self.host}:1231/{path}', body=content).text


storage_nodes = [
    StorageNode(name='A', host='239.67.52.72'),
    StorageNode(name='B', host='137.70.131.229'),
    StorageNode(name='C', host='98.5.87.182'),
    StorageNode(name='D', host='11.225.158.95'),
    StorageNode(name='E', host='203.187.116.210'),
]


def hash_fn(key):
    return sum(bytearray(key.encode('utf-8'))) % 5


def hash_fn_complex(key: str, total_slots: int) -> int:
    hsh = hashlib.sha256()
    # converting data to bytes and passing to hash fn
    hsh.update(bytes(key.encode('utf-8')))
    return int(hsh.hexdigest(), 16) % total_slots


def upload(path):
    index = hash_fn(path)  # we get the index to find the server
    node = storage_nodes[index]
    return node.put_file(path)


def fetch(path):
    index = hash_fn(path)
    node = storage_nodes[index]
    return node.fetch_file(path)


for file in ['f1.txt', 'f2.txt', 'f3.txt', 'f4.txt', 'f5.txt']:
    print(
        f'file{file} resides on the node {storage_nodes[hash_fn(file)].name}')


class ConsistentHash:
    def __init__(self) -> None:
        self._keys = []  # indices taken up in the ring
        self.nodes = []  # nodes present in the ring. nodes[i] is present at index keys[i]
        self.total_slots = 50

    def __repr__(self):
        return str(self)

    def add_node(self, node: StorageNode) -> int:
        if len(self._keys) == self.total_slots:
            raise Exception("hash space is full")

        key = hash_fn_complex(node.host, self.total_slots)
        print(f'key for the new node is {key}')
        index = bisect(self._keys, key)
        print(f'index for the new node is {index}')

        if index > 0 and self._keys[index-1] == key:
            raise Exception("collision occurec")

        self.nodes.insert(index, node)
        self._keys.insert(index, key)

        return key

    # def plot(self, item: str = None, node: StorageNode = None) -> None:
    #     pyplot.(
    #         self.total_slots,
    #         self._keys,
    #         self.nodes,
    #         item_key=hash_fn(item, self.total_slots) if item else None,
    #         node_key=hash_fn(node.host, self.total_slots) if node else None,
    #     )


ch = ConsistentHash()

for node in storage_nodes:
    ch.add_node(node)
print(ch._keys)
# ch.plot()
