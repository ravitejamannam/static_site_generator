import os
import shutil
from generate_page import generate_page

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

    # Generate markdown pages
    content_dir = "content"
    if os.path.exists(content_dir):
        print(f"✅ Generating pages from {content_dir}")
        for root, _, files in os.walk(content_dir):
            for file in files:
                if file.endswith(".md"):
                    from_path = os.path.join(root, file)

                    # Create relative path inside `public/`
                    relative_path = os.path.relpath(root, content_dir)
                    dest_dir = os.path.join("public", relative_path)
                    os.makedirs(dest_dir, exist_ok=True)

                    # Generate the corresponding HTML file
                    dest_path = os.path.join(dest_dir, "index.html")
                    generate_page(from_path, "template.html", dest_path)
    else:
        print(f"❌ Directory {content_dir} not found!")

    print("🎉 Site generation complete!")

if __name__ == "__main__":
    main()