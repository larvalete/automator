import os

def create_folder(version, label, label_version):
    """Create a folder with the specified versioning and label."""
    folder_name = f"ver-{version}_{label}-{label_version}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

def get_next_version(start_patch, label, label_version, count):
    """Generate next version numbers based on the starting patch and count."""
    for i in range(count):
        yield ('1', '0', str(start_patch + i), label, str(label_version + i))

def main():
    print("Folder creation script")
    start_patch = int(input("Enter the starting patch version: "))
    label = input("Enter version label (e.g., 'alpha', 'beta', 'rc'): ")
    label_version = int(input(f"Enter starting {label} version number: "))
    count = int(input("How many folders should be created? "))
    
    for version_info in get_next_version(start_patch, label, label_version, count):
        version = '-'.join(version_info[:3])
        create_folder(version, version_info[3], version_info[4])

if __name__ == "__main__":
    main()
