import sys

import mysql
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QStackedWidget, QMainWindow, \
    QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import mysql.connector as conn


#
class MAIN(QWidget):
    def __init__(self):
        super(MAIN, self).__init__()
        loadUi("welcome.ui", self)
        self.login_btn.clicked.connect(self.gotologin)
        self.reg_btn.clicked.connect(self.registration)

        self.setWindowTitle("Welcome Screen")
        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="",
        #     database="unistore"
        # )
        # mycursor = mydb.cursor()
        # if mycursor:
        #     print("connected")
        # else:
        #     print("failed")
        # self.show()

    def registration(self):
        register = regScreen()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # print(200)

    def gotologin(self):
        # print(200)
        logins = loginscreen()
        widget.addWidget(logins)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class regScreen(QWidget):
    def __init__(self):
        super(regScreen, self).__init__()
        loadUi("register.ui", self)
        self.rere_btn.clicked.connect(self.regfunc)

    def regfunc(self):
        username = self.username1.text()
        email = self.email1.text()
        password = self.password1.text()
        confirm = self.cpass.text()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="unistore"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        val = (username, email, password)
        mycursor.execute(sql, val)

        mydb.commit()
        if mycursor:
            QMessageBox.information(self, "Registration successful", "Registration successful", QMessageBox.Ok,
                                    QMessageBox.Ok)
            # self.close()
            school = schoolscreen()
            widget.addWidget(school)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        # print(mycursor.rowcount, "record inserted.")


class loginscreen(QWidget):
    def __init__(self):
        super(loginscreen, self).__init__()
        loadUi("login.ui", self)
        self.login_btn2.clicked.connect(self.loginfunction)

    def loginfunction(self):
        # print(300)
        username = self.username_input.text()
        password = self.password_input.text()
        if len(username) == 0 or len(password) == 0:
            self.error.setText("input all fields")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="unistore"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT username, password FROM users")

        myresult = mycursor.fetchall()

        for x in myresult:
            if username == x[0] and password == x[1]:
                QMessageBox.information(self, "Login successful", "Login successful", QMessageBox.Ok,
                                        QMessageBox.Ok)
                school = schoolscreen()
                widget.addWidget(school)
                widget.setCurrentIndex(widget.currentIndex() + 1)

        else:
            self.error.setText("User not found")


class schoolscreen(QMainWindow):
    def __init__(self):
        super(schoolscreen, self).__init__()
        loadUi("school.ui", self)
        self.iniui()

    def iniui(self):
        self.setGeometry(700, 700, 800, 800)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    firstWindow = MAIN()
    widget = QStackedWidget()
    widget.addWidget(firstWindow)
    widget.setFixedHeight(300)
    widget.setFixedWidth(400)
    widget.show()
    sys.exit(app.exec_())
