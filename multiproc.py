from multiprocessing import Pool

def square(x):
    return x*x


if __name__ == '__main__':

    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print('Dataset ' + str(dataset))

    agents = 5
    chunksize = 3
    with Pool(processes=agents) as pool:
        result = pool.map(square,dataset,chunksize)
    
    print('Result ' + str(result))