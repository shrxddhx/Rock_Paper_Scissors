from tkinter import *
from PIL import Image,ImageTk
from random import randint
root=Tk()
root.title("Rock Paper Scissors")
root.configure(background="#9b59b6")

rock_img=PhotoImage(file=".\\rockuser.png")
paper_img=PhotoImage(file=".\\paperuser.png")
scissors_img=PhotoImage(file=".\\scissorsuser.png")
rock_img_comp=PhotoImage(file=".\\rock.png")
paper_img_comp=PhotoImage(file=".\\paper.png")
scissors_img_comp=PhotoImage(file=".\\scissors.png")

user_label=Label(root,image=scissors_img,bg="#9b59b6")
comp_label=Label(root,image=scissors_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

msg=Label(root,font=50,bg="#9b59b6",fg="white",text="You lose!")
msg.grid(row=3,column=2)

def updatemessage(x):
    msg['text']=x

def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)

def updateCompScore():
    score=int(computerScore["text"])
    score+=1
    computerScore["text"]=str(score)

def checkwin(player,computer):
    if player==computer:
        updatemessage("It's a tie!")
    elif player=="rock":
        if computer=="paper":
            updatemessage("You lose")
            updateCompScore()
        else:
            updatemessage("You win!")
            updateUserScore()
    elif player=="paper":
        if computer=="scissors":
            updatemessage("You lose")
            updateCompScore()
        else:
            updatemessage("You win!")
            updateUserScore()
    elif player=="scissors":
        if computer=="rock":
            updatemessage("You lose")
            updateCompScore()
        else:
            updatemessage("You win!")
            updateUserScore()

    else:
        pass

choices=["rock","paper","scissors"]
def updateChoice(x):
    compChoice=choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)
    
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)

    checkwin(x,compChoice)

rock=Button(root,width=20,height=2,text="ROCK",bg="#ff3e4d",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#fad02e",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissors=Button(root,width=20,height=2,text="SCISSORS",bg="#0abde3",fg="white",command=lambda:updateChoice("scissors")).grid(row=2,column=3)

"""user_wins=0
computer_wins=0

options=["rock","paper","scissors"]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input=="q":
        break

    if user_input not in options:
        print("Wrong spelling? Try again!")
        continue

    random_number=random.randint(0,2)
    #rock=0, paper=1, scissors=2
    computer_pick=options[random_number]
    print("Computer picked",computer_pick + ".")

    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins+=1

    elif user_input=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins+=1

    elif user_input=="scissors" and computer_pick=="paper":
        print("You won!")
        user_wins+=1

    elif user_input==computer_pick:
        print("It's a draw!")

    else:
        print("You lost!")
        computer_wins+=1

print("You won!", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")"""

root.mainloop()
