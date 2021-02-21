'''
map() 函数会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
'''


# function -- 函数
# iterable -- 一个或多个序列

# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
def newMap(func, *iterators):
    res = []
    # *seqs 相当于拆解成 list1,list2,...,listN
    for args in zip(*seqs):
        # zip 之后， args 其实是一个元组
        print(args)
        # *args 相当于拆解成 e1,e2,...,eN ,也就是 func(e1,e2,...,eN)
        res.append(func(*args))
    return res