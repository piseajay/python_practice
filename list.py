
cities = ['London', 'Budapest', 'Vienna', 'Prague', 'Amsterdam']

print(len(cities))
print(cities[1])
print(cities[-1])
print(cities[0:2])
print(cities[:3])
print(cities[0:-1])
print(cities[1:])


cities.append('Lisbon')
cities.insert(2, 'Edinburgh');

print('Amsterdam' in cities)

print(cities)

uk_cities = ['Birmingham', 'Manchester']

cities.extend(uk_cities)
cities.remove('London')
removed = cities.pop()

print(cities)
print(removed)
cities.reverse()
print('Reversed List : ', cities)

cities.sort(reverse=True)
print('Sorted List : ', cities)

uk_cities_sorted = sorted(uk_cities)
print(uk_cities_sorted)


nums = [1,2,3,4,5]
print(sum(nums))

