
import os,time

list = ["/","-","\\"]
for _ in range(10):
    for x in list:
        print(x, end='\r')
        time.sleep(1)
