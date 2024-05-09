import sqlite3

class Connection:
    
    def __init__(self) -> None:
        self.connection = sqlite3.connect('cars.db')
        self.cursor = self.connection.cursor()
        
    def create_cars_table(self):
        self.connection.execute("""
                                CREATE TABLE IF NOT EXISTS cars (
                                    idCar INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    car_type TEXT NOT NULL CHECK(car_type IN ('sedan', 'suv', 'hatch', 'picape')),
                                    car_year INTEGER NOT NULL,
                                    car_doors INTEGER NOT NULL,
                                    car_horsepower INTEGER NOT NULL
                                )""")