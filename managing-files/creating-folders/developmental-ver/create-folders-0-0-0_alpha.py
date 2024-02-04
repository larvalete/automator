import os

for i in range(10):
    folder_name = f"ver-0-0-0_alpha-{i}"
    os.makedirs(folder_name, exist_ok=True)
