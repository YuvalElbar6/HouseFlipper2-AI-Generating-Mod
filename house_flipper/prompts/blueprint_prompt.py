def build_blueprint_prompt() -> str:
    prompt = """
Simple 2D house floor plan blueprint, top-down view.
White background with a very light grey square grid.
Thick solid blue walls outlining each room.
No furniture, no textures, no shading.
Room names written in clean flat blue text (Living Room, Kitchen, Bedroom, Bathroom).
No objects, no icons, no appliances, no decorations.
No perspective, no realism, no 3D — schematic only.
Style exactly like a simple architectural sketch or House Flipper 2 workshop plan.
"""
    return prompt
