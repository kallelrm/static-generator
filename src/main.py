import sys
from file import copier
from helpers import generate_page_recursive
def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/' 
    print(basepath)
    copier('static', 'docs')
    generate_page_recursive("content", "template.html", "docs", basepath)

main()