# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
t=name1.lower()
s=name2.lower()

a=t.count("t")
b=t.count("r")
c=t.count("u")
d=t.count("e")


x=s.count("t")
y=s.count("r")
z=s.count("u")
w=s.count("e")


e=t.count("l")
f=t.count("o")
g=t.count("v")
h=t.count("e")

i=s.count("l")
j=s.count("o")
k=s.count("v")
l=s.count("e")

total1 = a + b + c + d + x + y + z + w
total2 = e + f + g + h + i + j + k + l 
score = (f"{total1}{total2}")
score1 = int(score)


if score1 < 10 or score1 > 90:
    print(f"Your score is {score1} , you go together like coke and mentos.")
elif score1 > 40 and score1 < 50:
    print(f"Your score is {score1} , you are alright together.")
else:
    print(f"Your score is {score1}.")

