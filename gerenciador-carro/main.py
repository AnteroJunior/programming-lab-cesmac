from utils.show_menu import main_menu
from modules.Car import Car
from modules.Connection import Connection

def main():

    while True:
        main_menu()
        try:
            user_option = int(input('Informe a opção desejada: '))
            
            match user_option:
                case 1:
                    try:
                        print('\nVocê selecionou cadastro de carro. Vamos lá!\n')
                        car_type = input('Tipo do carro [suv, hatch, picape, sedan]: ')
                        car_year = int(input('Ano do carro: '))
                        car_doors = int(input('Quantidade de portas: '))
                        car_horsepower = int(input('Potência do carro (hp): '))

                        Car.insert_into_db(car_type, car_year, car_doors, car_horsepower)

                    except ValueError:
                        print('Por favor, informe valores válidos.')
                case 2:
                    Car.select_all_cars()
                case 3:
                    user_option = int(input('Informe a identificação do carro: '))
                    Car.search_car_by_id(user_option)
                case 4:
                    break

        except KeyboardInterrupt:
            print('Por favor, informe uma opção NUMÉRICA! Sistema parando.')


Connection().create_cars_table()
main()