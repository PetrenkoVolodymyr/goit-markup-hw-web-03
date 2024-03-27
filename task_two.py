from time import time
from multiprocessing import Pool, Process, Manager, cpu_count



def factorize(*number):
    total_list = []
    for i in number:
        local_list = []
        for j in range(1, i+1):
            if i % j == 0:
                local_list.append(j)
        total_list.append(local_list)
    return total_list


def factorize1(figure, val: Manager):
    local_list = []
    for j in range(1, figure+1):
        if figure % j == 0:
            local_list.append(j)
    val.append(local_list)

def worker(figure):
    local_list = []
    for j in range(1, figure+1):
        if figure % j == 0:
            local_list.append(j)
    return local_list


if __name__ == '__main__':
    list_to_check = (128, 255, 99999, 10651060)

    print('СИНХРОННЕ ВИКОНАННЯ:')
    timer = time()
    print (factorize(128, 255, 99999, 10651060))
    print (f'Синхронний час: {time() - timer}\n')


    print('АСИНХРОННЕ ВИКОНАННЯ №1:')
    timer = time()
    with Manager() as manager:
        m = manager.list()
        processes = []
        for figure in list_to_check:
            pr = Process(target=factorize1, args=(figure, m))
            pr.start()
            processes.append(pr)

        [pr.join() for pr in processes]
        print(m)
    print (f'Асинхронний час1: {time() - timer}\n')


    print('АСИНХРОННЕ ВИКОНАННЯ №2:')
    timer = time()
    with Pool(cpu_count()) as pool:
        print(pool.map(worker, list_to_check))
    print (f'Асинхронний час2: {time() - timer}\n')