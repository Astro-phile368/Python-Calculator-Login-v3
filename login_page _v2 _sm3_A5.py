from tkinter import *
from tkinter import messagebox
root=Tk()
root.configure(bg="black")
root.geometry("500x400") 

#labels<>
l1=Label(root,text='username',fg ='blue',bg ='yellow')
l1.place(x=100,y=100)

l2=Label(root,text='password',fg ='blue',bg='yellow')
l2.place(x=100,y=170)
#labels<\>

#userdata
user_data = {
    'test': '123',
    "bob": "pass"
}

#fincrions
def check():
    global user_data

    y=ep.get()
    x=eu.get()    
    
    if x in user_data and user_data[x]==y:
    
        messagebox.showinfo( "info",'you have successfullly login!')
    else:
        messagebox.showinfo('info','wrong password or username')        

#to add user                
def screen():
    #second sceeen
    root1 = Toplevel(root)
    root1.geometry("800x800")
    root1.configure(bg="black")
    
    #labels<>
    l1=Label(root1,text='username',fg ='blue',bg ='yellow')
    l1.place(x=100,y=100)

    l2=Label(root1,text='password',fg ='blue',bg='yellow')
    l2.place(x=100,y=170)
    
    def add():
        y=ep1.get()
        x=eu1.get() 
        if x in user_data:
            messagebox.showinfo('info','user name in the database')   
            
        else:
            user_data[x]=y
            messagebox.showinfo('info','save to database')   
                          
    
    #entry<>
    eu1=Entry(root1)
    eu1.place(x=310,y=100)

    ep1=Entry(root1)
    ep1.place(x=310,y=170)
    
    b1=Button(root1,text='submit',command=add)
    b1.place(x=250,y=250)
        
                                                                            
    
                              
#entry<>
eu=Entry(root)
eu.place(x=310,y=100)

ep=Entry(root)
ep.place(x=310,y=170)
#entry<\>

        

b1=Button(root,text='submit',command=check)
b1.place(x=250,y=250)

b2=Button(root,text="register",command=screen)
b2.place(x=550,y=250)







mainloop()