"""

判斷輸入的正整數是不是回文數
回文數是指將一個正整數從左往右排列和從右往左排列值一樣的數

Version: 0.1
Author: 駱昊
Date: 2018-03-02

"""

num = int(input('請輸入一個正整數: '))
temp = num
num2 = 0
while temp > 0:
	num2 *= 10
	num2 += temp % 10
	temp //= 10
if num == num2:
	print('%d是回文數' % num)
else:
	print('%d不是回文數' % num)
