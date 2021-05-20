import threading
import time
"""使用线程锁，对文件读写进行保护"""

def readt(lock):
    lock.acquire(True)
    with open('lock_test.txt', 'r') as f:
        while True:
            line = f.readline()
            if line == "":
                break
            print(f"读取：{line}")
            time.sleep(2)
    f.close()
    lock.release()
    # with open('lock_test.txt', 'r') as f:
    #     while True:
    #         line = f.readline()
    #         if line == "":
    #             break
    #         print(f"读取：{line}")
    #         time.sleep(2)
    # f.close()


def writet(lock):
    # if lock.acquire(True):
    #     with open('lock_test.txt', 'w') as f:
    #         for i in range(3):
    #             t = time.ctime()
    #             f.write(f"{t} \n")
    #             print(f"写入：{t}")
    #             time.sleep(1)
    #     f.close()
    #     lock.release()
    lock.acquire()
    with open('lock_test.txt', 'w') as f:
        for i in range(3):
            t = time.ctime()
            f.write(f"{t} \n")
            print(f"写入：{t}")
            time.sleep(1)
    f.close()
    lock.release()

tloop = []
mu = threading.Lock()
tloop.append(threading.Thread(target=readt, args=(mu,)))
tloop.append(threading.Thread(target=writet, args=(mu,)))

for j in tloop:
    j.start()

for x in tloop:
    x.join()


