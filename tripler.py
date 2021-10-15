def tripler(func):
    def wrapper(*args, **kwargs):

        output=func(*args, **kwargs)
        output=func(*args, **kwargs)
        output=func(*args, **kwargs)
        # Puts the output 3 times rather than 1 normally
        return output
    return wrapper
