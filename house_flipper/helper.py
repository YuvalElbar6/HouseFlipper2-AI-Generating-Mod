import json
import os
from pathlib import Path

from models import HouseDesign, JobModel

def get_ai_mods_dir() -> Path:
    '''Get the json mod path'''
    docs = Path(os.path.expanduser("~/Documents"))
    hf2_docs = docs / "House Flipper 2"
    ai_mods = hf2_docs / "AI_Mods"
    ai_mods.mkdir(parents=True, exist_ok=True)
    return ai_mods


def get_custom_images_dir() -> Path:
    '''Get the blueprint mod's path'''
    docs = Path(os.path.expanduser("~/AppData"))
    file_location = docs / "LocalLow" / "Frozen District"
    hf2_docs = file_location / "House Flipper 2"
    ai_mods = hf2_docs / "Pictures"
    ai_mods.mkdir(parents=True, exist_ok=True)
    return ai_mods

def save_bundle(house_name: str ,job: JobModel, design: HouseDesign, blueprint_path: Path, out_dir: Path):
    '''
    The function is saving all the generated data as a bundle.
    :param house_name - str - The name of the house
    :param job - JobModel - The generated job object
    :param design - HouseDesign - The generated design object
    :param blueprint_path - Path - The path to the generated blueprint
    :param out_dir - Path - The path to save the bundle in
    '''
    bundle_path = out_dir / f"{house_name}_bundle.json"
    job_path = out_dir / f"{house_name}_job.json"
    design_path = out_dir / f"{house_name}_design.json"

    job_path.write_text(job.model_dump_json(indent=2), encoding="utf8")
    design_path.write_text(design.model_dump_json(indent=2), encoding="utf8")

    bundle = {
        "job": job.model_dump(),
        "design": design.model_dump(),
        "blueprint_png": str(blueprint_path)
    }
    bundle_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False), encoding="utf8")

    print(f"💾 Saved job -> {job_path}")
    print(f"💾 Saved design -> {design_path}")
    print(f"💾 Saved bundle -> {bundle_path}")