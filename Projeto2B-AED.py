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
        array.sort()
        print(array[i - 1] - array[0])
        end = time.time()
        print(end-start)
        y.append(end-start)
    model = np.polyfit(x, y, 1)
    predict = np.poly1d(model)
    print(r2_score(y, predict(x)))
    xl = range(20000, 130000)
    yl = predict(xl)
    plt.scatter(x, y)
    plt.plot(xl, yl)
    plt.show()
    return 0


if __name__ == "__main__":
    main()
