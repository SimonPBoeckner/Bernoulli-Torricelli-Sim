import customtkinter as ctk
import myLabel, myFrame, constants

import tankFrame

w = constants.window_constants
c = constants.canvas_constants

class SettingsFrame(myFrame.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        tank_label = myLabel.Label(master=self, text="Tank Settings", font=w.subheader_font, anchor="w")
        tank_label.grid(row=0, column=0, padx=w.subheader_padding_x, pady=w.subheader_padding_y, sticky="ew")

        tank_frame = tankFrame.TankFrame(self)
        tank_frame.grid(row=1, column=0, padx=w.frame_padding_x, pady=w.frame_padding_y, sticky="ew")

        simulate_button = ctk.CTkButton(self, text="Start Simulation", font=w.body_font)
        simulate_button.grid(row=2, column=0, padx=w.body_padding_x, pady=w.body_padding_y, sticky="ew")

