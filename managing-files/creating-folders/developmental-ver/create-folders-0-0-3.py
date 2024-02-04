import os

def create_folder(version, label, label_version):
    """Create a folder with the specified versioning and label."""
    folder_name = f"ver-{version}_{label}-{label_version}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

def get_next_version():
    """Scan the current directory and return the next version to create."""
    existing_versions = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('ver-')]
    if not existing_versions:
        return ('1', '0', '0', 'alpha', '1')  # Return the initial version if none exist
    # Simplified logic for example purposes
    return ('1', '0', str(len(existing_versions) + 1), 'alpha', '1')

def main():
    version_info = get_next_version()
    # Combine the first three elements into a single version string
    version = '-'.join(version_info[:3])
    label = version_info[3]
    label_version = version_info[4]
    create_folder(version, label, label_version)

if __name__ == "__main__":
    main()
