import requests as r
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3 as sq
import os


class Myapp:
    def __init__(self, root):
        self.f1 = tk.Frame(root)
        self.f1.grid()
        self.bt1 = tk.Button(self.f1, text="favorite movies", font="Arial 20", command=self.favorite_movies)
        self.bt1.grid(row=2, column=0)
        self.bt2 = tk.Button(self.f1, text="search a movie", font="Arial 20", command=self.for_search)
        self.bt2.grid(row=2, column=1)
        self.buttonquit1 = tk.Button(self.f1, text="Exit", command=root.destroy)
        self.buttonquit1.grid()
    def Return(self):
        for widget in self.f1.winfo_children():
            widget.destroy()
        self.bt1 = tk.Button(self.f1, text="favorite movies", font="Arial 20", command=self.favorite_movies)
        self.bt1.grid(row=2, column=0)
        self.bt2 = tk.Button(self.f1, text="search a movie", font="Arial 20", command=self.for_search)
        self.bt2.grid(row=2, column=1)
    def for_search(self):
        for widget in self.f1.winfo_children():
            widget.destroy()
        self.e = tk.Entry(self.f1, font="Arial 24")
        self.e.grid()
        self.b = tk.Button(self.f1, text="search", font="Arial 20", command=self.search)
        self.b.grid()
        self.b2 = tk.Button(self.f1, text="return", command=self.Return)
        self.b2.grid()

    def search(self):
        self.b2 = tk.Button(self.f1, text="return", command=self.Return)
        self.b2.grid()
        self.title = self.e.get()
        if self.title:
            url = f"http://www.omdbapi.com/?t={self.title}&apikey=2692ec2"
            self.r1 = r.get(url)
            self.r1 = self.r1.json()
            print(self.r1)
            self.r2 = r.get(self.r1["Poster"])

            with open(str(self.title) + ".jpg", "wb") as f:
                f.write(self.r2.content)
            self.img = ImageTk.PhotoImage(Image.open(str(self.title) + ".jpg"))
            print(self.img)
            self.l = tk.Label(self.f1, text=(self.r1["Year"] + self.r1["Actors"]))
            self.l.grid()
            self.l1 = tk.Label(self.f1, image=self.img)
            self.l1.grid()
            self.b1 = tk.Button(self.f1, text=" + ", command=self.add)
            self.b1.grid()
            self.b2 = tk.Button(self.f1, text="return", command=self.Return)
            self.b2.grid()

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
            print("Movie already exists in favorites")
        else:
            c.execute("INSERT INTO movies1 VALUES (?,?,?,?)",
                      (self.title, self.r1['Year'], self.r1['Actors'], self.r1['Poster']))
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
        cnt = 0
        for item in items:
            print(item)
            cnt += 1
            if str(self.e1.get()) == item[0] and str(self.e2.get()) == item[1]:
                mylabel = tk.Label(self.root, text="Καλως ορισες " + str(self.e1.get()))
                mylabel.grid()
                self.f1.destroy()
                my_app = Myapp(self.root)
                self.root.mainloop()
            elif cnt == len(items):
                l2 = tk.Label(self.root, text="Wrong username or password")
                l2.grid()
                break

    def for_register(self):
        for widget in self.f1.winfo_children():
            widget.destroy()
        self.l = tk.Label(self.f1, text="username: ")
        self.l2 = tk.Label(self.f1, text="password: ")
        self.l.grid(row=0, column=0)
        self.l2.grid(row=1, column=0)
        self.entry = tk.Entry(self.f1)
        self.entry2 = tk.Entry(self.f1, show="*")
        self.entry.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.b = tk.Button(self.f1, text="Register", command=self.register)
        self.b.grid()

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
            c.execute("INSERT INTO members VALUES (?,?)", (str(self.entry.get()), str(self.entry2.get())))
            conn.commit()
            conn.close()
            self.f1.destroy()
            my_app = Myapp(self.root)
            self.root.mainloop()

    def run(self):
        self.root = tk.Tk()
        self.root.title(" My films ")
        self.root.iconbitmap(r"cin.ico")
        self.root.geometry("700x450")
        self.f1 = tk.Frame(self.root)
        self.f1.grid()
        self.label1 = tk.Label(self.f1, text="username: ")
        self.label2 = tk.Label(self.f1, text="password: ")
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.e1 = tk.Entry(self.f1)
        self.e2 = tk.Entry(self.f1, show="*")
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.mybutton = tk.Button(self.f1, text="Login", command=self.my_click)
        self.mybutton.grid(row=2, column=0)
        self.button2 = tk.Button(self.f1, text="Register", command=self.for_register)
        self.button2.grid(row=2, column=1)
        self.buttonquit = tk.Button(self.f1, text="Close", command=self.root.quit)
        self.buttonquit.grid()
        self.root.mainloop()


if __name__ == "__main__":
    Login()