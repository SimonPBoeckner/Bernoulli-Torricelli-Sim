import myFrame, myCanvas

import constants

w = constants.window_constants
c = constants.canvas_constants

class CanvasFrame(myFrame.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        canvas = myCanvas.Canvas(self, width=c.canvas_width, height=c.canvas_height, takefocus=False, background="gray17", highlightthickness=0, borderwidth=0)
        canvas.grid(row=0, column=0, padx=c.canvas_padding_x, pady=c.canvas_padding_y, sticky="ne")