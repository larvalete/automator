import os

def create_folder(version, label, label_version):
    """Create a folder with the specified versioning and label."""
    folder_name = f"ver-{version}_{label}-{label_version}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

def parse_version_input(version_input):
    """Parse the full version input into its components."""
    version_part, label_part = version_input.split('_')
    major, minor, patch = version_part.split('-')[1:]  # Skip 'ver' prefix
    label, label_version = label_part.split('-')
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
    start_version = input("Enter the starting version (e.g., 'ver-1-0-0_alpha-1'): ")
    count = int(input("How many folders should be created? "))
    
    for version_info in get_next_version(start_version, count):
        version = '-'.join(version_info[:3])
        create_folder(version, version_info[3], version_info[4])

if __name__ == "__main__":
    main()
