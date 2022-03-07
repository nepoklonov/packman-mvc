from model.point import Point


class Sprite:
    position: Point
    r: int
    color: str

    def __init__(self, position):
        self.position = position


class Player(Sprite):
    r = 20
    color = "red"
    direction = Point(0, 1)


class Food(Sprite):
    r = 10
    color = "green"
