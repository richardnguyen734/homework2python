def tripler(func):
    def wrapper(*args, **kwargs):

        output=func(*args, **kwargs)
        output=func(*args, **kwargs)
        output=func(*args, **kwargs)
        return output
    return wrapper
