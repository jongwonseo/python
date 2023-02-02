from tkinter import *

def one():
  print('aaaa')
  
def two():
  window.after(3000, one)
  

window = Tk()
button = Button(command=two)
button.pack()

window.after(3000, one)

window.mainloop()
