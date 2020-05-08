# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal, QThread, QTimer, QEvent, QTime
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox,QToolButton,QComboBox
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon, QLabel, QColorDialog, QTextEdit
from PyQt5.QtGui import QIcon, QCursor, QFont,QTextCharFormat
import os, sys, threading, time, traceback, platform

from Ui_main import Ui_MainWindow
from Ui_setting import Ui_DlgSetting
from lib.Icon import Icon
from lib.Util import Util
from lib.Mailer import Mailer

class MyMailer(Mailer, QThread):
    signal = pyqtSignal(object)
    def __init__(self, parent=None):
        Mailer.__init__(self,False)
        QThread.__init__(self)

    def log(self, str, extra=None):
        self.signal.emit({"str":str, "extra":extra})


class DlgSetting(QDialog, Ui_DlgSetting):
    parent = None

    def __init__(self, parent=None):
        super(DlgSetting, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.chk_min_tray.setChecked(parent.settings['chkMinToTray'])
    
    @pyqtSlot() 
    def on_btn_ok_clicked(self):
        self.parent.settings = {
            "chkMinToTray":self.chk_min_tray.isChecked(),
        }
        #print(self.parent.settings)
        self.close()

    @pyqtSlot() 
    def on_btn_cancel_clicked(self):
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    tmpPath = os.path.dirname(os.path.realpath(sys.argv[0])) + '/tmp'

    mailer = None
    runThread = None
    time = 0
    taskInfo = None

    tray = None
    dlgSetting = None
    settings = {
        "chkMinToTray":True,
    }

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.mailer = MyMailer()
        self.mailer.signal.connect(self.log)
        self.mailer.init()
        
        
    def changeEvent(self, e):
        if e.type() == QEvent.WindowStateChange:
            if self.isMinimized() and Util.isWindows():
                if self.settings["chkMinToTray"]:
                    self.hide()
            elif self.isMaximized():
                pass
            elif self.isFullScreen():
                pass
            elif self.isActiveWindow():
                pass
        elif e.type()==QEvent.ActivationChange:
            #self.repaint()
            pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', "您确认要退出吗?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) 
        if reply == QMessageBox.Yes: 
            self.exitAll()
        else: 
            event.ignore()

    def addSystemTray(self):
        self.tray = QSystemTrayIcon() 

        self.icon = Icon.getLogoIcon()
        self.tray.setIcon(self.icon) 

        self.tray.activated.connect(self.clickTray) 
        self.tray.messageClicked.connect(self.clickTray)
        self.tray_menu = QMenu(QApplication.desktop()) 
        self.RestoreAction = QAction('主界面', self, triggered=self.restoreAction)
        self.SettingsAction = QAction('设置', self, triggered=self.settingsAction) 
        self.QuitAction = QAction('退出', self, triggered=self.exitAction) 
        self.tray_menu.addAction(self.RestoreAction) 
        self.tray_menu.addAction(self.SettingsAction)
        self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu) 
        self.tray.show()
    
    def settingsAction(self):
        self.dlgSetting = DlgSetting(self)
        self.dlgSetting.show()
    
    def exitAction(self):
        self.close()

    def clickTray(self, reason):
        if reason != QSystemTrayIcon.DoubleClick:
            return

        self.restoreAction()

    def restoreAction(self):
        if self.isMaximized():
            self.showMaximized()
        elif self.isFullScreen():
            self.showFullScreen()
        else:
            self.showNormal()
            
        self.activateWindow()

        #scrollbar
        self.txt_log.verticalScrollBar().setValue(self.txt_log.verticalScrollBar().maximum())

    def addContextMenu(self):
        #export log
        self.logContextMenu = QMenu(self)
        self.txt_log.setContextMenuPolicy(Qt.CustomContextMenu)
        self.txt_log.customContextMenuRequested.connect(lambda: self.logContextMenu.exec_(QCursor.pos()))
        self.clearLogAction = self.logContextMenu.addAction('清空')
        self.clearLogAction.triggered.connect(lambda: self.txt_log.clear())

        self.emailContextMenu = QMenu(self)
        self.txt_email_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.txt_email_list.customContextMenuRequested.connect(lambda: self.emailContextMenu.exec_(QCursor.pos()))
        self.clearEmailAction = self.emailContextMenu.addAction('清空')
        self.clearEmailAction.triggered.connect(lambda: self.txt_email_list.clear())
        self.reloadAction = self.emailContextMenu.addAction('重新加载')
        self.reloadAction.triggered.connect(lambda: self.loadEmail())
        self.loadErrorAction = self.emailContextMenu.addAction('加载错误数据')
        self.loadErrorAction.triggered.connect(lambda: self.loadErrorEmail())
        

    
    def setTimer(self):
        if self.time>0:
            self.lbl_timer.setText(self.convertTime(time.time() - self.time))

    def convertTime(self, raw_time):
        hour = int(raw_time // 3600)
        minute = int((raw_time % 3600) // 60)
        second = int(raw_time % 60)

        return '{:0>2d}:{:0>2d}:{:0>2d}'.format(hour, minute, second)

    def exitAll(self):
        if self.tray:
            self.tray.hide()
        
        sys.exit()

    #############################################################
    @pyqtSlot()
    def on_btn_bold_clicked(self):
        tmpFormat = self.txt_email_body.currentCharFormat()
        if tmpFormat.fontWeight() == QFont.Bold:
            self.txt_email_body.setFontWeight(QFont.Normal)
        else:
            self.txt_email_body.setFontWeight(QFont.Bold)

        #self.txt_email_body.mergeCurrentCharFormat(tmpFormat)
    
    @pyqtSlot()
    def on_btn_italic_clicked(self):
        self.txt_email_body.setFontItalic(not self.txt_email_body.fontItalic())
    
    @pyqtSlot()
    def on_btn_underline_clicked(self):
        self.txt_email_body.setFontUnderline(not self.txt_email_body.fontUnderline())

    @pyqtSlot()
    def on_btn_undo_clicked(self):
        self.txt_email_body.undo()
    
    @pyqtSlot()
    def on_btn_redo_clicked(self):
        self.txt_email_body.redo()

    @pyqtSlot()
    def on_btn_left_clicked(self):
        self.txt_email_body.setAlignment(Qt.AlignLeft)

    @pyqtSlot()
    def on_btn_center_clicked(self):
        self.txt_email_body.setAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def on_btn_right_clicked(self):
        self.txt_email_body.setAlignment(Qt.AlignRight)

    @pyqtSlot()
    def on_btn_size_clicked(self):
        pass

    @pyqtSlot()
    def on_btn_color_clicked(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.txt_email_body.setTextColor(col)

    @pyqtSlot()
    def on_btn_bgcolor_clicked(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.txt_email_body.setTextBackgroundColor(col)

    @pyqtSlot(int)
    def on_combo_size_currentIndexChanged(self, x):
        self.txt_email_body.setFontPointSize(int(self.combo_size.currentText()))

    @pyqtSlot(int)
    def on_combo_font_currentIndexChanged(self, x):
        self.txt_email_body.setFontFamily (self.combo_font.currentText())

    @pyqtSlot()
    def on_btn_erase_clicked(self):
        self.txt_email_body.setCurrentCharFormat(self.getDefaultTextFormat())
    

    #############################################################
    def getDefaultTextFormat(self):
        defaultFormat = QTextCharFormat()
        defaultFormat.setFontPointSize(10)

        return defaultFormat

    @pyqtSlot()
    def on_btn_source_clicked(self):
        html = self.txt_email_body.toHtml()
        text = self.txt_email_body.toPlainText()

        defaultFormat = self.getDefaultTextFormat()

        if self.btn_source.isChecked():
            self.txt_email_body.setAcceptRichText(False)

            self.txt_email_body.clear()
            self.txt_email_body.setCurrentCharFormat(defaultFormat)

            self.txt_email_body.setPlainText(html)
            
            self.editable = False
            self.txt_email_body.setStyleSheet('QTextEdit{background:#434343;color:#fff;}')
        else:
            self.txt_email_body.setAcceptRichText(True)

            self.txt_email_body.clear()
            self.txt_email_body.setCurrentCharFormat(defaultFormat)

            self.txt_email_body.setHtml(text)

            self.editable = True
            self.txt_email_body.setStyleSheet('QTextEdit{background:#fff;color:#000;}')

        #enabled
        list = self.group_editor_toolbar.findChildren(QToolButton)
        for i in range(0, len(list)):
            if list[i].objectName() not in ['btn_source', 'btn_undo', 'btn_redo']:
                list[i].setEnabled(self.editable)
        list = self.group_editor_toolbar.findChildren(QComboBox)
        for i in range(0, len(list)):
            list[i].setEnabled(self.editable)

    def on_txt_email_body_selectionChanged(self):
        tmpFormat = self.txt_email_body.currentCharFormat()
        if tmpFormat.fontWeight() == QFont.Bold:
            self.btn_bold.setChecked(True)
        else:
            self.btn_bold.setChecked(False)

        if tmpFormat.fontItalic():
            self.btn_italic.setChecked(True)
        else:
            self.btn_italic.setChecked(False)

        if tmpFormat.fontUnderline():
            self.btn_underline.setChecked(True)
        else:
            self.btn_underline.setChecked(False)

        #align
        if self.txt_email_body.alignment() == Qt.AlignLeft:
            self.btn_left.setChecked(True)
        else:
            self.btn_left.setChecked(False)

        if self.txt_email_body.alignment() == Qt.AlignCenter:
            self.btn_center.setChecked(True)
        else:
            self.btn_center.setChecked(False)
        if self.txt_email_body.alignment() == Qt.AlignRight:
            self.btn_right.setChecked(True)
        else:
            self.btn_right.setChecked(False)

        #family


    def on_txt_email_body_undoAvailable(self, bool):
        if bool:
            self.btn_undo.setEnabled(True)
        else:
            self.btn_undo.setEnabled(False)

    def on_txt_email_body_redoAvailable(self, bool):
        if bool:
            self.btn_redo.setEnabled(True)
        else:
            self.btn_redo.setEnabled(False)

    #######################################################################################
    @pyqtSlot()
    def on_btn_test_clicked(self):
        self.on_btn_save_clicked()

        #check upgrade
        t1 = threading.Thread(target=self.mailer.test,args=())
        t1.setDaemon(True)
        t1.start()

        self.btn_test.setDisabled(True)

    @pyqtSlot()
    def on_btn_save_clicked(self):
        if not self.txt_host.text() or not self.txt_user.text():
            self.log({'str':'SMTP服务器信息不能为空！', 'extra':['error']})
            return

        if not self.mailer.saveSetting({
            'EmailBody':self.txt_email_body.toPlainText() if self.btn_source.isChecked() else self.txt_email_body.toHtml(),
            'Mailer':{
                'host':self.txt_host.text(),
                'port':self.txt_port.text(),
                'user':self.txt_user.text(),
                'password':self.txt_password.text(),
                'ssl':self.chk_ssl.isChecked(),
                'fromName':self.txt_fromName.text(),
                'fromEmail':self.txt_fromEmail.text(),
                'subject':self.txt_subject.text(),
                'replyTo':self.txt_reply.text(),
            }}):
            return False
    
    @pyqtSlot()
    def on_btn_start_clicked(self):
        if self.taskInfo['start'] > 0 and self.taskInfo['start']<self.taskInfo['total']:
            reply = QMessageBox.question(self, '提示', "任务尚未结束，您确定要重新开始吗？建议您恢复运行！", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) 
            if reply != QMessageBox.Yes: 
                return



        if self.runThread and self.runThread.isAlive():
            self.log({'str':'程序已经在运行中，请等待结束！', 'extra':['error']})
        else:
            self.runThread = threading.Thread(target=self.mailer.startTask,args=(self.txt_email_list.toPlainText(),))
            self.runThread.setDaemon(True)
            self.runThread.start()

            self.btn_start.setDisabled(True)
            self.btn_resume.setDisabled(True)
            self.btn_stop.setDisabled(False)


    @pyqtSlot()
    def on_btn_resume_clicked(self):
        if self.runThread and self.runThread.isAlive():
            self.log({'str':'程序已经在运行中，请等待结束！', 'extra':['error']})
        else:
            self.runThread = threading.Thread(target=self.mailer.resumeTask,args=())
            self.runThread.setDaemon(True)
            self.runThread.start()

            self.btn_start.setDisabled(True)
            self.btn_resume.setDisabled(True)
            self.btn_stop.setDisabled(False)

    @pyqtSlot()
    def on_btn_stop_clicked(self):
        #check upgrade
        t1 = threading.Thread(target=self.mailer.stopTask,args=())
        t1.setDaemon(True)
        t1.start()

        self.btn_stop.setDisabled(True)

    @pyqtSlot()
    def on_chk_ssl_clicked(self):
        if self.chk_ssl.isChecked():
            self.txt_port.setText('465')
        else:
            self.txt_port.setText('25')

    @pyqtSlot()
    def on_txt_email_list_textChanged(self):
        c = self.txt_email_list.toPlainText()
        self.lbl_total.setText('总共 %s 条Email' % (format(c.count('\n')+1,'0,') if c else '0'))
        
    
    def log(self, o):
        if o['str']:
            msg = '['+time.strftime("%H:%M:%S", time.localtime()) + ']' + o['str']
            self.txt_log.appendPlainText(msg) 
        
        #auto clear
        if self.txt_log.toPlainText().count('\n') > 10000 :
            self.txt_log.clear()
        

        if o['extra']:
            if o['extra'][0] == 'test-end':
                self.btn_test.setDisabled(False)
            
            if o['extra'][0] in ['task-end', 'task-stop']:
                self.btn_start.setDisabled(False)
                self.btn_resume.setDisabled(False)
                self.btn_stop.setDisabled(True)


            if o['extra'][0] == 'loaded':
                self.txt_email_list.setPlainText(o['extra'][1])

            if o['extra'][0] == 'update':
                self.lbl_result.setText('成功 %s 条，失败 %s 条' % (format(o['extra'][1],'0,'), format(o['extra'][2],'0,')))

            
            if o['extra'][0] == 'exit':
                QMessageBox.critical(self, 'Message', o['str'], QMessageBox.Ok, QMessageBox.Ok) 
                sys.exit()
            elif o['extra'][0] == 'check-end' and o['extra'][1]['allowUpgrade']:
                reply = QMessageBox.question(self, '提示', "发现新版本，您确认要更新吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) 
                if reply == QMessageBox.Yes: 
                    mainScript = os.path.basename(sys.argv[0])[0:os.path.basename(sys.argv[0]).rfind('.')]
                    Util.runScriptFile(self.mailer.updaterFilePath, ' -s' + mainScript)
                    self.exitAll()

            #progress
            if o['extra'][0] in ['progress']:
                #o['extra'][1]>self.pb_export.value() and self.pb_export.setValue(o['extra'][1])
                self.pb_send.setValue(o['extra'][1])


    def loadData(self):
        self.taskInfo = self.mailer.getTaskInfo()
        self.pb_send.setValue(self.taskInfo['progress'])
        self.lbl_result.setText('成功 %s 条，失败 %s 条' % (format(self.taskInfo['success'],'0,'), format(self.taskInfo['error'],'0,')))

        self.btn_stop.setDisabled(True)
        self.txt_log.setReadOnly(True)


        '''
        if self.taskInfo['start'] > 0 and self.taskInfo['start']<self.taskInfo['total']:
            self.btn_resume.setDisabled(False)
        else:
            self.btn_resume.setDisabled(True)
        '''

        self.config = self.mailer.config
        if self.config:
            if 'Mailer' in self.config.keys():
                self.txt_host.setText(self.config['Mailer']['host'])
                self.txt_port.setText(str(self.config['Mailer']['port']))
                self.txt_user.setText(self.config['Mailer']['user'])
                self.txt_password.setText(self.config['Mailer']['password'])
                self.chk_ssl.setChecked(self.config['Mailer']['ssl'])
                self.txt_fromName.setText(self.config['Mailer']['fromName'])
                self.txt_fromEmail.setText(self.config['Mailer']['fromEmail'])
                self.txt_subject.setText(self.config['Mailer']['subject'])
                self.txt_reply.setText(self.config['Mailer']['replyTo'] if 'replyTo' in self.config['Mailer'].keys() else '')
        else:
            QMessageBox.critical(self, '错误', '配置文件不存在，请检查！', QMessageBox.Ok, QMessageBox.Ok) 
            os._exit(0)
            return

        #splitter
        self.frame_splitter.setStretchFactor(1,2)
        self.bottom_splitter.setStretchFactor(1,2)

        #email
        defaultHtml = self.mailer.getEmailBody()
        self.txt_email_body.setHtml(defaultHtml)
        self.txt_email_body.selectionChanged.connect(self.on_txt_email_body_selectionChanged)
        self.txt_email_body.undoAvailable.connect(self.on_txt_email_body_undoAvailable)
        self.txt_email_body.redoAvailable.connect(self.on_txt_email_body_redoAvailable)
        #self.txt_email_body.setAutoFormatting(QTextEdit.AutoNone)

        #check upgrade
        t1 = threading.Thread(target=self.mailer.checkUpgrade,args=())
        t1.setDaemon(True)
        t1.start()

        #load
        self.loadEmail()

    def loadEmail(self):
        t1 = threading.Thread(target=self.mailer.loadData,args=())
        t1.setDaemon(True)
        t1.start()
    
    def loadErrorEmail(self):
        t1 = threading.Thread(target=self.mailer.loadErrorData,args=())
        t1.setDaemon(True)
        t1.start()
        

#handle error
def saveError(v):
    #save
    s = '['+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']\n' + v + '\n'
    p = os.path.dirname(os.path.realpath(sys.argv[0])) + '/error.log'
    with open(p, "a+", encoding="utf-8") as f:
        f.write(s)
def errorHandler(type, value, trace):  
    v = 'Main Error: \n%s' % (''.join(traceback.format_exception(type, value, trace)))
    print(v)
    saveError(v)
    sys.__excepthook__(type, value, trace) 
sys.excepthook = errorHandler

#main
if __name__ == '__main__':
    #scale
    if Util.isNewSystem():QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    if Util.isNewSystem():app.setAttribute(Qt.AA_EnableHighDpiScaling)
    app.setQuitOnLastWindowClosed(False)
    
    dlg = MainWindow()
    
    #single instance
    if  Util.isWindows() and Util.isNewSystem():
        import win32con,win32file,pywintypes
        
        LOCK_EX = win32con.LOCKFILE_EXCLUSIVE_LOCK
        LOCK_SH = 0
        LOCK_NB = win32con.LOCKFILE_FAIL_IMMEDIATELY
        __overlapped = pywintypes.OVERLAPPED()

        pid_dir = dlg.tmpPath
        self_name = os.path.basename(sys.argv[0])[0:os.path.basename(sys.argv[0]).rfind('.')]
        if os.path.exists(pid_dir):
            try:
                fd = open(pid_dir + '/'+self_name+'.pid', 'w')
                hfile = win32file._get_osfhandle(fd.fileno())
                win32file.LockFileEx(hfile, LOCK_EX | LOCK_NB, 0, 0xffff0000,__overlapped)
            except:
                QMessageBox.critical(dlg, '提示', "程序已经运行，请点击右下角系统图标显示窗口!", QMessageBox.Ok, QMessageBox.Ok) 
                sys.exit()
    elif not Util.isWindows():
        import fcntl
        pid_dir = dlg.tmpPath
        self_name = os.path.basename(sys.argv[0])[0:os.path.basename(sys.argv[0]).rfind('.')]
        if os.path.exists(pid_dir):
            try:
                fd = open(pid_dir + '/'+self_name+'.pid', 'w')
                fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except:
                #traceback.print_exc()
                QMessageBox.critical(dlg, '提示', "程序已经运行，请点击右下角系统图标显示窗口!", QMessageBox.Ok, QMessageBox.Ok) 
                sys.exit()
    
    
    #resize
    desktop = QApplication.desktop()
    screenRect = desktop.availableGeometry()
    dlgRect = dlg.geometry()
    if screenRect.width() < dlgRect.width() or screenRect.height()<dlgRect.height():
        dlg.resize(screenRect.width(), screenRect.height())
        dlg.showMaximized()
        dlg.show()
    else:
        #dlg.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        dlg.show()
    del desktop
    del screenRect
    del dlgRect

    #show window
    try:
        dlg.setWindowIcon(Icon.getLogoIcon())
        dlg.setWindowTitle('Mailer (%s)' % os.path.realpath(sys.argv[0]))
        dlg.loadData()

        if Util.isWindows():
            dlg.addSystemTray()
        dlg.addContextMenu()
    except:
        traceback.print_exc()
        saveError('Startup Error:\n' + traceback.format_exc())
    finally:
        sys.exit(app.exec_())
