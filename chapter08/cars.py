def make_car(manufacturer, model, **car):
    """Builds a car with manufacturer, model and other add ons"""
    car['manufacturer'] =  manufacturer
    car['model'] =  model
    return car

new_car = make_car('Tesla', 'Model 3', color ='red', FSD=True)
print(new_car)