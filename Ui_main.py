# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\python\email\main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 643)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_splitter = QtWidgets.QSplitter(self.centralWidget)
        self.frame_splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_splitter.setOrientation(QtCore.Qt.Vertical)
        self.frame_splitter.setObjectName("frame_splitter")
        self.groupBox = QtWidgets.QGroupBox(self.frame_splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
"    border:none;\n"
"}")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setContentsMargins(2, 8, -1, 8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.txt_subject = QtWidgets.QLineEdit(self.groupBox_6)
        self.txt_subject.setObjectName("txt_subject")
        self.horizontalLayout_6.addWidget(self.txt_subject)
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.txt_fromName = QtWidgets.QLineEdit(self.groupBox_6)
        self.txt_fromName.setMaximumSize(QtCore.QSize(100, 16777215))
        self.txt_fromName.setObjectName("txt_fromName")
        self.horizontalLayout_6.addWidget(self.txt_fromName)
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.txt_fromEmail = QtWidgets.QLineEdit(self.groupBox_6)
        self.txt_fromEmail.setObjectName("txt_fromEmail")
        self.horizontalLayout_6.addWidget(self.txt_fromEmail)
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.txt_reply = QtWidgets.QLineEdit(self.groupBox_6)
        self.txt_reply.setObjectName("txt_reply")
        self.horizontalLayout_6.addWidget(self.txt_reply)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.group_editor_toolbar = QtWidgets.QGroupBox(self.groupBox)
        self.group_editor_toolbar.setMinimumSize(QtCore.QSize(0, 0))
        self.group_editor_toolbar.setStyleSheet("QGroupBox{\n"
"    border:none;\n"
"}")
        self.group_editor_toolbar.setTitle("")
        self.group_editor_toolbar.setObjectName("group_editor_toolbar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.group_editor_toolbar)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_undo = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/editor/misc/icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_undo.setIcon(icon)
        self.btn_undo.setObjectName("btn_undo")
        self.horizontalLayout_4.addWidget(self.btn_undo)
        self.btn_redo = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/editor/misc/icons/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_redo.setIcon(icon1)
        self.btn_redo.setObjectName("btn_redo")
        self.horizontalLayout_4.addWidget(self.btn_redo)
        self.combo_font = QtWidgets.QComboBox(self.group_editor_toolbar)
        self.combo_font.setObjectName("combo_font")
        self.combo_font.addItem("")
        self.combo_font.addItem("")
        self.combo_font.addItem("")
        self.combo_font.addItem("")
        self.combo_font.addItem("")
        self.combo_font.addItem("")
        self.combo_font.addItem("")
        self.horizontalLayout_4.addWidget(self.combo_font)
        self.combo_size = QtWidgets.QComboBox(self.group_editor_toolbar)
        self.combo_size.setObjectName("combo_size")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.combo_size.addItem("")
        self.horizontalLayout_4.addWidget(self.combo_size)
        self.btn_bgcolor = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/editor/misc/icons/bgcolor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_bgcolor.setIcon(icon2)
        self.btn_bgcolor.setObjectName("btn_bgcolor")
        self.horizontalLayout_4.addWidget(self.btn_bgcolor)
        self.btn_color = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/editor/misc/icons/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_color.setIcon(icon3)
        self.btn_color.setObjectName("btn_color")
        self.horizontalLayout_4.addWidget(self.btn_color)
        self.btn_bold = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/editor/misc/icons/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_bold.setIcon(icon4)
        self.btn_bold.setCheckable(True)
        self.btn_bold.setObjectName("btn_bold")
        self.horizontalLayout_4.addWidget(self.btn_bold)
        self.btn_italic = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/editor/misc/icons/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_italic.setIcon(icon5)
        self.btn_italic.setCheckable(True)
        self.btn_italic.setObjectName("btn_italic")
        self.horizontalLayout_4.addWidget(self.btn_italic)
        self.btn_underline = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/editor/misc/icons/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_underline.setIcon(icon6)
        self.btn_underline.setCheckable(True)
        self.btn_underline.setObjectName("btn_underline")
        self.horizontalLayout_4.addWidget(self.btn_underline)
        self.btn_left = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/editor/misc/icons/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_left.setIcon(icon7)
        self.btn_left.setCheckable(True)
        self.btn_left.setObjectName("btn_left")
        self.horizontalLayout_4.addWidget(self.btn_left)
        self.btn_center = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/editor/misc/icons/center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_center.setIcon(icon8)
        self.btn_center.setCheckable(True)
        self.btn_center.setObjectName("btn_center")
        self.horizontalLayout_4.addWidget(self.btn_center)
        self.btn_right = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/editor/misc/icons/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_right.setIcon(icon9)
        self.btn_right.setCheckable(True)
        self.btn_right.setObjectName("btn_right")
        self.horizontalLayout_4.addWidget(self.btn_right)
        self.btn_erase = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/editor/misc/icons/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_erase.setIcon(icon10)
        self.btn_erase.setObjectName("btn_erase")
        self.horizontalLayout_4.addWidget(self.btn_erase)
        self.btn_source = QtWidgets.QToolButton(self.group_editor_toolbar)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/editor/misc/icons/source.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_source.setIcon(icon11)
        self.btn_source.setCheckable(True)
        self.btn_source.setObjectName("btn_source")
        self.horizontalLayout_4.addWidget(self.btn_source)
        self.verticalLayout_2.addWidget(self.group_editor_toolbar, 0, QtCore.Qt.AlignLeft)
        self.txt_email_body = QtWidgets.QTextEdit(self.groupBox)
        self.txt_email_body.setObjectName("txt_email_body")
        self.verticalLayout_2.addWidget(self.txt_email_body)
        self.group_smtp = QtWidgets.QGroupBox(self.groupBox)
        self.group_smtp.setMinimumSize(QtCore.QSize(0, 0))
        self.group_smtp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.group_smtp.setTitle("")
        self.group_smtp.setObjectName("group_smtp")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.group_smtp)
        self.horizontalLayout_2.setContentsMargins(-1, 8, -1, 8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.group_smtp)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.txt_host = QtWidgets.QLineEdit(self.group_smtp)
        self.txt_host.setObjectName("txt_host")
        self.horizontalLayout_2.addWidget(self.txt_host)
        self.chk_ssl = QtWidgets.QCheckBox(self.group_smtp)
        self.chk_ssl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chk_ssl.setObjectName("chk_ssl")
        self.horizontalLayout_2.addWidget(self.chk_ssl)
        self.label_2 = QtWidgets.QLabel(self.group_smtp)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txt_port = QtWidgets.QLineEdit(self.group_smtp)
        self.txt_port.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_port.setObjectName("txt_port")
        self.horizontalLayout_2.addWidget(self.txt_port)
        self.label_3 = QtWidgets.QLabel(self.group_smtp)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.txt_user = QtWidgets.QLineEdit(self.group_smtp)
        self.txt_user.setObjectName("txt_user")
        self.horizontalLayout_2.addWidget(self.txt_user)
        self.label_4 = QtWidgets.QLabel(self.group_smtp)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.txt_password = QtWidgets.QLineEdit(self.group_smtp)
        self.txt_password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txt_password.setInputMask("")
        self.txt_password.setText("")
        self.txt_password.setObjectName("txt_password")
        self.horizontalLayout_2.addWidget(self.txt_password)
        self.btn_test = QtWidgets.QPushButton(self.group_smtp)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_test.setFont(font)
        self.btn_test.setObjectName("btn_test")
        self.horizontalLayout_2.addWidget(self.btn_test)
        self.verticalLayout_2.addWidget(self.group_smtp)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    border:none;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_save = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_5.addWidget(self.btn_save)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 4)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_start = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_3.addWidget(self.btn_start)
        self.btn_resume = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_resume.setFont(font)
        self.btn_resume.setObjectName("btn_resume")
        self.horizontalLayout_3.addWidget(self.btn_resume)
        self.btn_stop = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_3.addWidget(self.btn_stop)
        self.lbl_timer = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.lbl_timer.setFont(font)
        self.lbl_timer.setObjectName("lbl_timer")
        self.horizontalLayout_3.addWidget(self.lbl_timer)
        self.pb_send = QtWidgets.QProgressBar(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pb_send.setFont(font)
        self.pb_send.setProperty("value", 24)
        self.pb_send.setObjectName("pb_send")
        self.horizontalLayout_3.addWidget(self.pb_send)
        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.bottom_splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.bottom_splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bottom_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.bottom_splitter.setObjectName("bottom_splitter")
        self.txt_email_list = QtWidgets.QPlainTextEdit(self.bottom_splitter)
        self.txt_email_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txt_email_list.setBaseSize(QtCore.QSize(0, 0))
        self.txt_email_list.setObjectName("txt_email_list")
        self.txt_log = QtWidgets.QPlainTextEdit(self.bottom_splitter)
        self.txt_log.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txt_log.setObjectName("txt_log")
        self.gridLayout.addWidget(self.bottom_splitter, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 20))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"    border:none;\n"
"}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_total = QtWidgets.QLabel(self.groupBox_5)
        self.lbl_total.setObjectName("lbl_total")
        self.horizontalLayout.addWidget(self.lbl_total)
        self.lbl_result = QtWidgets.QLabel(self.groupBox_5)
        self.lbl_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_result.setObjectName("lbl_result")
        self.horizontalLayout.addWidget(self.lbl_result)
        self.gridLayout.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_splitter)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mailer"))
        self.groupBox.setTitle(_translate("MainWindow", "邮件设置"))
        self.label_8.setText(_translate("MainWindow", "邮件主题"))
        self.txt_subject.setPlaceholderText(_translate("MainWindow", "邮件主题"))
        self.label_6.setText(_translate("MainWindow", "发件人昵称"))
        self.txt_fromName.setPlaceholderText(_translate("MainWindow", "姓名"))
        self.label_7.setText(_translate("MainWindow", "发件人邮箱"))
        self.txt_fromEmail.setPlaceholderText(_translate("MainWindow", "xx@xx.com"))
        self.label_9.setText(_translate("MainWindow", "回复邮箱"))
        self.txt_reply.setPlaceholderText(_translate("MainWindow", "yy@yy.com"))
        self.btn_undo.setText(_translate("MainWindow", "..."))
        self.btn_redo.setText(_translate("MainWindow", "..."))
        self.combo_font.setItemText(0, _translate("MainWindow", "Arial"))
        self.combo_font.setItemText(1, _translate("MainWindow", "Times New Roman"))
        self.combo_font.setItemText(2, _translate("MainWindow", "Verdana"))
        self.combo_font.setItemText(3, _translate("MainWindow", "宋体"))
        self.combo_font.setItemText(4, _translate("MainWindow", "黑体"))
        self.combo_font.setItemText(5, _translate("MainWindow", "微软雅黑"))
        self.combo_font.setItemText(6, _translate("MainWindow", "幼圆"))
        self.combo_size.setItemText(0, _translate("MainWindow", "6"))
        self.combo_size.setItemText(1, _translate("MainWindow", "7"))
        self.combo_size.setItemText(2, _translate("MainWindow", "8"))
        self.combo_size.setItemText(3, _translate("MainWindow", "9"))
        self.combo_size.setItemText(4, _translate("MainWindow", "10"))
        self.combo_size.setItemText(5, _translate("MainWindow", "11"))
        self.combo_size.setItemText(6, _translate("MainWindow", "12"))
        self.combo_size.setItemText(7, _translate("MainWindow", "13"))
        self.combo_size.setItemText(8, _translate("MainWindow", "14"))
        self.combo_size.setItemText(9, _translate("MainWindow", "15"))
        self.combo_size.setItemText(10, _translate("MainWindow", "16"))
        self.combo_size.setItemText(11, _translate("MainWindow", "17"))
        self.combo_size.setItemText(12, _translate("MainWindow", "18"))
        self.combo_size.setItemText(13, _translate("MainWindow", "19"))
        self.combo_size.setItemText(14, _translate("MainWindow", "20"))
        self.combo_size.setItemText(15, _translate("MainWindow", "22"))
        self.combo_size.setItemText(16, _translate("MainWindow", "24"))
        self.combo_size.setItemText(17, _translate("MainWindow", "26"))
        self.combo_size.setItemText(18, _translate("MainWindow", "28"))
        self.combo_size.setItemText(19, _translate("MainWindow", "30"))
        self.combo_size.setItemText(20, _translate("MainWindow", "36"))
        self.combo_size.setItemText(21, _translate("MainWindow", "40"))
        self.combo_size.setItemText(22, _translate("MainWindow", "46"))
        self.combo_size.setItemText(23, _translate("MainWindow", "50"))
        self.combo_size.setItemText(24, _translate("MainWindow", "54"))
        self.combo_size.setItemText(25, _translate("MainWindow", "60"))
        self.combo_size.setItemText(26, _translate("MainWindow", "66"))
        self.combo_size.setItemText(27, _translate("MainWindow", "72"))
        self.btn_bgcolor.setText(_translate("MainWindow", "..."))
        self.btn_color.setText(_translate("MainWindow", "..."))
        self.btn_bold.setText(_translate("MainWindow", "..."))
        self.btn_italic.setText(_translate("MainWindow", "..."))
        self.btn_underline.setText(_translate("MainWindow", "..."))
        self.btn_left.setText(_translate("MainWindow", "..."))
        self.btn_center.setText(_translate("MainWindow", "..."))
        self.btn_right.setText(_translate("MainWindow", "..."))
        self.btn_erase.setText(_translate("MainWindow", "..."))
        self.btn_source.setText(_translate("MainWindow", "..."))
        self.txt_email_body.setPlaceholderText(_translate("MainWindow", "这里输入邮件内容，支持HTML"))
        self.label.setText(_translate("MainWindow", "SMTP服务器"))
        self.txt_host.setPlaceholderText(_translate("MainWindow", "IP或域名"))
        self.chk_ssl.setText(_translate("MainWindow", "SSL"))
        self.label_2.setText(_translate("MainWindow", "端口"))
        self.txt_port.setText(_translate("MainWindow", "25"))
        self.txt_port.setPlaceholderText(_translate("MainWindow", "端口"))
        self.label_3.setText(_translate("MainWindow", "用户名"))
        self.txt_user.setPlaceholderText(_translate("MainWindow", "用户名"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "登录密码"))
        self.btn_test.setText(_translate("MainWindow", "测试连接"))
        self.btn_save.setText(_translate("MainWindow", "保存设置"))
        self.groupBox_2.setTitle(_translate("MainWindow", "发送进程"))
        self.btn_start.setText(_translate("MainWindow", "重新运行"))
        self.btn_resume.setText(_translate("MainWindow", "恢复运行"))
        self.btn_stop.setText(_translate("MainWindow", "停止"))
        self.lbl_timer.setText(_translate("MainWindow", "00:00:00"))
        self.txt_email_list.setPlaceholderText(_translate("MainWindow", "Email地址列表"))
        self.txt_log.setPlaceholderText(_translate("MainWindow", "日志监视窗口"))
        self.lbl_total.setText(_translate("MainWindow", "总共 0 条记录"))
        self.lbl_result.setText(_translate("MainWindow", "成功 0 条，失败 0 条"))


import main_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
