fav_lang = {
    'chandra': 'rust',
    'varun': 'sql',
    'madhan': 'python',
    'arvind': 'c++'
}

friends = ['chandra','varun','madhan', 'arvind','babu']

for name in friends:
    if name in fav_lang.keys():
        print(f"{name.title()},Thanks for taking the poll")
    else:
        print(f"{name.title()},please take the poll")