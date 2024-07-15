friends = ['John','Michael','Terry','Eric','Graham']

#Tuples - faster Lists you can't change
friends_tuple = ('John','Michael','Terry','Eric','Graham')

#Sets - blazingly fast unordered Lists 
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}

print(friends[2:4])

print(friends_tuple[2:4])

print(friends_set)


#Sets - blazingly fast unordered Lists 
#empty Lists
empty_list = []
empty_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()


#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']


print('Eric' in friends and 'John' in friends)

print(friends.union(my_friends))

print(friends ^ my_friends)

print(friends.difference(my_friends))

print(friends.difference(my_friends))
print(my_friends.difference(friends))


cars_list = list(set(cars))

print(cars_list)
