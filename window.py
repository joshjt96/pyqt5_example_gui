import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Best approach to creating a custom window is to subclass QMainWindow
# and include the custom setup in the __init__ block.
# This allows the window behaviour to be self-contained.

# Subclass QMainWindow to customise the app's main window:
class MainWindow(QMainWindow):
    def __init__(self):
