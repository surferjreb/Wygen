from tkinter import *
from gen_menu import GenMenu


FONT = ('Arial', 14, 'bold')
TITLE_FONT = ('Arial', 20, 'bold')


class GenStartMenu:
    def __init__(self):
        self.window = Tk()
        self.start_button = None
        self.w_menu = None

    def config_menu(self):
        self.window.minsize(width=300, height=500)
        self.window.title('Wiegand Generator')
        self.window.config(padx=10, pady=20)
        # row
        self.window.rowconfigure(0, weight=1)
        # self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=2)
        self.window.rowconfigure(4, weight=2)
        # column
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)


    def gen_start(self):
        self.config_menu()
        title = Label(text='Welcome', font=TITLE_FONT)
        title.grid(column=0, row=0, columnspan=3)
        to = Label(text='to', font=FONT)
        to.grid(column=0, row=1, sticky=N, columnspan=3)
        p_title = Label(text='WyGen26', font=TITLE_FONT)
        p_title.grid(column=0, row=2, sticky=N, columnspan=3)
        start_button = Button(text='Start', command=self.start_clicked)
        start_button.grid(column=0, row=3, sticky=N)
        exit_button = Button(text='Exit', command=self.exit_menu)
        exit_button.grid(column=2, row=3, sticky=N)

    def exit_menu(self):
        self.window.destroy()

    def start_clicked(self):
        self.w_menu = GenMenu()
        self.window.destroy()
        self.w_menu.gen_menu()

    def show_start(self):
        self.gen_start()
        self.window.mainloop()


menu = GenStartMenu()
menu.show_start()
