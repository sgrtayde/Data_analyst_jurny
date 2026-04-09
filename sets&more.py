# sets in python
s1 = set()
print(type(s1))


set = {1,2,3,3,4,4}
print(set)



set2 = {"book","notebook","pean"}

set2.add("watch")
print(set2)

set2.update(["compass"])
print(set2)

set2.remove("book")
print(set2)

set2.pop()
print(set2)

set2.clear()
print(set2)


a = {1,2,3,4}
b = {4,5,6,7}

# c = a.union(b)
c = a.intersection(b)
print(c)




# #  Dictionary in python 

students = {
    "name" : "sagar",
    "city" : "Sambhaji namgar",
 "company" : "TAYDES.PVT.LTD"

}
print(students)
print(students.get("company"))
print(students.get("name"))

students["city"] = "sillod"
print(students)

students.pop("name")
print(students)

students["class"] = "second year"
print(students)

students.popitem()
print(students)

students.keys()
print(students)



# if-else statement in python

s = int(input("Enter a number"))
if(s >= 18):
    print("now you can do vote : ")
else:
    print("you can not do vote : ")
    print("TRY next year")
print("Program NED")



score= int(input("Enter a number: "))

if(score >= 80):
    print("Grade A")
elif(score >= 60):
    print("Grade B")
elif(score >= 40):
    print("Grade C")
elif(score >= 35):
    print("Grade D")
else:
    print("faile")



# For Loop in python

for i in range(0 ,15,3):
    print(i)    


for char in "sagar":
    print(char)


for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


for i in range(1 ,6):
    print(" *" * i)



# # While loop in python

count = 1
while(count <= 10):
    print(count)
    count += 1



n = int(input("Enter a number"))

i = 1
while i <= 10:
    print(n, "x", i ,"=", n*i)
    i += 1


# Brek statement

for i in range(10):
    if(i==5):
        break
    print(i)


# continue statemant
for i in range(10):
    if(i==6):
        continue
    print(i)








