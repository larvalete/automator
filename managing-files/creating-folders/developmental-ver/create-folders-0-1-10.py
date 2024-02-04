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
    """Parse the version input into major, minor, patch components, handling missing parts."""
    if '_' in version_input:
        version_part, label_part = version_input.split('_')
        label, label_version = label_part.split('-')
    else:
        version_part = version_input
        label, label_version = None, None  # Assume no label if not provided

    # Split the version part and fill in missing values with '0'
    version_components = version_part.replace('ver-', '').split('-')
    while len(version_components) < 3:
        version_components.append('0')  # Default missing components to '0'

    major, minor, patch = version_components[:3]
    return major, minor, patch, label, label_version

def get_next_version(start_version, count):
    major, minor, start_patch, label, start_label_version = parse_version_input(start_version)
    
    # Convert to integers for arithmetic operations
    minor = int(minor)
    versions = []

    for i in range(count):
        # Increment the minor version and reset patch to '0' for each iteration
        if label is None:
            version = f"ver-{major}-{minor + i}-0"
        else:
            # If there's a label, keep the original logic for label version increment
            version = f"ver-{major}-{minor}-{start_patch}"
            label_version = f"{label}-{int(start_label_version) + i}" if start_label_version is not None else None
            versions.append((version, label_version))
            continue

        versions.append((version, None))

    return versions

def main():
    parser = argparse.ArgumentParser(description="Create a series of versioned directories.")
    parser.add_argument('base_path', help="Base path where directories will be created")
    parser.add_argument('start_version', help="Starting version (e.g., 'ver-1-0-0_alpha-1')")
    parser.add_argument('count', type=int, help="Number of directories to create")
    args = parser.parse_args()

    # This function now returns a list of tuples (version, label_version)
    versions = get_next_version(args.start_version, args.count)

    # Loop through each version tuple and create folders accordingly
    for version, label_version in versions:
        create_folder(args.base_path, version, label_version)

if __name__ == "__main__":
    main()
