"""Bar chart of current infections and cumulative deaths"""

import graphics.graphics as graphics
import time

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# re-export color_rgb as chart.rgb
color = graphics.color_rgb

class Chart:
    """The bar chart"""
    def __init__(self, pxwidth: int, pxheight: int,
                 ncols: int, v_min: int, v_max: int,
                 autoflush=True, title="Chart", background=graphics.color_rgb(255,255,255)):
        self.width = pxwidth
        self.height = pxheight
        self.ncols = ncols
        self.win = graphics.GraphWin("Chart", pxwidth, pxheight,autoflush=autoflush)
        bkgrnd = graphics.Rectangle( graphics.Point(0,0), graphics.Point(pxwidth,pxheight) )
        bkgrnd.setFill( background )
        self.col_width = pxwidth / ncols
        self.unit_height = pxheight / (v_max - v_min)
        self._last_update = time.time()

    def bar(self, col: int, height: int, color, frac_width=1.0):
        if col > self.ncols:
            log.debug(f"Column {col} off chart")
            return
        thin_by = (1.0 - frac_width) * self.col_width
        right = col  * self.col_width - thin_by
        left = (col - 1) * self.col_width + thin_by
        bottom = self.height
        top = self.height - (height * self.unit_height) # Measuring from top of window
        r = graphics.Rectangle(graphics.Point(left,bottom), graphics.Point(right,top))
        r.setFill(color)
        r.draw(self.win)

def main():
    """Smoke test: bars 1..10 """
    chart = Chart(500,500,ncols=10,v_min=0,v_max=10,title="Stairs")
    for i in range(1,11):
        chart.bar(i,i,color(200,100,100), frac_width=0.90)
    input("Press enter to close")

if __name__ == "__main__":
    main()
