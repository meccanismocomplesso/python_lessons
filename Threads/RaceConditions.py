import concurrent.futures
import time

class FakeDatabase:
  def __init__(self):
    self.value = 0

  def update(self, name):
    print("Thread ", name , "is reading the DB value")
    local_copy = self.value
    local_copy += 1
    time.sleep(0.1)
    self.value = local_copy
    #self.value = name
    print("Thread ", name ,"has modified the DB value")


database = FakeDatabase()

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
  for index in range(3):
    executor.submit(database.update, index+1)

print("DB Value is ", database.value)