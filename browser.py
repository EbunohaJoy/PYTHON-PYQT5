import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        # self.centralWidget(self.browser)
        self.setCentralWidget(self.browser)
        self.showMaximized()

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebBrowser()
    sys.exit(app.exec_())

