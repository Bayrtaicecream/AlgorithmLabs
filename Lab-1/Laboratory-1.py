
try:
    with open('','r') as file:
        content = file.read()
        if content:
            print(content)
        else:
            print("file hooson baina")
except FileNotFoundError:
    print("file oldsongui")