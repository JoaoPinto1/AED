import time
import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score


def main():
    x = range(25000,125001,25000)
    y = []
    for i in x:
        array = [random.randint(0, 1000000) for c in range(i)]
        aux = 0
        start = time.time()
        for b in range(i):
            for a in range(b, i):
                if b != a:
                    res = abs(array[b] - array[a])
                    if res > aux:
                        aux = res
        end = time.time()
        y.append(end-start)
        print(aux)
        print(end-start)
    model = np.polyfit(x, y, 1)
    predict = np.poly1d(model)
    print(r2_score(y, predict(x)))
    xl = range(20000, 130000)
    yl = predict(xl)
    plt.scatter(x, y)
    plt.plot(xl, yl)
    plt.show()


if __name__ == "__main__":
    main()
