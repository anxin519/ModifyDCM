'''
Create Date: 2020年5月19日
Version: 1.0
Description: 修改dcm
Author: Ace
e-mail: anxin001@outlook.com
'''


from PyQt5 import QtCore, QtWidgets
import pydicom
import sys
import os


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        self.update_dcm_path = (os.path.expanduser(
            '~')+'/update_dcm_path.ini').replace("\\", "/")
        self.dirs = ''
        self.open_config()

        Dialog.setObjectName("Dialog")
        Dialog.resize(366, 203)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label.setObjectName("label")
        self.ProtocolName = QtWidgets.QLineEdit(Dialog)
        self.ProtocolName.setGeometry(QtCore.QRect(40, 20, 113, 20))
        self.ProtocolName.setObjectName("ProtocolName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.label_2.setObjectName("label_2")
        self.PatientSex = QtWidgets.QLineEdit(Dialog)
        self.PatientSex.setGeometry(QtCore.QRect(40, 50, 113, 20))
        self.PatientSex.setObjectName("PatientSex")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 31, 16))
        self.label_3.setObjectName("label_3")
        self.PatientAge = QtWidgets.QLineEdit(Dialog)
        self.PatientAge.setGeometry(QtCore.QRect(40, 80, 113, 20))
        self.PatientAge.setObjectName("PatientAge")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_4.setObjectName("label_4")
        self.SOPInstanceUID = QtWidgets.QLineEdit(Dialog)
        self.SOPInstanceUID.setGeometry(QtCore.QRect(100, 110, 241, 21))
        self.SOPInstanceUID.setObjectName("SOPInstanceUID")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 170, 75, 23))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.StudyDate = QtWidgets.QLineEdit(Dialog)
        self.StudyDate.setGeometry(QtCore.QRect(220, 20, 113, 20))
        self.StudyDate.setObjectName("StudyDate")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 20, 31, 16))
        self.label_5.setObjectName("label_5")
        self.InstitutionName = QtWidgets.QLineEdit(Dialog)
        self.InstitutionName.setGeometry(QtCore.QRect(220, 50, 113, 20))
        self.InstitutionName.setObjectName("InstitutionName")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(190, 50, 31, 16))
        self.label_6.setObjectName("label_6")
        self.PatientID = QtWidgets.QLineEdit(Dialog)
        self.PatientID.setGeometry(QtCore.QRect(220, 80, 111, 20))
        self.PatientID.setObjectName("PatientID")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(170, 80, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 331, 21))
        self.label_8.setObjectName("label_8")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "dcm修改_v1.0    by:Ace"))
        self.label.setText(_translate("Dialog", "姓名:"))
        self.label_2.setText(_translate("Dialog", "性别:"))
        self.label_3.setText(_translate("Dialog", "年龄:"))
        self.label_4.setText(_translate("Dialog", "SOPInstanceUID:"))
        self.pushButton.setText(_translate("Dialog", "打 开"))
        self.pushButton_2.setText(_translate("Dialog", "保 存"))
        self.pushButton_3.setText(_translate("Dialog", "退 出"))
        self.label_5.setText(_translate("Dialog", "时间:"))
        self.label_6.setText(_translate("Dialog", "机构:"))
        self.label_7.setText(_translate("Dialog", "PatientID:"))
        self.label_8.setText(_translate("Dialog", "重复上传只需修改 SOPInstanceUID"))
        self.pushButton_3.clicked.connect(
            QtCore.QCoreApplication.instance().quit)
        self.pushButton.clicked.connect(self.click_choice_dir)
        self.pushButton_2.clicked.connect(self.save_dcm)

    def click_choice_dir(self, Dialog):
        global fname
        fname, ftype = QtWidgets.QFileDialog.getOpenFileName(None,
                                                             "选取文件",
                                                             r"./" if not self.dirs else self.dirs,
                                                             "DCM Files (*.dcm *.DCM);;All Files (*)")
        if("DCM" in ftype):  # self.dirs if self.dirs else
            fname = fname.replace("\\", "/")
            self.dirs = fname[0:fname.rfind('/')]
            self.open_config(self.dirs)
            global ds
            ds = pydicom.read_file(fname)
            self.ProtocolName.setText(str(ds.PatientName))
            self.PatientSex.setText(str(ds.PatientSex))
            self.PatientAge.setText(str(ds.PatientAge))
            self.PatientID.setText(str(ds.PatientID))
            self.InstitutionName.setText(str(ds.InstitutionName))
            self.StudyDate.setText(str(ds.StudyDate))
            self.SOPInstanceUID.setText(str(ds.SOPInstanceUID))

    def save_dcm(self, Dialog):
        if ds:
            ds.PatientName = self.ProtocolName.text()
            ds.PatientSex = self.PatientSex.text()
            ds.PatientAge = self.PatientAge.text()
            ds.PatientID = self.PatientID.text()
            ds.InstitutionName = self.InstitutionName.text()
            ds.StudyDate = self.StudyDate.text()
            ds.SOPInstanceUID = self.SOPInstanceUID.text()
            ds.save_as(fname[0:fname.rfind('.')]+"_update.dcm")
            QtWidgets.QMessageBox.about(None,
                                        "OK",
                                        "文件修改成功")

    def open_config(self, config=None):
        if(config):
            with open(self.update_dcm_path, mode='w', encoding='utf-8') as f:
                f.write(config)
        else:
            with open(self.update_dcm_path, mode='a+', encoding='utf-8') as f:
                f.seek(0)
                self.dirs = f.readline()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
