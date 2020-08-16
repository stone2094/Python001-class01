def my_map1(func, *iterables):
    try:
        length = len(iterables[0])
        print(length)
        for i in range(length):
            yield(func(*[iterables[i] for iterable in iterables]))

    except TypeError:
        raise

    except IndexError:
        pass

    else:
        pass

def my_map2(func, *iterable_obj):
    try:
        if len(iterable_obj) == 1:
            for i in iterable_obj:
                yield func(i)
        else:
            for args in zip(*iterable_obj):
                yield func(*args)

    except TypeError:
        print('error: obj must be iterable')

def square(x) : 
    return x ** 2

if __name__ == '__main__':
   
    mp1 = my_map2(square, [1,2,3,4,5])
    list(mp1)
    mp2 = my_map1(lambda x: x ** 2, [1, 2, 3, 4, 5])
    print(mp2)
    mp3 = my_map1(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    print(mp3)
