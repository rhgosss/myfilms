from tkinter import *



root = Tk()
root.title('Search bar')
root.configure(bg='#242526')
root.geometry("1199x600")


my_Label= Label(root, text='Search for a film...', font=( 'Impact', 40), bg ='#242526', fg='White')
my_Label.pack(pady=20)

my_entry = Entry(root, font=('consolas', 20))
my_entry.pack()


favorite_btn = PhotoImage(file="kardoula.png")
img = Button(root, command='' , image=favorite_btn , borderwidth = 0, bg='#242526').place(x=1100, y=10)



root.mainloop()



