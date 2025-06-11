import os
import pathlib
from blocks import *

def extract_title(markdown):
    if markdown[0:2] == "# ":
        return markdown[2: markdown.index('\n')]
    else:
        raise Exception("No h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    md_file = open(from_path)
    md = md_file.read()
    template_file = open(template_path)
    template = template_file.read()

    title = extract_title(md)
    # print("TITLE",title)
    html_string = markdown_to_html_node(md).to_html()
    template = template.replace(r"{{ Title }}", title)
    template = template.replace(r"{{ Content }}", html_string)
    # print(template)
    
    dirname = os.path.dirname(dest_path)
    print("dirname", dirname)
    if dirname not in os.listdir():
        os.makedirs(dirname, exist_ok=True)
    # print(dirname)

    with open(dest_path, "w") as f:
        f.write(template)
        f.close()
    
    md_file.close()
    template_file.close()
    return

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    print(dir_path_content)
    dirs = os.listdir(dir_path_content)
    print("DIRS", dirs)
    if not dirs:
        return
    for entry in dirs:
        print("ENTRY", entry)
        path = os.path.join(dir_path_content, entry)
        print("FORMED PATH", path)
        isFile = os.path.isfile(path)
        print("IS FILE", isFile)
        if not isFile:
            generate_page_recursive(path, template_path, dest_dir_path)
        else:
            generate_page(path, template_path, pathlib.Path(f"{os.path.join(dest_dir_path, path).replace("/content", "").removesuffix(".md")}.html"))
    return
