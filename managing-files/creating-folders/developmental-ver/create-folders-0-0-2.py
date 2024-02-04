import os

def get_next_version():
    """Scan the current directory and return the next version to create."""
    existing_versions = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('ver-')]
    if not existing_versions:
        return ('1', '0', '0', 'alpha', '1')  # Return the initial version if none exist
    # This is a simplified example; real logic might need to sort and determine the actual next version
    return ('1', '0', str(len(existing_versions) + 1), 'alpha', '1')

def create_folder(version, label, label_version):
    """Create a folder with the specified versioning and label."""
    folder_name = f"ver-{version}_{label}-{label_version}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

def main():
    version_info = get_next_version()
    create_folder(*version_info)

if __name__ == "__main__":
    main()
