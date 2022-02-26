from curses import window
import sys
from Pyside import QtUiTools, QtGui, QtCore
from AssetRenamer import AssetRenamer

CreatedGUIDirectory = ""

class RenameGUI(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RenameGUI, self).__init__(parent)

        #Load the created GUI
        self.widget = QtUiTools.QUiLoader().load(CreatedGUIDirectory)
        self.widget.setParent(self)

        #set size
        self.widget.setGeometry(0,0,self.widget.getWidth(),self.widget.getHeight())

        #find interaction elements -- This is provided you created one in qt desinger
        self.search = self.widget.findChild(QtGui.QLineEdit, "searchPattern")
        self.replace = self.widget.findChild(QtGui.QLineEdit, "replacePattern")
        self.use_case = self.widget.findChild(QtGui.QcheckBox, "checkbox")

        # find and assign trigger to input button
        self.rename = self.widget.findChild(QtGui.QPushButton, "inputButton")
        self.rename_button.clicked.connect(self.rename_handler)

    def rename_handler(self):
        searchPattern = self.search.text()
        replacePattern = self.replace.text()
        use_case = self.use_case.isChecked()



app = None

if not QtGui.QApplication.instance():
    app = QtGui.QApplication(sys.argv)

window = RenameGUI()
window.show() 
