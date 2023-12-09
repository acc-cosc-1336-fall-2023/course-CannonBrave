import tkinter
import tkinter.messagebox

class Form:
        def __init__(self):
            self.__form = tkinter.Tk() #creates form

            self.__button = tkinter.Button(self.__form, text='Click me!', command=self.display_dialog)
            self.__button.pack()

            self.__amount_entry = tkinter.Entry(self.__form, width=10)
            self.__amount_entry.pack()

            self.__label = tkinter.Label(self.__form, text="Hello World! ")
            self.__label.pack(side='left')


            self.__form.mainloop()

        def display_dialog(self):
            tkinter.messagebox.showinfo('Response', 'You clicked the button...')
            self.__label['text'] = 'Hello World, ' + str(self.__amount_entry.get())