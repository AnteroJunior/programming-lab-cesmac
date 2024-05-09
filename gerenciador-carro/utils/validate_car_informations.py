def validate_informations(car_type, car_year, car_doors, car_horsepower):
    is_valid = True

    if(car_type not in ['suv', 'picape', 'hatch', 'sedan'] or 
        car_year < 1950 or (car_doors <= 0 or car_doors > 4) or car_horsepower <= 0):
        is_valid = False
    
    return is_valid