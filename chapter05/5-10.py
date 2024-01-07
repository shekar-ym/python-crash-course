current_users = ['chandra','bhumi','sri','tesla','meera','koppen', 
'john', 'reese']

new_users = ['koppen','meera','ira','Anhad', 'JOHN', 'REESE']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} is in use,please choose a different user name")
    else:
        print(f"{new_user} is available")