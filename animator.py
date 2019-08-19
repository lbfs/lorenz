import sys
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np

class Animator:
    def __init__(self, title, limit, generators):
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.opts["distance"] = 350
        self.w.setWindowTitle(title)
        self.w.setGeometry(50, 50, 720, 480)
        self.w.show()

        self.limit = limit
        self.plot_items = []
        for i, generator in enumerate(generators):
            points = [next(generator)]
            pts = np.vstack(points)
            plot_item = gl.GLLinePlotItem(
                    pos=pts,
                    color=pg.glColor((1, (i + 1) * 1.2)),
                    width=1,
                    antialias=True
                )
            self.plot_items.append((i, generator, plot_item, points))
            self.w.addItem(plot_item)

    def update(self):
        for i, generator, plot_item, points in self.plot_items:
            points.append(next(generator))

            if self.limit is not None and len(points) > self.limit:
                del points[0]

            pts = np.vstack(points)
            plot_item.setData(pos=pts, color=pg.glColor((1, (i + 1) * 1.2)), width=1)

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def animate(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        self.start()
