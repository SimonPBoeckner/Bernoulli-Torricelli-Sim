import customtkinter as ctk

import constants

w = constants.window_constants
c = constants.canvas_constants

class Label(ctk.CTkLabel):
    def __init__(self, master, **kwargs,):
        super().__init__(master, **kwargs)

        self._text = "Placeholder"
        self._font = w.body_font
        self._anchor = "w"