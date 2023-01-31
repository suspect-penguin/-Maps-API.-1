import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from untitled import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Отображение карты')
        self.z = 12
        self.map_file = str()
        self.pixmap = None
        self.image = None
        self.image = QLabel(self)
        self.image.move(50, 50)
        self.image.resize(600, 450)
        self.get_image()

    def get_image(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&z={self.z}&spn=0.002,0.002&l=map"
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
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
                self.get_image()
                self.pixmap = QPixmap(self.map_file)
                self.image.setPixmap(self.pixmap)
        elif event.key() == Qt.Key_PageDown:
            if self.z - 1 >= 1:
                self.z -= 1
                self.get_image()
                self.pixmap = QPixmap(self.map_file)
                self.image.setPixmap(self.pixmap)
        self.update()

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())