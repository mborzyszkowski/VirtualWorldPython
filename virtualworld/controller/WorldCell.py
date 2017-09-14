
class WorldCell(object):
    def __init__(self, x=0, y=0, color=None, is_empty=True, shape=None):
        self.__x = x
        self.__y = y
        self.__color = color
        self.__is_empty = is_empty
        self.__shape = shape

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def is_empty(self):
        return self.__is_empty

    @is_empty.setter
    def is_empty(self, value):
        self.__is_empty = value

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, value):
        self.__shape = value

    def __str__(self):
        return "<WorldCell: x: {0}, y: {1}, isEmpty: {2}, color: {3}, shape: {4}>"\
            .format(str(self.x), str(self.y), str(self.is_empty), self.color, self.shape.__class__.__name__)