print("Welcome to my computer quiz!")

playing = input ("Do You Want To Play(y or n)? ")

if playing.lower() != "y":
    quit()

print("let's get to the quiz!!")


answer = input("what does CPU stand for? ")
if answer.lower() == "centeral processing unit" :
    print("Correct!!")
else:
    print("Wrong!!")


answer = input("what does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!!")
else:
    print("Wrong!!")


answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("Correct!!")
else:
    print("Wrong!!")

print("Game Over")
quit()
