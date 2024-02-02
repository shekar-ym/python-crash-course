from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        #Count number of 'the' word in the file.
        # lines = contents.splitlines()
        count =  contents.count('the ')
        print(f"Count of word 'the ' in the file {path} is {count}")


file_names = ['chapter10/siddhartha.txt','chapter10/little_woman.txt']
for file_name in file_names:
    path = Path(file_name)
    count_words(path)