from tkinter import*
from PIL import ImageTk
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1199x600+100+50')
        self.root.resizable(False,False)
        
        self.bg=ImageTk.PhotoImage(file='movies image.jpg')
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        
        Frame_login=Frame(self.root, bg='black')
        Frame_login.place(x=150, y=150, height=340, width=500)

        title=Label(Frame_login,text='Welcome to MyFILMS', font=('Impact',35, 'bold'), fg='white',bg='black').place(x=90,y=30)
        desc=Label(Frame_login, text='Users login area',font=('Impact',15,'normal'),fg='white',bg='black').place(x=90,y=100)

        lbl_user=Label(Frame_login, text='Username', font=('Impact',15,'normal'),fg='white',bg='black').place(x=90 , y=140)
        self.txt_user=Entry(Frame_login, font=('times new roman',15),bg='white')
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login, text='Password', font=('Impact',15,'normal'),fg='white',bg='black').place(x=90 , y=210)
        self.txt_pass=Entry(Frame_login, font=('times new roman',15),bg='white')
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        
        forget_btn=Button(Frame_login,text='Forget Password?', bg='black', fg='red',bd=0, font=('Impact', 12)).place(x=90,y=280)        
        Login_btn=Button(self.root,command=self.login_function,text='Login', fg='white', bg='black', font=('Impact', 20, 'bold')).place(x=300,y=470,width=180,height=40)        

    def login_function(self):
        if self.txt_pass.get()=='' or self.txt_user.get()=='':
            messagebox.showerror('Error','All fields are required', parent=self.root)
        elif self.txt_pass.get()!='Ilias' or self.txt_user.get()=='Tsironis':
            messagebox.showerror('Error', 'Invalid Username/Password',parent=self.root)
        else:
            messagebox.showinfo('Welcome',f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get}", parent=self.root)


root=Tk()
obj=Login(root)
root.mainloop()
