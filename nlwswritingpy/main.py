# This Python file uses the following encoding: utf-8
import sys
import numpy as np
from enum import Enum,auto
from PySide6.QtWidgets import (QApplication,QMainWindow,QMenu,QWidget,QToolTip,QMessageBox,QPushButton)
from PySide6.QtGui import (QFont,QIcon,QAction,QKeyEvent)
from graph import *
from glyph import *

#https://wiki.python.org/moin/PythonGraphLibraries
#https://graphviz.readthedocs.io/en/stable/

class Mode(Enum):
    """
    Traverse Mode:
    1. render the n outgoing edges of selected node with an outline/color difference
    2. assign selection controls:
      a. if n <= 4, use dir_edge·dir_cardinal to assign highest scoring edge to the matching cardninal traverse button
      b. if n >= 4, assign cardinal directions as above, but use rotation keys to snap to next edge in that direction
    3. use jump key to move to next selected node
    4. pressing enter on a node enters Node Adjust Mode
    """
    Traverse = auto()
    """
    Node Adjust Mode:
    1. allow directional inputs to move/rotate selected node
    2. using edge selection rules above, alter binding point angles & positions (cancel with ???)
    3. pressing enter with an edge selected creates a null node in that direction (allows for fine-tuning paths)
    4. holding shift and navigating will select many edges/nodes to do operations to (like grouping into a sub-graph)
    5. pressing enter with a node selected edits the glyph:
      a. move/rotate components with directional inputs
      b. have keys for each shape, build splines, etc.
      c. have key for binding points
      d. press enter to finalize the glyph
      e. press ctrl+enter to saves it in dictionary ordered by sizes of shapes, e.g. for UNLWS.communicate, it'd be triangle, then line
    """
    Node_Adjust = auto()
    """
    Ravoz Edit Mode:
    1. on selected node, accept typed input for glyph
    2. on selected node, accept keypress for adding new edges
    """
    Ravoz = auto()
    """
    Dictionary Edit Mode:
    1. open dropdown search menu from selected node location
      a. search will allow finding the glyph by eng gloss, ravoz gloss, shape, or id
      b. click or enter to select
      c. by default, add all binding points (or minimum required for variadic glyphs) without domains
    2. if legal, add new edges as with ravoz mode
    """
    Dictionary_Edit = auto()

class Editor(QMainWindow):
    saved = True
    mode = Mode.Traverse
    file = None
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    def closeEvent(self,event):
        if not self.saved:
            reply = QMessageBox.question(self,'quit',"Unsaved progress will be lost. Are you sure you want to quit?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
    def initMenus(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')
        modeMenu = menubar.addMenu('&Mode')

        exitAct = QAction("&Exit",self)
        exitAct.setShortcut('Ctrl+W')
        exitAct.setStatusTip('Exit')
        exitAct.triggered.connect(QApplication.instance().quit)
        fileMenu.addAction(exitAct)

        newAct = QAction('&New',self)
        newAct.setShortcut('Ctrl+N')
        fileMenu.addAction(newAct)

        openAct = QAction('Open',self)
        openAct.setShortcut('Ctrl+O')
        fileMenu.addAction(openAct)

        saveAct = QAction('Save',self)
        saveAct.setShortcut('Ctrl+s')
        saveAct.triggered.connect(self.save)
        fileMenu.addAction(saveAct)

        undoAct = QAction('Undo',self)
        redoAct = QAction('Redo',self)
        editMenu.addAction(undoAct)
        editMenu.addAction(redoAct)

        modeActs = {};
        modes = {};
        for data in Mode:
            print(data.name)
            modes[data.name] = data.name
            modeActs[data.name] = QAction(data.name,self)
            def fn(checked=None, dataname=data.name): # Eldrich QT things DO NOT CHANGE
                self.setMode(dataname) # you see, it sets the first arg to False, but if that arg has no default value, it says its missing an argument. so uh don't fuck with this
            modeActs[data.name].triggered.connect(fn)
            modeMenu.addAction(modeActs[data.name])
        print(modeActs[data.name])

    def initUI(self):
        self.initMenus()
        QToolTip.setFont(QFont('Serif',10))
        self.setWindowTitle('NLWS Editor')
        self.statusBar().showMessage('Ready')
    def setMode(self,mode):
        self.mode = Mode[mode]
        self.statusBar().showMessage(mode)
        print("set mode "+mode)
    def autosave(self):
        self.save(self.file)
    def save(self,file):
        self.saved = True
        #raise NotImplementedError()
    def keyPressEvent(self,e: QKeyEvent) -> None:
        # make a dictionary of lambdas which map inputs to adding things to the extant graph
        raise NotImplementedError()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ed = Editor()
    sys.exit(app.exec())
