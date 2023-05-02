score = 0
def right(num):
    num += 1
    print("Correct!!")
    print("Score: " + str(num))
    return num

def wrong():
    print("Wrong!!")
    quit()

print("Welcome to my computer quiz!")

playing = input ("Do You Want To Play(y or n)? ")

if playing.lower() != "y":
    quit()

print("let's get to the quiz!!")


answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit" :
    score = right(score)
else:
    wrong()


answer = input("what does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    score = right(score)
else:
    wrong()


answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory" :
    score = right(score)
else:
    wrong()

print("YOU WON!!!")
quit()




