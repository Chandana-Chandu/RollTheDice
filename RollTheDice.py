from tkinter import *
import random
root = Tk()
root.title('Dice Rolling Simulator')
root.geometry("500x500")
i = PhotoImage(file='C:/Users/Chandana/Desktop/Chandana/projects/python/DiceRoll.PNG')
root.iconphoto(False,i)
bg=PhotoImage(file='C:/Users/Chandana/Desktop/Chandana/projects/python/Dice.PNG')
label1 = Label(root,image=bg)
label1.place(x=0,y=0)
#Get Dice Number
def get_number(x):
    if x=='\u2680':
        return(1)
    elif x=='\u2681':
        return(2)
    elif x=='\u2682':
        return(3)
    elif x=='\u2683':
        return(4)
    elif x=='\u2684':
        return(5)
    else:
        return(6)
#Roll the Dice
def roll_dice():
    #Roll Random Choice
    d1 = random.choice(My_Dice)
    d2 = random.choice(My_Dice)

    #Dtermine Dice Number
    sd1 = get_number(d1)
    sd2 = get_number(d2)
    
    #Update the Label
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)

    #Update Sub Labels
    sub_dice_label1.config(text=sd1) 
    sub_dice_label2.config(text=sd2)

    #update total label
    total = sd1 + sd2
    total_label.config(text=f"You Rolled:{total}")#interpolation

#Create a Dice List
My_Dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

#Create a Frame
My_frame = Frame(root,bg='#000000')
My_frame.pack(pady=20)

#Create Dice Labels
dice_label1 = Label(My_frame,font=("Helvetica",100),fg="#EBF4FA",bg='#000000')
dice_label1.grid(row=0,column=0,padx=5)
sub_dice_label1 = Label(My_frame,fg='#F433FF',bg='#000000',font=('Helvetica',20))
sub_dice_label1.grid(row=1,column=0)
dice_label2 = Label(My_frame,font=("Helvetica",100),fg="#EBF4FA",bg='#000000')
dice_label2.grid(row=0,column=1,padx=5)
sub_dice_label2 = Label(My_frame,fg='#F433FF',bg='#000000',font=('Helvetica',20))
sub_dice_label2.grid(row=1,column=1)


#Create Roll Button
My_Button = Button(root,text="Roll Dice",command=roll_dice,font=("Helvetica",24),bg='#16E2F5')
My_Button.pack(pady=20)

#Create Total Labels
total_label = Label(root,font=("Helvetica",24),fg='#228B22',bg='#000000')
total_label.pack(pady=40)

#Roll the Dice
roll_dice()

Exit= Button(root,text="Exit",command=root.quit,fg='Red',bg='#000000',font=('Helvetica',19))
Exit.pack()
                                                              
root.mainloop()
