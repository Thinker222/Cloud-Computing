# This a test file for cloud computing. 

def factorio(x):
    if x <= 1:
        return x
    else:
        return x * factorio(x - 1)


def add_all(x):
    if x <= 1:
        return x
    else:
        return x + add_all(x - 1)


def main():
    x = 2
    y = 4
    z = 3
    print((x + y) / z)
    v = [factorio(var) for var in range(100) if var % 2 == 0]
    print(v)
    print('yeet')
    
   

if '__main__':
    main()
