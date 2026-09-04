import customtkinter as ctk

import myLabel, myFrame, constants

w = constants.window_constants
c = constants.canvas_constants

class TankFrame(myFrame.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        tank_shape_label = myLabel.Label(master=self, text="Tank Shape")
        tank_shape_label.grid(row=0, column=0, padx=w.body_padding_x, pady=w.body_padding_y, sticky="ew")

        self.tank_shape_entry = ctk.CTkComboBox(self, values=w.dropdown_values, variable=w.dropdown_var, font=w.body_font, dropdown_font=w.body_font, state="readonly")
        w.dropdown_var = w.dropdown_values[0]
        self.tank_shape_entry.grid(row=0, column=1, padx=w.body_padding_x, pady=w.body_padding_y, sticky="e")

        tank_height_label = myLabel.Label(master=self, text="Tank Height")
        tank_height_label.grid(row=1, column=0, padx=w.body_padding_x, pady=w.body_padding_y, sticky="ew")

        self.tank_height_entry = ctk.CTkEntry(self, textvariable=w.tank_height_var, font=w.body_font)
        self.tank_height_entry.grid(row=1, column=1, padx=w.body_padding_x, pady=w.body_padding_y, sticky="e")

        tank_radius_label = myLabel.Label(master=self, text="Tank Radius")
        tank_radius_label.grid(row=2, column=0, padx=w.body_padding_x, pady=w.body_padding_y, sticky="ew")

        self.tank_radius_entry = ctk.CTkEntry(self, textvariable=w.tank_radius_var, font=w.body_font)
        self.tank_radius_entry.grid(row=2, column=1, padx=w.body_padding_x, pady=w.body_padding_y, sticky="e")

    