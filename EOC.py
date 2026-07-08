import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QScrollArea, QWidget, QVBoxLayout, QStackedWidget, QMessageBox, QFrame, QHBoxLayout
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap
import pygame
import pickle

pygame.mixer.init()

saveloc = "Data/game_data.dat"

#### SAVE HANDLING ####

def save_data():
    data = {
        "wonderhoys" : wonderhoys
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
            "wonderhoys": 0
        }
    
game_data = load_data()


#### SAVE HANDLING ####

#### GLOBAL VARIABLES ####

wonderhoys = game_data['wonderhoys'] #(main currency)


#### GLOBAL VARIABLES ####




app = QApplication(sys.argv)

window = QMainWindow()
mainwidget = QWidget()
mainwidget.setObjectName("background")
window.setCentralWidget(mainwidget)
window.setFixedSize(1910,1000)

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
    global wonderhoys, money

    wonderhoys += 1
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
    x = (1910 - input.width()) // 2
    y = (1000 - input.height()) // 2
    input.move(x + xoffset,y + yoffset)

centerer(emubutton, 0, -100)

emubutton.clicked.connect(clickevent)

money = QLabel(f"Wonderhoys:{wonderhoys}")
money.setParent(mainwidget)
money.resize(250,140)
money.setObjectName("money")
money.setAlignment(Qt.AlignCenter)
money.setStyleSheet(""" 
    #money {
    background-color: #fce0ed;
    color: #ffb2d7;
    border: 4px solid #ffb2d7;   
    border-radius: 4px;
    font-size: 24px;    
    font-weight: bold;
    }
""")

shopmainwidget = QWidget()
shopmainlayout = QVBoxLayout()
shopmainwidget.setLayout(shopmainlayout)
shopmainwidget.resize(400,1000)
shopmainwidget.setParent(mainwidget)
shopmainwidget.setObjectName("Test")
shopmainwidget.setStyleSheet("""
    #Test {
    background-color: #fce0ed;
    color: #ffb2d7;
    border: 4px solid #ffb2d7;   
    border-radius: 4px;
    }
""")
shoptitle = QLabel("Shop!")
shoptitle.setAlignment(Qt.AlignCenter)
shoptitle.resize(200,10)
shoptitle.setObjectName("Shopname")
shoptitle.setStyleSheet("""
    #Shopname{
    background-color: #ffb8ce;
    color: #ff7aa4;
    border: 5px solid #ff7aa4;   
    border-radius: 4px;
    font-size: 65px;
    font-weight: bold;
    }
""")
shopmainlayout.addWidget(shoptitle)
rowstyle ="""
    #Row {
    background-color: #ffb8ce;
    color: #ff7aa4;
    border: 3px solid #ff7aa4;   
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
testrow1=QPushButton("Test1")
testrow1.setObjectName("Row")

testrow2=QPushButton("Test2")
testrow2.setObjectName("Row")

shopscroller = QScrollArea(shopmainwidget)
shopscroller.setWidgetResizable(True)
rowstyle2 ="""
    #RowScroller {
    background-color: #ffb8ce;
    color: #ff7aa4;
    border: 3px solid #ff7aa4;   
    border-radius: 4px;
    font-size: 17px;
    font-weight: bold;
    }
"""
app.setStyleSheet(rowstyle + rowstyle2)
shopcontainerstack = QStackedWidget()
shopcontainerstack.setObjectName("RowScroller")

# 1st page
firstpage = QWidget()
firstpagelayout = QVBoxLayout(firstpage)
for i in range(1, 21):
    upgrade_button = QPushButton(f"TestUpg{i}\nprice: NaN")
    upgrade_button.setObjectName("Row")
    firstpagelayout.addWidget(upgrade_button)
firstpagelayout.addStretch()

# 2nd page
secondpage = QWidget()
secondpagelayout = QVBoxLayout(secondpage)
placeholder12 = QPushButton("TestUpg3\nprice: NaN", secondpage)
secondpagelayout.addWidget(placeholder12)
placeholder22 = QPushButton("TestUpg4\nprice: NaN", secondpage)
secondpagelayout.addWidget(placeholder22)
secondpagelayout.addStretch()

shopcontainerstack.addWidget(firstpage)
shopcontainerstack.addWidget(secondpage)

testrow1.clicked.connect(lambda: shopcontainerstack.setCurrentIndex(0))
testrow2.clicked.connect(lambda: shopcontainerstack.setCurrentIndex(1))

shopscroller.setWidget(shopcontainerstack)
shopscroller.resize(shopmainwidget.width(), shopmainwidget.height()-120)
shopscroller.move(0,120)


upgraderow.addWidget(testrow1)
upgraderow.addWidget(testrow2)
shopmainlayout.addLayout(upgraderow)
shopmainlayout.addStretch()
shopmainlayout.setContentsMargins(0, 0, 0, 0)
shopmainlayout.setSpacing(2)


centerer(shopmainwidget, 755 , 0)

centerer(money, -5, -350)



load_data()
window.show()



app.aboutToQuit.connect(on_exit)
sys.exit(app.exec())