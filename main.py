from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from logica import currency_converter


def convert():
    try:
        chose = int(choice.text())
        kurs = int(rate.text())
        am = int(amount.text())
    except:
        print('помилкеа отримання даних')
    try:
        result.setText(str(currency_converter(chose, am , kurs)))
    except:
        print('виклик функції помилка')


app=QApplication([])
window=QWidget()

btn=QPushButton("конвертувати")
amount=QLineEdit()
rate=QLineEdit()
choice=QLineEdit()
result=QLabel()

amount.setPlaceholderText("Сума для конвертації")
rate.setPlaceholderText("Курс валют")
choice.setPlaceholderText("Напрямок конвертації (1 для UAH -> USD, 2 для USD -> UAH)v")

v_line = QVBoxLayout()

v_line.addWidget(amount)
v_line.addWidget(rate)
v_line.addWidget(choice)
v_line.addWidget(result)
v_line.addWidget(btn)
window.setLayout(v_line)

btn.clicked.connect(convert)


window.show()
app.exec_()
