from threading import Thread, Event, Lock
from math import fabs
from time import sleep

event = Event()

lock = Lock()

stop_thread = False

def func(x: float, eps: float, T: int):
    i: int = 0
    result: float = 0
    iterations: int = 0
    cicle_exp: bool = True
    prev: int = 0
    
    while cicle_exp:
        if iterations % T == 0:
            event.set()
            
        prev = result    
        result += (-1 ** (i + 1)) * ((2 * x) / (3 * i + 2))
        i += 1
        cicle_exp = fabs(result - prev) > eps
        iterations += 1
        
        if iterations % T == 0:
            event.wait()
            print(f'x = {x} | ({iterations}, {result})')
            # sleep(5)
            
        if stop_thread:
            break
    
    print(result)
        
if __name__ == '__main__':
    S: int = 10 
    
    t1 = Thread(target=func, args=(0.3, 0.0000000001, 3,))
    t2 = Thread(target=func, args=(0.5, 0.0000000001, 9,))
    t1.start()
    t2.start()
    
    sleep(S)
    
    if t1.is_alive() or t2.is_alive():
        lock.acquire()
        stop_thread = True
        lock.release()