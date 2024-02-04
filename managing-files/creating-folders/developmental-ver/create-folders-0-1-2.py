import os
import argparse

def create_folder(base_path, version, label, label_version):
    folder_name = f"ver-{version}_{label}-{label_version}"
    full_path = os.path.join(base_path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created folder: {full_path}")

def parse_version_input(version_input):
    parts = version_input.split('_')
    version_part = parts[0]
    label_part = parts[1] if len(parts) > 1 else "alpha-0"
    major, minor, patch = version_part.replace('ver-', '').split('-')
    label, label_version = label_part.split('-')
    return major, minor, patch, label, label_version

def get_next_version(start_version, count):
    major, minor, start_patch, label, start_label_version = parse_version_input(start_version)
    start_patch = int(start_patch)
    start_label_version = int(start_label_version)
    for i in range(count):
        yield (major, minor, str(start_patch + i), label, str(start_label_version + i))

def main():
    parser = argparse.ArgumentParser(description="Create a series of versioned directories.")
    parser.add_argument('base_path', help="Base path where directories will be created")
    parser.add_argument('start_version', help="Starting version (e.g., 'ver-1-0-0_alpha-1')")
    parser.add_argument('count', type=int, help="Number of directories to create")
    args = parser.parse_args()

    for version_info in get_next_version(args.start_version, args.count):
        version = '-'.join(version_info[:3])
        create_folder(args.base_path, version, version_info[3], version_info[4])

if __name__ == "__main__":
    main()
