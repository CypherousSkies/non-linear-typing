# This Python file uses the following encoding: utf-8

class Glyph():
    def __init__(self,gloss,img,outgoing=0):
        """
        Glyph(gloss,img,outgoing) creates a glyph with name `gloss`, display
        `img`, and a dict of outgoing connections, `outgoing` (which has the
        form: outgoing[node] = np.array(x,y,dx,dy))
        """
        self.gloss = gloss
        self.img = img
        self.outgoing = outgoing
    def getAnchor(self,num):
        """
        getOutgoing(node) gets the `num`th outgoing spline anchor
        (a 4-vector relative to the glyph). Each glyph will respond to this
        differently, but should be able to produce at least one anchor.
        """
        raise NotImplementedError("Glyph doesn't have an anchor!")
