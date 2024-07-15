friends = ['John','Michael','Terry','Eric','Graham']

cars = [911,130,328,535,740,308]
print(friends)
cars.sort()
print(cars)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
print(min(cars))
print(max(cars))
print(sum(cars))



friends.insert(1,'TerryG')
print(friends)


friends[2]='TerryG'
print(friends)

friends.extend(cars)
print(friends)

friends.remove('Terry')

print(friends)