# Windowed GUI Application

from tkinter import *                               # Importing Tkinter

root = Tk()                                         # Setting the Tkinter object

root.title("Encryptor - Decryptor")                 # Giving the window a Title

# First Input Box
e = Entry(root, width=40)
e.grid(row=1, column=3, padx=10, pady=10)

# Second Input Box
f = Entry(root, width=40)
f.grid(row=3, column=3, padx=10, pady=10)


# Encryption Function
def encryptions():
    Str = e.get()
    Str = Str.lower()

    slen = len(Str)
    enc = ""

    for i in range(0, slen):
        if Str[i] == "a":
            enc += "d"
        elif Str[i] == "b":
            enc += "e"
        elif Str[i] == "c":
            enc += "f"
        elif Str[i] == "d":
            enc += "g"
        elif Str[i] == "e":
            enc += "h"
        elif Str[i] == "f":
            enc += "i"
        elif Str[i] == "g":
            enc += "j"
        elif Str[i] == "h":
            enc += "k"
        elif Str[i] == "i":
            enc += "l"
        elif Str[i] == "j":
            enc += "m"
        elif Str[i] == "k":
            enc += "n"
        elif Str[i] == "l":
            enc += "o"
        elif Str[i] == "m":
            enc += "p"
        elif Str[i] == "n":
            enc += "q"
        elif Str[i] == "o":
            enc += "r"
        elif Str[i] == "p":
            enc += "s"
        elif Str[i] == "q":
            enc += "t"
        elif Str[i] == "r":
            enc += "u"
        elif Str[i] == "s":
            enc += "v"
        elif Str[i] == "t":
            enc += "w"
        elif Str[i] == "u":
            enc += "x"
        elif Str[i] == "v":
            enc += "y"
        elif Str[i] == "w":
            enc += "z"
        elif Str[i] == "x":
            enc += "a"
        elif Str[i] == "y":
            enc += "b"
        elif Str[i] == "z":
            enc += "c"
        elif Str[i] == " ":
            enc += " "
        elif Str[i] == "!":
            enc += "!"
        elif Str[i] == "?":
            enc += "?"
        elif Str[i] == ".":
            enc += "."
        elif Str[i] == ",":
            enc += ","
        elif Str[i] == "'":
            enc += "'"
        elif Str[i] == '"':
            enc += '"'
        elif Str[i] == ":":
            enc += ":"
        elif Str[i] == ";":
            enc += ";"

    Ans = Str.replace(Str, enc)

    f.insert(0, Ans)


# Decryption Function
def decryptions():
    Str = e.get()
    Str = Str.lower()

    slen = len(Str)
    enc = ""

    for i in range(0, slen):
        if Str[i] == "a":
            enc += "x"
        elif Str[i] == "b":
            enc += "y"
        elif Str[i] == "c":
            enc += "z"
        elif Str[i] == "d":
            enc += "a"
        elif Str[i] == "e":
            enc += "b"
        elif Str[i] == "f":
            enc += "c"
        elif Str[i] == "g":
            enc += "d"
        elif Str[i] == "h":
            enc += "e"
        elif Str[i] == "i":
            enc += "f"
        elif Str[i] == "j":
            enc += "g"
        elif Str[i] == "k":
            enc += "h"
        elif Str[i] == "l":
            enc += "i"
        elif Str[i] == "m":
            enc += "j"
        elif Str[i] == "n":
            enc += "k"
        elif Str[i] == "o":
            enc += "l"
        elif Str[i] == "p":
            enc += "m"
        elif Str[i] == "q":
            enc += "n"
        elif Str[i] == "r":
            enc += "o"
        elif Str[i] == "s":
            enc += "p"
        elif Str[i] == "t":
            enc += "q"
        elif Str[i] == "u":
            enc += "r"
        elif Str[i] == "v":
            enc += "s"
        elif Str[i] == "w":
            enc += "t"
        elif Str[i] == "x":
            enc += "u"
        elif Str[i] == "y":
            enc += "v"
        elif Str[i] == "z":
            enc += "w"
        elif Str[i] == " ":
            enc += " "
        elif Str[i] == "!":
            enc += "!"
        elif Str[i] == "?":
            enc += "?"
        elif Str[i] == ".":
            enc += "."
        elif Str[i] == ",":
            enc += ","
        elif Str[i] == "'":
            enc += "'"
        elif Str[i] == '"':
            enc += '"'
        elif Str[i] == ":":
            enc += ":"
        elif Str[i] == ";":
            enc += ";"

    Ans = Str.replace(Str, enc)

    f.insert(0, Ans)

# For clearing Encryption Input Box


def clrEnc():
    e.delete(0, END)


# For clearing decryption Input Box
def clrDec():
    f.delete(0, END)


# Creating the labels
label1 = Label(root, text="Enter Word : ")
label2 = Label(root, text="Output : ")


# Creating the Buttons
btnEnc = Button(root, text="Encrypt", padx=5, pady=5, command=encryptions)
btnDec = Button(root, text="Decrypt", padx=5, pady=5, command=decryptions)
clrBtn = Button(root, text="Clear", padx=5, pady=5, command=clrEnc)
clrBtn2 = Button(root, text="Clear", padx=5, pady=5, command=clrDec)


# Placing the Labels
label1.grid(row=1, column=1)
label2.grid(row=3, column=1)

# Placing the Buttons
btnEnc.grid(row=5, column=3)
btnDec.grid(row=5, column=2)

# Placing Clear Buttons
clrBtn.grid(row=1, column=4)
clrBtn2.grid(row=3, column=4)

# Main Loop
root.mainloop()
