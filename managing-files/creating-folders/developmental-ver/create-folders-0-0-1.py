import os

def create_folder(version, label, label_version):
    """Create a folder with the specified versioning and label."""
    folder_name = f"ver-{version}_{label}-{label_version}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

def create_folders_from_list(version_details):
    """Create folders from a list of version details."""
    for version_info in version_details:
        major, minor, patch, label, label_version = version_info
        version = f"{major}-{minor}-{patch}"
        create_folder(version, label, label_version)

def main():
    version_details = [
        ('1', '0', '0', 'alpha', '1'),
        ('1', '0', '1', 'beta', '2'),
        # Add more version details as needed
    ]
    create_folders_from_list(version_details)

if __name__ == "__main__":
    main()
