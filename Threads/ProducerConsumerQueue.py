import random
import concurrent.futures
import threading
import queue

def producer(queue, event):
  while not event.is_set():
    message = random.randint(1, 99) 
    print("Producer received data: ", message)
    queue.put(message)


def consumer(queue, event):
    message = 0
    while not event.is_set() or not queue.empty():
      message = queue.get()
      print("Consumer stored : ", message, " (queue size=",queue.qsize(), ")")

pl = queue.Queue(maxsize=10)
event = threading.Event()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
  executor.submit(producer, pl, event)
  executor.submit(consumer, pl, event)
  event.set()

