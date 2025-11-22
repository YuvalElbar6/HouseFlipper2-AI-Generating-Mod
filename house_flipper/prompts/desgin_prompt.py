def build_design_prompt(house_name: str):
    return f"""
You are generating a House Flipper 2 HOUSE BLUEPRINT.

House:
- Name: {house_name}

IMPORTANT RULES:
- EXACTLY 2 rooms: living_room AND bathroom.
- Valid JSON ONLY.
- No trailing commas.
- Keep lists small (max 5 items each).
- No explanation before or after JSON.
- Keep styles practical for HF2.

Return ONLY JSON matching EXACTLY this structure:

{{
  "title": "{house_name}",
  "theme": "string",
  "budget": 10000,
  "rooms": [
    {{
      "id": "living_room",
      "type": "Living room",
      "floor": 0,
      "approx_size_m2": 20,
      "style": "string",
      "color_palette": ["color1", "color2"],
      "must_have": ["item1", "item2"],
      "nice_to_have": ["item1"]
    }},
    {{
      "id": "bathroom",
      "type": "Bathroom",
      "floor": 0,
      "approx_size_m2": 6,
      "style": "string",
      "color_palette": ["color1"],
      "must_have": ["item1"],
      "nice_to_have": ["item1"]
    }}
  ]
}}

JSON ONLY.
"""
