import os

def create_folder(version, alpha_version):
    """Create a folder with the specified versioning and alpha version."""
    folder_name = f"ver-{version}_alpha-{alpha_version}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"Created folder: {folder_name}")

def main():
    print("Enter the version details for the folder:")
    major = input("Major version (e.g., 1 for '1' in ver-1-0-0): ")
    minor = input("Minor version (e.g., 0 for '0' in ver-1-0-0): ")
    patch = input("Patch version (e.g., 0 for '0' in ver-1-0-0): ")
    alpha = input("Alpha version (e.g., 0 for '0' in _alpha-0): ")
    
    version = f"{major}-{minor}-{patch}"
    create_folder(version, alpha)

if __name__ == "__main__":
    main()
