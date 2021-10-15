import time

def calculate_time(func):
    def wrapper():
        task=time.time()
        # Inputs a time in seconds for the task involved
        func()
        print("Total time ", time.time()-task)
        
    return wrapper
