import winsound

type= input("Which sound:")

if type == "Beep":
    winsound.Beep(1000,3000)

if type == "MessageBeep":
    winsound.MessageBeep(type=0)
    
