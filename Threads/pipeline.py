import threading

class Pipeline:

  def __init__(self):
    self.message = 0
    self.producer_lock = threading.Lock()
    self.consumer_lock = threading.Lock()
    self.consumer_lock.acquire()

  def get_message(self, name):
    self.consumer_lock.acquire()
    message = self.message
    self.producer_lock.release()
    return message

  def set_message(self, message, name):
    self.producer_lock.acquire()
    self.message = message
    self.consumer_lock.release()
