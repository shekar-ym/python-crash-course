from pathlib import Path

def count_words(path):
    """Count approximate number of workds in a file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except:
        print(f"Sorry, the file {path} does not exist")
    else:
        #Count number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has approximately {num_words} words")

# path = Path('/workspaces/python-crash-course/chapter10/alice.txt')

file_names = ["/workspaces/python-crash-course/chapter10/alice.txt", "/workspaces/python-crash-course/chapter10/mobi_dick.txt", "/workspaces/python-crash-course/chapter10/little_woman.txt", "/workspaces/python-crash-course/chapter10/siddhartha.txt"]

for file_name in file_names:
    path = Path(file_name)
    count_words(path)


