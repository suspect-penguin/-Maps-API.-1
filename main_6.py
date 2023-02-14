import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from untitled_5 import Ui_Form


class MapWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Отображение карты')
        self.is_pt = False
        self.map_request = str()
        self.z = 12
        self.lon = 37.530887
        self.lat = 55.703118
        self.lon2, self.lat2 = float(), float()
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
        self.pushButton.clicked.connect(self.FindObject)

    def get_image(self):
        if self.is_pt:
            self.map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.lon},{self.lat}&z={self.z}&l={self.v}" \
                               f"&pt={self.lon2},{self.lat2}"
        else:
            self.map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.lon},{self.lat}&z={self.z}&l={self.v}"
        response = requests.get(self.map_request)
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
        elif event.key() == Qt.Key_W:
            self.lat += 0.0015 * (18 - self.z)
        elif event.key() == Qt.Key_S:
            self.lat -= 0.0015 * (18 - self.z)
        elif event.key() == Qt.Key_D:
            self.lon += 0.002 * (18 - self.z)
        elif event.key() == Qt.Key_A:
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

    def FindObject(self):
        geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
                           f"&geocode={self.textEdit.toPlainText()}&format=json"

        # Выполняем запрос.
        response = requests.get(geocoder_request)
        if response:
            # Преобразуем ответ в json-объект
            json_response = response.json()

            # Получаем первый топоним из ответа геокодера.
            # Согласно описанию ответа, он находится по следующему пути:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            # Полный адрес топонима:
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            # Координаты центра топонима:
            toponym_coodrinates = toponym["Point"]["pos"]
            # Печатаем извлечённые из ответа поля:
            self.is_pt = True
            self.lat2 = float(toponym_coodrinates.split()[1])
            self.lat = self.lat2
            self.lon2 = float(toponym_coodrinates.split()[0])
            self.lon = self.lon2
            self.z = 12
            self.map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.lon},{self.lat}&z={self.z}&l={self.v}" \
                          f"&pt={self.lon2},{self.lat2}"
        self.get_image()
        self.update()

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MapWindow()
    sys.excepthook = except_hook
    mw.show()
    sys.exit(app.exec())