import time

def timestamp(func):
    def wrapper(*args, **kwargs):       #allows u to pass multiple arg/keywords to function
        print(time.ctime())
        result = func(*args, *kwargs)
        return result
    
    return wrapper