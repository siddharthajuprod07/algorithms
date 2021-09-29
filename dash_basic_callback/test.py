

def repeat(number_times):
    def func2(another_function):

        def wrapper_function(*args, **kwargs):
            print("The activities before calling {}".format(another_function))
            for i in range(number_times):
                another_function(*args, **kwargs)
            print("The activities after calling {}".format(another_function))
        
        return wrapper_function
    return func2

@repeat(number_times=2)
def func1(name):
    print("Hello {}, from func1".format(name))


#func1 = func2(func1)

func1("Sid")