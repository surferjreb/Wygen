from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox
from gen_manager import GenManager
from validate_card import ValidateCard


FONT = ('Arial', 14, 'bold')
TITLE_FONT = ('Arial', 18, 'bold')


class GenMenu:
    def __init__(self):
        self.window = Tk()
        self.manager = GenManager()
        self.validate = ValidateCard()
        self.fac_code = None
        self.codeStart = None
        self.codeEnd = None

    def setup_menu(self):
        self.window.title('Wiegand Generator')
        self.window.minsize(width=300, height=500)
        self.window.config(padx=10, pady=20)
        # row sizes
        self.window.rowconfigure(0, weight=2)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=1)
        # column sizes
        self.window.columnconfigure(1, weight=1, pad=2)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)

    def gen_menu(self):
        self.setup_menu()
        # Labels
        title = Label(text='Wiegand 26 bit Generator', font=TITLE_FONT)
        title.grid(column=0, row=0, sticky='N', columnspan=4)
        title.config(padx=25, pady=25)
        facility = Label(text='Facility Code:', font=FONT)
        facility.grid(column=0, row=1, sticky='W')
        card_code = Label(text='Card Number:', font=FONT)
        card_code.grid(column=0, row=3, sticky='W')
        to = Label(text='to', font=FONT)
        to.grid(column=2, row=3, sticky='W')
        description = Label(text='*Enter a range of cards below you '
                            'want to generate',
                            font=('Arial', 12, 'bold'))
        description.grid(column=0, row=2, columnspan=4)
        # Entry
        self.fac_code = Entry(width=4)
        self.fac_code.grid(column=1, row=1, sticky='W')
        self.codeStart = Entry(width=5)
        self.codeStart.grid(column=1, row=3, sticky='W')
        self.codeEnd = Entry(width=5)
        self.codeEnd.grid(column=3, row=3, sticky='W')
        # Button
        generate = Button(text='Generate', command=self.gen_clicked)
        generate.grid(column=2, row=4, columnspan=2)
        clear_button = Button(text='Clear', command=self.clear_fields)
        clear_button.grid(column=0, row=4, columnspan=2)

        self.window.mainloop()

    def gen_clicked(self):
        fac_code = self.check_fac(self.fac_code.get())
        card_start = self.check_card(self.codeStart.get())
        card_end = self.check_card(self.codeEnd.get())

        for i in range(card_start, (card_end + 1)):
            self.manager.gen_card_bin(i, fac_code)

        self.manager.output_csv()

    def check_fac(self, fac_code):
        try:
            fac = int(fac_code)
            if self.validate.check_fac_code(fac):
                return fac
            else:
                raise ValueError()
        except ValueError:
            messagebox.showerror('Error', 'Please correct the facility'
                                 ' code')

    def check_card(self, cardNumber):
        try:
            card = int(cardNumber)
            if self.validate.check_card_number(card):
                return card
            else:
                raise ValueError()
        except ValueError:
            messagebox.showerror('Error',
                                 'Please correct the card range')

    def clear_fields(self):
        self.fac_code.delete(0, 'end')
        self.codeStart.delete(0, 'end')
        self.codeEnd.delete(0, 'end')
