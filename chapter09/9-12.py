from adminprivileges import Admin

chandra_user = Admin('chandrashekar', 'y m', 40, 'sydney', 'australia')
chandra_user.describe_user()
chandra_user.privileges.show_privileges()