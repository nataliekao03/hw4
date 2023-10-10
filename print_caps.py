def allcaps(func):
    def wrapper():
        result = func()
        if isinstance(result, str):
            return result.upper()
        else:
            raise TypeError("Function must return a string")
    
    return wrapper

# Example of how to use the decorator:
# @allcaps
# def greet():
#     return "hello, world!"

# When you call greet(), it will return "HELLO, WORLD!"
