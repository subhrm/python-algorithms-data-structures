""" 
decorator =  a function that takes another function as an argument and returns a function
"""

def log_every_call(n):

    # Inner function
    def wrapper(*args, **kwargs):
        print(f'Calling {n.__name__} with arguments {args} & {kwargs}')
        return n(*args, **kwargs)

    # return the wrapper (inner function)
    return wrapper


@log_every_call
def add(x,y):
    return x+y

# print(add.__name__)
# log_add = log_every_call(add)
# print(log_add(5,6))

print(add(5,6))
