def division(a,b):
    return a/b


def decorator_fuction(func):
    def smart_inner_function(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return smart_inner_function


smart_division = decorator_fuction(division)
print(smart_division(4,8))
