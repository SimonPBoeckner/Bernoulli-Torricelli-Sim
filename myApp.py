import customtkinter as ctk

import constants
import myLabel, settingsFrame, canvasFrame

w = constants.window_constants
c = constants.canvas_constants

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        w.dropdown_var = ctk.StringVar(value=w.dropdown_values[0])
        w.tank_height_var = ctk.StringVar()
        w.tank_radius_var= ctk.StringVar()

        self.title("Bernoulli-Torricelli Simulation")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(1, weight=1)

        settings_label = myLabel.Label(master=self, text="Settings", font=w.header_font, anchor="w")
        settings_label.grid(row=0, column=0, padx=w.header_padding_x, pady=w.header_padding_y, sticky="ew")

        settings_frame = settingsFrame.SettingsFrame(self, fg_color="transparent")
        settings_frame.grid(row=1, column=0, padx=w.frame_padding_x, pady=w.frame_padding_y, sticky="new")

        canvas_frame = canvasFrame.CanvasFrame(self)
        canvas_frame.grid(row=0, column=1, rowspan=2, padx=w.frame_padding_x, pady=w.frame_padding_y, sticky="ne")


if __name__ == "__main__":
    ctk.set_default_color_theme("blue")
    ctk.set_appearance_mode("system")
    
    app = App()
    app.mainloop()