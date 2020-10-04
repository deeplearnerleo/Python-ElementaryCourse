#TextProBarV3.py
import time
scale = 50
print("程序开始".center(scale//2,"_"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(),end="")
    time.sleep(0.1)
print("\n"+"程序结束".center(scale//2,'_'))
