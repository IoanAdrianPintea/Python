def ex_0332():
    n = int(input())
    suma = 0
    for i in range(1, n + 1):
        suma += i * (i + 1)
    print("Rezultatul este", suma)


if __name__ == '__main__':
    ex_0332()
