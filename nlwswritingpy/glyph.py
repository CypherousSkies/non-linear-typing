# This Python file uses the following encoding: utf-8
from PySide6.QtGui import (QPicture,QPainter)
import numpy as np

class Glyph():
    def __init__(self,gloss,img,outgoing=None):
        """
        Glyph(gloss,img,outgoing) creates a glyph with name `gloss`, display
        `img` (of either the form QPainter->[Float,Float]->None or DisplayGraph), and a dict of outgoing connections, `outgoing` (which has the
        form: outgoing[node] = np.array(x,y,dx,dy))
        """
        self.gloss = gloss
        self.img = img
        self.outgoing = outgoing
    def get_binding_point(self,node):
        return self.outgoing[node]
    def get_nth_Anchor(self,num):
        """
        getAnchor(node) gets the `num`th outgoing spline anchor
        (a 4-vector relative to the glyph). Each glyph will respond to this
        differently, but should be able to produce at least one anchor.
        """
        raise NotImplementedError("Glyph doesn't have an anchor!")
    def addAnchor(self,node):
        """
        addAnchor(node) adds an len(outgoing)th bp
        Returns a Glyph if one needs to be added to the graph as a result or None otherwise
        """
        num = 0 if self.outgoing is None else len(self.outgoing.keys())
        self.outgoing[node] = self.get_nth_Anchor(num)
        return None
    def pruneAnchor(self,node):
        """
        undo addAnchor(node)
        """
        self.outgoing.pop(node)

class BindingPoint(Glyph):
    def __init__(self,theta=np.pi/6,outgoing=None):
        super().__init__(None,QPicture(),outgoing)
        self.theta=theta
    def get_nth_Anchor(self,num):
        """
        connect outputs (e.g. ᴬᵦ =>- C)
        """
        theta = num*self.theta #pick some nice function to lay out angles
        dx = np.cos(theta)
        dy = np.sin(theta)
        return np.array(0,0,dx,dy)

class StackedBindingPoint(Glyph):
    def __init__(self,outgoing=None):
        super().__init__(None,QPicture(),outgoing)
    def get_nth_Anchor(self,num):
        """
        stack outputs (e.g. ᴬᵦ =- C)
        """
        r = 1
        theta = 0 #pick some nice function
        return np.array(r*np.cos(theta),r*np.sin(theta),np.cos(theta),np.sin(theta))

class EvenlySpacedAlong(Glyph):
    def __init__(self,gloss,img,curve,outgoing=None):
        """
        curve(l) = (x,y,dx,dy) parameterized by length, l
        """
        super().__init__(gloss,img,outgoing=None)
        self.curve = curve
    def addAnchor(self,node):
        """
        evenly space the n binding points along the positive direction of the curve
        """
        raise NotImplementedError("NYI")

class CW90(Glyph):
    def __init__(self,length,bp):
        """
        at bp take CW 90 deg turn
        """
        r = np.sqrt(bp[2]**2 + bp[3]**2)
        pic = QPicture()
        painter = QPainter()
        painter.begin(pic)
        cx = bp[2]/r #Corner.x
        cy = bp[3]/r #Corner.y
        self.cx,self.cy = cx,cy
        self.ex = length*cy #End.x
        self.ey = -length*cx #End.y
        painter.drawLine(0,0,self.ex,self.ey)
        painter.end()
        super().__init__('',pic)
    def addAnchor(self,node):
        if self.outgoing is None:
            self.outgoing[node] = np.array([self.ex,self.ey,self.cy,-self.cx])
            return None
        else:
            bp = BindingPoint(outgoing=self.outgoing)
            self.outgoing = None
            self.addAnchor(bp)
            return bp

class CCW90(Glyph):
    def __init__(self,length,bp):
        """
        at bp take CCW 90 deg turn
        """
        r = np.sqrt(bp[2]**2 + bp[3]**2)
        pic = QPicture()
        painter = QPainter()
        painter.begin(pic)
        cx = bp[2]/r #Corner.x
        cy = bp[3]/r #Corner.y
        self.cx,self.cy = cx,cy
        self.ex = -length*cy #End.x
        self.ey = length*cx #End.y
        painter.drawLine(0,0,self.ex,self.ey)
        painter.end()
        super().__init__('',pic)
    def addAnchor(self,node):
        if self.outgoing is None:
            self.outgoing[node] = np.array([self.ex,self.ey,-self.cy,self.cx])
            return None
        else:
            bp = BindingPoint(outgoing=self.outgoing)
            self.outgoing = None
            self.addAnchor(bp)
            return bp
