from tkinter import *
from tkinter import ttk
import pygame
import pickle
from numerize import numerize
from tkinter import messagebox
import os
from itertools import cycle




pygame.mixer.init()
current_track = ""
paused = False
clickamm = 0
alltimewonderhoys = 0
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


def center_label(label, window_width, y_position):
    label.update_idletasks()  
    label_width = label.winfo_width()
    x_position = (window_width - label_width) // 2  
    label.place(x=x_position, y=y_position)



###### MUSIC HANDLING START ######
MUSIC_FOLDER = "SFX\Music"
pygame.mixer.music.set_volume(0.2)

musicfiles= []
for f in os.listdir(MUSIC_FOLDER):
    if f.endswith(('mp3')):
        musicfiles.append(f)
    print(musicfiles)
        
playlist = cycle(musicfiles)



def nextrack():
    global current_track
    current_track = next(playlist)
    track_name, extension = os.path.splitext(current_track)
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, current_track)) 
    pygame.mixer.music.play(loops=0) 
    currentsong.config(text=f"Now Playing: {track_name}")
    center_label(currentsong, window_width, 666)





def skiptrack():
    global paused
    paused = False
    pauseb.config(text="Pause")
    nextrack()


def stopmusic():
    global paused
    if paused == False:
        paused = True
        pygame.mixer.music.pause()
        pauseb.config(text="Unpause")
        print(f"Pause is set to {paused}")
    elif paused == True:
        paused = False
        pauseb.config(text="Pause")
        pygame.mixer.music.unpause()
    

def check_music_playing():
    if not pygame.mixer.music.get_busy():
        nextrack() 




###### MUSIC HANDLING END ######

###### DECRYPTION/ENCRYPTION START ######
saveloc = "Data/game_data.dat"

def load_data():
    try:
        with open(saveloc, "rb") as file:
            data = pickle.load(file)
        return data
    except (FileNotFoundError, EOFError, pickle.UnpicklingError, ImportError, MemoryError):
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
            "totalwonderhoys": 0,
            "totalclicks": 0
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
        "totalwonderhoys": alltimewonderhoys,
        "totalclicks": clickamm
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
clickamm = game_data["totalclicks"]
alltimewonderhoys = game_data["totalwonderhoys"]



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
wondahoy.set_volume(0.05)

def clickevent():
    global Wonderhoys, clickpower, clickamm, alltimewonderhoys
    clickamm += 1
    alltimewonderhoys += clickpower
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
        cpslabel.config(text=f"ClickP: {clickpower}")
        clickpower += 2

def cscndupg():
    global Wonderhoys, clickpower, scndclickupgrpay
    if Wonderhoys >= scndclickupgrpay:
        Wonderhoys -= scndclickupgrpay
        scndclickupgrpay += scndclickupgrpay + 10
        cpsupgrade2.config(text=f"Lin Helper\n\n{scndclickupgrpay}\n\nAdds 5 Click Power")
        update_wonderhoy_label()
        cpslabel.config(text=f"ClickP: {clickpower}")
        clickpower += 5

def cthrdupg():
    global Wonderhoys, clickpower, thrdclickupgrpay
    if Wonderhoys >= thrdclickupgrpay:
        Wonderhoys -= thrdclickupgrpay
        thrdclickupgrpay += thrdclickupgrpay + 15
        cpsupgrade3.config(text=f"Len Helper\n\n{thrdclickupgrpay}")
        update_wonderhoy_label()
        cpslabel.config(text=f"ClickP: {clickpower}")
        clickpower += 50

def cfrthupg():
    global Wonderhoys, clickpower, frthclickupgrpay
    if Wonderhoys >= frthclickupgrpay:
        Wonderhoys -= frthclickupgrpay
        frthclickupgrpay += frthclickupgrpay+ 15
        cpsupgrade3.config(text=f"Meiko")
        update_wonderhoy_label()
        cpslabel.config(text=f"ClickP: {clickpower}")
        clickpower += 100



        

def update_wonderhoy_label():
    global Wonderhoys, wps,clickpower,firstupgrpay, scndupgrpay, thrdupgrpay, frthupgrpay
    global firstclickupgrpay, scndclickupgrpay, thrdclickupgrpay, frthclickupgrpay
    global clickamm, alltimewonderhoys
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
    # stats numerize
    readable_everwond = numerize.numerize(alltimewonderhoys)
    readable_everclick = numerize.numerize(clickamm)
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
    #stat labels
    everclicks.config(text=f"Total Clicks: {readable_everclick}")
    everwonds.config(text=f"Total Wonderhoys: {readable_everwond}")


# main clicker button GUI
emuherself = PhotoImage(file="Images\other\emu.png")
emuherselflabel = Label(image=emuherself)
wonderhoy = Button(window, image=emuherself, command=clickevent, borderwidth=0, background="Pink", activebackground="Pink")
wonderhoy.place(x=(950/2) - (296/2), y=(700/2) - (256/2)) # 950x700



# Click counter 
Wonderhoyammount = Label(window, text=f"Wonderhoys:\n{numerize.numerize(Wonderhoys)}", font=("Arial", 35, "bold"), fg='#e236be', background="Pink", activebackground="Pink")
Wonderhoyammount.place(x=330, y=50)
wpslabel = Label(window, text=f"WPS: {wps}", font=("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
wpslabel.place(x=435, y=160)
cpslabel = Label(window, text=f"ClickP: {clickpower}", font=("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
cpslabel.place(x=435, y=182)

# WPS Upgrades GUI
upgr = Label(window, text="WPS\nUpgrades", font=("Arial", 25, 'bold'), fg='#e236be', background="pink", activebackground="Pink", relief='solid', width= 8)
upgr.place(x=745, y=100)
upgrade1 = Button(window, command=firstupgr, text=f"Emu Helper = {firstupgrpay} WH\nadds 2 WPS", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade1.place(x=740, y=200)
upgrade2 = Button(window, text=f"Tsukasa Helper\n{scndupgrpay} WH\nadds 5 WPS", command=scndupgr, bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade2.place(x=740, y=320)
upgrade3 = Button(window, text=f"Nene Helper\n{thrdupgrpay} WH\n\nadds 15 WPS", command=thrdupgr, bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade3.place(x=740, y=440)
upgrade4 = Button(window, text=f"Rui Helper\ntext", bg="pink", relief='groove', fg="#e236be", command=frthupgrr, font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
upgrade4.place(x=740, y=560)

# CPS Upgrades GUI
cpsupgr = Label(window, text="Click\nUpgrades", font=("Arial", 25, 'bold'), fg='#e236be', background="pink", activebackground="Pink", relief='solid',width=8)
cpsupgr.place(x=31, y=100)
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
version = Label(window, text= "Game Currently\nbreaks formatting\nafter a Trillion WH's.\n(still playable,\nhowever hard to read.)", background="pink", font= ("arial", 10, "bold"))
version.place(x=35, y=10)
nextup = Label(window, text= "Next up:\n InfVersion.\nBetter Upgrades", background="pink", font= ("Arial", 10, "bold"))
nextup.place(x=777, y=10)
currentsong = Label(window, text=f"Currently Playing: {current_track}", font=("arial", 19), background="#FFA5CC", relief='solid')
currentsong.place(y=666)
nextb = Button(window, text="Next", command=skiptrack, background="#FFA5CC", font=("arial", 10, "bold"), width=10, activebackground="White")
nextb.place(y=0)
pauseb = Button(window, text="Pause", command= stopmusic, background="#FFA5CC", font=("arial", 10, "bold"), width= 10, activebackground="White")
pauseb.place(y=620)



# Stats GUI
stats = Label(window, text="Stats", background="pink", font=("arial", 25, "bold"), width= 14,relief='solid', fg='#e236be')
stats.place(y=100)
everclicks = Label(window, text=f"Total Clicks:", font=("arial", 10, "bold"), background="Pink") # text doesnt matter.
everclicks.place(y=1, x=10)
everwonds = Label(window, text="Total Wonderhoys:", font=("arial",10,"bold"), background="Pink") # text doesnt matter.
everwonds.place(y=1, x= 10)
placeholder = Label(window, text="That's all for 1.0 lol", font=("arial", 10,"bold"), background="Pink")
placeholder.place(y=650)

#chibi GUI
emuchibiparent = PhotoImage(file="Images\Chibi\Emu_Casual_chibi.png")
emuchibi = Label(window, image=emuchibiparent, background="Pink")
emuchibi.place(x=624, y=185)
tsukasachibiparent = PhotoImage(file="Images\Chibi\Tsukasa_Casual_chibi.png")
tsukasachibi = Label(window, image= tsukasachibiparent, background="Pink")
tsukasachibi.place(x=624, y=300)
nenechibiparent = PhotoImage(file="Images\Chibi\ene_Casual_chibi.png")
nenechibi = Label(window, image= nenechibiparent, background='Pink')
nenechibi.place(x=624, y=415)
ruichibiparent = PhotoImage(file="Images\Chibi\download.png")
ruichibi = Label(window, image = ruichibiparent, background="Pink")
ruichibi.place(x=624, y=530)
# vocaloid chibi GUI
mikuchibiparent = PhotoImage(file="Images\Chibi\WxS_Miku_chibi.png")
mikuchibi = Label(window, image = mikuchibiparent, background="pink")
mikuchibi.place(x=220,y=190)
rinchibiparent = PhotoImage(file="Images\Chibi\download (1).png")
rinchibi = Label(window, image= rinchibiparent, background="Pink")
rinchibi.place(x=219,y=305)
lenchibiparent = PhotoImage(file="Images\Chibi\download (2).png")
lenchibi = Label(window, image= lenchibiparent, background="Pink")
lenchibi.place(x=214,y=420)
meikochibiparent = PhotoImage(file="Images\Chibi\download (3).png")
meikochibi= Label(window, image= meikochibiparent, background="Pink")
meikochibi.place(x=214, y=535)



    

window_width = 950

center_label(Wonderhoyammount, window_width, 50)
center_label(noninf, window_width, 10)
center_label(wpslabel, window_width, 160)
center_label(cpslabel, window_width, 182)
center_label(stats, window_width, 500)
center_label(pauseb, window_width, 615)
center_label(nextb, window_width, 640)
center_label(placeholder, window_width, 590)

def wpsloop():
    center_label(everclicks, window_width, 550)
    center_label(everwonds, window_width, 570)
    center_label(Wonderhoyammount, window_width, 50)
    global wps, Wonderhoys, alltimewonderhoys, paused
    alltimewonderhoys += wps
    if paused == False:
        check_music_playing()
    Wonderhoys = Wonderhoys + wps
    update_wonderhoy_label()
    window.after(1000, wpsloop)


nextrack()
wpsloop()

window.mainloop()