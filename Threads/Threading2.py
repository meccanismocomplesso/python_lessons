import time
from threading import Thread

def test(i):
    print("thread ", i, " started")
    time.sleep(10)
    print("thread ", i, " ended")

for i in range(5):
    t = Thread(target=test, args=(i,), daemon=False)
    t.start()
print("End Process")
