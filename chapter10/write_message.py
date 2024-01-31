from pathlib import Path

contents = 'I am learning programming.\n'
contents += 'I love solving problems.\n'
contents += 'I want to be a good programmer, someday.'

path = Path('programming.txt')
path.write_text(contents)