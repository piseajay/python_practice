
a = 30
b = 20

print('addition :', a + b)
print('Substraction : ', a - b)
print('Multiplication : ', a * b)
print('Division : ', a / b)
print('Division pre Python 3: ', a // b)
print('Remainder : ', a % b)


nums = [1,2,3,4,5,6,7,8]

for num in range(10):
	print(num)


for index, num in enumerate(nums):
	print(index, num)

fruits = ['apple', 'banana']

comma = ', '.join(fruits)
print(comma)