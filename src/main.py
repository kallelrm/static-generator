from file import copier
from helpers import generate_page_recursive
def main():
    copier('static', 'public')
    generate_page_recursive("content", "template.html", "public")

main()