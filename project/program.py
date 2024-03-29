import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

class Cinemaaaa2(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('cinemaaaa2.ui', self)
        
        self.marvel.clicked.connect(self.open_cinemaaaa1)
        self.cinemaaaa1 = Cinemaaaa1()
        self.avatar.clicked.connect(self.open_avatar)
        self.avatar = Avatar()
        self.sobaka.clicked.connect(self.open_sobaka)
        self.sobaka = Sobaka()
        self.potter.clicked.connect(self.open_harry)
        self.harry = Harry()
        self.barbie.clicked.connect(self.open_barbie)
        self.barbie = Barbie()
        self.duna.clicked.connect(self.open_duna)
        self.duna = Duna()
        self.pony.clicked.connect(self.open_pony)
        self.pony = Pony()
        self.turtles.clicked.connect(self.open_turtles)
        self.turtles = Turtles()
        self.gravity.clicked.connect(self.open_gravity)
        self.gravity = Gravity()
        self.bob.clicked.connect(self.open_bob)
        self.bob = Bob()
        self.panda.clicked.connect(self.open_panda)
        self.panda = Panda()
        self.winx.clicked.connect(self.open_winx)
        self.winx = Winx()
        self.wednesday.clicked.connect(self.open_wednesday)
        self.wednesday = Wednesday()
        self.pretty.clicked.connect(self.open_pretty)
        self.pretty = Pretty()
        self.umbrella.clicked.connect(self.open_umbrella)
        self.umbrella = Umbrella()
        self.strong.clicked.connect(self.open_strong)
        self.strong = Strong()
        self.sherlock.clicked.connect(self.open_sherlock)
        self.sherlock = Sherlock()
        self.roxolana.clicked.connect(self.open_hurrem)
        self.hurrem = Hurrem()
    
    def open_cinemaaaa1(self):
        self.cinemaaaa1.show()
        self.hide()
    
    def open_avatar(self):
        self.avatar.show()
        self.hide()

    def open_sobaka(self):
        self.sobaka.show()
        self.hide()

    def open_harry(self):
        self.harry.show()
        self.hide()
    
    def open_barbie(self):
        self.barbie.show()
        self.hide()

    def open_duna(self):
        self.duna.show()
        self.hide()

    def open_pony(self):
        self.pony.show()
        self.hide()

    def open_turtles(self):
        self.turtles.show()
        self.hide()

    def open_gravity(self):
        self.gravity.show()
        self.hide()

    def open_bob(self):
        self.bob.show()
        self.hide()

    def open_panda(self):
        self.panda.show()
        self.hide()

    def open_winx(self):
        self.winx.show()
        self.hide()

    def open_wednesday(self):
        self.wednesday.show()
        self.hide()

    def open_pretty(self):
        self.pretty.show()
        self.hide()

    def open_umbrella(self):
        self.umbrella.show()
        self.hide()

    def open_strong(self):
        self.strong.show()
        self.hide()

    def open_sherlock(self):
        self.sherlock.show()
        self.hide()

    def open_hurrem(self):
        self.hurrem.show()
        self.hide()

class Cinemaaaa1 (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('cinemaaaa1.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()
    

class Avatar (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('avatar.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Sobaka (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('sobaka.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Harry (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('harry.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Barbie (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('barbie.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Duna (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('dune.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Pony (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('pony.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Turtles (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('turtles.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Gravity (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('gravity.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Bob (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('bob.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Panda (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('panda.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Winx (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('winx.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Wednesday (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('wednesday.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Pretty (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('pretty.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Umbrella (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('umbrella2.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Strong (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('strong.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

class Sherlock (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('sherlok.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()
        
class Hurrem (QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('hurrem.ui', self)
        self.setWindowTitle("Cinemaaaa2")
        self.vert.clicked.connect(self.go_back)

    def go_back(self):
        self.cinemaaaa2 = Cinemaaaa2()
        self.cinemaaaa2.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cinemaaaa2 = Cinemaaaa2()
    cinemaaaa2.show()
    sys.exit(app.exec_())

