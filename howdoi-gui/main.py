import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication, QComboBox, QDateEdit, QDateTimeEdit, QSpinBox, QDoubleSpinBox, QLabel, QLineEdit,
    QProgressBar, QPushButton, QRadioButton, QSlider, QTimeEdit, QMainWindow, QVBoxLayout, QCheckBox, QWidget,
    QTabWidget, QFormLayout, QHBoxLayout
)
from PySide2.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets App")
        layout = QVBoxLayout()
        widgets = [
            QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
            QSpinBox, QDoubleSpinBox, QLabel, QLineEdit,
            QProgressBar, QPushButton, QRadioButton, QSlider, QTimeEdit,
        ]
        for w in widgets:
            layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Example")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(600, 400)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with 2 tabs
        tabs = QTabWidget()
        tabs.addTab(self.general_tab_ui(), "General")
        tabs.addTab(self.settings_tab_ui(), "Settings")
        layout.addWidget(tabs)

    def general_tab_ui(self):
        general_tab = QWidget()
        layout = QFormLayout()

        line = QLineEdit()
        line.setPlaceholderText("Ask me anything")

        layout.addRow("How do I: ", line)

        buttons_layout = QHBoxLayout()
        btn_ok = self.get_fixed_push_button("OK", 100)
        btn_ok.clicked.connect(self.the_button_was_clicked)
        btn_discard = self.get_fixed_push_button("Discard", 100)
        btn_discard.clicked.connect(line.clear())
        buttons_layout.addWidget(btn_ok)
        buttons_layout.addWidget(btn_discard)
        buttons_layout.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        layout.addItem(buttons_layout)
        general_tab.setLayout(layout)
        return general_tab

    @staticmethod
    def settings_tab_ui():
        general_tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.addWidget(QCheckBox("Option 1"))
        layout.addWidget(QCheckBox("Option 2"))
        layout.addWidget(QCheckBox("Option 3"))
        layout.addStretch()
        general_tab.setLayout(layout)
        return general_tab

    @staticmethod
    def the_button_was_clicked(line):
        line.setText("ciao")

    @staticmethod
    def get_fixed_push_button(name, width):
        btn = QPushButton(name)
        btn.setFixedWidth(width)
        return btn


class SMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QLineEdit()
        self.widget.setMaxLength(10)
        self.widget.setPlaceholderText("Enter your text")
        # self.widget.setReadOnly(True) # uncomment this to make readonl
        self.widget.returnPressed.connect(self.return_pressed)
        self.widget.selectionChanged.connect(self.selection_changed)
        self.widget.textChanged.connect(self.text_changed)
        self.widget.textEdited.connect(self.text_edited)

    def return_pressed(self):
        self.widget.setText("BOOM!")

    def selection_changed(self):
        print(self.widget.selectedText())

    def text_changed(self, text):
        print(text)

    def text_edited(self, text):
        print(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


