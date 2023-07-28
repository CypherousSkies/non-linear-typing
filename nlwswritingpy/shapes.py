# This Python file uses the following encoding: utf-8
from glyph import Glyph
from math import sin,cos
# if __name__ == "__main__":
#     pass
class halfCircle(Glyph):
    def __init__(self,radius):
        """
        -C
        """
        self.radius = radius
        def draw(painter,pos):
            return
        super.__init__(None,draw,outgoing=None)
    def get_nth_Anchor(self, num):
        def th(num):
            round(num/2)*(-1)**num
            return 0
        theta = th(num)
        return (self.radius*sin(theta),self.radius*cos(theta),sin(theta),cos(theta))
