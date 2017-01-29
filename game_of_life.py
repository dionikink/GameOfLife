import pyglet

import random as rnd


class GameOfLife:
    def __init__(self, window_width, window_height, cell_size):
        self.grid_width = int(window_width / cell_size)
        self.grid_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.cells = []
        self.generate_cells()
        pyglet.gl.glClearColor(255, 255, 255, 255)

    def generate_cells(self):
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                if rnd.random() < 0.4:
                    self.cells[row].append(1)
                else:
                    self.cells[row].append(0)

    def run_rules(self):
        temp = []

        for row in range(0, self.grid_height):
            temp.append([])
            for col in range(0, self.grid_width):
                cell_sum = sum([self.get_cell_value(row, col + 1),
                                self.get_cell_value(row + 1, col + 1),
                                self.get_cell_value(row + 1, col),
                                self.get_cell_value(row + 1, col - 1),
                                self.get_cell_value(row, col - 1),
                                self.get_cell_value(row - 1, col - 1),
                                self.get_cell_value(row - 1, col),
                                self.get_cell_value(row - 1, col + 1)])

                if self.cells[row][col] == 0 and cell_sum == 3:
                    temp[row].append(1)
                elif self.cells[row][col] == 1 and (cell_sum == 2 or cell_sum == 3):
                    temp[row].append(1)
                else:
                    temp[row].append(0)

        self.cells = temp

    def get_cell_value(self, row, col):
        if 0 <= row < self.grid_height and 0 <= col < self.grid_width:
            return self.cells[row][col]
        else:
            return 0

    def draw_grid(self):
        main_batch = pyglet.graphics.Batch()

        for row in range(0, self.grid_height):
            line_coords = [0, row * self.cell_size,
                           self.grid_width * self.cell_size, row * self.cell_size]

            main_batch.add(2, pyglet.gl.GL_LINES, None,
                           ('v2i', line_coords),
                           ('c3B', [0, 0, 0, 0, 0, 0]))

        for col in range(0, self.grid_width):
            line_coords = [col * self.cell_size, 0,
                           col * self.cell_size, self.grid_height * self.cell_size]

            main_batch.add(2, pyglet.gl.GL_LINES, None,
                           ('v2i', line_coords),
                           ('c3B', [0, 0, 0, 0, 0, 0]))

        main_batch.draw()

    def draw(self):
        main_batch = pyglet.graphics.Batch()

        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):
                if self.cells[row][col] == 1:
                    square_coords = [col * self.cell_size, row * self.cell_size,
                                     col * self.cell_size + self.cell_size, row * self.cell_size,
                                     col * self.cell_size, row * self.cell_size + self.cell_size,
                                     col * self.cell_size + self.cell_size, row * self.cell_size + self.cell_size]

                    main_batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, None,
                                           [0, 1, 2, 1, 2, 3],
                                           ('v2i', square_coords),
                                           ('c3B', [0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0]))

        main_batch.draw()

    def fill_cell(self, row, col):
        self.cells[row][col] = 1

    def empty_cell(self, row, col):
        self.cells[row][col] = 0

    def clear(self):
        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):
                self.cells[row][col] = 0
