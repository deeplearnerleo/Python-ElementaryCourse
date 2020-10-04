#TextProBarV2.py


#单行动态刷新
#刷新本质是：用后打印的字符覆盖之前的字符

import time
for i in range(101):
    print("\r{:10}%".format(i),end="")
    time.sleep(0.1)
