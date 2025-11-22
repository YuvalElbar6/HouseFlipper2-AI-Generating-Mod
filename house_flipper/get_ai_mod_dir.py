from pathlib import Path
import os

def get_ai_mods_dir() -> Path:
    docs = Path(os.path.expanduser("~/Documents"))
    hf2_docs = docs / "House Flipper 2"
    ai_mods = hf2_docs / "AI_Mods"
    ai_mods.mkdir(parents=True, exist_ok=True)
    return ai_mods

AI_MODS_DIR = get_ai_mods_dir()
print("AI_Mods dir:", AI_MODS_DIR)
