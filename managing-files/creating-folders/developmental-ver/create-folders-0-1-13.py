import os
import argparse

def create_folder(base_path, version, label_version):
    if label_version:
        folder_name = f"{version}_{label_version}"
    else:
        folder_name = version
    full_path = os.path.join(base_path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created folder: {full_path}")

def parse_version_input(version_input):
    """Parse the version input into major, minor, patch components, and label info."""
    label, label_version = None, None
    version_components = ['0', '0', '0']  # Defaults
    
    if '_' in version_input:
        version_part, label_part = version_input.split('_')
        label, label_version = label_part.split('-')
        version_components = version_part.replace('ver-', '').split('-')
    else:
        version_components = version_input.replace('ver-', '').split('-')

    while len(version_components) < 3:
        version_components.append('0')
    
    major, minor, patch = version_components[:3]

    return major, minor, patch, label, label_version

def get_next_version(start_version, count):
    major, minor, patch, label, label_version = parse_version_input(start_version)
    versions = []
    
    major, minor, patch = int(major), int(minor), int(patch)
    label_version = int(label_version) if label_version is not None else 0

    for i in range(count):
        if label is not None:
            # Handle labeled version increment
            new_version = f"ver-{major}-{minor}-{patch}_alpha-{label_version + i}"
        elif len(start_version.split('-')) == 2:
            # Increment major version if input was like 'ver-0'
            new_version = f"ver-{major + i}-0-0"
        else:
            # Default behavior: increment patch version
            new_version = f"ver-{major}-{minor}-{patch + i}"
        
        versions.append(new_version)

    return versions

def main():
    parser = argparse.ArgumentParser(description="Create a series of versioned directories.")
    parser.add_argument('base_path', help="Base path where directories will be created")
    parser.add_argument('start_version', help="Starting version (e.g., 'ver-1-0-0_alpha-1')")
    parser.add_argument('count', type=int, help="Number of directories to create")
    args = parser.parse_args()

    versions = get_next_version(args.start_version, args.count)
    
    for version in versions:
        create_folder(args.base_path, version, None)

if __name__ == "__main__":
    main()
