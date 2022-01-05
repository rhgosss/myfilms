from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Search bar')
root.iconbitmap('')
root.configure(bg='#3D3D3D')
root.geometry("1199x600")


#h epikefalida
my_Label= Label(root, text='Search for a film...', font=( 'Impact', 40), bg ='#3D3D3D', fg='White')
my_Label.pack(pady=20)

#to search bar
my_entry = Entry(root, font=('consolas', 20) ,borderwidth=4 , fg='white', bg='#2d2d2d')
my_entry.pack()

#mia eikona megethintikou akou etsi gia tin tsaxpinia (simpliroste to)
img_megethintikos = ImageTk.PhotoImage(Image.open("megethintikos.png"))

#gia to favorite button
favorite_btn = PhotoImage(file="kardoula.png")
img_kardoula = Button(root, command='' , image=favorite_btn , borderwidth = 0, bg='#3D3D3D').place(x=1140, y=545)

#gia to exit 
x_btn = PhotoImage(file="x.png")
img_x = Button(root, command=root.quit , image=x_btn , borderwidth=0, bg='#3D3D3D').place(x=578 , y=530 )


root.mainloop()
