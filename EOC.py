import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QScrollArea, QWidget, QVBoxLayout, QStackedWidget, QMessageBox, QFrame, QHBoxLayout
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap
import pygame
import pickle

pygame.mixer.init()

saveloc = "Data/game_data.dat"

app = QApplication(sys.argv)

window = QMainWindow()
mainwidget = QWidget()
mainwidget.setObjectName("background")
window.setCentralWidget(mainwidget)
window.setFixedSize(1910,1000)

#### SAVE HANDLING ####

def save_data():
    '''
    Data saving function. Call to save the game (Used on exit and autosaves if enabled [NOT IMPLEMENTED YET])
    '''
    data = {
        "wonderhoys" : wonderhoys,
        "clickspersecond": clickspersecond,
        "Clickstrength": clickstrength,
        "Tutorialfinished": tutorialfinished
    }
    with open(saveloc, "wb") as file:
        pickle.dump(data, file)


def on_exit():
    print("Saving...")
    save_data()


def load_data():
    try:
        with open(saveloc, "rb") as file:
            data= pickle.load(file)
        return data
    except (FileNotFoundError, EOFError, pickle.UnpicklingError, ImportError, MemoryError):
        print("Error loading data or file not found. Defaulting.")
        QMessageBox.warning(window, "Warning!", "Save data corrupt or not found! (Normal on first time launch) Resetting..")
        return {
            "wonderhoys": 0,
            "clickspersecond": 1,
            "Clickstrength": 1,
            "Tutorialfinished": 0
        }
    
game_data = load_data()
'''
This is the variable that the global variables obtain their values from the save file
'''

#### SAVE HANDLING ####

#### GLOBAL VARIABLES ####

wonderhoys = game_data['wonderhoys']
'''
main currency variable (USED TO ADD TO/MODIFY WONDERHOYS)
'''
clickspersecond = game_data['clickspersecond']
'''
how many clicks the game does per tick
'''
clickstrength = game_data['Clickstrength']
'''
how much wonderhoys the user gets from clicking emu
'''

tutorialfinished = game_data['Tutorialfinished']
'''
checks if the tutorial was fully seen.
If 1 do not display tutorial on launch.
If 0 DO display tutorial on launch.
'''

#### GLOBAL VARIABLES ####

pixmap = QPixmap("Images\other\emu.png").scaled(350,350, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

mainwidget.setStyleSheet("""
    #background {
        border-image: url(Images/other/gamebckgrn3.png) 0 0 0 0 stretch stretch;
    }
""")

layout = QVBoxLayout()
mainwidget.setLayout(layout)

wondahoy = pygame.mixer.Sound("SFX/WONDERHOY SOUND EFFECT (no background music).mp3")
wondahoy.set_volume(0.05)

def clickevent():
    '''
    Ran on user click on emu
    '''
    global wonderhoys, money, clickstrength

    wonderhoys += clickstrength
    money.setText(f"Wonderhoys: {wonderhoys}")
    wondahoy.play(loops=0)



emubutton = QPushButton()
emubutton.setIcon(QIcon(pixmap))
emubutton.setIconSize(pixmap.size())
emubutton.setFixedSize(pixmap.size())
emubutton.setFlat(True)
emubutton.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
        padding-top: 4px;
    }
""")

emubutton.setParent(mainwidget)

def centerer(input, xoffset, yoffset):
    '''
    function used to help center widgets
    INPUT - The widget to center
    XOFFSET - offset on x axis after centering
    YOFFSET - offset on y axis after centering
    '''
    x = (1910 - input.width()) // 2
    y = (1000 - input.height()) // 2
    input.move(x + xoffset,y + yoffset)

centerer(emubutton, 0, -100)

emubutton.clicked.connect(clickevent)

money = QLabel(f"Wonderhoys: {wonderhoys}")
'''
ONLY THE VISUAL LABEL OF THE WONDERHOYS DISPLAYED FOR THE USER (goto wonderhoys variable to edit that)
'''
money.setParent(mainwidget)
money.resize(250,140)
money.setObjectName("money")
money.setAlignment(Qt.AlignCenter)
money.setStyleSheet(""" 
    #money {
    background-color: #fce0ed;
    color: #de6a8f;
    padding-bottom:30px;
    border: 4px solid #ffb2d7;   
    border-radius: 4px;
    font-size: 30px;    
    font-weight: bold;
    }
""")
rowstyle3 ="""
    #details{
    color: #de6a8f;
    font-size:18px;
    font-weight:bold;
    }
"""
rowstyle4 = """
    #tutorialtop{
    color: #de6a8f;
    font-size:30px;
    font-weight:bold;
    }

"""
wonderhoyspersecond = QLabel(f"WPS: {clickspersecond}")
'''
label for WPS on the UI (NOT THE VARIABLE FOR WPS! goto clickspersecond to edit that variable!)
'''
wonderhoyspersecond.setParent(mainwidget)
wonderhoyspersecond.resize(100,100)
wonderhoyspersecond.setObjectName("details")
wonderhoyspersecond.setAlignment(Qt.AlignCenter)


def tick():
    '''
    main gameloop function, runs every second.
    '''
    global clickspersecond, wonderhoys, tutorialfinished
    print(tutorialfinished)
    wonderhoys += clickspersecond
    money.setText(f"Wonderhoys: {wonderhoys}")

timer = QTimer()
timer.timeout.connect(tick)
timer.start(1000)

clickstrengthlabel = QLabel(f"ClickPow:{clickstrength}")
'''
label for ClickPow on the UI (goto clickstrength to edit the variable.)
'''
clickstrengthlabel.setParent(mainwidget)
clickstrengthlabel.resize(100,100)
clickstrengthlabel.setObjectName("details")
clickstrengthlabel.setAlignment(Qt.AlignCenter)

###################
##### SHOP UI #####
###################

shopmainwidget = QWidget()
shopmainlayout = QVBoxLayout()
shopmainwidget.setLayout(shopmainlayout)
shopmainwidget.resize(400,1000)
shopmainwidget.setParent(mainwidget)
shopmainwidget.setObjectName("Row")


shoptitle = QLabel("Shop!")
shoptitle.setAlignment(Qt.AlignCenter)
shoptitle.resize(200,10)
shoptitle.setObjectName("Shopname")
shoptitle.setStyleSheet("""
    #Shopname{
    background-color: #ffb8ce;
    color: #de6a8f;
    border: 5px solid #de6a8f;   
    border-radius: 4px;
    font-size: 65px;
    font-weight: bold;
    }
""")
shopmainlayout.addWidget(shoptitle)
rowstyle ="""
    #Row {
    background-color: #ffb8ce;
    color: #de6a8f;
    border: 3px solid #de6a8f;   
    border-radius: 4px;
    font-size: 17px;
    font-weight: bold;
    }
    #Row:hover{
    background-color: #f0adc2;
    }
    #Row:pressed{
    padding-top:2px;
    background-color: #e6a6b9;
    color: white;
    }
"""

upgraderow = QHBoxLayout()
testrow1=QPushButton("Click Upgrades!")
testrow1.setObjectName("Row")

testrow2=QPushButton("WPS Upgrades!")
testrow2.setObjectName("Row")

shopscroller = QScrollArea()
shopscroller.setWidgetResizable(True)
rowstyle2 ="""
    #RowScroller {
    background-color: #b38190;
    color: #ff7aa4;
    border: 3px solid #ff7aa4;   
    border-radius: 4px;
    font-size: 17px;
    font-weight: bold;
    
    }
"""
shopscroller.setStyleSheet("""
    QScrollBar:vertical {
        background: #fce0ed;
        width: 5px;
        margin: 0px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical {
        background: #ff7aa4;
        border-radius: 5px;
        min-height: 20px;
    }
    QScrollBar::handle:vertical:hover {
        background: #e66e94;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
""")

shopcontainerstack = QStackedWidget()
shopcontainerstack.setObjectName("RowScroller")

# 1st page (click power updates)
firstpage = QWidget()
firstpagelayout = QVBoxLayout(firstpage)
upgrade_button = QPushButton("TestUpg1\nprice: NaN")
upgrade_button.setToolTip("This is a test upgrade! \nAdds 1 ClickPow for free")
tooltipstyle="""
    QToolTip {
        background-color: #ffb8ce;
        color: #de6a8f;
        border: 4px solid #de6a8f;
        border-radius: 4px;
        padding: 6px;
        font-size: 14px;
        font-weight: bold;
    }
"""

rowstyle5 ="""
    #Rowbuttonless {
    background-color: #ffb8ce;
    color: #de6a8f;
    border: 3px solid #de6a8f;   
    border-radius: 4px;
    font-size: 17px;
    font-weight: bold;
}
"""
rowstyle6 ="""
    #Rowbuttonborderless {
    background-color: #ffb8ce;
    color: #de6a8f;
    font-size: 17px;
    font-weight: bold;
}
"""
app.setStyleSheet(rowstyle + rowstyle2 + rowstyle3 + tooltipstyle + rowstyle4 + rowstyle5 + rowstyle6)
upgrade_button.setObjectName("Row")
firstpagelayout.addWidget(upgrade_button)
firstpagelayout.addStretch()

def firstclickupg():
    global clickstrength

    clickstrength += 1
    clickstrengthlabel.setText(f"ClickPow: {clickstrength}")
    print(clickstrength)


upgrade_button.clicked.connect(firstclickupg)

# 2nd page
secondpage = QWidget()
secondpagelayout = QVBoxLayout(secondpage)
upgrade_button = QPushButton(f"TestUpg2\nprice: NaN")
upgrade_button.setObjectName("Row")
secondpagelayout.addWidget(upgrade_button)
secondpagelayout.addStretch()

shopcontainerstack.addWidget(firstpage)
shopcontainerstack.addWidget(secondpage)

testrow1.clicked.connect(lambda: shopcontainerstack.setCurrentIndex(0))
testrow2.clicked.connect(lambda: shopcontainerstack.setCurrentIndex(1))

shopscroller.setWidget(shopcontainerstack)

upgraderow.addWidget(testrow1)
upgraderow.addWidget(testrow2)
shopmainlayout.addLayout(upgraderow)
shopmainlayout.addWidget(shopscroller)
shopmainlayout.setContentsMargins(0, 0, 0, 0)
shopmainlayout.setSpacing(2)



WIPbutton = QPushButton("WIP")
WIPbutton.setObjectName("WIPbutton")
WIPbutton.setStyleSheet("""
    #WIPbutton{
    background-color: #ffb8ce;
    color: #de6a8f;
    border: 3px solid #de6a8f;   
    border-radius: 4px;
    font-size: 40px;
    font-weight: bold;
    }
    #WIPbutton:hover{
    background-color: #f0adc2;
    }
    #WIPbutton:pressed{
    padding-top:2px;
    background-color: #e6a6b9;
    color: white;
    }
""")
shopmainlayout.addWidget(WIPbutton)

###################
##### SHOP UI #####
###################

###################
##### LEFT UI #####
###################

leftuicontainerstack = QStackedWidget()
leftuicontainerstack.setObjectName("RowScroller")

leftuiwidget = QWidget()
leftuimainlayout = QVBoxLayout()
leftuiwidget.setLayout(leftuimainlayout)
leftuiwidget.resize(400,1000)
leftuiwidget.setParent(mainwidget)
leftuiwidget.setObjectName("Row")

leftuilabel = QLabel("Info!")
leftuilabel.setAlignment(Qt.AlignCenter)
leftuilabel.resize(200,10)
leftuilabel.setObjectName("Shopname")
leftuilabel.setStyleSheet("""
    #Shopname{
    background-color: #ffb8ce;
    color: #de6a8f;
    border: 5px solid #de6a8f;   
    border-radius: 4px;
    font-size: 65px;
    font-weight: bold;
    }
""")
leftuimainlayout.addWidget(leftuilabel)
leftuimainlayout.setContentsMargins(0, 0, 0, 0)
leftuimainlayout.setSpacing(2)
upgraderowleft = QHBoxLayout()

testrowL2 = QPushButton("Stats")
testrowL2.setObjectName("Row")
upgraderowleft.addWidget(testrowL2)

testrowL3 = QPushButton("Achievements")
testrowL3.setObjectName("Row")
upgraderowleft.addWidget(testrowL3)


testrowL1 = QPushButton("Settings")
testrowL1.setObjectName("Row")
upgraderowleft.addWidget(testrowL1)

#1st page (Settings)
firstpageleft = QWidget()
firstpageleftlayout = QVBoxLayout(firstpageleft)
lefttest = QLabel("This is a test")
lefttest.setObjectName("Row")
firstpageleftlayout.addWidget(lefttest)
firstpageleftlayout.addStretch()

#2nd page (Stats)
secondpageleft = QWidget()
secondpageleftlayout = QVBoxLayout(secondpageleft)
lefttest2 = QLabel("This is ALSO a test")
lefttest2.setObjectName("Row")
secondpageleftlayout.addWidget(lefttest2)
secondpageleftlayout.addStretch()

#3rd page (Achievos)

thirdpageleft = QWidget()
thirdpageleftlayout= QVBoxLayout(thirdpageleft)
lefttest3 = QLabel("yet ANOTHER test")
lefttest3.setObjectName("Row")
thirdpageleftlayout.addWidget(lefttest3)
thirdpageleftlayout.addStretch()

leftuicontainerstack.addWidget(firstpageleft)
leftuicontainerstack.addWidget(secondpageleft)
leftuicontainerstack.addWidget(thirdpageleft)

testrowL1.clicked.connect(lambda: leftuicontainerstack.setCurrentIndex(1))
testrowL2.clicked.connect(lambda: leftuicontainerstack.setCurrentIndex(0))
testrowL3.clicked.connect(lambda: leftuicontainerstack.setCurrentIndex(2))

leftuiscroller = QScrollArea()
leftuiscroller.setObjectName("Leftscroller")
leftuiscroller.setWidget(leftuicontainerstack)
leftuiscroller.setWidgetResizable(True)
leftuiscroller.setStyleSheet("""
    QScrollBar:vertical {
        background: #fce0ed;
        width: 5px;
        margin: 0px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical {
        background: #ff7aa4;
        border-radius: 5px;
        min-height: 20px;
    }
    QScrollBar::handle:vertical:hover {
        background: #e66e94;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    #Leftscroller {
    background-color: #b38190;
    color: #ff7aa4;
    border: 3px solid #ff7aa4;   
    border-radius: 4px;
    font-size: 17px;
    font-weight: bold;
    }
""")
leftuimainlayout.addLayout(upgraderowleft)
leftuimainlayout.addWidget(leftuiscroller)

musicplayertop = QLabel("Music Player")
musicplayertop.setAlignment(Qt.AlignCenter)
musicplayertop.setObjectName("musicplayertop")
musicplayertop.setStyleSheet("""
    #musicplayertop{
    background-color: #ffb8ce;
    color: #de6a8f;
    border: 3px solid #de6a8f;   
    border-radius: 4px;
    font-size: 25px;
    font-weight: bold;
    }
""")
leftuimainlayout.addWidget(musicplayertop)
currenttrack = QLabel("Current track placeholder")
currenttrack.setAlignment(Qt.AlignCenter)
currenttrack.setObjectName("Rowbuttonborderless")
leftuimainlayout.addWidget(currenttrack)

musicplayer = QHBoxLayout()
prevbutton = QPushButton("<<")
prevbutton.setObjectName("Row")
musicplayer.addWidget(prevbutton)
pausebutton = QPushButton("Pause")
pausebutton.setObjectName("Row")
musicplayer.addWidget(pausebutton)
nextbutton= QPushButton(">>")
nextbutton.setObjectName("Row")
musicplayer.addWidget(nextbutton)

leftuimainlayout.addLayout(musicplayer)



###################
##### LEFT UI #####
###################

###################
####  TUTORIAL  ###
###################

def tutorialcheck():
    global tutorialfinished
    if tutorialfinished == 1:
        pass
    else:
        tutorialdisplay()

def tutorialdisplay():
    global tutorialfinished
    tutorialfinished = 1
    print("Tutorial displayed!")
    ### Background dimmer ###
    dimmer = QWidget(mainwidget)
    dimmer.setObjectName("DimmerStyle")
    dimmer.setStyleSheet("""
    #DimmerStyle{
    background-color: rgba(0,0,0,150);
    }
    """)
    dimmer.resize(1910, 1000)
    dimmer.move(0,0)
    ### Background dimmer ###

    tutorial = QWidget(dimmer)
    tutorial.setObjectName("Rowbuttonless")
    tutorial.resize(700,455)
    centerer(tutorial, 0,0)
    tutoriallayout = QVBoxLayout(tutorial)
    tutoriallayout.setObjectName("Row")

    tutorialgreeting = QLabel("! ATTENTION !")
    tutorialgreeting.setObjectName("tutorialtop")
    tutorialgreeting.setAlignment(Qt.AlignCenter)

    tutoriallayout.addWidget(tutorialgreeting)

    demomsg = QLabel("Hello! Welcome to Emu Otori Clicker!\nThis message is here to tell you the game is currently only a DEMO!!!\nUI and gameplay may change as development continues!\nThis version has limited functionality!! Keep up with updates on the Itch.io page!\nI post devlogs as i work on the game!\nAnyways! I hope you enjoy my silly little clicker game :D It is tons of fun to make!\nThis will be the Tutorial screen later so uhh.. terminology!\n\nWPS: Wonderhoys Per Second! (How many Wonderhoys you make per second automatically)\nUpgrade this in the WPS upgrades section in the shop!\n(This is all the tutorial has for now. uhh.. upgrade your stuff and click lots!)\nThere are things like Ascension planned that will give you a reason to actually play!!!")
    demomsg.setObjectName("demotxt")
    demomsg.setStyleSheet("""
    #demotxt{
    color: #de6a8f;
    font-size:15px;
    font-weight:bold;
    }
""")
    demomsg.setAlignment(Qt.AlignCenter)
    tutoriallayout.addWidget(demomsg)

    demoemu = QLabel()
    demoemupixmap = QPixmap("Images\other\emututorial.png").scaled(100,100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    demoemu.setPixmap(demoemupixmap)
    demoemu.setAlignment(Qt.AlignCenter)
    tutoriallayout.addWidget(demoemu)


    tutoriallayout.addStretch()
    tutorialexit = QPushButton("I understand!")
    tutorialexit.setObjectName("Row")
    tutoriallayout.addWidget(tutorialexit)
    tutorialexit.clicked.connect(lambda: dimmer.hide())


###################
####  TUTORIAL  ###
###################
centerer(shopmainwidget, 755 , 0)
centerer(money, -5, -350)
centerer(wonderhoyspersecond, -5, -330)
centerer(clickstrengthlabel, -5,-310)
centerer(leftuiwidget,-755,0)


load_data()
tutorialcheck()
window.show()



app.aboutToQuit.connect(on_exit)
sys.exit(app.exec())