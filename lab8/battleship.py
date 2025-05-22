import wx

BOARD_SIZE = 8  # размер поля
CELL_SIZE = 40  # размер клетки в пикселях
SHIP_SIZES = [3, 2, 2, 1, 1, 1]  # корабли: 1x3, 2x2, 3x1

class PlacementError(Exception):
    pass

class Ship:
    def __init__(self, size, coordinates):
        self.size = size
        self.coordinates = coordinates
        self.hits = set()

    def is_sunk(self):
        return len(self.hits) == self.size

class PlayerBoard:
    def __init__(self):
        self.grid = [['~'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.ships = []
        self.shots_taken = set()

    def can_place_ship(self, row, col, size, horizontal):
        coords = []
        for i in range(size):
            r = row + (0 if horizontal else i)
            c = col + (i if horizontal else 0)
            if r >= BOARD_SIZE or c >= BOARD_SIZE or self.grid[r][c] != '~':
                return False, []
            coords.append((r, c))

        # Проверка соседних клеток (горизонталь/вертикаль)
        for r, c in coords:
            neighbors = [
                (r-1, c), (r+1, c),
                (r, c-1), (r, c+1)
            ]
            for rr, cc in neighbors:
                if 0 <= rr < BOARD_SIZE and 0 <= cc < BOARD_SIZE:
                    if (rr, cc) not in coords and self.grid[rr][cc] == 'S':
                        return False, []
        return True, coords

    def place_ship(self, row, col, size, horizontal):
        can_place, coords = self.can_place_ship(row, col, size, horizontal)
        if not can_place:
            raise PlacementError("Нельзя поставить корабль здесь")
        for r, c in coords:
            self.grid[r][c] = 'S'
        self.ships.append(Ship(size, coords))

    def receive_shot(self, row, col):
        if (row, col) in self.shots_taken:
            return 'repeat'
        self.shots_taken.add((row, col))
        for ship in self.ships:
            if (row, col) in ship.coordinates:
                ship.hits.add((row, col))
                if ship.is_sunk():
                    return 'sunk'
                return 'hit'
        return 'miss'

class BattleshipGame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Морской бой", size=(BOARD_SIZE*CELL_SIZE + 150, BOARD_SIZE*CELL_SIZE + 150))
        self.players = [PlayerBoard(), PlayerBoard()]
        self.current_player = 0
        self.phase = 'placement'  # placement или battle
        self.ship_index = 0
        self.horizontal = True

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        self.info_text = wx.StaticText(self.panel, label="Игрок 1: расставьте корабль размером 3", pos=(10, 10))
        self.orientation_btn = wx.Button(self.panel, label="Горизонтально", pos=(10, 40))
        self.orientation_btn.Bind(wx.EVT_BUTTON, self.toggle_orientation)

        self.board_panel = wx.Panel(self.panel, size=(CELL_SIZE*BOARD_SIZE, CELL_SIZE*BOARD_SIZE), pos=(10, 80))
        self.board_panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.board_panel.Bind(wx.EVT_MOTION, self.on_mouse_move)
        self.board_panel.Bind(wx.EVT_LEFT_DOWN, self.on_left_click)

        self.hover_cell = None

        self.Show()

    def toggle_orientation(self, event):
        self.horizontal = not self.horizontal
        self.orientation_btn.SetLabel("Горизонтально" if self.horizontal else "Вертикально")
        self.board_panel.Refresh()

    def on_mouse_move(self, event):
        x, y = event.GetPosition()
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            self.hover_cell = (row, col)
        else:
            self.hover_cell = None
        self.board_panel.Refresh()

    def on_left_click(self, event):
        if self.phase == 'placement':
            if not self.hover_cell:
                return
            row, col = self.hover_cell
            size = SHIP_SIZES[self.ship_index]
            board = self.players[self.current_player]
            try:
                board.place_ship(row, col, size, self.horizontal)
            except PlacementError:
                wx.MessageBox("Нельзя поставить корабль здесь!", "Ошибка", wx.OK | wx.ICON_ERROR)
                return
            self.ship_index += 1
            if self.ship_index >= len(SHIP_SIZES):
                if self.current_player == 0:
                    self.current_player = 1
                    self.ship_index = 0
                    self.info_text.SetLabel(f"Игрок 2: расставьте корабль размером {SHIP_SIZES[self.ship_index]}")
                    self.board_panel.Refresh()
                else:
                    self.phase = 'battle'
                    self.current_player = 0
                    self.info_text.SetLabel(f"Игрок {self.current_player + 1}, ваш ход. Стрелять по противнику.")
                    self.orientation_btn.Hide()
                    self.board_panel.Refresh()
            else:
                self.info_text.SetLabel(f"Игрок {self.current_player + 1}: расставьте корабль размером {SHIP_SIZES[self.ship_index]}")
            self.board_panel.Refresh()

        elif self.phase == 'battle':
            if not self.hover_cell:
                return
            row, col = self.hover_cell
            enemy = self.players[1 - self.current_player]
            result = enemy.receive_shot(row, col)
            if result == 'repeat':
                wx.MessageBox("Вы уже стреляли в эту клетку!", "Внимание", wx.OK | wx.ICON_INFORMATION)
                return
            elif result == 'miss':
                wx.MessageBox("Промах!", "Результат", wx.OK | wx.ICON_INFORMATION)
                self.current_player = 1 - self.current_player
                self.info_text.SetLabel(f"Игрок {self.current_player + 1}, ваш ход. Стрелять по противнику.")
            elif result == 'hit':
                wx.MessageBox("Попадание!", "Результат", wx.OK | wx.ICON_INFORMATION)
            elif result == 'sunk':
                wx.MessageBox("Корабль потоплен!", "Результат", wx.OK | wx.ICON_INFORMATION)

            self.board_panel.Refresh()

            if all(ship.is_sunk() for ship in enemy.ships):
                wx.MessageBox(f"Игрок {self.current_player + 1} выиграл!", "Игра окончена", wx.OK | wx.ICON_INFORMATION)
                self.Close()

    def on_paint(self, event):
        dc = wx.PaintDC(self.board_panel)
        dc.Clear()
        pen = wx.Pen('black', 1)
        dc.SetPen(pen)
        for i in range(BOARD_SIZE + 1):
            dc.DrawLine(0, i*CELL_SIZE, BOARD_SIZE*CELL_SIZE, i*CELL_SIZE)
            dc.DrawLine(i*CELL_SIZE, 0, i*CELL_SIZE, BOARD_SIZE*CELL_SIZE)

        if self.phase == 'placement':
            board = self.players[self.current_player]
            for ship in board.ships:
                for r, c in ship.coordinates:
                    dc.SetBrush(wx.Brush('gray'))
                    dc.DrawRectangle(c*CELL_SIZE+1, r*CELL_SIZE+1, CELL_SIZE-2, CELL_SIZE-2)

            if self.hover_cell and self.ship_index < len(SHIP_SIZES):
                size = SHIP_SIZES[self.ship_index]
                row, col = self.hover_cell
                can_place, coords = board.can_place_ship(row, col, size, self.horizontal)
                color = wx.Colour(0, 255, 0, 100) if can_place else wx.Colour(255, 0, 0, 100)
                dc.SetBrush(wx.Brush(color))
                dc.SetPen(wx.Pen(color))
                for (r, c) in coords:
                    dc.DrawRectangle(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE)

        elif self.phase == 'battle':
            enemy = self.players[1 - self.current_player]

            for r in range(BOARD_SIZE):
                for c in range(BOARD_SIZE):
                    x = c*CELL_SIZE
                    y = r*CELL_SIZE

                    if (r, c) in enemy.shots_taken:
                        hit = False
                        for ship in enemy.ships:
                            if (r, c) in ship.coordinates:
                                hit = True
                                break
                        if hit:
                            dc.SetBrush(wx.Brush('green'))
                            dc.SetPen(wx.Pen('black'))
                            dc.DrawCircle(x + CELL_SIZE//2, y + CELL_SIZE//2, CELL_SIZE//3)
                        else:
                            dc.SetPen(wx.Pen('red', 2))
                            dc.DrawLine(x+5, y+5, x+CELL_SIZE-5, y+CELL_SIZE-5)
                            dc.DrawLine(x+CELL_SIZE-5, y+5, x+5, y+CELL_SIZE-5)

            # Обводка и зачёркивание потопленных кораблей
            for ship in enemy.ships:
                if ship.is_sunk():
                    dc.SetPen(wx.Pen('blue', 2))
                    dc.SetBrush(wx.TRANSPARENT_BRUSH)
                    for r, c in ship.coordinates:
                        dc.DrawEllipse(c*CELL_SIZE+2, r*CELL_SIZE+2, CELL_SIZE-4, CELL_SIZE-4)
                        dc.DrawLine(c*CELL_SIZE+5, r*CELL_SIZE+5, c*CELL_SIZE+CELL_SIZE-5, r*CELL_SIZE+CELL_SIZE-5)
                        dc.DrawLine(c*CELL_SIZE+CELL_SIZE-5, r*CELL_SIZE+5, c*CELL_SIZE+5, r*CELL_SIZE+CELL_SIZE-5)

    def Refresh(self):
        self.board_panel.Refresh()

def main():
    app = wx.App()
    frame = BattleshipGame()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()

