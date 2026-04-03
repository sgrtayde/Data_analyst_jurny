# function in python
def file(surename):
    print("My name ia sagar",surename)
    print("Work in Taydes.PVT.LTD")
    print("Salary : 200,000")

file(surename="tayde")



def greet(fname,lname):
    print("good morning",fname,lname)
    print("'how are you")
    print("Thnak you")
greet(fname="sagar",lname="tayde")


def add(a,b):
    print(a+b)

add(12,8)



def sagar(name = "sagar", city = "khupta"):
    print('HELLO',name , city)

sagar()
sagar("Harshal")
sagar("Ritesh", "khupta")


# File Handelibg

g = "I will be Billionaire in 2030"

file = open("sagar.txt",'w')
file.write(g)


file = open("Harshal.txt", "r")
# content = file.read()
content = file.readline()
print(content)


a = "\n Sagar is also smart boy"
file = open("Harshal.txt", 'a')
file.write(a)
file.close()



# Error handeling in python

print("initializing...")

a = int(input("Enter a: "))
b = int(input("inter b: "))
try:
    print("the value of a/b",a/b)
except Exception as e:
    print("some error occurring!--",e)
finally:
    print("Thank you")
    






try:
    num = int(input("Enter a number:"))
    print(10 / num )

except:
    print("error! somthing went wrong.")