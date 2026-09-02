import customtkinter as ctk

import constants

w = constants.window_constants
c = constants.canvas_constants

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._border_width=0
        self._corner_radius=w.frame_radius