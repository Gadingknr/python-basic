import random

name = "Jackie"

question = "Will you win a lottery?"

answer = ""

random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes - Definitely!"
elif random_number == 2:
    answer = "Most likely!"
elif random_number == 3:
    answer = "Probably"
elif random_number == 4:
    answer = "Could be"
elif random_number == 5:
    answer = "Unlikely"
elif random_number == 6:
    answer = "Probably not"
elif random_number == 7:
    answer = "Mostlikely not"
elif random_number == 8:
    answer = "Slime chance!"
elif random_number == 9:
    answer = "No"
else:
    answer = "Error"

print(name, "ask:", question)
print("Magic 8-Ball's answer:", answer)

