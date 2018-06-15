"""

用for循環實現1~100求和

Version: 0.1
Author: 駱昊
Date: 2018-03-01

"""

sum = 0
for x in range(1, 101):
	if x % 2 == 0:
		sum += x
print(sum)
