def build_house_name_prompt() -> str:
    prompt = """
Generate a House Flipper 2 style property name.

Rules:
- Return ONLY JSON.
- Format:
{
  "house_name": "string",
  "slug": "lower_snake_case_string"
}
- House name must sound realistic for HF2.
- No commas. No special symbols.
- 1–3 words max.

Examples:
- Willow Creek Cottage
- Modern Harbor Loft
- Pinewood Residence
"""
    return prompt
