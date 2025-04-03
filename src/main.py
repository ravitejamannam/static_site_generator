# src/main.py
import os
import shutil
from generate_page import generate_page

def main():
    # Delete anything in the public directory
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    # Create public directory
    os.makedirs("public", exist_ok=True)
    
    # Copy all static files from static to public
    if os.path.exists("static"):
        for item in os.listdir("static"):
            src = os.path.join("static", item)
            dst = os.path.join("public", item)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
    
    # Generate page from content/index.md
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()