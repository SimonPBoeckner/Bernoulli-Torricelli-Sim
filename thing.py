import customtkinter as ctk

def combobox_callback(choice):
    print(choice)

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("system")

app = ctk.CTk()
app.geometry("720x480")
app.title("Bernoulli-Torricelli Simulation")
app.resizable(False, False)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)

settingFrame = ctk.CTkFrame(app, border_width=1, corner_radius=5)
settingFrame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

settingLabel = ctk.CTkLabel(app, text="Settings", font=("San Francisco", 20, "bold"), anchor="w")
settingLabel.grid(row=0, column=0, padx=(22, 0), pady=(10, 0), sticky="ew")

tankLabel = ctk.CTkLabel(settingFrame, text="Tank Settings", font=("San Francisco", 16, "bold"), anchor="w")
tankLabel.grid(row=0, column=0, padx=(14, 0), pady=(5, 0), sticky="ew")

tankFrame = ctk.CTkFrame(settingFrame, border_width=1, corner_radius=3)
tankFrame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

tankshapeLabel = ctk.CTkLabel(tankFrame, text="Tank Shape", font=("San Francisco", 14), anchor="w")
tankshapeLabel.grid(row=0, column=0, padx=10, pady=10, stick="ew")

comboboxVar = ctk.StringVar(value="Spherical")
combobox = ctk.CTkComboBox(tankFrame, values=["Spherical", "Conical", "Cylindrical"], command=combobox_callback, variable=comboboxVar)
combobox.grid(row=0, column=1, padx=10, pady=10, sticky="e")

app.mainloop()