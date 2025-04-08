message = 'Hello World!!'

message = message.lower();

name = 'Ajay'

new_message = f'My name is {name.lower()}'

message = message.replace('hello', 'Holla')

index = message.find('World')  // -1
index = message.find('world')  // 6

print('Holla found at index', index)

print(new_message)
print(message)
print('length of the message is ',len(message))
