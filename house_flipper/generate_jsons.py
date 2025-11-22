
import base64
import json
from pathlib import Path
from typing import Optional, Tuple
from ai_generate import safe_image_request, safe_text_request
from helper import get_custom_images_dir
from models import HouseDesign, JobModel
from prompts.blueprint_prompt import build_blueprint_prompt
from prompts.desgin_prompt import build_design_prompt
from prompts.house_prompt import build_house_name_prompt
from prompts.job_prompt import build_job_prompt

def generate_job_json(house_name: str ,retries: int = 3) -> Optional[JobModel]:
    job_prompt = build_job_prompt(house_name)
    print("📨 Generating job JSON...")

    response = safe_text_request(job_prompt, model="gpt-5.1", retries=retries)
    if not response:
        return None

    try:
        job = JobModel.model_validate_json(response.output_text)
        print("✅ Job JSON generated.")
        return job
    except Exception as e:
        print("❌ Job JSON validation failed:", e)
        print("Raw output:", response.output_text)
        return None


def generate_house_name(retries: int = 3) -> Optional[JobModel]:
    name_prompt = build_house_name_prompt()
    print("📨 Generating name prompt")

    response = safe_text_request(name_prompt, model="gpt-5.1", retries=retries)
    if not response:
        return "Unnamed_House"

    try:
        data = json.loads(response.output_text)
        return data["house_name"]
    except Exception as e:
        print(f"The exception is: {e}")
        return "Unnamed_House"


def generate_design_json(house_name: str, retries: int = 3) -> Optional[HouseDesign]:
    design_prompt = build_design_prompt(house_name)
    print("🏠 Generating design JSON...")

    response = safe_text_request(design_prompt, model="gpt-4.1", retries=retries)
    if not response:
        return None

    try:
        design_dict = json.loads(response.output_text)
        design = HouseDesign.model_validate(design_dict)
        print("✅ Design JSON generated.")
        return design
    except Exception as e:
        print("❌ Design JSON validation failed:", e)
        print("Raw output:", response.output_text)
        return None


def generate_blueprint_png(
    house_name: str,
    out_dir: Path,
    retries: int = 3
) -> Optional[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    blueprint_path = out_dir / f"{house_name}_blueprint.png"

    image_prompt = build_blueprint_prompt()

    print("📐 Generating blueprint PNG...")
    img_resp = safe_image_request(image_prompt, retries=retries)
    if not img_resp:
        return None

    try:
        b64png = img_resp.data[0].b64_json
        img_bytes = base64.b64decode(b64png)
        blueprint_path.write_bytes(img_bytes)
        print(f"✅ Blueprint saved -> {blueprint_path}")
        return blueprint_path
    except Exception as e:
        print("❌ Failed saving blueprint image:", e)
        return None



def generate_all_for_house(
    house_name: str,
    retries: int = 3
) -> Optional[Tuple[JobModel, HouseDesign, Path]]:
    job = generate_job_json(house_name, retries=retries)
    if not job:
        print("Stopping: job failed.")
        return None

    design = generate_design_json(house_name, retries=retries)
    if not design:
        print("Stopping: design failed.")
        return None

    blueprint_out_dir = get_custom_images_dir()
    blueprint = generate_blueprint_png(house_name, blueprint_out_dir, retries=retries)
    if not blueprint:
        print("Stopping: blueprint failed.")
        return None

    return job, design, blueprint