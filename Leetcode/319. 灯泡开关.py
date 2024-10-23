import math


def bulb_switch(n: int):
    y = int(math.sqrt(n))
    return y


if __name__ == "__main__":
    n = 120
    x = bulb_switch(n)
    print(x)
