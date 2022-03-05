from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting an icon for a window
        self.setWindowIcon(QIcon('icon.png'))

        # set the title
        self.setWindowTitle('vk.com/away to normal url')

        # setting the minimum size
        width = 620
        height = 250
        self.setMinimumSize(width, height)

        # making the textbox for input
        self.textBox1 = QLineEdit(self)
        self.textBox1.move(50, 60)
        # resizing textbox with input
        self.textBox1.resize(500, 30)

        # creating a label widget
        self.info = QLabel('Enter vk.com/away address', self)
        self.info.move(50, 30)
        # resizing label
        self.info.resize(1000, 20)

        # adding a button for transformation
        self.button1 = QPushButton('Transform', self)
        self.button1.move(450, 100)

        # creating second label widget
        self.info = QLabel("Here's your normal url", self)
        self.info.move(50, 130)
        # resizing label
        self.info.resize(1000, 20)

        # making the textbox for output
        self.textBox2 = QLineEdit(self)
        self.textBox2.move(50, 160)
        # resizing textbox with input
        self.textBox2.resize(500, 30)

        # adding a button for transformation
        self.button2 = QPushButton('Clear Screen', self)
        self.button2.move(450, 200)

        # resuts of clicking on btn
        self.button1.clicked.connect(lambda: self.transform())
        self.button2.clicked.connect(lambda: self.clearScreen())

    # method for applying transformation to string
    def transform(self):
        brief = self.textBox1.text()
        self.textBox2.setText(
            brief.replace('https://vk.com/away.php?to=', '') \
                .replace('%3A', ':') \
                .replace('%2F', '/')
        )

    # method for clearing screen
    def clearScreen(self):
        self.textBox1.clear()
        self.textBox2.clear()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

window.create()

# testing string
# https://vk.com/away.php?to=https%3A%2F%2Fgist.github.com%2Fshahwan42%2F279f6ec17dfc91ec9c6f778ae2877b2d
# https://gist.github.com/shahwan42/279f6ec17dfc91ec9c6f778ae2877b2d
