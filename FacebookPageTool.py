from PyQt6 import QtGui
from PyQt6.QtWidgets import QVBoxLayout, QApplication, QWidget, QLabel, QHBoxLayout, QPlainTextEdit, QPushButton, QMessageBox
from PyQt6.QtGui import *
from PyQt6.QtCore import *



class PostView(QVBoxLayout):

    def setup(self):

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        schPostLabel = QLabel()
        schPostLabel.setText("Quick Post")
        schPostLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        schPostFont = QFont()
        schPostFont.setPointSize(20)

        schPostLabel.setFont(schPostFont)

        line = QLabel()
        line.setStyleSheet("background-color : black")
        line.setFixedHeight(4)

        newPostLabel = QLabel()
        newPostLabel.setText("New Post")

        self.postText = QPlainTextEdit()
        self.postText.setStyleSheet("margin-left : 20px; margin-right : 20px;")


        photoButton = QPushButton()
        photoButton.setFixedHeight(90)
        photoButton.setFixedWidth(90)
        photoButton.setStyleSheet("border-image : url(image_add.png);")



        self.postButton = QPushButton()
        self.postButton.setText("Post")
        self.postButton.setStyleSheet("background-color : blue; color: white;")




        self.addWidget(schPostLabel)
        self.addWidget(line)
        self.addWidget(self.postText)
        self.addWidget(self.postButton)

        self.addStretch()



class PageList(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.selected = -1

    def getSelected(self):
        return self.selected

    def setup(self):
        self.selected = -1

        pageItem = self.PageItem()
        pageItem.setup()

        pageItem2 = self.PageItem()
        pageItem2.setup()


        self.addLayout(pageItem)
        self.addLayout(pageItem2)
        self.addStretch()

    def loadPageList(self, pageList):
        pageNum = len(pageList["Pages"])
        self.pageItems = []
        i = 0
        for page in pageList["Pages"]:
            print(i)
            self.pageIndex = i
            pageItem = self.PageItem()
            pageItem.setPageIndex(i)
            pageItem.setup()
            pageItem.setPageName(page["name"])
            pageItem.setPageToken(page["access_token"])
            pageItem.setPageID(page["id"])

            self.pageItems.append(pageItem)
            self.addLayout(pageItem)
            i += 1

    def setActive(self, activeIndex):
        if(activeIndex == -1):
            return
        self.pageItems[activeIndex].pageTitle.setStyleSheet("color: green;")
        if(self.selected != -1):
            self.pageItems[self.selected].pageTitle.setStyleSheet("color: black;")
        self.selected = activeIndex


    class PageItem(QHBoxLayout):

        def __init__(self):
            super().__init__()
            self.pageIndex = None

        def setup(self):
            print("Setup")
            self.profImage = QLabel()
            self.profImage.setFixedHeight(50)
            self.profImage.setFixedWidth(50)
            self.profImage.setScaledContents(True)
            self.profImage.setPixmap(QPixmap("R.JFIF"))

            self.pageTitle = PageList.ClickLabel()
            self.pageTitle.setPageIndex(self.pageIndex)

            self.pageTitle.setText("Page Name")
            f = QFont()
            f.setPointSize(18)
            self.pageTitle.setFont(f)


            self.addWidget(self.pageTitle)


        def setPageName(self, pageTitle):
            self.pageTitle.setText(pageTitle)

        def setPageID(self, pageID):
            self.pageID = pageID

        def setPageToken(self, pageToken):
            self.pageToken = pageToken

        def setPageIndex(self, pageIndex):
            self.pageIndex = pageIndex

    class ClickLabel(QLabel):

        def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
            super().mousePressEvent(ev)
            outerFun(self.pageIndex)

        def setPageIndex(self, pageIndex):
            self.pageIndex = pageIndex

def outerFun(pageIndex):
    mainPageList.setActive(pageIndex)


mainPageList = PageList()