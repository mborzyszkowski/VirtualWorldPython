import math
import wx.lib.ogl as ogl


class HexagonShape(ogl.PolygonShape):
    def __init__(self, side_lenght=1.0):
        ogl.PolygonShape.__init__(self)
        points = []
        for i in range(0, 6):
            points.append((math.cos(2* math.pi * i / 6.0) * side_lenght,
                           math.sin(2* math.pi * i / 6.0) * side_lenght))
        self.Create(points)
