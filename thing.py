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

settingLabel = ctk.CTkLabel(app, text="Settings", font=("San Francisco", 20, "bold"), anchor="w")
settingLabel.grid(row=0, column=0, padx=40, pady=(20, 0), sticky="ew")

settingFrame = ctk.CTkFrame(app, border_width=0, corner_radius=5, bg_color="transparent", fg_color="transparent")
settingFrame.grid(row=1, column=0, padx=20, pady=0, sticky="ew")
settingFrame.grid_columnconfigure(0, weight=1)
settingFrame.grid_rowconfigure(0, weight=1)

tankLabel = ctk.CTkLabel(settingFrame, text="Tank Settings", font=("San Francisco", 16, "bold"), anchor="w")
tankLabel.grid(row=0, column=0, padx=28, pady=(5, 0), sticky="ew")

tankFrame = ctk.CTkFrame(settingFrame, border_width=0, corner_radius=10)
tankFrame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")
tankFrame.grid_columnconfigure(0, weight=1)
tankFrame.grid_rowconfigure(0, weight=1)

tankshapeLabel = ctk.CTkLabel(tankFrame, text="Tank Shape", font=("San Francisco", 14), anchor="w")
tankshapeLabel.grid(row=0, column=0, padx=10, pady=(10,5), stick="ew")

comboboxVar = ctk.StringVar(value="Spherical")
combobox = ctk.CTkComboBox(tankFrame, values=["Spherical", "Conical", "Cylindrical"], command=combobox_callback, variable=comboboxVar)
combobox.grid(row=0, column=1, padx=10, pady=(10,5), sticky="e")

tankHeightLabel = ctk.CTkLabel(tankFrame, text="Tank Height", font=("San Francisco", 14), anchor="w")
tankHeightLabel.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

tankHeightVar = ctk.StringVar()
tankHeightEntry = ctk.CTkEntry(tankFrame, textvariable=tankHeightVar, font=("San Francisco", 14))
tankHeightEntry.grid(row=1, column=1, padx=10, pady=5, sticky="e")

tankRadiusLabel = ctk.CTkLabel(tankFrame, text="Tank Radius", font=("San Francisco", 14), anchor="w")
tankRadiusLabel.grid(row=2, column=0, padx=10, pady=(5,10), sticky="ew")

tankRadiusVar = ctk.StringVar()
tankRadiusEntry = ctk.CTkEntry(tankFrame, textvariable=tankRadiusVar, font=("San Francisco", 14))
tankRadiusEntry.grid(row=2, column=1, padx=10, pady=(5,10), sticky="e")

app.mainloop()