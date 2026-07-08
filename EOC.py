import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QScrollArea, QWidget, QVBoxLayout, QStackedWidget, QMessageBox, QFrame
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap
import pygame
import pickle

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
window.setFixedSize(1920,1080)

pixmap = QPixmap("Images\other\emu.png").scaled(350,350, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

mainwidget.setStyleSheet("""
    #background {
        border-image: url(Images/other/gamebckgrn3.png) 0 0 0 0 stretch stretch;
    }
""")

layout = QVBoxLayout()
mainwidget.setLayout(layout)

def clickevent():
    global wonderhoys, money

    wonderhoys += 1
    money.setText(f"Wonderhoys: {wonderhoys}")


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
    x = (1920 - input.width()) // 2
    y = (1080 - input.height()) // 2
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





centerer(money, -5, -350)



load_data()
window.show()



app.aboutToQuit.connect(on_exit)
sys.exit(app.exec())