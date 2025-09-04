

import time

def tictoc(func):

    

    def wrapper():

        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f'it took {func.__name__} {t2} seconds to run')

    return wrapper

@tictoc
def doThis():
    time.sleep(1.3)

@tictoc
def doThat():
    time.sleep(.4)

doThis()
doThat()