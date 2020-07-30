import time
import multiprocessing

def something():
    print('Sleeping for 1 Second..\n')
    time.sleep(1)
    print('Done with sleeping\n')

if __name__ ==  '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=something)
    p2 = multiprocessing.Process(target=something)
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    
    
    print(f'{finish - start} second(s)')