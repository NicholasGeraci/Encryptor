"""A simple GUI to encrypt files."""
from encryptor import encrypt, decrypt
from tkinter import *


def encryptor():
    """Encrypts file."""
    path = path_entry.get()
    encrypt(path)
    done_label['text'] = 'Done.'


def decryptor():
    """Decrypts file."""
    path = path_entry.get()
    decrypt(path)
    done_label['text'] = 'Done.'


def clear():
    """Clears the widgets."""
    path_entry.delete(0, END)
    done_label['text'] = ''


if __name__ == '__main__':
    window = Tk()
    window.geometry('240x150')
    window.minsize(240, 150)
    window.maxsize(240, 150)

    top_frame = Frame()
    path_label = Label(top_frame, text='Path:')
    empty_label = Label(top_frame, text='')
    clear_button = Button(top_frame, text='Clear', command=clear)

    path_entry = Entry()

    endecrypt_frame = Frame()
    encrypt_button = Button(endecrypt_frame, text='Encrypt', command=encryptor)
    decrypt_button = Button(endecrypt_frame, text='Decrypt', command=decryptor)

    done_label = Label(text='')

    top_frame.pack()
    path_label.pack(side=LEFT, pady=5)
    empty_label.pack(side=LEFT, padx=63)
    clear_button.pack(side=LEFT, pady=5)

    path_entry.pack(fill=X, padx=10)

    endecrypt_frame.pack()
    encrypt_button.pack(side=LEFT, pady=10, padx=10)
    decrypt_button.pack(side=LEFT, pady=10, padx=10)

    done_label.pack()

    window.mainloop()

