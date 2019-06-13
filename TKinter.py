from tkinter import *

root = Tk(baseName='basic')



button1 = Button(root, text='submit', fg='red')
button2 = Button(root, text='submit', fg='blue')
button3 = Button(root, text='submit', fg='green')
button4 = Button(root, text='submit', fg='purple')
label1 = Label(root, text =  'Password', bg ='grey')


button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=1, column=1)
button4.grid(row=1, column=2)
label1.grid(row=0, column=3)





root.mainloop()
