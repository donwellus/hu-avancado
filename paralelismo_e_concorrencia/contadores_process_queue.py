from multiprocessing import Process, JoinableQueue, current_process
from time import time, sleep

def generate_counter(q, name, n):
    for i in range(n):
        q.put([f'{current_process().name}', i])
        sleep(0.01)

def retrieve_counter(q):
    while True:
        print(f'{current_process().name}', q.get(True, 5))
        sleep(0.01)
        q.task_done()

if __name__ == '__main__':
    print('Criando processs')
    q = JoinableQueue()
    n = 10
    n_producers = 10
    n_consumers = 10

    consumers = [
        Process(target=retrieve_counter, args=[q])
        for _ in range(n_consumers)
    ]

    producers = [
        Process(target=generate_counter, args=[q, f'Serie-{i}', n])
        for i in range(n_producers)
    ]

    elapsed = time()
    for p in consumers:
        p.start()

    for p in producers:
        p.start()

    for p in producers:
        p.join()

    q.join()

    for p in consumers:
        p.terminate()

    # r.join()
    # while not q.empty():
    #     print('not yet')
    #     pass

    print(f'Process time:', time()-elapsed)

    print('fim')