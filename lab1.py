from multiprocessing import *
from time import sleep

def process1_func(sleep_time):
    sleep(sleep_time)
    return 'stop'    

def process2_func():
    while True:
        sleep(0.1)    

def process3_func():
    while True:
        sleep(0.1)
        
if __name__ == '__main__':
    FIRST_PROCESS_WORK_TIME = 7

    process1 = Process(target=process1_func, args=(FIRST_PROCESS_WORK_TIME,), daemon=True)
    process2 = Process(target=process2_func, daemon=True)
    process3 = Process(target=process3_func, daemon=True)
    
    print('Запуск всіх процесів...')
    process1.start()
    process2.start()
    process3.start()

    print('Очікуємо 10 секунд...')
    sleep(10)
    print('Перевірка стану першого процесу...')
    if process1.exitcode == 0:
        print('Перший процес завершено за десять секунд')
        print('Завершуємо другий процес')
        process2.terminate()
        sleep(10)
        print('Завершуємо третій процес')        
        process3.terminate()
    else:
        print('Перший процес НЕ завершено за десять секунд')
        print('Завершуємо всі процеси')
        process1.terminate()
        process2.terminate()
        process3.terminate()