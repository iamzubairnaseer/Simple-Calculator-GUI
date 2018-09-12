from tkinter import*

calculator=Tk()
calculator.title('Simple Calculator')
calculator.geometry('400x440')

BackGround=Frame(calculator,bg='blue',width=400,height=440)
BackGround.pack()

Input=StringVar()
Display=Entry(BackGround,textvariable=Input,font='Times 20 bold')
Display.place(x=60,y=30)
Input.set('Write Here')

number=''
def entry(num):
    global number
    number=number+num
    Input.set(number)

def clear():
    global number
    number=''
    Input.set('Write Here')

def Del():
    global number
    number=number[:-1]
    if len(number)==0:
       Input.set('Write Here')
    else:
        Input.set(number)

def equal():
    global number
    Answer=Display.get()
    number=str(eval(Answer))
    Input.set(number)
    

def exit():
    calculator.destroy()
    
buttonwsquare=Button(BackGround,command=lambda:entry('**2'),text='x^2',font=('times', 16, ' roman'),bg='black',fg='White')
buttonwsquare.place(x=20,y=100)

buttonwsquare=Button(BackGround,command=lambda:entry('**'),font=('times', 16, ' roman'),text='x^x',bg='black',fg='White')
buttonwsquare.place(x=100,y=100)

buttonbracketopen=Button(BackGround,command=lambda:entry('('),font=('times', 16, ' roman'),text='(',bg='black',fg='White')
buttonbracketopen.place(x=170,y=100)

buttonbracketclose=Button(BackGround,command=lambda:entry(')'),text=')',font=('times', 16, ' roman'),bg='black',fg='White')
buttonbracketclose.place(x=240,y=100)

buttonzero=Button(BackGround,command=lambda:entry('0'),text='0',bg='black',fg='White',font=('times', 16, ' roman'))
buttonzero.place(x=100,y=340)

buttonpoint=Button(BackGround,command=lambda:entry('.'),text='.',font=('times', 16, ' roman'),bg='black',fg='White')
buttonpoint.place(x=20,y=340)

buttonminus=Button(BackGround,command=lambda:entry('-'),text='-',bg='black',fg='White',font=('times', 16, ' roman'))
buttonminus.place(x=240,y=340)

buttonpi=Button(BackGround,command=lambda:entry('π'),text='π',bg='black',fg='White',font=('times', 16, ' roman'))
buttonpi.place(x=170,y=340)

buttonone=Button(BackGround,command=lambda:entry('1'),text='1',bg='black',fg='White',font=('times', 16, ' roman'))
buttonone.place(x=20,y=160)

buttontwo=Button(BackGround,command=lambda:entry('2'),text='2',bg='black',fg='White',font=('times', 16, ' roman'))
buttontwo.place(x=100,y=160)

buttonthree=Button(BackGround,command=lambda:entry('3'),text='3',bg='black',fg='White',font=('times', 16, ' roman'))
buttonthree.place(x=170,y=160)

buttonplus=Button(BackGround,command=lambda:entry('+'),text='+',bg='black',fg='White',font=('times', 16, ' roman'))
buttonplus.place(x=240,y=160)

buttonfour=Button(BackGround,command=lambda:entry('4'),text='4',bg='black',fg='White',font=('times', 16, ' roman'))
buttonfour.place(x=20,y=220)

buttonfive=Button(BackGround,command=lambda:entry('5'),text='5',bg='black',fg='White',font=('times', 16, ' roman'))
buttonfive.place(x=100,y=220)

buttonsix=Button(BackGround,command=lambda:entry('6'),text='6',bg='black',fg='White',font=('times', 16, ' roman'))
buttonsix.place(x=170,y=220)

buttonmul=Button(BackGround,command=lambda:entry('*'),text='x',bg='black',fg='White',font=('times', 16, ' roman'))
buttonmul.place(x=240,y=220)

buttonseven=Button(BackGround,command=lambda:entry('7'),text='7',bg='black',fg='White',font=('times', 16, ' roman'))
buttonseven.place(x=20,y=280)

buttoneight=Button(BackGround,command=lambda:entry('8'),text='8',bg='black',fg='White',font=('times', 16, ' roman'))
buttoneight.place(x=100,y=280)

buttonnine=Button(BackGround,command=lambda:entry('9'),text='9',bg='black',fg='White',font=('times', 16, ' roman'))
buttonnine.place(x=170,y=280)

buttondivid=Button(BackGround,command=lambda:entry('/'),text='/',bg='black',fg='White',font=('times', 16, ' roman'))
buttondivid.place(x=240,y=280)

buttonEqual=Button(BackGround,command=equal,text='EQUAL',font=50,bg='black',fg='White',padx=20,pady=10)
buttonEqual.place(x=290,y=270)

buttonClear=Button(BackGround,command=clear,text='CLEAR',font=50,bg='black',fg='White',padx=20,pady=10)
buttonClear.place(x=290,y=210)

btnDel=Button(BackGround,text='DEL',bg='black',fg='White',font=50,padx=30,pady=10)
btnDel.config(command=lambda:Del())
btnDel.place(x=290,y=150)

buttonExit=Button(BackGround,command=exit,text='EXIT',font=50,bg='black',fg='White',padx=30,pady=10)
buttonExit.place(x=290,y=330)

calculator.mainloop()
