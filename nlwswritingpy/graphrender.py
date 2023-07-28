# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PySide6.QtCore import QPoint, QRect, QSize, Qt, qVersion
from PySide6.QtGui import (QBrush, QConicalGradient, QLinearGradient, QPainter, QPainterPath, QPalette, QPen, QPixmap, QPolygon, QRadialGradient)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout, QLabel, QSpinBox, QWidget)
from graph import DisplayGraph
import numpy as np

class GraphRenderArea(QWidget):
    def __init__(self,parent,graph:DisplayGraph=None):
        super().__init__(parent)
        self.updateGraph(graph)
        self.pen = QPen()
    def updateGraph(self, graph):
        self.graph = graph
        if graph is not None:
            self.graph.update = self.update
        self.update()
    def set_pen(self,pen):
        self.pen = pen
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(Qt.NoBrush)
        def drawDisplayGraph(graph,offset):
            dgraph = self.graph.deepcopy()
            for node in dgraph.keys():
                (node_glyph, pos) = dgraph.getData(node)
                pos = offset + pos
                path = QPainterPath()
                if type(node_glyph.img) is DisplayGraph:
                    drawDisplayGraph(node_glyph.img)
                else:
                    painter.drawPicture(pos,node_glyph.img(pos))
                for edge in dgraph.getConnections(node):
                    (edge_glyph, epos) = dgraph.getData(edge)
                    epos = offset + epos
                    (inx,iny,indx,indy) = node_glyph.get_binding_point(edge)
                    (outx,outy,outdx,outdy) = edge_glyph.get_binding_point(node)
                    path.moveTo(pos[0]+inx,pos[1]+iny)
                    path.cubicTo(indx,indy,outdx,outdy,epos[0]+outx,epos[1]+outy)
                dgraph.pop(node)
            painter.drawPath(path)
        if self.graph is not None:
            drawDisplayGraph(self.graph,np.array([0,0]))
        painter.end()
