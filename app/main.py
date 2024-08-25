from typing import Any


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> Any:
        result = 0
        for car in cars_list:
            if car.clean_mark is None:
                result += 0
            elif car.clean_mark < self.clean_power:
                result += self.wash_single_car(car.clean_mark,
                                               car.comfort_class)
                car.clean_mark = self.clean_power
        return result

    def calculate_washing_price(self, car: Car) -> Any:
        calculate = 0
        if car.clean_mark < self.clean_power:
            calculate = (car.comfort_class
                         * (self.clean_power - car.clean_mark)
                         * self.average_rating
                         / self.distance_from_city_center)
        return round(calculate, 1)

    def wash_single_car(self, car_mark: int, car_class: int) -> Any:
        calculate = 0
        if car_mark < self.clean_power:
            calculate = (car_class * (self.clean_power - car_mark)
                         * self.average_rating
                         / self.distance_from_city_center)
        return round(calculate, 1)

    def rate_service(self, mark: int) -> Any:
        self.count_of_ratings += 1
        result = (((self.average_rating * (self.count_of_ratings - 1)) + mark)
                  / self.count_of_ratings)
        self.average_rating = round(result, 1)
        return self.average_rating
