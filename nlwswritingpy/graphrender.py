# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PySide6.QtCore import QPoint, QRect, QSize, Qt, qVersion
from PySide6.QtGui import (QBrush, QConicalGradient, QLinearGradient, QPainter, QPainterPath, QPalette, QPen, QPixmap, QPolygon, QRadialGradient)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout, QLabel, QSpinBox, QWidget)
from graph import DisplayGraph

class GraphRenderArea(QWidget):
    def __init__(self,graph:DisplayGraph=None,parent=None):
        super.__init__(parent)
        graph.update = self.update
        self.graph = graph
        self.pen = QPen()
    def updateGraph(self, graph):
        self.graph = graph
        self.update()
    def set_pen(self,pen):
        self.pen = pen
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(Qt.NoBrush)
        def drawDisplayGraph(graph):
            dgraph = self.graph.deepcopy()
            for node in dgraph.keys():
                (node_glyph, pos) = dgraph.getData(node)
                path = QPainterPath()
                if type(node_glyph.img) is DisplayGraph:
                    drawDisplayGraph(node_glyph.img)
                else:
                    node_glyph.img(painter)
                for edge in dgraph.getConnections(node):
                    (edge_glyph, epos) = dgraph.getData(edge)
                    (inx,iny,indx,indy) = node_glyph.get_binding_point(edge)
                    (outx,outy,outdx,outdy) = edge_glyph.get_binding_point(node)
                    path.moveTo(pos[0]+inx,pos[1]+iny)
                    path.cubicTo(indx,indy,outdx,outdy,epos[0]+outx,epos[1]+outy)
                dgraph.pop(node)
        drawDisplayGraph(self.graph)
        painter.end()
