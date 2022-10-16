
def rd(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return round(value, 2)
    return wrapper
