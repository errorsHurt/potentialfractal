import sys
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QToolBar, QLineEdit, QVBoxLayout, QWidget

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Potential Fractals")
        self.resize(1000, 1000)

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar(self.sc, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self._createactions()
        self._createmenubar()
        self._createToolBars()
        self._connectActions()
        self.show()

    def run(self):
        size = int(self.canvasSizeTextLine.text())
        data = np.random.random((size, size, 1))
        self.sc.axes.set_xlim(0, size, auto=True)
        self.sc.axes.set_ylim(0, size, auto=True)
        self.sc.axes.cla()
        self.sc.axes.imshow(data, cmap='Greens', interpolation='nearest', origin='lower')
        self.sc.draw()

    def save(self):
        plt.savefig("plot.png")

    def _connectActions(self):
        self.runAction.triggered.connect(self.run)
        self.exitAction.triggered.connect(self.close)
        self.saveAction.triggered.connect(self.save)




    def _createactions(self):
        # Creating actions using the second constructor
        self.newAction = QAction("&New", self)
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("&Cut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
        self.runAction = QAction("&Run", self)
        self.createMassAction = QAction("&Create Mass")
        self.potential1r = QAction("1/r potential", self)
        self.potential2r = QAction("1/r^2 potential", self)
        self.potentialx = QAction("1/x potential", self)
        self.potentialy = QAction("1/y potential", self)



    def _createmenubar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)

        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):
        runToolBar = QToolBar("Run", self)
        self.addToolBar(Qt.TopToolBarArea, runToolBar)
        runToolBar.addAction(self.runAction)
        runToolBar.addAction(self.saveAction)
        runToolBar.addAction(self.createMassAction)
        self.simEndTimeTextLabel = QLabel()
        self.simEndTimeTextLabel.setText("Time to simulate : ")
        self.simEndTimeTextLine = QLineEdit()
        self.simEndTimeTextLine.setFixedWidth(50)
        self.simEndTimeTextLine.setText("1000")
        self.simDeltaTimeTextLabel = QLabel()
        self.simDeltaTimeTextLabel.setText(" Time between simulation steps : ")
        self.simDeltaTimeTextLine = QLineEdit()
        self.simDeltaTimeTextLine.setText("10")
        self.simDeltaTimeTextLine.setFixedWidth(30)
        self.canvasSizeTextLabel = QLabel()
        self.canvasSizeTextLabel.setText(" Sidelength of Canvas : ")
        self.canvasSizeTextLine = QLineEdit()
        self.canvasSizeTextLine.setText("10")
        self.canvasSizeTextLine.setFixedWidth(30)
        self.canvasScaleTextLabel = QLabel()
        self.canvasScaleTextLabel.setText(" ratio of distance to pixelsize")
        self.canvasScaleTextLine = QLineEdit()
        self.canvasScaleTextLine.setText("1")
        self.canvasScaleTextLine.setFixedWidth(20)

        runToolBar.addWidget(self.simEndTimeTextLabel)
        runToolBar.addWidget(self.simEndTimeTextLine)
        runToolBar.addWidget(self.simDeltaTimeTextLabel)
        runToolBar.addWidget(self.simDeltaTimeTextLine)
        runToolBar.addWidget(self.canvasSizeTextLabel)
        runToolBar.addWidget(self.canvasSizeTextLine)
        runToolBar.addWidget(self.canvasScaleTextLabel)
        runToolBar.addWidget(self.canvasScaleTextLine)

        potentialToolBar = QToolBar("Potentials", self)
        potentialToolBar.addAction(self.potential1r)
        potentialToolBar.addAction(self.potential2r)
        potentialToolBar.addAction(self.potentialx)
        potentialToolBar.addAction(self.potentialy)
        self.addToolBar(Qt.LeftToolBarArea, potentialToolBar)

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def createWindow():
    app = QApplication(sys.argv)
    window = Window()

    sys.exit(app.exec_())
