from os.path import exists

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QApplication, QWidget, QMessageBox, QPushButton, QDialog, QVBoxLayout

from FacebookApiUI import Ui_Form, storageFile
from FacebookPageTool import PageList, PostView, mainPageList


def postClick():
    if(postView.postText.toPlainText() == "" or mainPageList.selected == -1):
        return
    ui.postToPage(mainPageList.pageItems[mainPageList.selected].pageID, postView.postText.toPlainText(), mainPageList.pageItems[mainPageList.selected].pageToken)

def retryClick():
    if(ui.STTRetrieve() == False):
        return

    res2 = ui.LTTRetrieve()
    print(res2)
    res3 = ui.PagesRetrieve()
    q.hide()
    widget.setWindowOpacity(1)
    ui.getVariables()
    mainPageList.loadPageList(ui.getPageJSON())

app = QApplication([])
widget = QWidget()
widget.setWindowTitle("Page Quick Post")

widget.setFixedHeight(400)
widget.setFixedWidth(500)

fullLayout = QHBoxLayout()

pageList = PageList()

postView = PostView()
postView.setup()

line = QLabel()
line.setStyleSheet("background-color : black")

fullLayout.addLayout(mainPageList)
fullLayout.addWidget(line)
fullLayout.addLayout(postView)


Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.init()
msg = QMessageBox()
msg.setTextFormat(Qt.TextFormat.RichText)
msg.setWindowTitle("Login Required")

diagLayout = QVBoxLayout()
q = QDialog()
q.setWindowTitle("Login Required")
diagLabel = QLabel(q)
diagLabel.setOpenExternalLinks(True)
diagLabel.setTextFormat(Qt.TextFormat.RichText)
diagLabel.setText('Visit <a href="http://facebook.com/devices">Facebook.com/devices</a>' + " \nEnter Code:")
b1 = QPushButton(q)
b1.setText("Connect")
b1.clicked.connect(retryClick)
diagLayout.addWidget(diagLabel)
diagLayout.addWidget(b1)
q.setLayout(diagLayout)

retryBtn = QPushButton()
retryBtn.setText("Retry")
msg.addButton(retryBtn, QMessageBox.ButtonRole.NoRole)
msg.buttonClicked.connect(retryClick)

msgTemplate = 'Visit <a href="http://facebook.com/devices">Facebook.com/devices</a>' + " Enter Code:"
if not(exists(storageFile)):
    file = open(storageFile, "w")
    file.write("STT=X\n")
    file.write("LTT=X\n")
    file.write("PageList=X\n")
    file.write("PAT=X\n")
    file.close()


postView.postButton.clicked.connect(postClick)
widget.setLayout(fullLayout)





widget.show()

if(ui.getVariables()):
    mainPageList.loadPageList(ui.getPageJSON())
else:
    lc = ui.LCRetrieve()
    diagLabel.setText(msgTemplate + lc)
    widget.setWindowOpacity(.9)
    q.show()



app.exec()