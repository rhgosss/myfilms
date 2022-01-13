import requests as r
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3 as sq
from tkinter import messagebox
from tkinter import ttk


# valw se ola ta frames tin ikona p m eixes diksi (.ico)

class Myapp():

    def __init__(self, root, name):
        root.bind('<Return>', lambda e: "break")

        # self.bg = ImageTk.PhotoImage(file='wallpaper.jpg')
        # self.bg_image = tk.Label(root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.f1 = tk.Frame(root, bg='#3D3D3D')
        self.f1.place(x=0, y=0, relheight=2000, relwidth=2000)

        self.my_Label = tk.Label(self.f1, text='Search for a film...', font=('Impact', 50), bg='#3D3D3D',
                                 fg='White').place(x=759, y=20)

        self.name = name
        print(self.name)
        # Aspro koutaki giro apo ayta(giati)!
        self.favorite_btn = ImageTk.PhotoImage(file='FINAL FAVORITES.png')
        self.img_kardoula = tk.Button(self.f1, command=self.favorite_movies, image=self.favorite_btn, borderwidth=0, bg='#3D3D3D',
                                      fg='#3D3D3D').place(
            x=19, y=600)
        # quit den leitpyrgei
        self.x_btn = ImageTk.PhotoImage(file='FINAL X.png')
        self.img_x = tk.Button(self.f1, command=self.quit, image=self.x_btn, borderwidth=0,bg='#3D3D3D',
                                      fg='#3D3D3D').place(x=1000, y=600)

        self.my_entry = tk.Entry(self.f1, font=('Calibri', 20), borderwidth=4, fg='white', bg='#2d2d2d')
        self.my_entry.place(x=820, y=155)

        self.bt2 = tk.Button(self.f1, text="Search", font=('Impact', 20), borderwidth=3, bg="#2d2d2d", fg="white",
                             command=self.search)
        self.bt2.place(x=915, y=260)

    def quit(self):
        quit()

    def Return(self):

        for widget in self.f2.winfo_children():
            widget.destroy()

        self.f2.destroy()


    # ?tinauto


    def search(self):

        self.title = self.my_entry.get()

        try:
            if self.title == "":
                messagebox.showerror('Error', 'Please enter a film title!', parent=self.f1)
            else:
                self.f2 = tk.Frame(bg="#3D3D3D")
                self.f2.place(x=0, y=0, height=2000, width=2000)
                
                for widget in self.f2.winfo_children():
                    widget.destroy()

                url = f"http://www.omdbapi.com/?t={self.title}&apikey=2692ec2"
                self.r1 = r.get(url)
                self.r1 = self.r1.json()
                print(self.r1)
                self.r2 = r.get(self.r1["Poster"])

                # i eikona einai poli mikri , na mini stin idia thesi20x20 alla na ginei pio megali
                with open(str(self.title) + ".jpg", "wb") as f:
                    f.write(self.r2.content)
                self.img = ImageTk.PhotoImage(Image.open(str(self.title) + ".jpg"))
                print(self.img)

                self.lo = tk.Label(self.f2, text=(self.r1["Title"]), font=('Impact', 60, 'bold'), fg='white',
                                   bg='#3D3D3D').place(x=340, y=10)

                self.l = tk.Label(self.f2, text=(self.r1["Year"]), font=('Calibri', 18, 'normal'), fg='white',
                                  bg='#3D3D3D').place(x=340, y=250)

                self.l1 = tk.Label(self.f2, text=(self.r1["Director"]), font=('Calibri', 18, 'normal'), fg='white',
                                   bg='#3D3D3D').place(x=340, y=150)
                # i sintaksi na min einai mazemeni sto kentro , na einai skorpia se olo to diasthma p orisame me to wraplenght (1000)
                self.l2 = tk.Label(self.f2, text=(self.r1["Plot"]), font=('Calibri', 20, 'normal'), fg='white',
                                   bg='#3D3D3D', wraplength=1000).place(x=340, y=400)

                self.l4 = tk.Label(self.f2, text=(self.r1["Actors"]), font=('Calibri', 18, 'normal'), fg='white',
                                   bg='#3D3D3D').place(x=340, y=200)

                self.l3 = tk.Label(self.f2, image=self.img).place(x=20, y=20)

                self.b1 = ImageTk.PhotoImage(file='FINAL FAVORITES.png')
                self.img1 = tk.Button(self.f2, command=self.add, image=self.b1, borderwidth=0, bg='#3D3D3D',
                                      fg='#3D3D3D').place(x=19, y=910)

                self.b2 = ImageTk.PhotoImage(file='FINAL X.png')
                self.img2 = tk.Button(self.f2, command=self.Return, image=self.b2, borderwidth=0, bg='#3D3D3D').place(
                    x=100, y=660)

                self.b3 = tk.Button(self.f2, command=self.comments, text="Comments", font=('Impact', 20), fg='white',
                                    bg='#2d2d2d', borderwidth=4).place(x=940, y=100)

        except KeyError:
            self.Return()

    # otan patas return apo tis favorite movies laggarei kai petaei dio search bar othones i mia pano stin alli
    def favorite_movies(self):

        self.f2 = tk.Frame(bg="#3D3D3D")
        self.f2.place(x=0, y=0, height=2000, width=2000)
        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("SELECT * FROM movies1")
        items = c.fetchall()
        titles = []
        self.list1 = []
        cnt = 0

        for item in items:
            titles.append(item[0])
            self.list1.append(tk.Button(self.f2, text=str(item[0]), command=lambda m=item[0]: self.overview(m)))
            self.list1[cnt].grid()

            cnt += 1
        conn.commit()
        conn.close()

        self.b2 = tk.Button(self.f2, text="Return", command=self.Return, font=('Impact', 20), borderwidth=4,
                            bg='#3D3D3D', fg='white').place(x=958, y=660)

    # ????geia (ti simenei auto )
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

        self.img10 = ImageTk.PhotoImage(Image.open(str(title) + ".jpg"))
        print(self.img10)
        self.l10 = tk.Label(self.f2, image=self.img10).place(x=20, y=20)

        self.lo = tk.Label(self.f2, text=(info[0]), font=('Impact', 55, 'bold'), fg='white', bg='#3D3D3D').place(x=340,
                                                                                                                 y=10)

        self.l = tk.Label(self.f2, text=(info[1]), font=('Calibri', 18, 'normal'), fg='white', bg='#3D3D3D').place(
            x=340, y=250)

        self.l1 = tk.Label(self.f2, text=(info[2]), font=('Calibri', 18, 'normal'), fg='white', bg='#3D3D3D').place(
            x=340, y=150)

        self.l2 = tk.Label(self.f2, text=(info[3]), font=('Calibri', 20, 'normal'), fg='white', bg='#3D3D3D',
                           wraplength=800).place(x=340, y=400)

        self.l4 = tk.Label(self.f2, text=(info[4]), font=('Calibri', 18, 'normal'), fg='white', bg='#3D3D3D').place(
            x=340, y=200)

        self.b1 = ImageTk.PhotoImage(file='FINAL FAVORITES.png')
        self.img1 = tk.Button(self.f2, command=self.add, image=self.b1, borderwidth=0, bg='#3D3D3D',
                              fg='#3D3D3D').place(x=19, y=910)

        self.b2 = ImageTk.PhotoImage(file='FINAL X.png')
        self.img2 = tk.Button(self.f2, command=self.Return, image=self.b2, borderwidth=0, bg='#3D3D3D').place(x=1815,
                                                                                                              y=910)

        self.b3 = tk.Button(self.f2, command=self.comments, text="Comments", borderwidth=2, bg='#3D3D3D',
                            fg='white').place(x=940, y=920)

        conn.commit()
        conn.close()

    # select * FROM movies 1 WHERE like%
    def add(self):

        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE  if not exists movies1 (
            movie_title DATATYPE text,
            movie_Year DATATYPE text,
            movie_Director text,
            movie_Plot text,
            movie_Actors DATATYPE text,
            poster DATATYPE blob
            )""")
        c.execute("SELECT * FROM movies1 WHERE movie_title =? ", (self.title,))
        items = c.fetchall()
        lst = []

        for item in items:
            lst.append(item)
        if len(lst) > 0:
            messagebox.showerror('Error', 'Film already listed at favorites!', parent=self.f2)
        else:
            c.execute("INSERT INTO movies1 VALUES (?,?,?,?,?,?)", (
                self.title, self.r1['Year'], self.r1['Director'], self.r1['Plot'], self.r1['Actors'],
                self.r1['Poster']))
            conn.commit()
            conn.close()

    def comments(self):

        conn = sq.connect("members.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists user_film_comments (
                            username DATATYPE text,
                            comments DATATYPE text,
                            movie_title DATATYPE text
                            )""")
        c.execute("SELECT * FROM user_film_comments WHERE movie_title = ?", (self.title,))
        items = c.fetchall()

        root = tk.Tk()
        root.title('Comments')
        root.iconbitmap('')
        root.configure(bg='#3D3D3D')
        root.geometry('1200x600')

        my_scrollbar = tk.Scrollbar(root)
        my_scrollbar.pack(side=tk.RIGHT, fill="y")
        # prepei na mpei ena xromataki mesa sta comments , ena poli anixto gkri
        self.txtbox = tk.Text(root, height=20, width=35,bg='#3D3D3D',fg='white', yscrollcommand=my_scrollbar.set)

        self.txtbox.pack(expand=0, fill=tk.BOTH)

        my_scrollbar.config(command=self.txtbox.yview)

        for item in items:
            self.txtbox.insert(tk.END, item[0] + " said:" + "\n" + item[1] + "\n")
        # episis emfanizete ena akiro koutaki enter text to opoio den kanei tpt , prp na aferethei
        self.entr = tk.Entry(root)
        self.entr.pack()

        b = tk.Button(root, text="Post", command=self.show, font=('Impact', 18), borderwidth=4, bg='#2d2d2d',
                      fg='white')
        b.pack()

        root.mainloop()

    def show(self):
        if self.entr.get() == "":pass
        else:
            conn = sq.connect("members.db")
            c = conn.cursor()
            c.execute("SELECT (username) FROM members ")
            textitems = self.entr.get()
            self.txtbox.insert(tk.END, self.name + " said:" + "\n" + textitems)
            c.execute("INSERT INTO user_film_comments (username,comments,movie_title) VALUES (?,?,?)",
                      (self.name, textitems, self.title))
            conn.commit()
            conn.close()


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
        # giati bgenei me background image wallpaper1.png kai giati den einai sosta stixismena ta logia , to button kai to enter label ??
        cnt = 0
        for item in items:
            print(item)
            cnt += 1
            if str(self.e1.get()) == item[0] and str(self.e2.get()) == item[1]:

                mylabel = tk.Label(self.root, text="You're Welcome " + str(self.e1.get()), font=('Calibri', 10, 'bold'),
                                   bg='#3D3D3D').place(x=20, y=20)

                self.f1.destroy()

                my_app = Myapp(self.root, self.name)

                self.root.mainloop()

            elif cnt == len(items):
                messagebox.showerror('Error', 'Wrong username or password!', parent=self.root)
                break

    def for_register(self):

        for widget in self.f1.winfo_children():
            widget.destroy()

        title = tk.Label(self.f1, text='Sign up to MyFILMS', font=('Impact', 33, 'bold'), fg='white',
                         bg='#111111').place(x=90, y=30)

        self.l = tk.Label(self.f1, text='Username', font=('Impact', 15, 'normal'), fg='white', bg='#111111').place(x=90,
                                                                                                                   y=140)

        self.l2 = tk.Label(self.f1, text='Password', font=('Impact', 15, 'normal'), fg='white', bg='#111111').place(
            x=90, y=210)

        self.entry = tk.Entry(self.f1, font=('Calibri', 15), bg='white')
        self.entry.place(x=90, y=170, width=350, height=35)

        self.entry2 = tk.Entry(self.f1, font=('Calibri', 15), bg='white', show="*")
        self.entry2.place(x=90, y=240, width=350, height=35)

        self.b = tk.Button(self.f1, text='Register', command=self.register, fg='white', bg='#3D3D3D',
                           font=('Impact', 20, 'normal')).place(x=90, y=320, width=180, height=40)

        self.b1 = tk.Button(self.f1, text='Back', command=self.back, fg='white', bg='#3D3D3D',
                            font=('Impact', 20, 'normal')).place(x=351, y=320, width=90, height=40)

    # an den valeis username k password, patisis register kai meta ksanapas me back sto logininterface kai pathseis login xoris na valeis username k kodiko , to programma trexei xoris na prp
    def register(self):
        if self.entry.get() == "":
            messagebox.showerror('Error', 'Input username and password!', parent=self.root)
            pass
        elif self.entry2.get() =="":
            messagebox.showerror('Error', 'Input username and password!', parent=self.root)
            pass
        else:
            self.name = self.entry.get()
            conn = sq.connect("members.db")
            c = conn.cursor()
            c.execute("SELECT * FROM members WHERE username =?", (self.entry.get(),))
            items = c.fetchall()
            lst = []
            for item in items:
                lst.append(item)
            if len(lst) > 0:
                print("Username already exists!")
            else:
                c.execute("INSERT INTO members(username,password) VALUES (?,?)",
                          (str(self.entry.get()), str(self.entry2.get())))
                conn.commit()
                conn.close()
                self.f1.destroy()
                my_app = Myapp(self.root, self.name)

                self.root.mainloop()

    def back(self):

        for widget in self.f1.winfo_children():
            widget.destroy()

        title = tk.Label(self.f1, text='Login to MyFILMS', font=('Impact', 35, 'bold'), fg='white', bg='#111111').place(
            x=90, y=30)

        desc = tk.Label(self.f1, text='Users login area', font=('Impact', 15, 'normal'), fg='white',
                        bg='#111111').place(x=90, y=100)

        lbl_user = tk.Label(self.f1, text='Username', font=('Impact', 15, 'normal'), fg='white', bg='#111111').place(
            x=90, y=140)
        self.e1 = tk.Entry(self.f1, font=('Calibri', 15), bg='white')
        self.e1.place(x=90, y=170, width=350, height=35)
        self.name = self.e1.get()

        lbl_pass = tk.Label(self.f1, text='Password', font=('Impact', 15, 'normal'), fg='white', bg='#111111').place(
            x=90, y=210)
        self.e2 = tk.Entry(self.f1, font=('Calibri', 15), bg='white', show="*")
        self.e2.place(x=90, y=240, width=350, height=35)

        register_btn = tk.Button(self.f1, text='New? Click for registration', command=self.for_register, bg='#111111',
                                 fg='red', bd=0, font=('Impact', 12)).place(x=90, y=290)

        login_btn = tk.Button(self.f1, text='Login', command=self.my_click, fg='white', bg='#3D3D3D',
                              font=('Impact', 20, 'bold')).place(x=90, y=320, width=180, height=40)

    def run(self):

        conn = sq.connect("members.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists members (
            username DATATYPE text,
            password DATATYPE text
            )""")
        conn.commit()
        conn.close

        self.root = tk.Tk()
        self.root.title('MyFILMS')
        self.root.geometry('1200x1200')

        self.bg = ImageTk.PhotoImage(file='FINAL WALLPAPER.jpg')
        self.bg_image = tk.Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.f1 = tk.Frame(self.root, bg='#111111')
        self.f1.place(x=150, y=150, height=398, width=508)

        title = tk.Label(self.f1, text='Login to MyFILMS', font=('Impact', 35, 'bold'), fg='white', bg='#111111').place(
            x=90, y=30)

        desc = tk.Label(self.f1, text='Users login area...', font=('Impact', 15, 'normal'), fg='white',
                        bg='#111111').place(x=90, y=100)

        lbl_user = tk.Label(self.f1, text='Username', font=('Impact', 15, 'normal'), fg='white', bg='#111111').place(
            x=90, y=140)

        self.e1 = tk.Entry(self.f1, font=('Calibri', 15), bg='white')
        self.e1.place(x=90, y=170, width=350, height=35)

        lbl_pass = tk.Label(self.f1, text='Password', font=('Impact', 15, 'normal'), fg='white', bg='#111111').place(
            x=90, y=210)
        self.e2 = tk.Entry(self.f1, font=('Calibri', 15), bg='white', show="*")
        self.e2.place(x=90, y=240, width=350, height=35)

        register_btn = tk.Button(self.f1, text='New?Sing up', command=self.for_register, bg='#111111',
                                 fg='red', bd=0, font=('Impact', 12)).place(x=90, y=290)

        login_btn = tk.Button(self.f1, text='Login', command=self.my_click, fg='white', bg='#3D3D3D',
                              font=('Impact', 20, 'bold')).place(x=90, y=320, width=180, height=40)
        self.root.bind('<Return>', lambda event:self.my_click())

        self.root.mainloop()


if __name__ == "__main__":
    Login()
