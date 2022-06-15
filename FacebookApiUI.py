from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
import requests, json


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(713, 428)
        Form.setToolTip("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 417, 166))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.PID_LE = QtWidgets.QLineEdit(self.widget)
        self.PID_LE.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PID_LE.sizePolicy().hasHeightForWidth())
        self.PID_LE.setSizePolicy(sizePolicy)
        self.PID_LE.setToolTip("")
        self.PID_LE.setObjectName("PID_LE")
        self.verticalLayout_2.addWidget(self.PID_LE)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LCBtn = QPushButton(self.widget)
        self.LCBtn.setObjectName("LCBtn")
        self.LCBtn.clicked.connect(self.LCRetrieve)
        self.verticalLayout_3.addWidget(self.LCBtn)
        self.STTBtn = QPushButton(self.widget)
        self.STTBtn.setObjectName("STTBtn")
        self.STTBtn.clicked.connect(self.STTRetrieve)
        self.verticalLayout_3.addWidget(self.STTBtn)
        self.LTTBtn = QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LTTBtn.sizePolicy().hasHeightForWidth())
        self.LTTBtn.setSizePolicy(sizePolicy)
        self.LTTBtn.setObjectName("LTTBtn")
        self.LTTBtn.clicked.connect(self.LTTRetrieve)
        self.verticalLayout_3.addWidget(self.LTTBtn)
        self.GPLBtn = QPushButton(self.widget)
        self.GPLBtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GPLBtn.sizePolicy().hasHeightForWidth())
        self.GPLBtn.setSizePolicy(sizePolicy)
        self.GPLBtn.setObjectName("GPLBtn")
        self.GPLBtn.clicked.connect(self.PagesRetrieve)
        self.verticalLayout_3.addWidget(self.GPLBtn)
        self.PATBtn = QtWidgets.QPushButton(self.widget)
        self.PATBtn.setObjectName("PATBtn")
        self.verticalLayout_3.addWidget(self.PATBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LCLabel = QtWidgets.QLabel(self.widget)
        self.LCLabel.setObjectName("LCLabel")
        self.verticalLayout_4.addWidget(self.LCLabel)
        self.STTLabel = QtWidgets.QLabel(self.widget)
        self.STTLabel.setObjectName("STTLabel")
        self.verticalLayout_4.addWidget(self.STTLabel)
        self.LTTLabel = QtWidgets.QLabel(self.widget)
        self.LTTLabel.setObjectName("LTTLabel")
        self.verticalLayout_4.addWidget(self.LTTLabel)
        self.GPLLabel = QtWidgets.QLabel(self.widget)
        self.GPLLabel.setObjectName("GPLLabel")
        self.verticalLayout_4.addWidget(self.GPLLabel)
        self.PATLabel = QtWidgets.QLabel(self.widget)
        self.PATLabel.setObjectName("PATLabel")
        self.verticalLayout_4.addWidget(self.PATLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def init(self):
        self.appID = 780131783148278
        self.appSecret = "dd495f7b58f6a4581eaa74fabf30dade"
        self.clientToken = "bea87ab616584d0a577adcba25ede947"
        self.LCLink = "https://graph.facebook.com/v2.6/device/login?access_token=" + str(
            self.appID) + "|" + self.clientToken + "&scope=pages_show_list,pages_manage_posts,pages_read_engagement"
        self.code = ""
        self.STT = ""
        self.LTT = ""
        self.STTLink = "https://graph.facebook.com/v2.6/device/login_status?access_token=" + str(
            self.appID) + "|" + self.clientToken + "&code=" + self.code
        self.LTTLink = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + str(
            self.appID) + "&client_secret=" + self.appSecret + "&fb_exchange_token=" + self.STT

    def writeVariable(self, stringName, value):
        file = open("storage.txt", "r")
        currentLines = file.readlines()
        file.close()

        file = open("storage.txt", "w")
        found = 0

        for line in currentLines:
            items = line.split("=")
            if(items[0] == stringName):
                file.write(stringName + "=" + value + "\n")
                found = 1
                continue
            file.write(line)

        if(found == 0):
            file.write(stringName + "=" + value + "\n")

        file.close()

    def LCRetrieve(self):
        LCResponse = requests.post(self.LCLink)
        LCRJSON = LCResponse.json()
        for key, value in LCRJSON.items():
            if(key == "code"):
                self.code = value
                self.STTLink = self.STTLink = "https://graph.facebook.com/v2.6/device/login_status?access_token=" + str(self.appID) + "|" + self.clientToken + "&code=" + self.code
            if(key == "user_code"):
                return value

    def STTRetrieve(self):
        STTResponse = requests.post(self.STTLink)
        STTRJSON = STTResponse.json()
        for key, value in STTRJSON.items():
            if(key == "error"):
                return False
            if(key == "access_token"):
                self.STT = value
                self.LTTLink = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + str(
                    self.appID) + "&client_secret=" + self.appSecret + "&fb_exchange_token=" + self.STT
        self.writeVariable("STT", self.STT)
        return True

    def PagesRetrieve(self):
        getPages = "https://graph.facebook.com/v13.0/me/accounts?access_token=" + self.LTT
        pagesResponse = requests.get(getPages)
        pagesJSON = pagesResponse.json()


        PageList = '{"Pages": ['
        pos = 0

        for key in pagesJSON["data"]:
            PageList += '{"id": "'
            PageList += key["id"]
            PageList += '", '

            PageList += '"access_token": "'
            PageList += key["access_token"]
            PageList += '", '

            PageList += '"name": "'
            PageList += key["name"]

            if(pos == len(pagesJSON['data'])-1):
                PageList += '"}]}'
                break
            PageList += '"} , '

            pos += 1

        self.writeVariable("PageList", PageList)

    def LTTRetrieve(self):
        LTTResponse = requests.post(self.LTTLink)
        LTTRJSON = LTTResponse.json()
        for key, value in LTTRJSON.items():
            if(key == "access_token"):
                self.LTT = value
        self.writeVariable("LTT", self.LTT)

    def getVariables(self):
        file = open(storageFile, "r")
        lines = file.readlines()

        for line in lines:
            items = line.split("=")
            if (items[0] == "STT"):
                if(items[1].replace("\n", "") == "X"):
                    return False
                self.STT = items[1].replace("\n", "")
            elif (items[0] == "LTT"):
                self.LTT = items[1].replace("\n", "")
            elif (items[0] == "PageList"):
                pageListString = items[1].replace("\n", "")
                if(pageListString == "X"):
                    continue
                self.pageListJSON = json.loads(pageListString)
        return True

    def getPAT(self, pageID):
        PATLink = "https://graph.facebook.com/" + pageID + "?fields=access_token&access_token=" + self.LTT
        PATResult = requests.get(PATLink)
        PATJSON = PATResult.json()

    def getPageJSON(self):
        return self.pageListJSON

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "App ID:"))
        self.label_12.setText(_translate("Form", "780131783148278"))
        self.label_10.setText(_translate("Form", "Client Token:"))
        self.label_11.setText(_translate("Form", "bea87ab616584d0a577adcba25ede947"))
        self.label_5.setText(_translate("Form", "Login Code"))
        self.label.setText(_translate("Form", "Short-Term Token"))
        self.label_2.setText(_translate("Form", "Long-Term Token"))
        self.label_3.setText(_translate("Form", "Get Page List"))
        self.label_4.setText(_translate("Form", "Page Access Token"))
        self.PID_LE.setPlaceholderText(_translate("Form", "Page ID"))
        self.LCBtn.setText(_translate("Form", "Retrieve"))
        self.STTBtn.setText(_translate("Form", "Retrieve"))
        self.LTTBtn.setText(_translate("Form", "Retrieve"))
        self.GPLBtn.setText(_translate("Form", "Retrieve"))
        self.PATBtn.setText(_translate("Form", "Retrieve"))
        self.LCLabel.setText(_translate("Form", "---"))
        self.STTLabel.setText(_translate("Form", "---"))
        self.LTTLabel.setText(_translate("Form", "---"))
        self.GPLLabel.setText(_translate("Form", "---"))
        self.PATLabel.setText(_translate("Form", "---"))


    def postToPage(self, pageID, message, accessID):
        postLink = "https://graph.facebook.com/" + str(pageID) + "/feed?message=" + message + "&access_token=" + str(accessID)
        y = requests.post(postLink)

storageFile = "storage.txt"