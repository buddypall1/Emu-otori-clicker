from tkinter import *
from tkinter import ttk
import pygame
import pickle
from numerize import numerize
from tkinter import messagebox
import os
from itertools import cycle
import string



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
firstupgrpowr = 2
scndupgrpowr = 5
thrdupgrpowr = 50
frthupgrpowr = 100
# Click values
firstclickupgrpay = 10
scndclickupgrpay = 1500
thrdclickupgrpay = 15000
frthclickupgrpay = 1005000
firstcupgrpowr = 2
scndcupgrpowr = 5
thrdcupgrpowr = 50
frthcupgrpowr = 100

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


def infinitizer(magnitude):
    magnitude -= 4  # done to prevent stuff already in numerize interfering
    letters = string.ascii_lowercase
    base = len(letters)
    suffix = ""
    magnitude += 26  

    while magnitude >= 0: 

        suffix = letters[magnitude % base] + suffix  
        magnitude = magnitude // base - 1

    return suffix


def numerizeinf(number):

    suffixes = ["", "K", "M", "B", "T"]
    num = float(number)
    magnitude = 0

    while abs(num) >= 1000:

        num /= 1000.0
        magnitude += 1

    if magnitude < len(suffixes): # checks if magnitude has reached enough for a custom suffix
        suffix = suffixes[magnitude] 
    else:
        suffix = infinitizer(magnitude) # figuring out the letters for numbers past trillion

    return f"{num:.2f}{suffix}" # final




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
            "firstupgrpowr" : 2,
            "scndupgrpowr" : 5,
            "thrdupgrpowr" : 50,
            "frthupgrpowr" : 100,
            "firstclickupgrpay": 10,
            "scndclickupgrpay": 1500,
            "thrdclickupgrpay": 15000,
            "frthclickupgrpay": 1005000,
            "firstcupgrpowr": 2,
            "scndcupgrpowr": 5,
            "thrdcupgrpowr": 50,
            "frthcupgrpowr": 100,
            "clickpower": 1,
            "totalwonderhoys": 0,
            "totalclicks": 0
        }

def save_data():
    data = {
        "Wonderhoys": Wonderhoys,
        "wps": wps,
        "firstupgrpay": firstupgrpay,
        "scndupgrpay":  scndupgrpay,
        "thrdupgrpay":  thrdupgrpay,
        "frthupgrpay":  frthupgrpay,
        "firstupgrpowr": firstupgrpowr,
        "scndupgrpowr" : scndupgrpowr,
        "thrdupgrpowr" : thrdupgrpowr,
        "frthupgrpowr" : frthupgrpowr,
        "firstclickupgrpay": firstclickupgrpay,
        "scndclickupgrpay":  scndclickupgrpay,
        "thrdclickupgrpay":  thrdclickupgrpay,
        "frthclickupgrpay":  frthclickupgrpay,
        "firstcupgrpowr" : firstcupgrpowr,
        "scndcupgrpowr" : scndcupgrpowr,
        "thrdcupgrpowr" : thrdcupgrpowr,
        "frthcupgrpowr" : frthcupgrpowr,
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
firstupgrpowr= game_data["firstupgrpowr"]
scndupgrpowr= game_data["scndupgrpowr"]
thrdupgrpowr= game_data["thrdupgrpowr"]
frthupgrpowr= game_data["frthupgrpowr"]
# Click upgrade values
firstclickupgrpay = game_data["firstclickupgrpay"]
scndclickupgrpay = game_data["scndclickupgrpay"]
thrdclickupgrpay = game_data["thrdclickupgrpay"]
frthclickupgrpay = game_data["frthclickupgrpay"]
firstcupgrpowr  = game_data["firstcupgrpowr"]
scndcupgrpowr = game_data["scndcupgrpowr"]
thrdcupgrpowr = game_data["thrdcupgrpowr"]
frthcupgrpowr  = game_data["frthcupgrpowr"]
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
    global Wonderhoys, wps, firstupgrpay, firstupgrpowr
    if Wonderhoys >= firstupgrpay:
        Wonderhoys -= firstupgrpay
        firstupgrpay += firstupgrpay + 5
        print(firstupgrpowr)
        update_wonderhoy_label()
        wps += firstupgrpowr
        wpslabel.config(text=f"WPS: {numerizeinf(wps)}")
        firstupgrpowr += firstupgrpowr * 0.3
        print(wps)


def scndupgr():
    global Wonderhoys, wps, scndupgrpay, scndupgrpowr
    if Wonderhoys >= scndupgrpay:
        Wonderhoys -= scndupgrpay
        scndupgrpay += scndupgrpay + 7
        update_wonderhoy_label()
        wps += scndupgrpowr
        wpslabel.config(text=f"WPS: {numerizeinf(wps)}")
        scndupgrpowr += scndupgrpowr * 0.5
        print(wps)
    else:
        pass

def thrdupgr():
    global Wonderhoys, wps, thrdupgrpay, thrdupgrpowr
    if Wonderhoys >= thrdupgrpay:
        Wonderhoys -= thrdupgrpay
        thrdupgrpay += thrdupgrpay + 10
        update_wonderhoy_label()
        wps += thrdupgrpowr
        wpslabel.config(text=f"WPS: {numerizeinf(wps)}")
        thrdupgrpowr += thrdupgrpowr * 0.9
        print(wps)
    else:
        pass

def frthupgrr():
    global Wonderhoys, wps, frthupgrpay, frthupgrpowr
    if Wonderhoys >= frthupgrpay:
        Wonderhoys -= frthupgrpay
        frthupgrpay += frthupgrpay + 20
        update_wonderhoy_label()
        wps += frthupgrpowr
        wpslabel.config(text=f"WPS: {numerizeinf(wps)}")
        frthupgrpowr += frthupgrpowr * 1.3
        print(wps)
    else:
        pass


# Click Upgrades
def cfrstupg():
    global Wonderhoys, clickpower, firstclickupgrpay, firstcupgrpowr
    if Wonderhoys >= firstclickupgrpay:
        Wonderhoys -= firstclickupgrpay
        firstclickupgrpay += firstclickupgrpay + 10
        update_wonderhoy_label()
        clickpower += firstcupgrpowr
        cpslabel.config(text=f"ClickP: {numerizeinf(clickpower)}")
        firstcupgrpowr += firstcupgrpowr * 0.3

def cscndupg():
    global Wonderhoys, clickpower, scndclickupgrpay, scndcupgrpowr
    if Wonderhoys >= scndclickupgrpay:
        Wonderhoys -= scndclickupgrpay
        scndclickupgrpay += scndclickupgrpay + 12
        update_wonderhoy_label()
        clickpower += scndcupgrpowr
        cpslabel.config(text=f"ClickP: {numerizeinf(clickpower)}")
        scndcupgrpowr += scndcupgrpowr * 0.5
def cthrdupg():
    global Wonderhoys, clickpower, thrdclickupgrpay, thrdcupgrpowr
    if Wonderhoys >= thrdclickupgrpay:
        Wonderhoys -= thrdclickupgrpay
        thrdclickupgrpay += thrdclickupgrpay + 15
        update_wonderhoy_label()
        clickpower += 50
        cpslabel.config(text=f"ClickP: {numerizeinf(clickpower)}")
        thrdcupgrpowr += thrdcupgrpowr * 0.9
def cfrthupg():
    global Wonderhoys, clickpower, frthclickupgrpay, frthcupgrpowr
    if Wonderhoys >= frthclickupgrpay:
        Wonderhoys -= frthclickupgrpay
        frthclickupgrpay += frthclickupgrpay+ 20
        update_wonderhoy_label()
        clickpower += 100
        cpslabel.config(text=f"ClickP: {numerizeinf(clickpower)}")
        frthcupgrpowr += frthcupgrpowr * 1.3



        

def update_wonderhoy_label():
    global Wonderhoys, wps,clickpower,firstupgrpay, scndupgrpay, thrdupgrpay, frthupgrpay
    global firstclickupgrpay, scndclickupgrpay, thrdclickupgrpay, frthclickupgrpay
    global firstupgrpowr, scndcupgrpowr, thrdupgrpowr, frthupgrpowr, firstcupgrpowr, scndcupgrpowr, thrdcupgrpowr, frthcupgrpowr
    global clickamm, alltimewonderhoys
    # WPS upgrade numerize
    readable_wonderhoys = numerizeinf(Wonderhoys)
    readable_wpsupg1 = numerizeinf(firstupgrpay)
    readable_wpsupg2 = numerizeinf(scndupgrpay)
    readable_wpsupg3 = numerizeinf(thrdupgrpay)
    readable_wpsupg4 = numerizeinf(frthupgrpay)
    readable_wpspowupg1= numerizeinf(firstupgrpowr)
    readable_wpspowupg2= numerizeinf(scndupgrpowr)
    readable_wpspowupg3= numerizeinf(thrdupgrpowr)
    readable_wpspowupg4= numerizeinf(frthupgrpay)
    # click upgrade numerize
    readable_clckupg1 = numerizeinf(firstclickupgrpay)
    readable_clckupg2 = numerizeinf(scndclickupgrpay)
    readable_clckupg3 = numerizeinf(thrdclickupgrpay)
    readable_clckupg4 = numerizeinf(frthclickupgrpay)
    readable_cpowupg1= numerizeinf(firstcupgrpowr)
    readable_cpowupg2= numerizeinf(scndcupgrpowr)
    readable_cpowupg3= numerizeinf(thrdcupgrpowr)
    readable_cpowupg4= numerizeinf(frthcupgrpowr)
    Wonderhoyammount.config(text=f"Wonderhoys:\n{readable_wonderhoys}")
    # stats numerize
    readable_everwond = numerizeinf(alltimewonderhoys)
    readable_everclick = numerizeinf(clickamm)
    # WPS upgrade labels
    upgrade1.config(text=f"Emu Helper\n\n{readable_wpsupg1} WH\n\nAdds {readable_wpspowupg1} WPS")
    upgrade2.config(text=f"Tsukasa Helper\n\n{readable_wpsupg2} WH\n\nAdds {readable_wpspowupg2} WPS")
    upgrade3.config(text=f"Nene Helper\n\n{readable_wpsupg3} WH\n\nAdds {readable_wpspowupg3} WPS")
    upgrade4.config(text=f"Rui Helper\n\n{readable_wpsupg4} WH\n\nAdds {readable_wpspowupg4} WPS")
    # click upgrade labels
    cpsupgrade1.config(text=f"Miku Helper\n\n{readable_clckupg1} WH\n\nAdds {readable_cpowupg1} Click Power")
    cpsupgrade2.config(text=f"Lin Helper\n\n{readable_clckupg2} WH\n\nAdds {readable_cpowupg2} Click Power")
    cpsupgrade3.config(text=f"Len Helper\n\n{readable_clckupg3} WH\n\nAdds {readable_cpowupg3} Click Power")
    cpsupgrade4.config(text=f"Meiko Helper\n\n{readable_clckupg4} WH\n\nAdds {readable_cpowupg4} Click Power")
    #stat labels
    everclicks.config(text=f"Total Clicks: {readable_everclick}")
    everwonds.config(text=f"Total Wonderhoys: {readable_everwond}")


# main clicker button GUI
emuherself = PhotoImage(file="Images\other\emu.png")
emuherselflabel = Label(image=emuherself)
wonderhoy = Button(window, image=emuherself, command=clickevent, borderwidth=0, background="Pink", activebackground="Pink")
wonderhoy.place(x=(950/2) - (296/2), y=(700/2) - (256/2)) # 950x700



# Click counter 
Wonderhoyammount = Label(window, text=f"Wonderhoys:\n{numerizeinf(Wonderhoys)}", font=("Arial", 35, "bold"), fg='#e236be', background="Pink", activebackground="Pink")
Wonderhoyammount.place(x=330, y=50)
wpslabel = Label(window, text=f"WPS: {numerizeinf(wps)}", font=("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
wpslabel.place(x=435, y=160)
cpslabel = Label(window, text=f"ClickP: {numerizeinf(clickpower)}", font=("Arial", 10, "bold"), fg='#e236be', background="pink", activebackground="Pink")
cpslabel.place(x=435, y=182)
# WPS Upgrades GUI
upgr = Label(window, text="WPS\nUpgrades", font=("Arial", 25, 'bold'), fg='#e236be', background="pink", activebackground="Pink", relief='solid', width= 8)
upgr.place(x=745, y=100)
upgrade1 = Button(window, command=firstupgr, text=f"Emu Helper = {firstupgrpay} WH\nadds {firstupgrpowr} WPS", bg="pink", relief='groove', fg="#e236be", font=("Arial", 10, "bold"), borderwidth=5, width=20, height=5)
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
inf = Label(window, text= "Version: Inf!", background= "Pink", font= ("arial", 10, "bold"))
inf.place(y= 10)
version = Label(window, text= "(Game has fixed formatting!\nshould be infinite now.)", background="pink", font= ("arial", 10, "bold"))
version.place(x=35, y=10)
nextup = Label(window, text= "Next up:\nHeavy UI improvements\nNew features?!\nMore upgrades?!", background="pink", font= ("Arial", 10, "bold"))
nextup.place(x=755, y=10)
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
placeholder = Label(window, text="Woahh 1.1 is here (still no new stats)", font=("arial", 10,"bold"), background="Pink")
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
center_label(inf, window_width, 10)
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