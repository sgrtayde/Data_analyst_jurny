# string in python

name = "SagarTa"

# strings methon

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(len(name))
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.split())

print(name.replace("ar","ii"))
print(name.startswith("sa"))
print(name.endswith("ii"))

print(name.isalpha())
print(name.isnumeric())


# strings slicing

s = "My Name Is Sagar"
print(s[0:5])

print(s[0:16])
print(s[0:-1])

# f-string in python
name = input("What is your name : ")
work = input("where do you work: ")
city = input("where do you live: ")

print(f"{name} work at {work} and live in {city}")


# List in python

c = ["sagar","akash","alim","shubhan"]
element = [23,45,True ,99 ,False]


print(c)
print(type(c))
print(c[0])
print(element[4])

print(element[1:5])

element[1] = 33
print(element)


# List methon in python

item = ["banana","clusterbeen","sandelwood"]
print(len(item))

item.append("cheery")
print(item)

item.insert(1,"jagrry")
print(item)

item.extend(["more sandelwood","mangos"])
print(item)

item.remove("clusterbeen")
print(item)

item.pop(0)
print(item)

item.clear()
print(item)


number = [23,34,56,1,13,22,31,4,5,6]
number.sort()
print(number)

print( 56 in number)



# Tuple in python

numbers = (2,34,2,56)

print(numbers[0:3])
print(numbers[1])
print(numbers[2])

single = (1,)
print(type(single))

# Tuple methon in python
print(len(numbers))
print(numbers.count(2))

print(numbers.index(56))

list_1 = list(numbers)      # create new list
list_1 = list(numbers)     
print(list_1)           
