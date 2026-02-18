import time
import threading
start = time.perf_counter()
def sleep_func():
    print("sleeping for 1 second")
    time.sleep(1)
    print("finished sleeping")

t1 = threading.Thread(target=sleep_func)
t2 = threading.Thread(target=sleep_func)

t1.start()
t2.start()

finish = time.perf_counter()

print(f"finished in {round(finish-start)} seconds")
