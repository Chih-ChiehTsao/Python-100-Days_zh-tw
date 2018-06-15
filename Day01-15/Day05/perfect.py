"""

找出1~9999之間的所有完美數
完美數是除自身外其他所有因子的和正好等於這個數本身的數
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 駱昊
Date: 2018-03-02

"""
import time
import math

start = time.clock()
for num in range(1, 10000):
	sum = 0
	for factor in range(1, int(math.sqrt(num)) + 1):
		if num % factor == 0:
			sum += factor
			if factor > 1 and num / factor != factor:
				sum += num / factor
	if sum == num:
		print(num)
end = time.clock()
print("執行時間:", (end - start), "秒")

# 通過比較上面兩種不同的解決方案的執行時間 意識到優化程序的重要性
