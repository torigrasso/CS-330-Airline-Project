from tkinter import*


Login = Tk()
Login.title('Login')
a = Label(Login, text = 'Please, Login').grid(columnspan = 2)
Done = Button(Login, text = 'Done', fg = 'red',command = Login.quit).grid(row = 3, column = 4)
Label(Login, text='Username').grid(row = 1,column = 0)
username = Entry(Login).grid(row = 1 , column = 1)
Label(Login, text='Password').grid(row = 2 , column = 0)
password = Entry(Login).grid(row = 2, column = 1)
a()

Login.mainloop()