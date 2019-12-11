import concurrent.futures
import time

def thread1():
    print("Thread 1 started")
    time.sleep(10)
    print("Thread 1 ended")

def thread2():
    print("Thread 2 started")
    time.sleep(4)
    print("Thread 2 ended")


print("Main start")

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
  executor.submit(thread1)
  executor.submit(thread2)

print("Main end")

