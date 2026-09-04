import customtkinter as ctk

import constants

w = constants.window_constants
c = constants.canvas_constants

class Canvas(ctk.CTkCanvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._border_width = 0
        self._width = c.canvas_size
        self._height = c.canvas_size
        self._takefocus = False
        self._background = "gray17"
        self._highlightthickness = 0

    def draw_sphere(self):
        self.delete("all")
        self.create_oval(c.sphere_x1, c.sphere_y1, c.sphere_x2, c.sphere_y2)
        self.create_line(c.sphere_spout_x1, c.sphere_spout_y1, c.sphere_spout_x2, c.sphere_spout_y2)
        self.create_line(c.sphere_spout_x3, c.sphere_spout_y3, c.sphere_spout_x4, c.sphere_spout_y4)
        self.create_rectangle(c.sphere_spout_x3, c.sphere_spout_y3, c.sphere_spout_x1, c.sphere_spout_y1, fill="gray17", width=0)

    def draw_cone(self):
        self.delete("all")
        self.create_oval(c.oval_x1, c.oval_y1, c.oval_x2, c.oval_y2)
        self.create_line(c.oval_line1_x1, c.oval_line1_y1, c.oval_line1_x2, c.oval_line1_y2)
        self.create_line(c.oval_line2_x1, c.oval_line2_y1, c.oval_line2_x2, c.oval_line2_y2)
        self.create_line(c.cone_spout_x1, c.cone_spout_y1, c.cone_spout_x2, c.cone_spout_y2)
        self.create_line(c.cone_spout_x3, c.cone_spout_y3, c.cone_spout_x4, c.cone_spout_y4)
        self.create_rectangle(c.cone_spout_x3, c.cone_spout_y3, c.cone_spout_x1, c.cone_spout_y1, fill="gray17", width=0)

    def draw_cylinder(self):
        self.delete("all")
        self.create_oval(c.oval_x1, c.oval_y1, c.oval_x2, c.oval_y2)
        self.create_line(c.cylinder_line1_x1, c.cylinder_line1_y1, c.cylinder_line1_x2, c.cylinder_line1_y2)
        self.create_line(c.cylinder_line2_x1, c.cylinder_line2_y1, c.cylinder_line2_x2, c.cylinder_line2_y2)
        self.create_oval(c.cylinder_arc_x1, c.cylinder_arc_y1, c.cylinder_arc_x2, c.cylinder_arc_y2)
        self.create_rectangle(c.cylinder_line1_x1+1, c.cylinder_line1_y2, c.cylinder_line2_x1, c.cylinder_line1_y2 - c.oval_height / 2, fill="gray17", width=0)
        self.create_line(c.cylinder_spout_x1, c.cone_spout_y1, c.cylinder_spout_x2, c.cone_spout_y2)
        self.create_line(c.cylinder_spout_x1, c.cone_spout_y3, c.cylinder_spout_x2, c.cone_spout_y4)
        self.create_rectangle(c.cylinder_spout_x1, c.cone_spout_y1+1, c.cylinder_spout_x2, c.cone_spout_y4, fill="gray17", width=0)