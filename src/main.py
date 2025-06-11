from file import copier
from helpers import generate_page
def main():
    copier('static', 'public')
    generate_page("content/index.md", "template.html", "public/index.html")

main()