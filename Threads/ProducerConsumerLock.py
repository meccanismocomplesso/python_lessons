import random
import concurrent.futures
from pipeline import Pipeline
import time

END = object()

def producer(pl):
  for index in range(10):
    time.sleep(random.randint(1,11))
    message = random.randint(1, 101) 
    print("Producer received data: ", message, " (", index+1, " of 10 )")
    pl.set_message(message, "Producer")
  pl.set_message(END, "Producer")


def consumer(pl):
    message = 0
    while message is not END:
        message = pl.get_message("Consumer")
        if message is not END:
            time.sleep(random.randint(1,11))
            print("Consumer stored data: ", message)

pl = Pipeline()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
  executor.submit(producer, pl)
  executor.submit(consumer, pl)

