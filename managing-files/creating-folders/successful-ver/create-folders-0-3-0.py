import os
import argparse

def create_folder(base_path, version_with_label):
    """Create a folder for the specified version and label version."""
    full_path = os.path.join(base_path, version_with_label)
    os.makedirs(full_path, exist_ok=True)
    print(f"Created folder: {full_path}")

def parse_version_input(version_input):
    """Parse the version input into major, minor, patch components, and label info."""
    # Initialize default values
    label, label_version = None, None
    version_components = ['0', '0', '0']  # Defaults for major, minor, patch
    
    if '_' in version_input:
        version_part, label_part = version_input.split('_')
        label, label_version = label_part.split('-')
        version_components = version_part.replace('ver-', '').split('-')
    else:
        version_components = version_input.replace('ver-', '').split('-')

    # Ensure there are always three components
    while len(version_components) < 3:
        version_components.append('0')
    
    major, minor, patch = version_components[:3]
    return major, minor, patch, label, label_version

def get_next_version(prefix, start_version, count):
    """Generate next versions based on the start version and count, including a prefix."""
    major, minor, patch, label, start_label_version = parse_version_input(start_version)
    versions = []
    
    # Ensure prefix ends with an underscore for readability, if not empty
    formatted_prefix = f"{prefix}_" if prefix else ""
    
    # Convert label_version to integer if present
    start_label_version = int(start_label_version) if start_label_version is not None else 0
    
    if label:  # If there's a label, increment label version
        for i in range(count):
            version_with_label = f"{formatted_prefix}ver-{major}-{minor}-{patch}_{label}-{start_label_version + i}"
            versions.append(version_with_label)
    else:
        # Handle cases without a label by incrementing the appropriate version component
        for i in range(count):
            new_version = f"{formatted_prefix}ver-{major}-{int(minor) + i}-0"  # Increment minor version
            versions.append(new_version)

    return versions

def main():
    """Main function to parse arguments and create folders."""
    parser = argparse.ArgumentParser(description="Create a series of versioned directories.")
    parser.add_argument('base_path', help="Base path where directories will be created")
    parser.add_argument('prefix', help="Prefix to prepend before the version (e.g., 'pos-abs')")
    parser.add_argument('start_version', help="Starting version (e.g., 'ver-1-0-0_alpha-1')")
    parser.add_argument('count', type=int, help="Number of directories to create")
    args = parser.parse_args()

    versions = get_next_version(args.prefix, args.start_version, args.count)
    
    for version_with_label in versions:
        create_folder(args.base_path, version_with_label)

if __name__ == "__main__":
    main()
