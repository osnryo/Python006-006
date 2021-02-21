# 记录函数的运行时间，注意需要考虑函数可能会接收不定长参数
def timer(func):
    def func_wrapper(*args,**kwargs):
        from time import time
        time_start = time()
        result = func(*args,**kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print('\n{0} cost time {1} s\n'.format(func.__name__, time_spend))
        return result
    return func_wrapper

@timer
def test():
	print("hello world!")