"""
A simple grid view of the disease state of a population.
Each cell can have its own view object, responsible for updating
the depiction of that cell.  The view object knows about the
position of the cell in the grid.
"""

import graphics.grid
from graphics.graphics import color_rgb
import mvc
import model

import logging
logging.basicConfig()
log = logging.getLogger("__name__")

STATE_COLORS = {
    model.Health.vulnerable: color_rgb(0, 200, 100),
    model.Health.asymptomatic: color_rgb(50, 200, 200),
    model.Health.symptomatic: color_rgb(250, 200, 250),
    model.Health.recovered: color_rgb(50, 150, 50),
    model.Health.dead: color_rgb(0, 0, 0)
}


class GridView(graphics.grid.Grid):
    def __init__(self, width: int, height: int,
                 nrows: int, ncols: int, title: str = "Untitled",
                 background = graphics.graphics.color_rgb(255, 255, 255),
                 autoflush=False):
        """Same arguments as graphics.grid.Grid but different defaults"""
        super().__init__(width, height,
                 nrows, ncols, title,
                 background, autoflush)

class CellView(mvc.Listener):
    """View of one cell in the grid"""

    def __init__(self, row: int, col: int, grid_view: GridView):
        self.row = row
        self.col = col
        self.grid_view = grid_view

    def notify(self, subject: mvc.Listenable, event: str):
        """Update view of this cell. """
        assert isinstance(subject, model.Individual)  # because argument type is too general
        if event == "newstate":
            color = STATE_COLORS[subject.state]
            self.grid_view.fill_cell(self.row, self.col, color)
        else:
            log.warning(f"CellView does not handle event type '{event}'")





        



