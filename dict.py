
car_info = {'name' : 'Mustang GT', 'made' : 'Ford', 'model' : 2022, 'colors' : ['Yellow', 'Red']}

print(car_info)
print('length of the dictionary is :',len(car_info))
print(car_info.items())
print(car_info.keys())
print(car_info.values())

print(car_info['name'])
#print(car_info['names']) throws an error

car_info['name'] = 'Mustang GT Pro'
car_info['price'] = '£40000'

print(car_info)

car_info.update({'price' : '£50000'})

print(car_info)

price = car_info.pop('price')
print(price)
print(car_info)

for key in car_info:
	print(key)

for key,value in car_info.items():
	print(key,value)

for key,value in enumerate(car_info.items(), start = 1):
	print(key,value)






