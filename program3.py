'''
# thread bsed multi tasking in single program multipe program independently
import threading
# internally one thread is present that thred name is main thread
print(threading.current_thread().getName())
threading.current_thread().setName("python")
print(threading.current_thread().getName())
# in multi threading we cant guess the output

# without creating any class
# wirhout extendibng thread vlass
# with extending htread class
'''
'''
from threading import *
class Test:
    def span(self):
        for i in range(1,11):
            print("chlid thread")
t=Test()
x=Thread(target=t.span())
for i in range (1,11):
    print("thread")
'''
'''
def span():
    for i in range(1,11):
        print("child thread")
t=Thread(target=span)
t.start()
for i in range(1,11):
    print(" thread")
'''
'''
import time
from threading import *
def spam():
    print(current_thread().name,"starte3d")
    time.sleep(3)
    print(current_thread().name,"ended") 
print("total number of thread",active_count())
t=Thread(target=spam,name="child thread")
t1=Thread(target=spam, name="vhild thread")
t2=Thread(target=spam, name="vhild thread")
t.start()
t1.start()
t2.start()

# print("total number of active thread",active_count())
# time.sleep(5)
# print("total number of active thread",active_count())
print("total number of active thread",t.is_alive())
print("total number of active thread",t1.is_alive())
print("total number of active thread",t2.is_alive())
time.sleep(5)
print("total number of active thread",t.is_alive())
print("total number of active thread",t1.is_alive())
print("total number of active thread",t2.is_alive())
'''
#join method
import time
from threading import *
def display():
    for i in range(1,5):
        time.sleep(2)
        print("leazy thread")
t=Thread(target=display)

t.start()
t.join(0.5)
for i in range(1,5):
    print("mainthread")
