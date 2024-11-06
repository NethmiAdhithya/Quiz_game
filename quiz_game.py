print("Welcome to my computr quiz!")

name=input("Enter your name :")

print("Hi", name)

playing = input("Do you want to play?")

if playing.lower() !="yes":
    quit()

print("Okay! Let's play :")
score = 0

answer = input("What dows CPU stand for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What is GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')



answer = input("What dows RAM stand for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')



answer = input("What dows PSU stand for?")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(name, "got " + str(score) + " questions correct!")
print(name, "got " + str((score / 4) * 100) + "%.")

