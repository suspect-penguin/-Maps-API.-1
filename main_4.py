import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from untitled_4 import Ui_Form


class MapWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Отображение карты')
        self.z = 12
        self.lon = 37.530887
        self.lat = 55.703118
        self.v = 'map'
        self.current_text = 'Схема'
        self.map_file = str()
        self.pixmap = None
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.get_image()
        self.radioButton.clicked.connect(self.TextChargedEvent1)
        self.radioButton_2.clicked.connect(self.TextChargedEvent2)
        self.radioButton_3.clicked.connect(self.TextChargedEvent3)

    def get_image(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.lon},{self.lat}&z={self.z}&l={self.v}"
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(response)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        self.map_file = 'map.png'
        # Запишем полученное изображение в файл.
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.z + 1 <= 17:
                self.z += 1
        elif event.key() == Qt.Key_PageDown:
            if self.z - 1 >= 1:
                self.z -= 1
        elif event.key() == Qt.Key_Up:
            self.lat += 0.0015 * (18 - self.z)
        elif event.key() == Qt.Key_Down:
            self.lat -= 0.0015 * (18 - self.z)
        elif event.key() == Qt.Key_Right:
            self.lon += 0.002 * (18 - self.z)
        elif event.key() == Qt.Key_Left:
            self.lon -= 0.002 * (18 - self.z)
        self.get_image()
        self.update()

    def TextChargedEvent1(self):
        if self.current_text != self.radioButton.text():
            self.current_text = self.radioButton.text()
            self.v = "map"
        self.get_image()
        self.update()

    def TextChargedEvent2(self):
        if self.current_text != self.radioButton_2.text():
            self.current_text = self.radioButton_2.text()
            self.v = "sat"
        self.get_image()
        self.update()

    def TextChargedEvent3(self):
        if self.current_text != self.radioButton_3.text():
            self.current_text = self.radioButton_3.text()
            self.v = "sat,skl"
        self.get_image()
        self.update()

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MapWindow()
    mw.show()
    sys.exit(app.exec())
