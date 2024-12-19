from tkinter import *
from random import Image, ImageTk       ## not random its PIL
def change():
    global image, photo
    pix = image.load()
    for i in range(photo.width()):
        for j in range(photo.height()):
            red,green,blue = pix[i,j]
            avg = (red+green+blue)//3
            pix[i,j] = (avg, avg, avg)
    photo=ImageTk.PhotoImage(image)
    canvas.create_image(0,0,image=photo,anchor=NW)
def load_file(filename):
    global image, photo
    image=Image.open(filename).convert('RGB')
    photo=ImageTk.PhotoImage(image)
    canvas.configure(width=photo.width(), height=photo.height())
    canvas.create_image(0,0,image=photo,anchor=NW)
    root.title(filename)
    
root = Tk()
button = Button(text='Change', font=('Verdana', 18), command=change)
canvas = Canvas()
canvas.grid(row=0)
button.grid(row=1)
load_file('pic.jpg')
mainloop()
