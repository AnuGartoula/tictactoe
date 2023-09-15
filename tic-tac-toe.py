from tkinter import *
import random 

def nextturn(row, column):


    global player


    if buttons[row][column]['text']  == "" and checkwinner() is False:
        
        buttons[row][column].config(text=player, bg ='#6096ba' )
        

        if player == players[0]:

            buttons[row][column]['text'] == player

            if checkwinner() is False:
                player = players[1]
                label.config( text = (players[1] + " turn") )
            
            elif checkwinner() is True:
                label.config(text=(players[0] + " IS A WINNER"))
            
            elif checkwinner()  == "tie":
                label.config(text=( 'YOU TIED'))
        else:

            buttons[row][column]['text'] == player

            if checkwinner() is False:
                player = players[0]
                label.config( text = (players[0] + " turn") )

            elif checkwinner() is True:
                label.config(text=(players[1] + " IS A WINNER"))
            
            elif checkwinner()  == "tie":
                label.config(text=( 'YOU TIED'))
            





    

def checkwinner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg='#52b788')
            buttons[row][1].config(bg='#52b788')
            buttons[row][2].config(bg='#52b788')
            return True
        
    for column in range(3):    
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] !="":
            buttons[0][column].config(bg='#52b788')
            buttons[1][column].config(bg='#52b788')
            buttons[2][column].config(bg='#52b788')
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
            buttons[0][0].config(bg='#52b788')
            buttons[1][1].config(bg='#52b788')
            buttons[2][2].config(bg='#52b788')
            return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
            buttons[0][2].config(bg='#52b788')
            buttons[0][1].config(bg='#52b788')
            buttons[2][0].config(bg='#52b788')
            return True
    
    elif emptyspaces() is False:
        return 'tie'
    
    else:
        return False


def emptyspaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
            

    if spaces == 0:
        return False
    
    else:
        return True
        

def newgame():
    global player

    player = random.choice(players)


    label.config(text= player +' turn')

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg='#c6d2ed')












window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0], 
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text = player + " turn " )
label.pack(side = 'top')
reset_buttons = Button(text='Restart', command=newgame, height=3, width=8, bg='#e7e6f7')
reset_buttons.pack(side='top')

frame = Frame(window)
frame.pack()

for row in range (3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font=('consolas', 15), width=20, height=5, command =lambda row = row , column = column: nextturn(row, column ) ,bg='#c6d2ed'  )
        buttons[row][column].grid(row=row ,column=column)
window.mainloop()