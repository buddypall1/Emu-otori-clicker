from tkinter import *
from tkinter import ttk
import pygame
import pickle
from numerize import numerize
from tkinter import messagebox

Wonderhoys = 0
wps = 0
clickpower = 1
# WPS values
firstupgrpay = 10
scndupgrpay = 1000
thrdupgrpay = 10000
frthupgrpay = 1000000

# Click values
firstclickupgrpay = 10
scndclickupgrpay = 1500
thrdclickupgrpay = 15000
frthclickupgrpay = 1005000


###### DECRYPTION/ENCRYPTION START ######
saveloc = "Data/game_data.dat"

def load_data():
    try:
        with open(saveloc, "rb") as file:
            data = pickle.load(file)
        return data
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        print("Error loading data or file not found. Initializing default values.")
        messagebox.showerror('Data Error', "Data file has been deleted or tampered with. Resetting progress..")
        return {
            "Wonderhoys": 0,
            "wps": 0,
            "firstupgrpay": 10,
            "scndupgrpay": 1000,
            "thrdupgrpay": 10000,
            "frthupgrpay": 1000000,
            "firstclickupgrpay": 10,
            "scndclickupgrpay": 1500,
            "thrdclickupgrpay": 15000,
            "frthclickupgrpay": 1005000,
            "clickpower": 1,
        }

def save_data():
    data = {
        "Wonderhoys": Wonderhoys,
        "wps": wps,
        "firstupgrpay": firstupgrpay,
        "scndupgrpay": scndupgrpay,
        "thrdupgrpay": thrdupgrpay,
        "frthupgrpay": frthupgrpay,
        "firstclickupgrpay": firstclickupgrpay,
        "scndclickupgrpay": scndclickupgrpay,
        "thrdclickupgrpay": thrdclickupgrpay,
        "frthclickupgrpay": frthclickupgrpay,
        "clickpower": clickpower,
    }
    with open(saveloc, "wb") as file:
        pickle.dump(data, file)

game_data = load_data()

# UI values
Wonderhoys = game_data["Wonderhoys"]
wps = game_data["wps"]
clickpower = game_data["clickpower"]
# WPS upgrade values
firstupgrpay = game_data["firstupgrpay"]
scndupgrpay = game_data["scndupgrpay"]
thrdupgrpay = game_data["thrdupgrpay"]
frthupgrpay = game_data["frthupgrpay"]
# Click upgrade values
firstclickupgrpay = game_data["firstclickupgrpay"]
scndclickupgrpay = game_data["scndclickupgrpay"]
thrdclickupgrpay = game_data["thrdclickupgrpay"]
frthclickupgrpay = game_data["frthclickupgrpay"]



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

def thrdupgr():
    global Wonderhoys, wps, thrdupgrpay
    if Wonderhoys >= thrdupgrpay:
        Wonderhoys -= thrdupgrpay
        thrdupgrpay += thrdupgrpay + 10
        update_wonderhoy_label()
        wps += 50
        wpslabel.config(text=f"WPS: {wps}")
        print(wps)
    else:
        pass

def frthupgrr():
    global Wonderhoys, wps, frthupgrpay
    if Wonderhoys >= frthupgrpay:
        Wonderhoys -= frthupgrpay
        frthupgrpay += frthupgrpay + 20
        update_wonderhoy_label()
        wps += 100
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

def cscndupg():
    global Wonderhoys, clickpower, scndclickupgrpay
    if Wonderhoys >= scndclickupgrpay:
        Wonderhoys -= scndclickupgrpay
        scndclickupgrpay += scndclickupgrpay + 10
        cpsupgrade2.config(text=f"Lin Helper\n\n{scndclickupgrpay}\n\nAdds 5 Click Power")
        update_wonderhoy_label()
        cpslabel.config(text=f"Clicks: {clickpower}")
        clickpower += 5

def cthrdupg():
    global Wonderhoys, clickpower, thrdclickupgrpay
    if Wonderhoys >= thrdclickupgrpay:
        Wonderhoys -= thrdclickupgrpay
        thrdclickupgrpay += thrdclickupgrpay + 15
        cpsupgrade3.config(text=f"Len Helper\n\n{thrdclickupgrpay}")
        update_wonderhoy_label()
        cpslabel.config(text=f"Clicks: {clickpower}")
        clickpower += 50

def cfrthupg():
    global Wonderhoys, clickpower, frthclickupgrpay
    if Wonderhoys >= frthclickupgrpay:
        Wonderhoys -= frthclickupgrpay
        frthclickupgrpay += frthclickupgrpay+ 15
        cpsupgrade3.config(text=f"Meiko")
        update_wonderhoy_label()
        cpslabel.config(text=f"Clicks: {clickpower}")
        clickpower += 100



        

def update_wonderhoy_label():
    global Wonderhoys, wps,clickpower,firstupgrpay, scndupgrpay, thrdupgrpay, frthupgrpay
    global firstclickupgrpay, scndclickupgrpay, thrdclickupgrpay, frthclickupgrpay
    # WPS upgrade numerize
    readable_wonderhoys = numerize.numerize(Wonderhoys)
    readable_wpsupg1 = numerize.numerize(firstupgrpay)
    readable_wpsupg2 = numerize.numerize(scndupgrpay)
    readable_wpsupg3 = numerize.numerize(thrdupgrpay)
    readable_wpsupg4 = numerize.numerize(frthupgrpay)
    # click upgrade numerize
    readable_clckupg1 = numerize.numerize(firstclickupgrpay)
    readable_clckupg2 = numerize.numerize(scndclickupgrpay)
    readable_clckupg3 = numerize.numerize(thrdclickupgrpay)
    readable_clckupg4 = numerize.numerize(frthclickupgrpay)
    Wonderhoyammount.config(text=f"Wonderhoys:\n{readable_wonderhoys}")
    # WPS upgrade labels
    upgrade1.config(text=f"Emu Helper\n\n{readable_wpsupg1} WH\n\nAdds 2 WPS")
    upgrade2.config(text=f"Tsukasa Helper\n\n{readable_wpsupg2} WH\n\nAdds 5 WPS")
    upgrade3.config(text=f"Nene Helper\n\n{readable_wpsupg3} WH\n\nAdds 50 WPS")
    upgrade4.config(text=f"Rui Helper\n\n{readable_wpsupg4} WH\n\nAdds 100 WPS")
    # click upgrade labels
    cpsupgrade1.config(text=f"Miku Helper\n\n{readable_clckupg1} WH\n\nAdds 2 Click Power")
    cpsupgrade2.config(text=f"Lin Helper\n\n{readable_clckupg2} WH\n\nAdds 5 Click Power")
    cpsupgrade3.config(text=f"Len Helper\n\n{readable_clckupg3} WH\n\nAdds 50 Click Power")
    cpsupgrade4.config(text=f"Meiko Helper\n\n{readable_clckupg4} WH\n\nAdds 100 Click Power")


# main clicker button GUI
emuherself = PhotoImage(file="Images\kvxwxs89gqj81-ezgif.com-webp-to-png-converter.png")
emuherselflabel = Label(image=emuherself)
wonderhoy = Button(window, image=emuherself, command=clickevent, borderwidth=0, background="Pink", activebackground="Pink")
wonderhoy.place(x=(950/2) - (296/2), y=(700/2) - (256/2)) # 950x700



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
upgrade2 = Button(window, text=f"Tsukasa Helper\n{scndupgrpay} WH\nadds 5 WPS", command=scndupgr, bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade2.place(x=740, y=320)
upgrade3 = Button(window, text=f"Nene Helper\n{thrdupgrpay} WH\n\nadds 15 WPS", command=thrdupgr, bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade3.place(x=740, y=440)
upgrade4 = Button(window, text=f"Rui Helper\ntext", bg="pink", relief='groove', fg="#e236be", command=frthupgrr, font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade4.place(x=740, y=560)

# CPS Upgrades GUI
cpsupgr = Label(window, text="Click\nUpgrades", font=("Arial", 25, 'bold'), fg='#e236be', background="pink", activebackground="Pink", relief='solid')
cpsupgr.place(x=35, y=100)
cpsupgrade1 = Button(window, command=cfrstupg, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade1.place(x=27, y=200)
cpsupgrade2 = Button(window, command=cscndupg, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade2.place(x=27, y=320)
cpsupgrade3 = Button(window, command=cthrdupg, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade3.place(x=27, y=440)
cpsupgrade4 = Button(window, command=cfrthupg, text=f"CPSupgr\ntext", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
cpsupgrade4.place(x=27, y=560)
# Misc GUI
noninf = Label(window, text= "Version: NonInf!", background= "Pink", font= ("arial", 10, "bold"))
noninf.place(y= 10)
version = Label(window, text= "Game Currently\nbreaks formatting\nafter Trillion WH's.\n(still playable,\nhowever hard to read.)", background="pink", font= ("arial", 10, "bold"))
version.place(x=35, y=10)
nextup = Label(window, text= "Next up:\n InfVersion.\nBetter Upgrades", background="pink", font= ("Arial", 10, "bold"))
nextup.place(x=777, y=10)

#chibi GUI
emuchibiparent = PhotoImage(file="Images/Emu_Casual_chibi.png")
emuchibi = Label(window, image=emuchibiparent, background="Pink")
emuchibi.place(x=624, y=185)
tsukasachibiparent = PhotoImage(file="Images\Tsukasa_Casual_chibi.png")
tsukasachibi = Label(window, image= tsukasachibiparent, background="Pink")
tsukasachibi.place(x=624, y=300)
nenechibiparent = PhotoImage(file="Images\ene_Casual_chibi.png")
nenechibi = Label(window, image= nenechibiparent, background='Pink')
nenechibi.place(x=624, y=415)
ruichibiparent = PhotoImage(file="Images\download.png")
ruichibi = Label(window, image = ruichibiparent, background="Pink")
ruichibi.place(x=624, y=530)
mikuchibiparent = PhotoImage(file="Images\WxS_Miku_chibi.png")
mikuchibi = Label(window, image = mikuchibiparent, background="pink")
mikuchibi.place(x=220,y=185)
rinchibiparent = PhotoImage(file="Images\download (1).png")
rinchibi = Label(window, image= rinchibiparent, background="Pink")
rinchibi.place(x=219,y=300)
lenchibiparent = PhotoImage(file="Images\download (2).png")
lenchibi = Label(window, image= lenchibiparent, background="Pink")
lenchibi.place(x=214,y=415)
meikochibiparent = PhotoImage(file="Images\download (3).png")
meikochibi= Label(window, image= meikochibiparent, background="Pink")
meikochibi.place(x=214, y=530)

def center_label(label, window_width, y_position):
    label.update_idletasks()  
    label_width = label.winfo_width()
    x_position = (window_width - label_width) // 2  
    label.place(x=x_position, y=y_position)

    

window_width = 950  # width of window


center_label(Wonderhoyammount, window_width, 50)

center_label(noninf, window_width, 10)

center_label(wpslabel, window_width, 160)

center_label(cpslabel, window_width, 182)


def wpsloop():
    global wps, Wonderhoys
    Wonderhoys = Wonderhoys + wps
    update_wonderhoy_label()
    window.after(1000, wpsloop)


wpsloop()

window.mainloop()