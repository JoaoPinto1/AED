import time
import random
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np


def main():
    x = range(25000,125001,25000)
    y = []
    for i in x:
        array = [random.randint(0,1000000) for c in range(i)]
        start = time.time()
        if array[0] > array[1]:
            maximo = array[0]
            minimo = array[1]
        else:
            maximo = array[1]
            minimo = array[0]
        for a in range(2, i):
            if array[a] < minimo:
                minimo = array[a]
            if array[a] > maximo:
                maximo = array[a]
        print(maximo - minimo)
        end = time.time()
        y.append(end-start)
        print(end-start)
    model = np.polyfit(x, y, 1)
    predict = np.poly1d(model)
    print(r2_score(y, predict(x)))
    xl = range(20000,130000)
    yl = predict(xl)
    plt.scatter(x, y)
    plt.plot(xl, yl)
    plt.show()
    return 0


if __name__ == "__main__":
    main()
