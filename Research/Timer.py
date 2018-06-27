from datetime import datetime
import time
from threading import Timer
import threading

# t1 = datetime.now()
# print(t1)
# time.sleep(5)
# t2 = datetime.now()
# print(t2)
# delta = t2 - t1
# print(delta.seconds)

# def timeout():
#     print("Alarm!")

# t = Timer(2, timeout)
# t.start() 

def abc():
    print("GeeksforGeeks\n")
    print(1)
    timer = threading.Timer(2, abc)
    timer.start()
    
 
timer = threading.Timer(2, abc)
timer.start()

