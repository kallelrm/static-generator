import sys
from file import copier
from helpers import generate_page_recursive
def main():
    basepath = sys.argv
    copier('static', 'docs')
    generate_page_recursive("content", "template.html", "docs", basepath)

main()