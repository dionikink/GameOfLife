import pyglet

import pyglet.window.key as key
import pyglet.window.mouse as mouse

from game_of_life import GameOfLife

class Window(pyglet.window.Window):
    def __init__(self, x, y, title):
        super().__init__(x, y, title)

        x, y = self.get_size()
        self.game_of_life = GameOfLife(x, y, 20)

        pyglet.clock.schedule_interval(self.update, 1.0/6.0)
        self.running = True

    def on_draw(self):
        self.clear()
        self.game_of_life.draw()
        self.game_of_life.draw_grid()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE and self.running:
            pyglet.clock.unschedule(self.update)
            self.running = False
        else:
            pyglet.clock.schedule_interval(self.update, 1.0/6.0)
            self.running = True

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print(x, y)

    def update(self, dt):
        self.game_of_life.run_rules()

if __name__ == '__main__':
    window = Window(1280, 720, "Game of Life")
    pyglet.app.run()
