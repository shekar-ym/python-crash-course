from restaurant import Restaurant

fav_restaurant = Restaurant('mtr','South Indian')
fav_restaurant.describe_restaurant()

fav_restaurant.number_served = 4500
fav_restaurant.describe_restaurant()

fav_restaurant.set_number_served(5000)
fav_restaurant.describe_restaurant()