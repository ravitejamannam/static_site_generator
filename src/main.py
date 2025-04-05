import os
import shutil
from generate_pages_recursive import generate_pages_recursive

def main():
    # Delete public directory if it exists
    if os.path.exists("public"):
        shutil.rmtree("public")

    # Create public directory
    os.makedirs("public", exist_ok=True)

    # Copy static files (including images)
    static_dir = "static"
    public_static_dir = "public"
    if os.path.exists(static_dir):
        print(f"✅ Copying files from {static_dir} to {public_static_dir}")
        shutil.copytree(static_dir, public_static_dir, dirs_exist_ok=True)
    else:
        print(f"❌ Directory {static_dir} not found!")

    # Generate markdown pages recursively
    content_dir = "content"
    if os.path.exists(content_dir):
        print(f"✅ Generating pages recursively from {content_dir}")
        generate_pages_recursive(content_dir, "template.html", "public")
    else:
        print(f"❌ Directory {content_dir} not found!")

    print("🎉 Site generation complete!")

if __name__ == "__main__":
    main()