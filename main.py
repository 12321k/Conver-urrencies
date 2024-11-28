from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

app=QApplication([])
window=QWidget()
btn=QPushButton("конвертувати")
lineedit1=QLineEdit()
lineedit2=QLineEdit()
lineedit3=QLabel()

lineedit1.setPlaceholderText("Сума в першій валюті")
lineedit2.setPlaceholderText("курс")

v_line = QVBoxLayout()

v_line.addWidget(lineedit1)
v_line.addWidget(lineedit2)
v_line.addWidget(lineedit3)
v_line.addWidget(btn)
window.setLayout(v_line)

window.show()
app.exec_()