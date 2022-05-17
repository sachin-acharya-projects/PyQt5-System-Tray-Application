# System Tray Application
_______________
This is a PyQT5 based application that is built to run in background (on system tray) so it is accessible for anytime  
  
This is just a basic application  
  
_(Note  
File PyScriptSystemTray.py is irrelevant to this program  
This filec contains python-program to start any python application in SystemTray  
)_
#### Codes
````python
from PyQt5 import QtCore, QtGui, QtWidgets
from httpx import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow, app: QtWidgets.QApplication, tray: QtWidgets.QSystemTrayIcon):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 600)
        
        # Tired of editing whole code and passing variables to function everytime I call one
        self.mainWindow = MainWindow
        self.tray = tray
        MainWindow.closeEvent = lambda event: self.closeEvent(event, tray, app)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(26)
        self.gridLayout.setObjectName("gridLayout")
        self.minimizeBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy)
        self.minimizeBtn.setMinimumSize(QtCore.QSize(160, 0))
        self.minimizeBtn.setMaximumSize(QtCore.QSize(300, 40))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.minimizeBtn.clicked.connect(lambda: self.mini(tray))
        self.gridLayout.addWidget(self.minimizeBtn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QtCore.QSize(160, 0))
        self.closeBtn.setMaximumSize(QtCore.QSize(300, 40))
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.clicked.connect(lambda: self.forceClose(app))
        self.gridLayout.addWidget(self.closeBtn, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def mini(self, tray: QtWidgets.QSystemTrayIcon):
        # app.setQuitOnLastWindowClosed(False)
        print("Minimization Activated")
        _translate = QtCore.QCoreApplication.translate
        if not tray.isVisible():
            print("Tray Turned to Visible")
            tray.show()
            self.minimizeBtn.setText(_translate("MainWindow", "Disable System Tray Icon"))
        else:
            print("Tray turned Invisible")
            tray.hide()
            tray.setVisible(False)
            self.minimizeBtn.setText(_translate("MainWindow", "Enable System Tray Icon"))
    def forceClose(self, app: QtWidgets.QApplication):
        print("Force Close Activated")
        # app.setQuitOnLastWindowClosed(True)
        # tray.hide()
        app.quit()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minimizeBtn.setText(_translate("MainWindow", "Enable System Tray Icon"))
        self.closeBtn.setText(_translate("MainWindow", "Close The App"))
    def closeEvent(self, event: QtGui.QCloseEvent, tray: QtWidgets.QSystemTrayIcon, app: QtWidgets.QApplication):
        if tray.isVisible():
            event.ignore()
            print("Tray Icon is activated so closing event is ignored")
        else:
            print("Tray icon is not activated so closing event is accepted")
            app.quit()
            
def trayActivated(reason, MainWindow: QtWidgets.QMainWindow):
    # print(reason == QtWidgets.QSystemTrayIcon.DoubleClick)
    if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
        # print("Reason", reason == QtWidgets.QSystemTrayIcon.DoubleClick)
        if not MainWindow.isVisible():
            # print("Not")
            # print("Before", MainWindow.isVisible())
            toggleWindow("show", MainWindow)
        else:
            # print("Yes")
            # print("Before", MainWindow.isVisible())
            toggleWindow("hide", MainWindow)
        # print("After", MainWindow.isVisible())
def toggleWindow(context, mainWindow: QtWidgets.QMainWindow):
    # print(context)
    if context == 'show':
        mainWindow.show()
    else:
        mainWindow.hide()
    # print(mainWindow.isVisible())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    icon = QtGui.QIcon("icon.png")
    tray = QtWidgets.QSystemTrayIcon()
    tray.setIcon(icon)
    # tray.setVisible(True)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    # ui.setupUi(MainWindow, app)
    ui.setupUi(MainWindow, app, tray)
    
    menu = QtWidgets.QMenu()
    
    option_title = QtWidgets.QAction("System into Tray")
    option_title.triggered.connect(lambda: MainWindow.showMaximized())
    menu.addAction(option_title)
    
    option_show = QtWidgets.QAction("Show Window")
    option_show.triggered.connect(lambda: toggleWindow("show", MainWindow))
    menu.addAction(option_show)
    
    option_hide = QtWidgets.QAction("Hide Window")
    option_hide.triggered.connect(lambda: toggleWindow("hide", MainWindow))
    menu.addAction(option_hide)
    
    option_quit = QtWidgets.QAction("Exit")
    option_quit.triggered.connect(app.quit)
    menu.addAction(option_quit)

    tray.activated.connect(lambda reason: trayActivated(reason, MainWindow))
    # tray.activated.connect(trayActivated)
    tray.setContextMenu(menu)
    # tray.show()

    MainWindow.show()
    sys.exit(app.exec_())
````
