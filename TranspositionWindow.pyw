import tkinter
import transposition
from tkinter import scrolledtext


transposition = transposition.Transposition()


# create window.
window = tkinter.Tk()
window.title('transposition')
window.resizable(False, False)
color = 'white'
window.configure(bg=color)


is_upper = tkinter.BooleanVar()
upper_checkbutton = tkinter.Checkbutton(window, text='upper case.', variable=is_upper, bg=color)
upper_checkbutton.grid(row=0, column=0, sticky=tkinter.W)

is_lower = tkinter.BooleanVar()
lower_checkbutton = tkinter.Checkbutton(window, text='lower case.', variable=is_lower, bg=color)
lower_checkbutton.select()
lower_checkbutton.grid(row=1, column=0, sticky=tkinter.W)

is_alpha = tkinter.BooleanVar()
alpha_checkbutton = tkinter.Checkbutton(window, text='alphabetic', variable=is_alpha, bg=color)
alpha_checkbutton.grid(row=2, column=0, sticky=tkinter.W)

is_number = tkinter.BooleanVar()
number_checkbutton = tkinter.Checkbutton(window, text='number', variable=is_number, bg=color)
number_checkbutton.grid(row=3, column=0, sticky=tkinter.W)

is_other = tkinter.BooleanVar()
other_checkbutton = tkinter.Checkbutton(window, text='special character:', variable=is_other, bg=color)
other_checkbutton.grid(row=4, column=0, sticky=tkinter.W)

other = tkinter.StringVar()
other_Entry = tkinter.Entry(window, width=25, textvariable=other, relief=tkinter.SOLID)
other_Entry.grid(row=5, column=0, columnspan=2, sticky=tkinter.W)


def set_filter():
    conditions = list()
    if is_upper.get():
        conditions.append(lambda s: s.isupper())
    if is_lower.get():
        conditions.append(lambda s: s.islower())
    if is_alpha.get():
        conditions.append(lambda s: s.isalpha())
    if is_number.get():
        conditions.append(lambda s: s.isnumeric())
    if is_other.get():
        # # filter the others from any duplication in others conditions.
        # f_other = str()
        # other1 = other.get()
        # for i in other1:
        #     for condition in conditions:
        #         if not condition(i):
        #             f_other += i
        # conditions.append(lambda s: s in f_other)
        conditions.append(lambda s: s in other.get())
    transposition.set_filter(conditions)


ok_language_button = tkinter.Button(window, text='OK', command=set_filter)
ok_language_button.grid(row=6, column=0, columnspan=2, sticky=tkinter.EW)


key_label = tkinter.Label(window, text='key:', bg=color)
key_label.grid(row=7, column=0, sticky=tkinter.W)

key = tkinter.StringVar()
key_entry = tkinter.Entry(window, width=25, textvariable=key, relief=tkinter.SOLID)
key_entry.grid(row=8, column=0, sticky=tkinter.W)


def set_key():
    transposition.set_key(key.get())


ok_key_button = tkinter.Button(window, text='OK', command=set_key)
ok_key_button.grid(row=9, column=0, columnspan=2, sticky=tkinter.EW)


set_data_scrolled_text = scrolledtext.ScrolledText(window, width=30, wrap=tkinter.WORD, font=10)
set_data_scrolled_text.grid(row=0, column=2, rowspan=8)


def set_data():
    transposition.set_plan_text(set_data_scrolled_text.get('1.0', 'end-1c'))


set_data_button = tkinter.Button(window, text='set data', command=set_data)
set_data_button.grid(row=9, column=2, sticky=tkinter.EW)

encrypt_scrolled_text = scrolledtext.ScrolledText(window, width=30, font=10)
encrypt_scrolled_text.grid(row=0, column=3, rowspan=8)
# encrypt_scrolled_text.config(bg='blue')


def encrypt():
    encrypt_scrolled_text.delete(1.0, tkinter.END)
    encrypt_scrolled_text.insert(tkinter.INSERT, transposition.encrypt())


encrypt_button = tkinter.Button(window, text='encrypt', command=encrypt)
encrypt_button.grid(row=9, column=3, sticky=tkinter.NSEW)

decrypt_scrolled_text = scrolledtext.ScrolledText(window, width=30, font=10)
decrypt_scrolled_text.grid(row=0, column=4, rowspan=8)


def decrypt():
    decrypt_scrolled_text.delete(1.0, tkinter.END)
    decrypt_scrolled_text.insert(tkinter.INSERT, transposition.decrypt())


decrypt_button = tkinter.Button(window, text='decrypt', command=decrypt)
decrypt_button.grid(row=9, column=4, sticky=tkinter.NSEW)

# show.
window.mainloop()
