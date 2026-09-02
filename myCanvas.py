import customtkinter as ctk

import constants

w = constants.window_constants
c = constants.canvas_constants

class Canvas(ctk.CTkCanvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._border_width = 0
        self._width = c.canvas_width
        self._height = c.canvas_height
        self._takefocus = False
        self._background = "gray17"
        self._highlightthickness = 0