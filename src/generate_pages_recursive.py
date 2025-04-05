import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path="/"):
    for entry in os.listdir(dir_path_content):
        full_entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(full_entry_path) and entry.endswith(".md"):
            rel_path = os.path.relpath(full_entry_path, "content")
            rel_dir = os.path.dirname(rel_path)
            dest_dir = os.path.join(dest_dir_path, rel_dir)
            dest_path = os.path.join(dest_dir, "index.html")
            generate_page(full_entry_path, template_path, dest_path, base_path)

        elif os.path.isdir(full_entry_path):
            generate_pages_recursive(full_entry_path, template_path, dest_dir_path, base_path)