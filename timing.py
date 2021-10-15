import time

def calculate_time(func):
    def wrapper():
        task=time.time()
        func()
        print("Total time ", time.time()-task)
        
    return wrapper
