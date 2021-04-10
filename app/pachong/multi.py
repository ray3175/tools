import os
import multiprocessing


cpu_count = os.cpu_count()


def multi_run(func, list_args, global_args):
    semaphore = multiprocessing.Semaphore(cpu_count)
    p_pool = [multiprocessing.Process(target=func, args=(_list, global_args, semaphore)) for _list in list_args]
    p_number = len(p_pool)
    print(f"准备启动多进程，本次将共启动{p_number}个子进程！")
    for p in p_pool:
        p.start()
    for p in p_pool:
        p.join()
    return True
