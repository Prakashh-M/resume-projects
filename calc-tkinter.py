from tkinter import * 
root=Tk() 
root.title("prakash") 
e=Entry(root,width=40,borderwidth=15) 
e.grid(row=0,column=0,columnspan=3,padx=12,pady=15) 
def click(num): 
 
 current=e.get() 
 e.delete(0,END) 
 e.insert(0,str(current)+str(num)) 
def clr(): 
 e.delete(0,END) 
 
def addition(): 
 first=e.get() 
 global f_num 
 f_num=int(first) 
 global func 
 func=addition 
 e.delete(0,END) 
def subtraction(): 
 first=e.get() 
 global f_num 
 f_num=int(first) 
 global func 
 func=subtraction 
 e.delete(0,END) 
def multiplication(): 
 first=e.get() 
 global f_num 
 f_num=int(first) 
 global func 
 func=multiplication 
 e.delete(0,END) 
def division(): 
 first=e.get() 
 global f_num 
 f_num=int(first) 
 global func 
 func=division 
 e.delete(0,END) 
 
 
def eql(): 
 second=e.get() 
 e.delete(0,END) 
 if func==addition: 
    e.insert(0,f_num + int(second)) 
 if func==subtraction: 
    e.insert(0,f_num - int(second)) 
 if func==multiplication: 
    e.insert(0,f_num * int(second)) 
 if func==division: 
    e.insert(0,f_num / int(second)) 
 
 
 
 
 
 
but1=Button(root,text="1",padx=40,pady=20,command=lambda:click(1)) 
but2=Button(root,text="2",padx=40,pady=20,command=lambda:click(2)) 
but3=Button(root,text="3",padx=40,pady=20,command=lambda:click(3)) 
but4=Button(root,text="4",padx=40,pady=20,command=lambda:click(4)) 
but5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5)) 
but6=Button(root,text="6",padx=40,pady=20,command=lambda:click(6)) 
but7=Button(root,text="7",padx=40,pady=20,command=lambda:click(7)) 
but8=Button(root,text="8",padx=40,pady=20,command=lambda:click(8)) 
but9=Button(root,text="9",padx=40,pady=20,command=lambda:click(9)) 
but0=Button(root,text="0",padx=40,pady=20,command=lambda:click(0)) 
but_add=Button(root,text="+",padx=40,pady=20,command=addition) 
but_sub=Button(root,text="-",padx=40,pady=20,command=subtraction) 
but_mul=Button(root,text="*",padx=40,pady=20,command=multiplication) 
but_div=Button(root,text="/",padx=40,pady=20,command=division) 
but_clear=Button(root,text="C",padx=40,pady=20,bg="blue",fg="white",command=clr) 
but_equal=Button(root,text="=",padx=120,pady=30,bg="yellow",fg="black",command=eql) 
but1.grid(row=3,column=0) 
but2.grid(row=3,column=1) 
but3.grid(row=3,column=2) 
but4.grid(row=2,column=0) 
but5.grid(row=2,column=1) 
but6.grid(row=2,column=2) 
but7.grid(row=1,column=0) 
but8.grid(row=1,column=1) 
but9.grid(row=1,column=2) 
but_sub.grid(row=5,column=0) 
but_mul.grid(row=5,column=1) 
but_div.grid(row=5,column=2) 
but0.grid(row=4,column=0) 
but_add.grid(row=4,column=1) 
but_clear.grid(row=4,column=2) 
but_equal.grid(row=6,column=0,columnspan=3) 
root.mainloop() 
