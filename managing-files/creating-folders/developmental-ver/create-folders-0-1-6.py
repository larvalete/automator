import os
import argparse

def create_folder(base_path, base_version, label, start_label_version, count):
    """Create folders with incremented label versions."""
    for i in range(count):
        folder_name = f"{base_version}_{label}-{start_label_version + i}"
        full_path = os.path.join(base_path, folder_name)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created folder: {full_path}")

def parse_version_input(version_input):
    """Parse the full version input into its components, handling versions without labels."""
    if '_' in version_input:
        version_part, label_part = version_input.split('_')
    else:
        # Default label and version if not provided
        version_part = version_input
        label_part = "alpha-0"  # Default label and label version
    major, minor, patch = version_part.replace('ver-', '').split('-')
    label, label_version = label_part.split('-')
    return major, minor, patch, label, int(label_version)


def main():
    parser = argparse.ArgumentParser(description="Create a series of versioned directories.")
    parser.add_argument('base_path', help="Base path where directories will be created")
    parser.add_argument('start_version', help="Starting version (e.g., 'ver-1-0-0_alpha-1')")
    parser.add_argument('count', type=int, help="Number of directories to create")
    args = parser.parse_args()

    major, minor, patch, label, start_label_version = parse_version_input(args.start_version)
    base_version = f"ver-{major}-{minor}-{patch}"

    create_folder(args.base_path, base_version, label, start_label_version, args.count)

if __name__ == "__main__":
    main()
