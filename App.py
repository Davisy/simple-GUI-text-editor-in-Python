'''/

AUTHOR: Davis David
EMAIL: davisdavid179@gmail.com

/'''


import sys 
from PyQt4 import  QtGui, QtCore
from test.test_optparse import TestExtendAddActions

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1000,700)
        self.setWindowTitle("TEXT EDITOR")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        #open a file from the computer 
        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+E")
        openFile.setStatusTip("Open File")
        openFile.triggered.connect(self.file_open) 
        
        #save a file in the computer 
        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("Save File")
        saveFile.triggered.connect(self.file_save) 
         
        #Editor menu to write  a new text file
        openEditor = QtGui.QAction("&New File", self)
        openEditor.setShortcut("Ctrl+N")
        openEditor.setStatusTip("Open new File")
        openEditor.triggered.connect(self.editor)
        
        #Close the application 
        exitEditor = QtGui.QAction("&Exit", self)
        exitEditor.setShortcut("Ctrl+Q")
        exitEditor.setStatusTip("Leave the Applicatoin")
        exitEditor.triggered.connect(self.close_application)
        
     
        
        #Create a Menu Bar 
        mainMenu = self.menuBar()
        
        #Add Menu called File
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openEditor)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitEditor)
     
        self.show()
        
    #Method to open a file    
    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')
        
        self.editor()
        
        with file:
            text = file.read()
            self.textEdit.setText(text)
    
    #Method to save a file
    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        
    #Method to open Editor panel
    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
    
    #method to close the application
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Exit",
                                            "do you want to close the application? ",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Application closed")
            sys.exit()
        else:
            pass
        
        
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
        
        

run()