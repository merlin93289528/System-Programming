from threading import Thread, Lock
from time import sleep
from math import fabs

lock = Lock()

stop_thread = False

def func(x: float, eps: float, T: int):
    i: int = 0
    result: float = 0
    iterations: int = 0
    cicle_exp = True
    prev = 0
    while cicle_exp:
        prev = result    
        result += (-1 ** (i + 1)) * ((2 * x) / (3 * i + 2))
        i += 1
        cicle_exp = fabs(result - prev) > eps
        iterations += 1
        
        if iterations % T == 0:
            print(f'({iterations}, {result})')
        
        if stop_thread:
            break
    print(f'Результат {result}')
            
if __name__ == '__main__':
    x: float = 0.5
    eps: float = 0.00000001
    T: int = 3
    S: int = 2 
    
    th1 = Thread(target=func, args=(x, eps, T,))
    th1.start()
    
    sleep(S)
    
    if th1.is_alive():
        lock.acquire()
        stop_thread = True
        lock.release()
    