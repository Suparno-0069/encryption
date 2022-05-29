# Console Aapplication

def encryptions(Str):  # Encrypting Function
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

    return Ans


def decryptions(Str):  # Decrypting Function
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

    return Ans


# Choices
print("""Enter 1 to Encryption,
Enter 2 for Decryption
""")

# Selecting Choice
ch = int(input("Enter your choice : "))

# Tacking Input
inp = input("Enter a String : ")

if ch == 1:
    opt = encryptions(inp)           # Generating Output for Encryption
    print("Input => Otput : ")
    print(f"{inp} => {opt}")         # Displaying Output
elif ch == 2:
    opt = decryptions(inp)           # Generating Output for Decryption
    print("Input => Otput : ")
    print(f"{inp} => {opt}")         # Displaying Output
else:
    print("Unknown Input!!")
