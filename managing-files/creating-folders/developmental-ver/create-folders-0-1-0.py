import os

def create_folder(base_path, version, label, label_version):
    """Create a folder with the specified versioning and label at the given base path."""
    folder_name = f"ver-{version}_{label}-{label_version}"
    full_path = os.path.join(base_path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created folder: {full_path}")

def parse_version_input(version_input):
    """Parse the full version input into its components, handling versions without labels."""
    if '_' in version_input:
        version_part, label_part = version_input.split('_')
        label, label_version = label_part.split('-')
    else:
        version_part = version_input
        label, label_version = 'alpha', '0'  # Default label and version if not provided
    major, minor, patch = version_part.replace('ver-', '').split('-')
    return major, minor, patch, label, label_version

def get_next_version(start_version, count):
    """Generate next version numbers based on the starting version and count."""
    major, minor, start_patch, label, start_label_version = parse_version_input(start_version)
    start_patch = int(start_patch)
    start_label_version = int(start_label_version)
    
    for i in range(count):
        yield (major, minor, str(start_patch + i), label, str(start_label_version + i))

def main():
    print("Folder creation script")
    base_path = input("Enter the base path where folders should be created: ")
    start_version = input("Enter the starting version (e.g., 'ver-1-0-0_alpha-1'): ")
    count = int(input("How many folders should be created? "))
    
    for version_info in get_next_version(start_version, count):
        version = '-'.join(version_info[:3])
        create_folder(base_path, version, version_info[3], version_info[4])

if __name__ == "__main__":
    main()
