from tkinter import *
from tkinter import ttk
import pygame
import pickle
from numerize import numerize

Wonderhoys = 0
wps = 0
clickpower = 1
# WPS values
firstupgrpay = 10
scndupgrpay = 1000
# Click values
firstclickupgrpay = 10



# TODO: Fix UI elements not being centered, finish upgrades, add saving for click power

###### DECRYPTION/ENCRYPTION START ###### (IDK WHAT MOST OF THIS MEANS I COPIED THE DECRYPTION LMAO)
saveloc = "Data/game_data.dat"

def load_data():
    try:
        with open(saveloc, "rb") as file:
            data = pickle.load(file)
        return data
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        print("Error loading data or file not found. Initializing default values.")
        return {
            "Wonderhoys": 0,
            "wps": 0,
            "firstupgrpay": 10,
            "scndupgrpay": 1000,
            "firstclickupgrpay": 10,
            "clickpower": 1,
        }

def save_data():
    data = {
        "Wonderhoys": Wonderhoys,
        "wps": wps,
        "firstupgrpay": firstupgrpay,
        "scndupgrpay": scndupgrpay,
        "firstclickupgrpay": firstclickupgrpay,
        "clickpower": clickpower,
    }
    with open(saveloc, "wb") as file:
        pickle.dump(data, file)

game_data = load_data()

Wonderhoys = game_data["Wonderhoys"]
wps = game_data["wps"]
firstupgrpay = game_data["firstupgrpay"]
scndupgrpay = game_data["scndupgrpay"]
firstclickupgrpay = game_data["firstclickupgrpay"]
clickpower = game_data["clickpower"]

def on_closing():
    save_data()
    window.destroy()
###### DECRYPTION/ENCRYPTION END ######

# main clicker button GUI
window = Tk()
window.title("Emu Otori Clicker")
window.resizable(0, 0)
window.geometry("950x700")
window.configure(background="Pink")
window.iconbitmap("wondahoy.ico")
pygame.mixer.init()

window.protocol("WM_DELETE_WINDOW", on_closing)

wondahoy = pygame.mixer.Sound("SFX/WONDERHOY SOUND EFFECT (no background music).mp3")
wondahoy.set_volume(0.3)

def clickevent():
    global Wonderhoys, clickpower
    Wonderhoys += clickpower
    print(Wonderhoys)
    update_wonderhoy_label()
    wondahoy.play(loops=0)

# WPS upgrades
def firstupgr():
    global Wonderhoys, wps, firstupgrpay
    if Wonderhoys >= firstupgrpay:
        Wonderhoys -= firstupgrpay
        firstupgrpay += firstupgrpay + 5
        update_wonderhoy_label()
        wps += 2
        wpslabel.config(text=f"WPS: {wps}")
        print(wps)


def scndupgr():
    global Wonderhoys, wps, scndupgrpay
    if Wonderhoys >= scndupgrpay:
        Wonderhoys -= scndupgrpay
        scndupgrpay += scndupgrpay + 5
        update_wonderhoy_label()
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
        cpsupgrade1.config(text=f"Miku Helper \n {firstclickupgrpay}")
        update_wonderhoy_label()
        cpslabel.config(text=f"Clicks: {clickpower}")
        clickpower += 2
        
def update_wonderhoy_label():
    global Wonderhoys, wps,clickpower,firstupgrpay, scndupgrpay
    readable_wonderhoys = numerize.numerize(Wonderhoys)
    readable_wpsupg1 = numerize.numerize(firstupgrpay)
    readable_wpsupg2 = numerize.numerize(scndupgrpay)
    Wonderhoyammount.config(text=f"Wonderhoys:\n{readable_wonderhoys}")
    # WPS upgrade labels
    upgrade1.config(text=f"Emu Helper\n\n{readable_wpsupg1} WH\n\nadds 2 WPS")
    upgrade2.config(text=f"Tsukasa Helper\n\n{readable_wpsupg2} WH\n\nadds 5 WPS")


def addwonderhoys():
    global Wonderhoys
    Wonderhoys = Wonderhoys * 50 

def removewonderhoys():
    global Wonderhoys
    Wonderhoys = Wonderhoys - Wonderhoys


# main clicker button GUI
emuherself = PhotoImage(file="Images\kvxwxs89gqj81-ezgif.com-webp-to-png-converter.png")
emuherselflabel = Label(image=emuherself)
wonderhoy = Button(window, image=emuherself, command=clickevent, borderwidth=0, background="Pink", activebackground="Pink")
wonderhoy.place(x=(950/2) - (296/2), y=(700/2) - (256/2)) # 950x700
addwonds = Button(window, command= addwonderhoys, text="Add wonds")
remwonds = Button(window, command= removewonderhoys, text="remove wonds")



# Click counter 
Wonderhoyammount = Label(window, text=f"Wonderhoys:\n{numerize.numerize(Wonderhoys)}", font=("Arial", 35, "bold"), fg='#e236be', background="Pink", activebackground="Pink")
Wonderhoyammount.place(x=330, y=50)
wpslabel = Label(window, text=f"WPS: {wps}", font=("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
wpslabel.place(x=435, y=160)
cpslabel = Label(window, text=f"Clicks: {clickpower}", font=("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
cpslabel.place(x=435, y=182)

# WPS Upgrades GUI
upgr = Label(window, text="WPS\nUpgrades", font=("Arial", 25, 'bold'), fg='#e236be', background="pink", activebackground="Pink", relief='solid')
upgr.place(x=750, y=100)
upgrade1 = Button(window, command=firstupgr, text=f"Emu Helper = {firstupgrpay} WH\nadds 2 WPS", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade1.place(x=740, y=200)
emuchibiparent = PhotoImage(file="Images/Emu_Casual_chibi.png")
emuchibi = Label(window, image=emuchibiparent, background="Pink")
emuchibi.place(x=624, y=185)
upgrade2 = Button(window, text=f"Tsukasa Helper\n{scndupgrpay} WH\nadds 5 WPS", command=scndupgr, bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade2.place(x=740, y=320)
upgrade3 = Button(window, text=f"Dummytext\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade3.place(x=740, y=440)
upgrade4 = Button(window, text=f"Dummytext\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade4.place(x=740, y=560)

# CPS Upgrades GUI
cpsupgr = Label(window, text="Click\nUpgrades", font=("Arial", 25, 'bold'), fg='#e236be', background="pink", activebackground="Pink", relief='solid')
cpsupgr.place(x=35, y=100)
cpsupgrade1 = Button(window, command=cfrstupg, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade1.place(x=27, y=200)
cpsupgrade2 = Button(window, command=firstupgr, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade2.place(x=27, y=320)
cpsupgrade3 = Button(window, command=firstupgr, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade3.place(x=27, y=440)
cpsupgrade4 = Button(window, command=firstupgr, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade4.place(x=27, y=560)


def center_label(label, window_width, y_position):
    label.update_idletasks()  # Update the label to get its width
    label_width = label.winfo_width()
    x_position = (window_width - label_width) // 2  # Center horizontally
    label.place(x=x_position, y=y_position)

# Update positions for the labels
window_width = 950  # The width of your window

# Position Wonderhoyammount (Click Counter)
center_label(Wonderhoyammount, window_width, 50)

# Position wpslabel (WPS Label)
center_label(wpslabel, window_width, 160)

# Position cpslabel (Clicks Label)

center_label(cpslabel, window_width, 182)

center_label(addwonds, window_width, 200 )

center_label(remwonds, window_width, 300)

def wpsloop():
    global wps, Wonderhoys
    Wonderhoys = Wonderhoys + wps
    update_wonderhoy_label()
    window.after(1000, wpsloop)


wpsloop()

window.mainloop()