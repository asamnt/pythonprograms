items = ['amit', 'paddy','mandy','ramesh']

for item in items:
    print('Item is : {}'.format(item) )

#using enumerate
for (i,item) in enumerate(items):
    print('Item {} is {}'.format(i,item))