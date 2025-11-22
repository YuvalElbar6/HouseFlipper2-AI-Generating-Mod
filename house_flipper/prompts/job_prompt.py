def build_job_prompt(house_name: str):
    return f"""
You are generating a House Flipper 2 renovation JOB.

House:
- Name: {house_name}

IMPORTANT RULES:
- Return VALID JSON ONLY.
- No comments, no trailing commas.
- Keep lists short.
- Max 3 main tasks.
- Max 3 optional tasks.
- Max 3 style rules.
- Email: 1–3 short paragraphs.

Return ONLY JSON matching EXACTLY this structure:

{{
  "property_name": "{house_name}",
  "job_title": "string",
  "difficulty": "easy" or "normal" or "hard",
  "budget": 10000,

  "client_name": "string",
  "client_email": "string",
  "email_subject": "string",
  "email_content_paragraphs": ["para1", "para2"],

  "description_lines": ["line1", "line2"],

  "main_tasks": ["task1", "task2"],
  "optional_tasks": ["optional1"],
  "style_rules": ["rule1", "rule2"],

  "tools_enabled": {{
    "flipper_tool": true,
    "collecting_trash": true,
    "cleaning": true,
    "vacuuming": true,
    "demolishing": false,
    "building": true,
    "edit_wiring": false,
    "surface_finishes": true
  }}
}}

JSON ONLY.
"""
