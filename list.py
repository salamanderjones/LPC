friends = ["Julia", "Sam", "Jim"] #Julia is 0, Sam is 1, Jim is 2, etc.
print(friends [0])
print(friends[1:])

lucky_numbers = [8, 4, 15, 16, 23, 42]
lucky_numbers.sort() #this puts them in order. does with words in alphabetical order.
print(lucky_numbers)

enemies =["Kevin", "Karen", "Oscar", "Toby", "Dwight"]
enemies.extend(lucky_numbers)
enemies.append("Creed") #this adds Creed at the end
enemies.insert(1, "Kelly") #this inserts name in the list
enemies.remove("Toby")
print(enemies)

parents =["Father", "Father", "Father", "Mother", "Stepfather", "Stepmother"]
print(parents)
print(parents.index("Mother")) #This tells you if a value is in the list
print(parents.count("Father"))
parents.reverse() #reverses
print(parents)
parents2 = parents.copy() #copies the list
print(parents2)