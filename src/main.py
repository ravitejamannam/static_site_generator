import os
import shutil
import sys
from generate_pages_recursive import generate_pages_recursive

def main():
    # Get basepath from CLI arg or default to "/"
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    # Set output directory
    dest_dir = "docs"

    # Delete output directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    # Create output directory
    os.makedirs(dest_dir, exist_ok=True)

    # Copy static files
    static_dir = "static"
    if os.path.exists(static_dir):
        print(f"✅ Copying static files from {static_dir} to {dest_dir}")
        shutil.copytree(static_dir, dest_dir, dirs_exist_ok=True)
    else:
        print(f"❌ Static directory not found!")

    # Generate markdown pages recursively
    content_dir = "content"
    if os.path.exists(content_dir):
        print(f"✅ Generating pages recursively from {content_dir}")
        generate_pages_recursive(content_dir, "template.html", dest_dir, base_path)
    else:
        print(f"❌ Content directory not found!")

    print("🎉 Site generation complete!")

if __name__ == "__main__":
    main()