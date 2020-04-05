from time import sleep
from functools import wraps


def my_cache(func):

    cache = dict()

    @wraps(func)
    def my_cache_(*args, **kwargs):
        key = hash(tuple((sorted(kwargs.items(), key=lambda t: t[0]))))
        if key in cache:
            return cache[key]
        else:
            res = func(*args, **kwargs)
            cache[key] = res
            print(res)
            return res

    return my_cache_


@my_cache
def count(a, *x, z=10):
    x = list(x)
    x.append(z)
    x.append(a)
    return x


def main():
    count("kek", z=10)
    count(1, 2, 3, 4, 5)
    count(1, 2, 3, 4, 5, z=6)
    count(1)
    count(1, z=10)


if __name__ == '__main__':
    main()
