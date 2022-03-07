import tkinter as tk

from model.field import Field
from model.sprites import Sprite
from view.utils import find_cell
from view.configuration import ViewConfiguration


class View:
    canvas: tk.Canvas
    config: ViewConfiguration
    field: Field

    def __init__(self, field, window: tk.Tk, config: ViewConfiguration):
        self.field = field
        self.config = config
        self.canvas = tk.Canvas(window, width=800, height=600)
        self.canvas.pack()

    def start(self):
        self.start_timer()

    def start_timer(self):
        self.redraw()
        self.field.move()
        self.canvas.after(300, self.start_timer)

    def redraw(self):
        self.canvas.delete("all")
        self.draw(self.field.player)
        for f in self.field.food:
            self.draw(f)
        self.draw_field()

    def draw(self, sprite: Sprite):
        center = find_cell(self.config, sprite.position)
        return self.canvas.create_oval(center.x - sprite.r / 2,
                                       center.y - sprite.r / 2,
                                       center.x + sprite.r / 2,
                                       center.y + sprite.r / 2,
                                       fill=sprite.color)

    def draw_field(self):
        for i in range(self.field.settings.height):
            for j in range(self.field.settings.width):
                x1 = self.config.offset_x + j * self.config.square_length
                y1 = self.config.offset_y + i * self.config.square_length
                x2 = x1 + self.config.square_length
                y2 = y1 + self.config.square_length
                self.canvas.create_rectangle(x1, y1, x2, y2)
