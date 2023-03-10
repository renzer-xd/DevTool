# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser
import os
import subprocess
config_object = ConfigParser()
config_object.read("setting.ini")
Config = config_object["PATH"]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 251)
        MainWindow.setMinimumSize(QtCore.QSize(504, 251))
        MainWindow.setMaximumSize(QtCore.QSize(504, 251))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(44, 51, 51);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 311, 211))
        self.groupBox.setStyleSheet("background-color: rgb(57, 91, 100);\n"
                                    "border-radius: 5px;\n"
                                    "color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_path_cgf = QtWidgets.QLabel(self.groupBox)
        self.label_path_cgf.setGeometry(QtCore.QRect(20, 20, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_path_cgf.setFont(font)
        self.label_path_cgf.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_path_cgf.setObjectName("label_path_cgf")
        self.input_path_cfg = QtWidgets.QLineEdit(self.groupBox)
        self.input_path_cfg.setGeometry(QtCore.QRect(20, 40, 271, 20))
        self.input_path_cfg.setStyleSheet("background-color: rgb(231, 246, 242);\n"
                                          "color: rgb(0, 0, 0);")
        self.input_path_cfg.setObjectName("input_path_cfg")
        self.input_path_run = QtWidgets.QLineEdit(self.groupBox)
        self.input_path_run.setGeometry(QtCore.QRect(20, 90, 271, 20))
        self.input_path_run.setStyleSheet("background-color: rgb(231, 246, 242);\n"
                                          "color: rgb(0, 0, 0);")
        self.input_path_run.setObjectName("input_path_run")
        self.input_name_run = QtWidgets.QLineEdit(self.groupBox)
        self.input_name_run.setGeometry(QtCore.QRect(20, 140, 121, 20))
        self.input_name_run.setStyleSheet("background-color:rgb(231, 246, 242);\n"
                                          "color: rgb(0, 0, 0);")
        self.input_name_run.setObjectName("input_name_run")
        self.input_ip = QtWidgets.QLineEdit(self.groupBox)
        self.input_ip.setGeometry(QtCore.QRect(160, 140, 131, 20))
        self.input_ip.setStyleSheet("background-color:rgb(231, 246, 242);\n"
                                    "color: rgb(0, 0, 0);")
        self.input_ip.setObjectName("input_ip")
        self.ilabel_path_run = QtWidgets.QLabel(self.groupBox)
        self.ilabel_path_run.setGeometry(QtCore.QRect(20, 70, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ilabel_path_run.setFont(font)
        self.ilabel_path_run.setStyleSheet("color: rgb(255, 255, 255);")
        self.ilabel_path_run.setObjectName("ilabel_path_run")
        self.btn_save = QtWidgets.QPushButton(self.groupBox)
        self.btn_save.setGeometry(QtCore.QRect(200, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setStyleSheet("#btn_save {\n"
                                    "    background-color: rgb(10, 198, 255); \n"
                                    "}\n"
                                    "\n"
                                    "#btn_save::pressed {\n"
                                    "    \n"
                                    "    background-color: rgb(28, 130, 255);\n"
                                    "}\n"
                                    "")
        self.btn_save.setCheckable(False)
        self.btn_save.setAutoRepeat(False)
        self.btn_save.setAutoExclusive(False)
        self.btn_save.setObjectName("btn_save")
        self.label_name_run = QtWidgets.QLabel(self.groupBox)
        self.label_name_run.setGeometry(QtCore.QRect(20, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_name_run.setFont(font)
        self.label_name_run.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_name_run.setObjectName("label_name_run")
        self.label_ip = QtWidgets.QLabel(self.groupBox)
        self.label_ip.setGeometry(QtCore.QRect(160, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.btn__open_fivem = QtWidgets.QPushButton(self.centralwidget)
        self.btn__open_fivem.setGeometry(QtCore.QRect(350, 200, 131, 31))
        self.btn__open_fivem.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn__open_fivem.setStyleSheet("#btn__open_fivem {\n"
                                           "    border-radius: 10px;\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(10, 198, 255); \n"
                                           "}\n"
                                           "\n"
                                           "#btn__open_fivem::pressed {\n"
                                           "    \n"
                                           "    background-color: rgb(28, 130, 255);\n"
                                           "}\n"
                                           "")
        self.btn__open_fivem.setObjectName("btn__open_fivem")
        self.btn_run_server = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run_server.setGeometry(QtCore.QRect(350, 140, 131, 31))
        self.btn_run_server.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_run_server.setStyleSheet("#btn_run_server {\n"
                                          "    border-radius: 10px;\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(10, 198, 255); \n"
                                          "}\n"
                                          "\n"
                                          "#btn_run_server::pressed {\n"
                                          "    \n"
                                          "    background-color: rgb(28, 130, 255);\n"
                                          "}\n"
                                          "")
        self.btn_run_server.setObjectName("btn_run_server")
        self.btn_open_cfg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_cfg.setGeometry(QtCore.QRect(350, 80, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_open_cfg.sizePolicy().hasHeightForWidth())
        self.btn_open_cfg.setSizePolicy(sizePolicy)
        self.btn_open_cfg.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_open_cfg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_open_cfg.setFont(font)
        self.btn_open_cfg.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_open_cfg.setStyleSheet("#btn_open_cfg {\n"
                                        "    border-radius: 10px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(10, 198, 255); \n"
                                        "}\n"
                                        "\n"
                                        "#btn_open_cfg::pressed {\n"
                                        "    \n"
                                        "    background-color: rgb(28, 130, 255);\n"
                                        "}\n"
                                        "")
        self.btn_open_cfg.setAutoRepeatInterval(100)
        self.btn_open_cfg.setDefault(False)
        self.btn_open_cfg.setFlat(False)
        self.btn_open_cfg.setObjectName("btn_open_cfg")
        self.btn_open_folder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_folder.setGeometry(QtCore.QRect(350, 20, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_open_folder.sizePolicy().hasHeightForWidth())
        self.btn_open_folder.setSizePolicy(sizePolicy)
        self.btn_open_folder.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_open_folder.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_open_folder.setFont(font)
        self.btn_open_folder.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_open_folder.setStyleSheet("#btn_open_folder {\n"
                                           "    border-radius: 10px;\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(10, 198, 255); \n"
                                           "}\n"
                                           "\n"
                                           "#btn_open_folder::pressed {\n"
                                           "    \n"
                                           "    background-color: rgb(28, 130, 255);\n"
                                           "}\n"
                                           "")
        self.btn_open_folder.setAutoRepeatInterval(100)
        self.btn_open_folder.setDefault(False)
        self.btn_open_folder.setFlat(False)
        self.btn_open_folder.setObjectName("btn_open_folder")

        self.btn_save.clicked.connect(self.on_save)

        self.btn_open_folder.clicked.connect(self.on_folder)

        self.btn_open_cfg.clicked.connect(self.on_open_cfg)

        self.btn_run_server.clicked.connect(self.on_run_server)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "DevTool - RenZer Developer Shop"))
        self.groupBox.setTitle(_translate("MainWindow", "Setting Path"))
        self.label_path_cgf.setText(_translate(
            "MainWindow", "????????????????????? Path ????????? Server.cfg"))
        self.ilabel_path_run.setText(_translate(
            "MainWindow", "????????????????????? Path ????????? ?????????????????????????????????????????????"))
        self.btn_save.setText(_translate("MainWindow", "Save Setting"))
        self.label_name_run.setText(_translate(
            "MainWindow", "???????????????????????? ??????????????????????????????????????????????????????"))
        self.label_ip.setText(_translate("MainWindow", "IP Server"))
        self.btn__open_fivem.setText(
            _translate("MainWindow", "Connect Server"))
        self.btn_run_server.setText(_translate("MainWindow", "Run Server"))
        self.btn_open_cfg.setText(_translate("MainWindow", "Open server.cgf"))
        self.btn_open_folder.setText(_translate("MainWindow", "Open Folder"))

        self.input_path_cfg.setText(Config["path_sever_cfg"])
        self.input_path_run.setText(Config["path_run"])
        self.input_name_run.setText(Config["name_run"])
        self.input_ip.setText(Config["ip_server"])

    def on_save(self):
        Config["path_sever_cfg"] = self.input_path_cfg.text()
        Config["path_run"] = self.input_path_run.text()
        Config["name_run"] = self.input_name_run.text()
        Config["ip_server"] = self.input_ip.text()
        with open('setting.ini', 'w') as conf:
            config_object.write(conf)

    def on_folder(self):
        if Config["path_sever_cfg"] != "":
            os.path.realpath(Config["path_sever_cfg"])
            os.startfile(Config["path_sever_cfg"])

    def on_open_cfg(self):
        os.startfile(Config["path_sever_cfg"]+'/server.cfg')

    def on_run_server(self):
        # os.system("cmd.exe /C " + Config["path_run"]+'/{}'.format(Config["name_run"]))
        subprocess.run(
            [Config["path_run"] + "\\" + Config["name_run"]],
            cwd=Config["name_run"],
            shell=True
        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
