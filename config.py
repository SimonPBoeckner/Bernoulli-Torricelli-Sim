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

    frame_padding_x: int = 5
    frame_padding_y: int = 5

    header_padding_x: int = 30
    header_padding_y: Tuple[int] = (10,0)

    subheader_padding_x: int = 15
    subheader_padding_y: int = 0

    body_padding_x: int = 10
    body_padding_y: int = 5

    dropdown_values: List[str] = field(default_factory= lambda: ["Spherical", "Conical", "Cylindrical"])
    dropdown_var: str = ""

    tank_height_var: str = ""
    tank_radius_var: str = ""


@dataclass
class CanvasConfig:
    canvas_size: int = 480

    canvas_padding_x: int = 30
    canvas_padding_y: int = 30

    radius: float = 0.45 * canvas_size

    sphere_x1: float = (canvas_size/2) - radius
    sphere_y1: float = sphere_x1
    sphere_x2: float = (canvas_size/2) + radius
    sphere_y2: float = sphere_x2

    spout_length: int = radius * 0.2
    spout_height: int = radius * 0.2

    sphere_spout_y1: float = (0.8 * (2 * radius)) + sphere_y1
    sphere_spout_x1: float = ((radius**2)-((sphere_spout_y1-(canvas_size/2))**2))**0.5 + (canvas_size/2)
    sphere_spout_x2: float = sphere_spout_x1 + spout_length
    sphere_spout_y2: float = sphere_spout_y1
    
    sphere_spout_y3: float = sphere_spout_y1 + spout_height
    sphere_spout_x3: float = ((radius**2)-((sphere_spout_y3-(canvas_size/2))**2))**0.5 + (canvas_size/2)
    sphere_spout_y4: float = sphere_spout_y3
    sphere_spout_x4: float = sphere_spout_x2

    oval_width: float = canvas_size * 0.75
    oval_height: float = oval_width * 0.05

    cone_height: float = canvas_size * 0.9

    oval_x1: float = (canvas_size/2)-(oval_width/2)
    oval_y1: float = (canvas_size - cone_height)/2
    oval_x2: float = oval_x1 + oval_width
    oval_y2: float = oval_y1 + oval_height

    oval_line1_x1 = oval_x1
    oval_line1_y1 = oval_y1 + (oval_height/2)
    oval_line1_x2 = canvas_size/2
    oval_line1_y2 = oval_x1 + (cone_height - (oval_height/2))

    oval_line2_x1 = oval_x2
    oval_line2_y1 = oval_line1_y1
    oval_line2_x2 = oval_line1_x2
    oval_line2_y2 = oval_line1_y2

    slope = (oval_line2_y2 - oval_line2_y1) / (oval_line2_x2 - oval_line2_x1)
    yintercept = oval_line2_y1 - slope * oval_line2_x1

    cone_spout_y1 = cone_height * 0.85
    cone_spout_x1 = (cone_spout_y1 / slope) + (-yintercept / slope)
    cone_spout_y2 = cone_spout_y1
    cone_spout_x2 = cone_spout_x1 + spout_length

    cone_spout_y3 = cone_spout_y1 + spout_height
    cone_spout_x3 = (cone_spout_y3 / slope) + (-yintercept / slope)
    cone_spout_y4 = cone_spout_y3
    cone_spout_x4 = cone_spout_x2

    cylinder_line1_x1 = oval_x1
    cylinder_line1_y1 = oval_y1 + oval_height / 2
    cylinder_line1_x2 = oval_x1
    cylinder_line1_y2 = oval_y1 + cone_height - oval_height / 2

    cylinder_line2_x1 = oval_x1 + oval_width
    cylinder_line2_y1 = cylinder_line1_y1
    cylinder_line2_x2 = oval_x1 + oval_width
    cylinder_line2_y2 = cylinder_line1_y2

    cylinder_arc_x1 = oval_x1
    cylinder_arc_y1 = cylinder_line1_y2 - oval_height / 2
    cylinder_arc_x2 = oval_x1 + oval_width
    cylinder_arc_y2 = cylinder_line1_y2 + oval_height / 2

    cylinder_spout_x1 = oval_x1 + oval_width
    cylinder_spout_x2 = cylinder_spout_x1 + spout_length