import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
        print("Double clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
#
# import sys
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         self.label = QLabel()
#
#         self.input = QLineEdit()
#         self.input.textChanged.connect(self.label.setText)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.input)
#         layout.addWidget(self.label)
#
#         container = QWidget()
#         container.setLayout(layout)
#
#         # Set the central widget of the Window.
#         self.setCentralWidget(container)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()


# import sys
#
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from random import choice
#
# window_titles = [
#     'My App',
#     'My App',
#     'Still My App',
#     'Still My App',
#     'What on earth',
#     'What on earth',
#     'This is surprising',
#     'This is surprising',
#     'Something went wrong'
# ]
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.n_times_clicked = 0
#
#         self.setWindowTitle("My App")
#
#         self.button = QPushButton("Press Me!")
#         self.button.clicked.connect(self.the_button_was_clicked)
#
#         self.windowTitleChanged.connect(self.the_window_title_changed)
#
#         # Set the central widget of the Window.
#         self.setCentralWidget(self.button)
#
#     def the_button_was_clicked(self):
#         print("Clicked.")
#         new_window_title = choice(window_titles)
#         print("Setting title:  %s" % new_window_title)
#         self.setWindowTitle(new_window_title)
#
#     def the_window_title_changed(self, window_title):
#         print("Window title changed: %s" % window_title)
#
#         if window_title == 'Something went wrong':
#             self.button.setDisabled(True)
#
# # Best approach to creating a custom window is to subclass QMainWindow
# # and include the custom setup in the __init__ block.
# # This allows the window behaviour to be self-contained.
#
# # Subclass QMainWindow to customise the app's main window:
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         # Set the title of the window and create a button with some text:
# #         self.setWindowTitle("My App")
# #         self.button = QPushButton("Click Here!")
# #         self.button.setCheckable(True)
# #         # Set a fixed size for this window:
# #         # self.setFixedSize(1000, 500)
# #
# #         # Set min/max sizes:
# #         self.setMinimumSize(400, 200)
# #         self.setMaximumSize(800, 400)
# #
# #         # Set the button to accept a click signal that takes a custom method as a parameter:
# #         self.button.clicked.connect(self.button_click)
# #         # Accepting click signal for checking toggle method:
# #         self.button.clicked.connect(self.button_toggle)
# #         # Set the central widget of the window to be the button:
# #         self.setCentralWidget(self.button)
# #
# #     def button_click(self):
# #         self.button.setText("Already clicked")
# #         self.button.setEnabled(False)
# #         self.setWindowTitle("My Oneshot App")
# #     def button_toggle(self, checked):
# #         self.button_is_checked = checked
# #         print(self.button_is_checked)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()
