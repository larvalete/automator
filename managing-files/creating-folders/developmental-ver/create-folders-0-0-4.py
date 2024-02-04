import os

def create_folder(version, label, label_version):
    """Create a folder with the specified versioning and label."""
    folder_name = f"ver-{version}_{label}-{label_version}"
    confirmation = input(f"Do you want to create the folder '{folder_name}'? (y/n): ")
    if confirmation.lower() == 'y':
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created folder: {folder_name}")
    else:
        print("Folder creation canceled.")

def get_next_version():
    """Scan the current directory and return the next version to create."""
    existing_versions = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('ver-')]
    if not existing_versions:
        return ('1', '0', '0', 'alpha', '1')
    # This logic assumes incremental versioning and may need adjustment for your use case
    latest_version = sorted(existing_versions)[-1]
    major, minor, patch = latest_version.split('_')[0].replace('ver-', '').split('-')
    new_patch = str(int(patch) + 1)
    return (major, minor, new_patch, 'alpha', '1')

def main():
    version_info = get_next_version()
    version = '-'.join(version_info[:3])
    label = version_info[3]
    label_version = version_info[4]
    create_folder(version, label, label_version)

if __name__ == "__main__":
    main()
