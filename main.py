from PyQt5.QtWidgets import *
import sys
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.initUI()

    def initUI(self):
        self.l = QLabel(self)
        self.l.setText("Привет")
        self.l.move(50, 50)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Попробуй закрыть')
        self.show()


    def closeEvent(self, event):
        list = ["Ты точно хочешь закрыть программу?", "Ты уверен в этом?", "Зачем ты это делаешь?", "Ты безумец?"]
        x = random.randint(0, QApplication.desktop().screenGeometry().width() - self.width())
        y = random.randint(0, QApplication.desktop().screenGeometry().height() - self.height())
        self.move(x, y)
        event.ignore()
        reply = QMessageBox.question(self, 'Message',
            f"{random.choice(list)} : {self.counter}",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        while reply == QMessageBox.Yes:
            self.counter += 1
            x = random.randint(0, QApplication.desktop().screenGeometry().width() - self.width())
            y = random.randint(0, QApplication.desktop().screenGeometry().height() - self.height())
            self.move(x, y)
            reply = QMessageBox.question(self, 'Message',
                                         f"{random.choice(list)}: {self.counter}",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    a = input("Press enter to continue")