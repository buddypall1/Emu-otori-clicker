from tkinter import *
from tkinter import ttk
import pygame
from cryptography.fernet import Fernet, InvalidToken


Wonderhoys = 0
wps = 0
clickpower = 1
#WPS values
firstupgrpay= 10
scndupgrpay = 1000
#Click values
firstclickupgrpay = 10


# TODO: Fix UI elements not being centered, finish upgrades, add saving for click power


###### DECRYPTION/ENCRYPTION START ###### (IDK WHAT MOST OF THIS MEANS I COPIED THE DECRYPTION LMAO)
key = "T5rjXXmVwh_t8-mqA7gMSlqBNM3lXegNHQXDTWQsxRQ="
fernet = Fernet(key)


def load_encrypted(filename):
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
            return int(fernet.decrypt(encrypted_data).decode())
    except (FileNotFoundError, ValueError, InvalidToken):
        print(f"Error reading or decrypting {filename}. Resetting to 0.")
        return 0


def save_encrypted(filename, value):
    encrypted_data = fernet.encrypt(str(value).encode())
    with open(filename, "wb") as file:
        file.write(encrypted_data)


Wonderhoys = load_encrypted("Data\Wonderhoys.txt")
wps = load_encrypted("Data\WPS.txt")
firstupgrpay = load_encrypted("Data\stpg.txt")

def on_closing():
    global Wonderhoys, wps
    save_encrypted("Data\Wonderhoys.txt", Wonderhoys)
    save_encrypted("Data\WPS.txt", wps)
    save_encrypted("Data\stpg.txt", firstupgrpay)
    window.destroy()
###### DECRYPTION/ENCRYPTION END ######



# main clicker button GUI
window = Tk()
window.title("Emu Otori Clicker")
window.resizable(0,0) 
window.geometry("950x700")
window.configure(background= "Pink")
window.iconbitmap("wondahoy.ico")
pygame.mixer.init()

window.protocol("WM_DELETE_WINDOW", on_closing)

wondahoy = pygame.mixer.Sound("SFX\WONDERHOY SOUND EFFECT (no background music).mp3")
wondahoy.set_volume(0.3)
def clickevent():
    global Wonderhoys, clickpower
    Wonderhoys += clickpower
    print(Wonderhoys)
    Wonderhoyammount.config(text=f"Wonderhoys: {Wonderhoys}")
    wondahoy.play(loops=0)

# WPS upgrades
def firstupgr():
    global Wonderhoys, wps, firstupgrpay
    if Wonderhoys >= firstupgrpay:
        Wonderhoys -= firstupgrpay
        firstupgrpay += firstupgrpay + 5
        upgrade1.config(text=f"Emu Helper = {firstupgrpay} WH\nadds 2 AWPS")
        Wonderhoyammount.config(text=f"Wonderhoys: {Wonderhoys}")
        wps += 2
        wpslabel.config(text=f"WPS: {wps}")
        print(wps)
    else:
        pass
def scndupgr():
    global Wonderhoys, wps, scndupgrpay
    if Wonderhoys >= scndupgrpay:
        Wonderhoys -= scndupgrpay
        scndupgrpay += scndupgrpay + 5
        upgrade2.config(text=f"price= {scndupgrpay}")
        Wonderhoyammount.config(text=f"Wonderhoys: {Wonderhoys}")
        wps += 5
        wpslabel.config(text=f"WPS: {wps}")
        print(wps)
    else:
        pass

# Click Upgrades
def cfrstupg():
    global Wonderhoys, clickpower, firstclickupgrpay
    if Wonderhoys >= firstclickupgrpay:
        Wonderhoys -= firstclickupgrpay
        firstclickupgrpay += firstclickupgrpay + 10
        cpsupgrade1.config(text=f"price= {firstclickupgrpay}")
        Wonderhoyammount.config(text=f"Wonderhoys: {Wonderhoys}")
        cpslabel.config(text=f"Clicks/s: {clickpower}")
        clickpower += 2
    else:
        pass

# main clicker button GUI
emuherself = PhotoImage(file="Images\kvxwxs89gqj81-ezgif.com-webp-to-png-converter.png")
emuherselflabel= Label(image= emuherself)
wonderhoy = Button(window, image= emuherself, command= clickevent, borderwidth=0, background="Pink", activebackground="Pink")
wonderhoy.pack(pady=160)


# Click counter 
Wonderhoyammount = Label(window, text=f"Wonderhoys: {Wonderhoys}", font=("Arial", 35, "bold"), fg='#e236be', background="Pink", activebackground="Pink")
Wonderhoyammount.place(x=300,y=50)
wpslabel = Label(window, text=f"WPS: {wps}", font= ("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
wpslabel.place(x=444,y=110)
cpslabel = Label(window, text=f"Clicks/s: {clickpower}", font= ("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
cpslabel.place(x=444, y=132)

# AWP Upgrades GUI
upgr= Label(window, text="WPS\nUpgrades", font=("Arial", 25, 'bold'),fg='#e236be', background="pink", activebackground="Pink",relief='solid')
upgr.place(x=750, y=100)
upgrade1 = Button(window, command= firstupgr, text=f"Emu Helper = {firstupgrpay} WH\nadds 2 AWPS", bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5)
upgrade1.place(x=740,y=200)
emuchibiparent = PhotoImage(file="Images\Emu_Casual_chibi.png")
emuchibi = Label(window, image= emuchibiparent, background="Pink")
emuchibi.place(x=624,y=185)
upgrade2 = Button(window, text=f"Dummytext\ntext", command=scndupgr, bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5 )
upgrade2.place(x=740, y=320)
upgrade3 = Button(window, text=f"Dummytext\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5 )
upgrade3.place(x=740, y=440)
upgrade4 = Button(window, text=f"Dummytext\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5 )
upgrade4.place(x=740, y=560)

# CPS Upgrades GUI
cpsupgr = Label(window, text="Click\nUpgrades", font=("Arial", 25, 'bold'),fg='#e236be', background="pink", activebackground="Pink",relief='solid')
cpsupgr.place(x=35, y=100)
cpsupgrade1 = Button(window, command= cfrstupg, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5)
cpsupgrade1.place(x=27, y=200)
cpsupgrade2 = Button(window, command= firstupgr, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5)
cpsupgrade2.place(x=27, y=320)
cpsupgrade3 = Button(window, command= firstupgr, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5)
cpsupgrade3.place(x=27, y=440)
cpsupgrade4 = Button(window, command= firstupgr, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial",10,"bold"),borderwidth=5, width=20,height=5)
cpsupgrade4.place(x=27, y=560)

def wpsloop():
    global wps, Wonderhoys
    print("clicking")
    Wonderhoyammount.config(text=f"Wonderhoys: {Wonderhoys}")
    print(f"wps is {wps}")
    Wonderhoys = Wonderhoys + wps
    window.after(1000, wpsloop)  

# Click Upgrades GUI


wpsloop()

window.mainloop()