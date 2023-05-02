print("Welcome to my computer quiz!")

playing = input ("Do You Want To Play(y or n)? ")

if playing != "y":
    quit()

print("let's get to the quiz!!")


answer = input("what does CPU stand for? ")
if answer == "center processing unit" or answer == "Central processing unit" or answer == "central proccessing unit":
    print("Correct!!")
else:
    print("Wrong!!")


answer = input("what does GPU stand for? ")
if answer == "Graphic processing unit" or answer == "graphic processing unit" or answer == "graphic proccessing unit":
    print("Correct!!")
else:
    print("Wrong!!")


answer = input("what does RAM stand for? ")
if answer == "Random access memory" or answer == "random access memory":
    print("Correct!!")
else:
    print("Wrong!!")

print("Game Over")
quit()
