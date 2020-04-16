
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc import Ui_Form

#Create app
app = QtWidgets.QApplication(sys.argv)

#Create form and init UI
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# Globals
operator = ''
exp1 = ''
isFirst = True; # first digit

#Hook logic
def btn_0():
	global isFirst;
	if not isFirst:
		# if first digit is 0: do nothing
		if ui.lineEdit.text() != '0':
			ui.lineEdit.setText(ui.lineEdit.text() + str(0));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(0));
		isFirst = False;

def btn_1():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(1));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(1));
		isFirst = False;

def btn_2():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(2));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(2));
		isFirst = False;

def btn_3():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(3));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(3));
		isFirst = False;

def btn_4():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(4));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(4));
		isFirst = False;

def btn_5():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(5));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(5));
		isFirst = False;

def btn_6():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(6));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(6));
		isFirst = False;

def btn_7():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(7));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(7));
		isFirst = False;

def btn_8():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(8));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(8));
		isFirst = False;

def btn_9():
	global isFirst;
	if not isFirst:
		# if first digit is 0 remove it
		if ui.lineEdit.text() == '0':
			ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(9));
	else:
		ui.lineEdit.setText("")
		ui.lineEdit.setText(ui.lineEdit.text() + str(9));
		isFirst = False;

def erase():
	global operator;
	global exp1;
	global isFirst;
	isFirst = True;
	operator = ''
	exp1 = ''
	ui.lineEdit.setText("")

def equal():
	global operator;
	global exp1;
	global isFirst;
	isFirst = True;
	if operator is not '' and exp1 is not'':
		if operator=='+':
			ui.lineEdit.setText(str(int(exp1) + int(ui.lineEdit.text()))); # do math
			operator==''; # clear operator
		elif operator=='-':
			ui.lineEdit.setText(str(int(exp1) - int(ui.lineEdit.text()))); # do math
			operator==''; # clear operator
		elif operator=='*':
			ui.lineEdit.setText(str(int(exp1) * int(ui.lineEdit.text()))); # do math
			operator==''; # clear operator
		elif operator=='/':
			ui.lineEdit.setText(str(float(exp1) / float(ui.lineEdit.text()))); # do math
			operator==''; # clear operator

def mult():
	global operator;
	global exp1;
	operator='*';
	exp1=ui.lineEdit.text();
	global isFirst;
	isFirst = True;
def div():
	global operator;
	global exp1;
	global isFirst;
	isFirst = True;
	operator='/';
	exp1=ui.lineEdit.text();
def sub():
	global operator;
	global exp1;
	global isFirst;
	isFirst = True;
	operator='-';
	exp1=ui.lineEdit.text();
def add():
	global operator;
	global exp1;
	global isFirst;
	isFirst = True;
	operator='+';
	exp1=ui.lineEdit.text();
def back():
	ui.lineEdit.setText(ui.lineEdit.text()[:-1]);

# Connectors to functions	
ui.btn_0.clicked.connect(btn_0)
ui.btn_1.clicked.connect(btn_1)
ui.btn_2.clicked.connect(btn_2)
ui.btn_3.clicked.connect(btn_3)
ui.btn_4.clicked.connect(btn_4)
ui.btn_5.clicked.connect(btn_5)
ui.btn_6.clicked.connect(btn_6)
ui.btn_7.clicked.connect(btn_7)
ui.btn_8.clicked.connect(btn_8)
ui.btn_9.clicked.connect(btn_9)
ui.btn_erase.clicked.connect(erase)
ui.btn_equal.clicked.connect(equal)	
ui.btn_mult.clicked.connect(mult)
ui.btn_div.clicked.connect(div)	
ui.btn_sub.clicked.connect(sub)	
ui.btn_add.clicked.connect(add)	
ui.btn_back.clicked.connect(back)	

# Run main loop
sys.exit(app.exec_())
