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

        self.settings_frame = settingsFrame.SettingsFrame(self, fg_color="transparent")
        self.settings_frame.grid(row=1, column=0, padx=w.frame_padding_x, pady=w.frame_padding_y, sticky="new")

        self.canvas_frame = canvasFrame.CanvasFrame(self)
        self.canvas_frame.grid(row=0, column=1, rowspan=2, padx=c.canvas_padding_x, pady=c.canvas_padding_y, sticky="ne")

    def simulate(self):
        if w.dropdown_var == "Spherical":
            self.canvas_frame.canvas.draw_sphere()
        elif w.dropdown_var == "Conical":
            self.canvas_frame.canvas.draw_cone()
        elif w.dropdown_var == "Cylindrical":
            self.canvas_frame.canvas.draw_cylinder()

    def on_click(self):
        w.dropdown_var = self.settings_frame.tank_frame.tank_shape_entry.get()
        w.tank_height_var = self.settings_frame.tank_frame.tank_height_entry.get()
        w.tank_radius_var = self.settings_frame.tank_frame.tank_radius_entry.get()

        if w.dropdown_var != "" and w.tank_height_var != "" and w.tank_radius_var != "":
            if w.tank_height_var.isnumeric() and w.tank_radius_var.isnumeric():
                if float(w.tank_height_var) > 0 and float(w.tank_radius_var) > 0:
                    self.simulate()
                    self.settings_frame.simulate_button.configure(text="Success: Simulation started")
                else:
                    self.settings_frame.simulate_button.configure(text="Error: Non-positive entry")
            else:
                self.settings_frame.simulate_button.configure(text="Error: Non-numeric entry")
        else:
            self.settings_frame.simulate_button.configure(text="Error: Invalid entry")


if __name__ == "__main__":
    ctk.set_default_color_theme("blue")
    ctk.set_appearance_mode("system")

    app = App()
    app.mainloop()