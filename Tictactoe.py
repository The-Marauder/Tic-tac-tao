from tkinter import *
import tkinter
import tkinter.messagebox as msg

root = Tk()
root.title("Tic Tac Toe")
Label(root , text="Player 1 : X", font='Comic  22').grid(row=0,column=1)
Label(root , text="Player 2 : O", font='Comic  22').grid(row=0,column=3)

digits =[1,2,3,4,5,6,7,8,9]
count = 0
panels = ["panel"]*10
sign = ''
mark = ''
digit = ''
digitcount = 0


def win(panels ,sign) :
    return(
((panels[1] == panels[2] == panels [3] == sign)
or (panels[1] == panels[4] == panels [7] == sign)
or (panels[1] == panels[5] == panels [9] == sign)
or (panels[2] == panels[5] == panels [8] == sign)
or (panels[3] == panels[6] == panels [9] == sign)
or (panels[3] == panels[5] == panels [7] == sign)
or (panels[4] == panels[5] == panels [6] == sign)
or (panels[7] == panels[8] == panels [9] == sign)))

def checker(digit) :
    global count,mark,digits,digitcount
    digitcount = 0
    while digitcount <= 9 :
    
        if digit == digitcount and digit in digits :
            digits.remove(digit)

            if (count%2 == 0) :
                mark = 'X'
                panels[digit] = mark
            else :
                mark = 'O'
                panels[digit] = mark
            
            buttons[digitcount-1].config(text=mark)
            count +=1
            sign = mark

            if(win(panels,sign) and sign == 'X') :
                msg.showinfo("Result","Player1 wins!")
            elif win(panels,sign) and sign == 'O' :
                msg.showinfo("Result","Player2 wins!")
        digitcount +=1
    
    
    if(count > 8 and win(panels, 'X') == False and win(panels , 'O') == False) :
        msg.showinfo('Result','Match Tied!')
        root.destroy()
button1 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(1))
button1.grid(row=1,column=1)
button2 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(2))
button2.grid(row=1,column=2)
button3 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(3))
button3.grid(row=1,column=3)
button4 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(4))
button4.grid(row=2,column=1)
button5 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(5))
button5.grid(row=2,column=2)
button6 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(6))
button6.grid(row=2,column=3)
button7 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(7))
button7.grid(row=3,column=1)
button8 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(8))
button8.grid(row=3,column=2)
button9 = Button(root,width = 18,height  = 10,font=('Times 18 bold'),command= lambda : checker(9))
button9.grid(row=3,column=3)
buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
root.mainloop()