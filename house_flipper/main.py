from pathlib import Path
from generate_jsons import generate_all_for_house, generate_house_name
from helper import get_ai_mods_dir,  save_bundle


AI_MODS_DIR = get_ai_mods_dir()

def process_houses(limit: int = 5, out_dir: Path = AI_MODS_DIR):
    f'''
    The function is processing the house's request AKA Job, desgin and blueprint.
    :param limit - int - The limit of custom houses you can generate
    :param out_dir - Path - The dir in which you save your files
    '''
    results = []

    while len(results) < limit:
        house_name = generate_house_name()
        print(f"\n=== Processing: {house_name} ===")
        res = generate_all_for_house(house_name=house_name)

        if not res:
            print(f"⚠️ Skipping {house_name} due to generation failure.")
            continue

        job, design, blueprint = res
        save_bundle(house_name, job, design, blueprint, out_dir)

        results.append((job, design, blueprint))
        print(f"✅ Done {len(results)}/{limit}")

    return results



if __name__ == "__main__":
     process_houses(limit=5)
    