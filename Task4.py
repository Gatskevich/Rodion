from time import sleep

def my_cache(func):
    cache = dict()
    def my_cache_(*args, **my_Z):
        key = list(args)
        key.extend(my_Z.values())
        key = hash(tuple(key))
        if key in cache:
            #print(cache[key])
            return cache[key]
        else:
            res = func(*args, **my_Z)
            cache[key] = res
            #print(cache[key])
            return res

    return my_cache_
@my_cache
def count(a,*x, z = 10):
    sleep(2)
    x = list(x)
    x.append(z)
    x.append(a)
    return sum(x)


def main():
    count(1,2,3,4,5)
    count(1,2,3,4,5)
    count(1,2,3,4,5, z=6)
    count(1)
    count(1, z=10)

if __name__ == '__main__':
    main()