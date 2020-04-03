from time import sleep


def my_cache(func):
    cache = dict()

    def my_cache_(*args, **kwargs):
        keys = list(args)
        keys.extend(kwargs.values())
        sorted(keys)
        key = hash(tuple(keys))
        if key in cache:
            return cache[key]
        else:
            res = func(*args, **kwargs)
            cache[key] = res
            return res

    return my_cache_


@my_cache
def count(a, *x, z=10):
    sleep(2)
    x = list(x)
    x.append(z)
    x.append(a)
    return sum(x)


def main():
    count(1, 2, 3, 4, 5)
    count(1, 2, 3, 4, 5)
    count(1, 2, 3, 4, 5, z=6)
    count(1)
    count(1, z=10)


if __name__ == '__main__':
    main()
