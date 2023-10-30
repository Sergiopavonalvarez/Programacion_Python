import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QLineEdit, QVBoxLayout


class Conversor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de euros a pesetas")
        self.resize(400, 200)
        self.euros_label = QLabel("Euros:", self)
        self.pesetas_label = QLabel("Pesetas:", self)
        self.euros_slider = QSlider(Qt.Horizontal, self)
        self.euros_slider.setMinimum(0)
        self.euros_slider.setMaximum(100)
        self.pesetas_line_edit = QLineEdit(self)
        self.pesetas_line_edit.setReadOnly(True)
        self.euros_slider.valueChanged.connect(self.actualizar_pesetas)
        layout = QVBoxLayout()
        layout.addWidget(self.euros_label)
        layout.addWidget(self.euros_slider)
        layout.addWidget(self.pesetas_label)
        layout.addWidget(self.pesetas_line_edit)
        self.setLayout(layout)
    def actualizar_pesetas(self):
        euros = self.euros_slider.value()
        pesetas = euros * 166
        self.pesetas_line_edit.setText(str(pesetas))
        self.euros_label.setText(str(self.euros_slider.value()))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    conv = Conversor()
    conv.show()
    app.exec()