# Importing QApplication, the application handler and QWidget, a basic empty GUI widget, both from the QtWidgets module:
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

# Only needed for access to command line arguments:
import sys

# Next we create an instance of QApplication,
# passing in sys.arg, which is Python list containing the command line arguments passed to the application.
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
# The core of every Qt Applications is the QApplication class. Every application needs one — and only one —
# QApplication object to function. This object holds the event loop of your application —
# the core loop which governs all user interaction with the GUI.

# Create a Qt widget, which will be our window.
# In Qt all top level widgets are windows. They don't have a parent and are not nested within another widget or layout.
# What is a window? It holds the user-interface of your application.
# Every application needs at least one, but can have more. Application will (by default) exit when last window is closed
# window = QWidget()
window = QMainWindow()

# Widgets without a parent are invisible by default. So, after creating the window object, we must always call .show()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.