import os
import shutil
import uuid

def convert_to_edu(bedrock_world_path, edu_output_path):
    if not os.path.exists(bedrock_world_path):
        print(f"Error: Bedrock world path does not exist: {bedrock_world_path}")
        return

    # Ensure output path exists
    os.makedirs(edu_output_path, exist_ok=True)

    # Generate a new UUID for the world
    world_uuid = str(uuid.uuid4())

    # Destination folder (MCEE likes a .mcworld-like format)
    new_world_path = os.path.join(edu_output_path, f"edu_world_{world_uuid}")
    shutil.copytree(bedrock_world_path, new_world_path)

    # Optionally, rename level name or add a manifest.json if needed
    print(f"✅ Conversion complete. New world located at: {new_world_path}")
    print("📂 You can now import this folder into Minecraft Education Edition.")

# Replace with your actual paths
bedrock_world = r"C:\Users\username\AppData\Local\com.mojang\minecraftWorlds\"
edu_output = r"C:\Users\username\AppData\Local\output"

convert_to_edu(bedrock_world, edu_output)


#save as this doc as and rename file extention as .py instead of .txt (note where it has been saved)
#open Terminal (cmd prompt or PWR shell)
# type cd C:\path to file\ Python convert_world.py
#it will output a folder
#open minecraft edu, click import, find folder location, locate level.dat

