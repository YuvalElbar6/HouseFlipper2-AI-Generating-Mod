from ast import Dict
from typing import  List, Dict, Literal, Optional
from pydantic import BaseModel, Field
from enum import Enum

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "normal"
    HARD = "hard"


class JobModel(BaseModel):
    # General tab
    property_name: str
    job_title: str              # can mirror property_name or be more "email style"
    difficulty: Difficulty
    budget: int

    # Text that goes into the big Description box
    description_lines: List[str] = Field(default_factory=list)

    # Email tab
    client_name: str
    client_email: str
    email_subject: str
    email_content_paragraphs: List[str] = Field(default_factory=list)

    # Tasks
    main_tasks: List[str] = Field(default_factory=list)
    optional_tasks: List[str] = Field(default_factory=list)
    style_rules: List[str] = Field(default_factory=list)

    # Available tools
    tools_enabled: Dict[str, bool] = Field(default_factory=dict)

    model_config = {
        "use_enum_values": True
    }


class Room(BaseModel):
    id: str
    type: str
    size_m2: float
    floor: int
    must_have: List[str] = Field(default_factory=list)
    nice_to_have: List[str] = Field(default_factory=list)


class RoomSpec(BaseModel):
    """
    Optional, if you want ChatGPT to also design room level blueprint.
    """
    id: str 
    type:  str 
    floor: int
    approx_size_m2: int
    style: str

    color_palette: List[str] = Field(default_factory=list)
    must_have: List[str] = Field(default_factory=list)
    nice_to_have: List[str] = Field(default_factory=list)


class HouseDesign(BaseModel):
    """
    Optional full house design that you follow in sandbox.
    """
    title: str
    theme: str
    budget: int

    rooms: List[RoomSpec] = Field(default_factory=list)