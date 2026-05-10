def add(a, b, c):
    return a + b + c

def partial_apply(func, *preset_args):
    def wrapper(*new_args):
        return func(*preset_args, *new_args)  
    return wrapper


add_5 = partial_apply(add, 5)     
print(add_5(3, 2))                

add_5_3 = partial_apply(add, 5, 3) 
print(add_5_3(2))               