import customtkinter as ctk

from dataclasses import dataclass, field
from typing import Tuple, List

@dataclass
class WindowConfig:
    window_width: int|None = None
    window_height: int|None = None

    header_font: Tuple = ("San Francisco", 20, "bold")
    subheader_font: Tuple = ("San Francisco", 14, "bold")
    body_font: Tuple = ("San Francisco", 14, "normal")

    frame_radius: int = 10

    frame_padding_x: int = 10
    frame_padding_y: int = 10

    header_padding_x: int = 40
    header_padding_y: int = 20

    subheader_padding_x: int = 28
    subheader_padding_y: int = 5

    body_padding_x: int = 10
    body_padding_y: int = 10

    dropdown_values: List[str] = field(default_factory= lambda: ["Spherical", "Conical", "Cylindrical"])
    dropdown_var: ctk.StringVar|None = None

    tank_height_var: ctk.StringVar|None = None
    tank_radius_var: ctk.StringVar|None = None


@dataclass
class CanvasConfig:
    canvas_width: int = 480
    canvas_height: int = 480

    canvas_padding_x: int = 30
    canvas_padding_y: int = 30

    radius: float = 0.5 * canvas_width if canvas_width >= canvas_height else 0.5 * canvas_height

    sphere_x: float = (canvas_width/2) - radius
    sphere_y: float = (canvas_height/2) - radius

    spout_length: int = 35
    spout_height: int = 20

    sphere_spout_y1: float = (0.8 * (2 * radius)) + sphere_y
    sphere_spout_x1: float = ((radius**2)-((sphere_spout_y1-(canvas_width/2))**2))**0.5 + (canvas_width/2)
    sphere_spout_x2: float = sphere_spout_x1 + spout_length
    sphere_spout_y2: float = sphere_spout_y1
    
    sphere_spout_y3: float = sphere_spout_y1 + spout_height
    sphere_spout_x3: float = ((radius**2)-((sphere_spout_y3-(canvas_width/2))**2))**0.5 + (canvas_width/2)
    sphere_spout_y4: float = sphere_spout_y3
    sphere_spout_x4: float = sphere_spout_x2

    oval_width: float = canvas_width * 0.75
    oval_height: float = oval_width * 0.05

    cone_height: float = canvas_height * 0.8

    oval_x1: float = (canvas_width/2)-(oval_width/2)
    oval_y1: float = (canvas_height - cone_height)/2
    oval_x2: float = oval_x1 + oval_width
    oval_y2: float = oval_y1 + oval_height

    oval_line1_x1 = oval_x1
    oval_line1_y1 = oval_y1 + (oval_width/2)
    oval_line1_x2 = canvas_width/2
    oval_line1_y2 = oval_x1 + (cone_height - (oval_height/2))

    oval_line2_x1 = oval_x2
    oval_line2_y1 = oval_line1_y1
    oval_line2_x2 = oval_line1_x2
    oval_line2_y2 = oval_line1_y2

