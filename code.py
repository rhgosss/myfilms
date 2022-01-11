import requests as r
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3 as sq
from tkinter import messagebox
from tkinter import ttk


class Myapp():
    def __init__(self, root,name):
        self.bg = ImageTk.PhotoImage(file='pop2.jpg')
        self.bg_image = tk.Label(root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.f1 = tk.Frame(root, bg='black')
        self.f1.place(x=450, y=75, height=360, width=500)
        self.my_Label = tk.Label(self.f1, text='Search for a film...', font=('Impact', 40), bg='#3D3D3D',
                                 fg='White').place(x=55,y=0)
        self.name = name
        print(self.name)




        self.favorite_btn = tk.PhotoImage(file="kardoula.png")
        self.img_kardoula = tk.Button(root, command=self.favorite_movies, image=self.favorite_btn, borderwidth=0).place(x=1460, y=630)
        self.x_btn = tk.PhotoImage(file="x.png")
        self.img_x = tk.Button(root, command=root.quit, image=self.x_btn, borderwidth=0).place(
            x=730, y=530)
        self.my_entry = tk.Entry(self.f1, font=('consolas', 20), borderwidth=4, fg='white', bg='#2d2d2d')
        self.my_entry.place(x=100,y=160)
        self.bt2 = tk.Button(self.f1, text="search", font="Arial 20",bg="#2d2d2d",fg="white", command=self.search)
        self.bt2.place(x=200,y=300)
    def Return(self):

        for widget in self.f2.winfo_children():
            widget.destroy()
        self.f2.destroy()

        self.f1 = tk.Frame( bg='black')
        self.f1.place(x=450, y=75, height=360, width=500)
        self.my_Label = tk.Label(self.f1, text='Search for a film...', font=('Impact', 40), bg='#3D3D3D',
                                 fg='White').place(x=55, y=0)



        self.my_entry = tk.Entry(self.f1, font=('consolas', 20), borderwidth=4, fg='white', bg='#2d2d2d')
        self.my_entry.place(x=100, y=160)
        self.bt2 = tk.Button(self.f1, text="search", font="Arial 20", bg="#2d2d2d", fg="white", command=self.search)
        self.bt2.place(x=200, y=300)

    def for_search(self):
        self.f2 = tk.Frame()
        self.f2.grid()
        for widget in self.f1.winfo_children():
            widget.destroy()
        self.e = tk.Entry(self.f1, font="Arial 24")
        self.e.grid()
        self.b = tk.Button(self.f1, text="search", font="Arial 20", command=self.search)
        self.b.grid()
        self.b2 = tk.Button(self.f1, text="return", command=self.Return)
        self.b2.grid()

    def search(self):






        self.title = self.my_entry.get()

        try:
            if self.title == "":
                messagebox.showerror('Error', 'Input a movie!', parent=self.f1)

            else:
                self.f2 = tk.Frame(bg="#30475E")
                self.f2.place(x=0, y=0, height=2000, width=2000)
                for widget in self.f1.winfo_children():
                    widget.destroy()
                self.f1.destroy()
                for widget in self.f2.winfo_children():
                    widget.destroy()

                url = f"http://www.omdbapi.com/?t={self.title}&apikey=2692ec2"
                self.r1 = r.get(url)
                self.r1 = self.r1.json()
                print(self.r1)
                self.r2 = r.get(self.r1["Poster"])

                with open(str(self.title) + ".jpg", "wb") as f:
                    f.write(self.r2.content)
                self.img = ImageTk.PhotoImage(Image.open(str(self.title) + ".jpg"))
                print(self.img)
                self.lo = tk.Label(self.f2, text=(self.r1["Title"]), font=('Impact', 55, 'bold'), fg='white',
                                   bg='#30475E').place(x=340, y=10)
                self.l = tk.Label(self.f2, text=(self.r1["Year"]), font=('Calibri', 18, 'normal'), fg='white',
                                  bg='#30475E').place(x=340, y=250)
                self.l1 = tk.Label(self.f2, text=(self.r1["Director"]), font=('Calibri', 18, 'normal'), fg='white',
                                   bg='#30475E').place(x=340, y=150)
                self.l2 = tk.Label(self.f2, text=(self.r1["Plot"]), font=('Calibri', 20, 'normal'), fg='white',
                                   bg='#30475E',wraplength=800).place(x=340, y=400)
                self.l4 = tk.Label(self.f2, text=(self.r1["Actors"]), font=('Calibri', 18, 'normal'), fg='white',
                                   bg='#30475E').place(x=340, y=200)
                self.l3 = tk.Label(self.f2, image=self.img, borderwidth=2).place(x=20, y=20)

                self.b1 = ImageTk.PhotoImage(file='kardoula.png')
                self.img1 = tk.Button(self.f2, command=self.add, image=self.b1, borderwidth=0, bg='#30475E').place(x=19,
                                                                                                                   y=490)

                self.b2 = ImageTk.PhotoImage(file='x.png')
                self.img2 = tk.Button(self.f2, command=self.Return, image=self.b2, borderwidth=0, bg='#30475E').place(
                    x=1100, y=500)
        except KeyError:
            self.Return()



    def favorite_movies(self):
        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("SELECT * FROM movies1")
        items = c.fetchall()
        print(items)
        titles = []
        self.list1 = []
        cnt = 0
        for item in items:
            titles.append(item[0])
            self.list1.append(tk.Button(self.f1, text=str(item[0]), command=lambda m=item[0]: self.overview(m)))
            self.list1[cnt].grid()

            cnt += 1
        conn.commit()
        conn.close()
        self.b2 = tk.Button(self.f1, text="return", command=self.Return)
        self.b2.grid()

    def overview(self, title=""):
        print("geia", title)
        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("SELECT * FROM movies1 WHERE movie_title =? ", (title,))
        items = c.fetchone()
        info = []
        for item in items:
            info.append(item)
            print(info)

        self.img1 = ImageTk.PhotoImage(Image.open(str(title) + ".jpg"))
        l = tk.Label(self.f1, text=(info[1] + info[2]))
        l.grid()
        l1 = tk.Label(self.f1, image=self.img1)
        l1.grid()
        conn.commit()
        conn.close()

    # select * FROM movies 1 WHERE like%

    def add(self):
        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE  if not exists movies1 (
            movie_title DATATYPE text,
            movie_Year DATATYPE text,
            movie_Actors DATATYPE text,
            poster DATATYPE blob
            )""")
        c.execute("SELECT * FROM movies1 WHERE movie_title =? ", (self.title,))
        items = c.fetchall()
        lst = []
        for item in items:
            lst.append(item)
        if len(lst) > 0:
            messagebox.showerror('Error','Movie already exists in favorites!', parent=self.f2)
        else:
            c.execute("INSERT INTO movies1 VALUES (?,?,?,?)",
                      (self.title, self.r1['Year'], self.r1['Actors'], self.r1['Poster']))
            conn.commit()
            conn.close()


    def comments(self):
        print("s")


class Login():
    def __init__(self):
        self.run()


    def my_click(self):
        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("SELECT * FROM members")
        items = c.fetchall()
        print(items)
        self.name = self.e1.get()


        cnt = 0
        for item in items:
            print(item)
            cnt += 1
            if str(self.e1.get()) == item[0] and str(self.e2.get()) == item[1]:
                mylabel = tk.Label(self.root, text="Καλως ορισες " + str(self.e1.get()))
                mylabel.grid()
                self.f1.destroy()
                my_app = Myapp(self.root,self.name)
                self.root.mainloop()
            elif cnt == len(items):
                messagebox.showerror('Error', 'Wrong username or password!', parent=self.root)
                break




    def for_register(self):
        for widget in self.f1.winfo_children():
            widget.destroy()
        title = tk.Label(self.f1, text='Register to MyFILMS', font=('Impact', 35, 'bold'), fg='white',
                         bg='black').place(
            x=90, y=30)
        self.l = tk.Label(self.f1, text='Username', font=('Impact', 15, 'normal'), fg='white',
                          bg='black').place(
            x=90, y=140)
        self.l2 = tk.Label(self.f1, text='Password', font=('Impact', 15, 'normal'), fg='white',
                           bg='black').place(
            x=90, y=210)
        self.entry = tk.Entry(self.f1, font=('times new roman', 15), bg='white')
        self.entry2 = tk.Entry(self.f1, font=('times new roman', 15), bg='white', show="*")
        self.entry.place(x=90, y=170, width=350, height=35)
        self.entry2.place(x=90, y=240, width=350, height=35)
        self.b = tk.Button(self.f1, text='Register', command=self.register, fg='white', bg='black',
                           font=('Impact', 20, 'bold')).place(x=90, y=320, width=180, height=40)
        self.b1 = tk.Button(self.f1, text='Back', command=self.back, fg='white', bg='black',
                           font=('Impact', 20, 'bold')).place(x=320, y=320, width=90, height=40)

    def register(self):
        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("SELECT * FROM members WHERE username =?", (self.entry.get(),))
        items = c.fetchall()
        lst = []
        for item in items:
            lst.append(item)
        if len(lst) > 0:
            print("username already exists")
        else:
            c.execute("INSERT INTO members(username,password) VALUES (?,?)", (str(self.entry.get()), str(self.entry2.get())))
            conn.commit()
            conn.close()
            self.f1.destroy()
            my_app = Myapp(self.root,self.name)
            self.root.mainloop()

    def back(self):
        for widget in self.f1.winfo_children():
            widget.destroy()
        title = tk.Label(self.f1, text='Login to MyFILMS', font=('Impact', 35, 'bold'), fg='white',
                         bg='black').place(
            x=90, y=30)
        desc = tk.Label(self.f1, text='Users login area', font=('Impact', 15, 'normal'), fg='white',
                        bg='black').place(
            x=90, y=100)

        lbl_user = tk.Label(self.f1, text='Username', font=('Impact', 15, 'normal'), fg='white',
                            bg='black').place(
            x=90, y=140)
        self.e1 = tk.Entry(self.f1, font=('times new roman', 15), bg='white')
        self.e1.place(x=90, y=170, width=350, height=35)
        self.name = self.e1.get()

        lbl_pass = tk.Label(self.f1, text='Password', font=('Impact', 15, 'normal'), fg='white',
                            bg='black').place(
            x=90, y=210)
        self.e2 = tk.Entry(self.f1, font=('times new roman', 15), bg='white', show="*")
        self.e2.place(x=90, y=240, width=350, height=35)

        register_btn = tk.Button(self.f1, text='New?Click for registration', command=self.for_register, bg='black',
                                 fg='red', bd=0,
                                 font=('Impact', 12)).place(x=90, y=290)
        login_btn = tk.Button(self.f1, text='Login', command=self.my_click, fg='white', bg='black',
                              font=('Impact', 20, 'bold')).place(x=90, y=320, width=180, height=40)

    def run(self):
        conn = sq.connect("members.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists members (
            username DATATYPE text,
            password DATATYPE text,
            comment DATATYPE text
            )""")
        conn.commit()
        conn.close

        self.root = tk.Tk()
        self.root.title('My films')
        self.root.geometry('1199x600+100+50')


        self.bg = ImageTk.PhotoImage(file='wallpaper1.jpg')
        self.bg_image = tk.Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.f1 = tk.Frame(self.root, bg='black')
        self.f1.place(x=150, y=150, height=360, width=500)

        title = tk.Label(self.f1, text='Login to MyFILMS', font=('Impact', 35, 'bold'), fg='white',
                         bg='black').place(
            x=90, y=30)
        desc = tk.Label(self.f1, text='Users login area', font=('Impact', 15, 'normal'), fg='white',
                        bg='black').place(
            x=90, y=100)

        lbl_user = tk.Label(self.f1, text='Username', font=('Impact', 15, 'normal'), fg='white',
                            bg='black').place(
            x=90, y=140)
        self.e1 = tk.Entry(self.f1, font=('times new roman', 15), bg='white')
        self.e1.place(x=90, y=170, width=350, height=35)



        lbl_pass = tk.Label(self.f1, text='Password', font=('Impact', 15, 'normal'), fg='white',
                            bg='black').place(
            x=90, y=210)
        self.e2 = tk.Entry(self.f1, font=('times new roman', 15), bg='white', show="*")
        self.e2.place(x=90, y=240, width=350, height=35)

        register_btn = tk.Button(self.f1, text='New?Click for registration', command=self.for_register, bg='black',
                                 fg='red', bd=0,
                                 font=('Impact', 12)).place(x=90, y=290)
        login_btn = tk.Button(self.f1, text='Login', command=self.my_click, fg='white', bg='black',
                              font=('Impact', 20, 'bold')).place(x=90, y=320, width=180, height=40)
        self.root.mainloop()


if __name__ == "__main__":
    Login()
