import threading
import time


d = [2, 4]


def loop(num, des):
    for y in range(3):
        print(f"loop{num} 间隔 {des}s {time.ctime()}")
        time.sleep(des)


tloop = []


for i in range(d.__len__()):
    tloop.append(threading.Thread(target=loop, args=(i, d[i])))

for j in tloop:
    j.start()

for x in tloop:
    x.join()
