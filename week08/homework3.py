from functools import wraps
import datetime
import time

def timer(func):
    @wraps(func)
    def incr(*args,**kwargs):
        runbefore = datetime.datetime.now()
        rfunc = func(*args,**kwargs)
        runafter = datetime.datetime.now()
        total_seconds = (runafter - runbefore).total_seconds()
        mins = round(total_seconds/60, 3)
        print('start run at %s , end at %s, total mins %s' %(runbefore,runafter,mins))
        return rfunc
    return incr

@timer
def runtime_test(t):
    time.sleep(t)
    print('test for timer')

if __name__ == '__main__':
    runtime_test(10)