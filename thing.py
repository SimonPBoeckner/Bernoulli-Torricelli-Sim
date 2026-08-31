import customtkinter as ctk

def on_click():
    choice = comboboxVar.get()
    height = tankHeightVar.get()
    radius = tankRadiusVar.get()
    if height.isnumeric() and radius.isnumeric():
        if float(height) > 0 and float(radius) > 0:
            startButton.configure(text="Success: Simulation started")
            simulate(choice, height, radius)
        else:
            startButton.configure(text="Error: Invalid number")
    else:
        startButton.configure(text="Error: Invalid entry")

def getCircleX(setY):
    return ((200**2)-((setY-240)**2))**0.5 + 240

width = 480
_height = 480
radiusNum = 200
ovalHeight = 20
ovalWidth = 300

def simulate(choice, height, radius):
    if choice == "Spherical":
        print("test")
        canvas.delete("all")
        _drawSphere()
    elif choice == "Conical":
        canvas.delete("all")
        _drawCone()

def _drawSphere():
    canvas.create_oval(((width/2)-(radiusNum)),((_height/2)-(radiusNum)),((width/2)+(radiusNum)),((_height/2)+(radiusNum)))
    canvas.create_line(getCircleX(360), 360, getCircleX(360)+50, 360)
    canvas.create_line(getCircleX(340), 340, getCircleX(360)+50, 340)
    canvas.create_rectangle(getCircleX(360)-10, 360, getCircleX(340)+10, 341, fill="gray17", width=0)

def _drawCone():
    canvas.create_oval((width/2)-(ovalWidth/2), 100-(ovalHeight/2) , (width/2)+(ovalWidth/2), 100+(ovalHeight/2))
    canvas.create_line((width/2)-(ovalWidth/2), 100, width/2, 400)
    canvas.create_line((width/2)+(ovalWidth/2), 100, width/2, 400)
    canvas.create_line((-380/2)+440, 380, (-380/2)+440+20, 380)
    canvas.create_line((-390/2)+440, 390, (-380/2)+440+20, 390)
    canvas.create_rectangle((-390/2)+440, 390, (-380/2)+440, 380, fill="gray17", width=0)

def _drawCylinder():
    canvas.create_oval((width/2)-(ovalWidth/2), 50-(ovalHeight/2), (width/2)+(ovalWidth/2), 50+(ovalHeight/2))
    canvas.create_line((width/2)-(ovalWidth/2), 50, (width/2)-(ovalWidth/2), 450)
    canvas.create_line((width/2)+(ovalWidth/2), 50, (width/2)+(ovalWidth/2), 450)
    canvas.create_oval((width/2)-(ovalWidth/2), 450-(ovalHeight/2), (width/2)+(ovalWidth/2), 450+(ovalHeight/2))
    canvas.create_rectangle((width/2)-(ovalWidth/2)+1, 450, (width/2)+(ovalWidth/2), 450-(ovalHeight/2), fill="gray17", width=0)
    canvas.create_line((width/2)+(ovalWidth/2), 400, (width/2)+(ovalWidth/2)+30, 400)
    canvas.create_line((width/2)+(ovalWidth/2), 420, (width/2)+(ovalWidth/2)+30, 420)
    canvas.create_rectangle((width/2)+(ovalWidth/2), 400, (width/2)+(ovalWidth/2), 420, fill="gray17", width=0)


ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("system")

app = ctk.CTk()
# app.geometry("1080x720")
app.title("Bernoulli-Torricelli Simulation")
app.resizable(False, False)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=0)
app.grid_rowconfigure(1, weight=1)

settingLabel = ctk.CTkLabel(app, text="Settings", font=("San Francisco", 20, "bold"), anchor="w")
settingLabel.grid(row=0, column=0, padx=40, pady=(20, 0), sticky="ew")

settingFrame = ctk.CTkFrame(app, border_width=0, corner_radius=5, bg_color="transparent", fg_color="transparent")
settingFrame.grid(row=1, column=0, padx=20, pady=0, sticky="new")
settingFrame.grid_columnconfigure(0, weight=1)

tankLabel = ctk.CTkLabel(settingFrame, text="Tank Settings", font=("San Francisco", 14, "bold"), anchor="w")
tankLabel.grid(row=0, column=0, padx=28, pady=(5, 5), sticky="ew")

tankFrame = ctk.CTkFrame(settingFrame, border_width=0, corner_radius=10)
tankFrame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")
tankFrame.grid_columnconfigure(0, weight=1)
tankFrame.grid_rowconfigure(0, weight=1)

tankshapeLabel = ctk.CTkLabel(tankFrame, text="Tank Shape", font=("San Francisco", 14), anchor="w")
tankshapeLabel.grid(row=0, column=0, padx=10, pady=(10,5), stick="ew")

comboboxVar = ctk.StringVar(value="Spherical")
combobox = ctk.CTkComboBox(tankFrame, values=["Spherical", "Conical", "Cylindrical"], variable=comboboxVar, state="readonly")
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

startButton = ctk.CTkButton(settingFrame, text="Start Simulation", font=("San Francisco", 14), command=on_click)
startButton.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

canvasFrame = ctk.CTkFrame(app, border_width=0, corner_radius=5)
canvasFrame.grid(row=0, column=1, padx=10, pady=10, sticky="ne", rowspan=2)

canvas = ctk.CTkCanvas(canvasFrame, borderwidth=0, width=480, height=480, takefocus=False, background="gray17", highlightthickness=0)
canvas.grid(row=0, column=0, padx=10, pady=10, sticky="ne")

_drawCylinder()
app.mainloop()