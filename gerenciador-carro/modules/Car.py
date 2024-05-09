from modules.Connection import Connection
from utils.validate_car_informations import validate_informations

class Car:

    def insert_into_db(car_type, car_year, car_doors, car_horsepower):
        if validate_informations(car_type, car_year, car_doors, car_horsepower):
            try:
                cnx = Connection()
                cnx.cursor.execute(f'INSERT INTO cars (car_type, car_year, car_doors, car_horsepower) VALUES("{car_type}",{car_year},{car_doors},{car_horsepower})')
                cnx.connection.commit()
            except ConnectionError:
                print('Erro durante a execução da operação. Tente novamente.')
        else:
            print('Insira informações corretas para poder cadastrar um veículo.')
            raise ValueError
        
    def select_all_cars():
        try:
            cnx = Connection()
            cnx.cursor.execute('SELECT * FROM cars')

            cars_list = cnx.cursor.fetchall()
            
            print('\n')
            
            for car in cars_list:
                print(f'\nIdentificação: {car[0]}\nTipo: {car[1]}\nAno: {car[2]}\nPortas: {car[3]}\nPotência (HP): {car[4]}\n')
                print('----------------------------------------------------')    

        except ConnectionError:
            print('Erro na conexão. Tente novamente.')
    
    def search_car_by_id(id):
        try:
            cnx = Connection()
            cnx.cursor.execute(f'SELECT * FROM cars WHERE idCar = {id}')

            car = cnx.cursor.fetchone()
            print(f'\nIdentificação: {car[0]}\nTipo: {car[1]}\nAno: {car[2]}\nPortas: {car[3]}\nPotência (HP): {car[4]}\n')            

        except ConnectionError:
            print('Erro na conexão. Tente novamente.')