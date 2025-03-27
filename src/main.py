import os

# Get the absolute path of the project root (one level above src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define absolute paths
static_dir = os.path.join(BASE_DIR, "static")
public_dir = os.path.join(BASE_DIR, "public")

def copy_static(src, dest):
    if not os.path.exists(src):
        print(f"Error: Source directory '{src}' does not exist.")
        return

    print(f"Copying files from {src} to {dest}...")

    # Ensure destination is clean
    if os.path.exists(dest):
        import shutil
        shutil.rmtree(dest)
    
    os.makedirs(dest, exist_ok=True)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            copy_static(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)
            print(f"Copied: {src_path} -> {dest_path}")

def main():
    copy_static(static_dir, public_dir)

if __name__ == "__main__":
    main()