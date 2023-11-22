import random
from abc import ABC, abstractmethod


# Singleton: Car Repair Service

class CarRepairService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._repair_requests = []
        return cls._instance

    def add_repair_request(self, request):
        self._repair_requests.append(request)

    def get_all_requests(self):
        return self._repair_requests





# Factory: Additional Car Services

class AdditionalServiceFactory:
    def create_additional_service(self, service_type):
        if service_type == 'custom_service_1':
            return CustomService1()
        elif service_type == 'custom_service_2':
            return CustomService2()
        else:
            return DefaultAdditionalService()


class CustomService1:
    def execute_service(self):
        print("Executing Custom Service 1")


class CustomService2:
    def execute_service(self):
        print("Executing Custom Service 2")


class DefaultAdditionalService:
    def execute_service(self):
        print("Default Additional Service")


# Existing Services




# Mass Measurement Services
class LB:
    def lb_system(self, new_mass):
        print(f"M: {new_mass} lb")


class KG:
    def kg_system(self, mass):
        print(f"M: {mass} lb")


class KGAdapter(LB):
    def __init__(self, oldsystem):
        self.oldsystem = oldsystem

    def lb_system(self, new_mass):
        self.oldsystem.kg_system(new_mass * 2.205)




# Car Wash Services
class Car:
    def cost(self):
        pass


class Sedan(Car):
    def cost(self):
        return 1500


class Crossover(Car):
    def cost(self):
        return 2200


class WashDecorator(Car):
    def __init__(self, car):
        self.car = car


class FullServiceCarWash(WashDecorator):
    def cost(self):
        return self.car.cost() + 1500


class SelfServiceCarWash(WashDecorator):
    def cost(self):
        return self.car.cost() + 500




# News Notification Services
class Publisher(ABC):
    @abstractmethod
    def register(subscriber):
        pass

    @abstractmethod
    def unregister(subscriber):
        pass

    @abstractmethod
    def notify(subscriber):
        pass


class NewsAgency(Publisher):
    def __init__(self):
        self._subscribers = set()

    def register(self, subscriber):
        self._subscribers.add(subscriber)

    def unregister(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, *args):
        for subscriber in self._subscribers:
            subscriber.update(self, *args)


class Subscriber(ABC):
    @abstractmethod
    def update(publisher, *args):
        pass


class NewsSubscriber(Subscriber):
    def __init__(self, publisher):
        publisher.register(self)

    def update(self, publisher, *args):
        print(f"Subscriber ID: {id(self)} received news: {args}")




# Car Number Service
class CarNumberStrategy(ABC):
    @abstractmethod
    def number(self):
        pass


class VIPNumber1(CarNumberStrategy):
    def number(self):
        return "001, 002, 003, 004, 005, 006, 007, 008, 009, 777 and same letters"


class VIPNumber2(CarNumberStrategy):
    def number(self):
        return "001, 002, 003, 004, 005, 006, 007, 008, 009, 777 and random letters"


class MiddleNumber1(CarNumberStrategy):
    def number(self):
        return "100, 111, 200, 222, 300, 333, 400, 444, 500, 555, 600, 666, 700, 800, 888, 900, 999 and same letters"


class MiddleNumber2(CarNumberStrategy):
    def number(self):
        return "100, 111, 200, 222, 300, 333, 400, 444, 500, 555, 600, 666, 700, 800, 888, 900, 999 and random letters"


class SimpleNumber1(CarNumberStrategy):
    def number(self):
        return "010, 020, 030, 040, 050, 060, 070, 077, 080, 090, 707 and same letters"


class SimpleNumber2(CarNumberStrategy):
    def number(self):
        return "010, 020, 030, 040, 050, 060, 070, 077, 080, 090, 707 and random letters"


class RandomNumber(CarNumberStrategy):
    def number(self):
        return random.randint(1, 999)


class ChooseNumber:
    def choosen_number(self, number_gen=CarNumberStrategy):
        return number_gen.number()



if __name__ == "__main__":
    # Existing services
    masslb = LB()
    masskg = KG()
    kgadapter = KGAdapter(masskg)

    car = Sedan()
    car2 = Crossover()

    vipauto = FullServiceCarWash(car)
    auto_selfserv = SelfServiceCarWash(car)
    vipauto2 = FullServiceCarWash(car2)
    auto_selfserv2 = SelfServiceCarWash(car2)

    NEWS_AGENCY = NewsAgency()
    SUBSCRIBER_A = NewsSubscriber(NEWS_AGENCY)
    SUBSCRIBER_B = NewsSubscriber(NEWS_AGENCY)

    num = ChooseNumber()
    car_num = num.choosen_number(RandomNumber())

    # New services
    repair_service = CarRepairService()
    repair_service.add_repair_request("Engine Repair")
    repair_service.add_repair_request("Brake Check")

    additional_service_factory = AdditionalServiceFactory()
    custom_service_1 = additional_service_factory.create_additional_service('custom_service_1')
    custom_service_2 = additional_service_factory.create_additional_service('custom_service_2')

    # Usage
    print("--- Existing Services ---")
    new_mass_lb = float(input("Enter new mass in lb: "))
    new_mass_kg = float(input("Enter new mass in kg: "))

    masslb.lb_system(new_mass_lb)
    kgadapter.lb_system(new_mass_kg)

    print("FullService Car Wash: T", vipauto.cost())
    print("SelfService Car Wash: T", auto_selfserv.cost())
    print("FullService Car Wash: T", vipauto2.cost())
    print("SelfService Car Wash: T", auto_selfserv2.cost())

    news_input_1 = input("Enter news update A: ")
    news_input_2 = input("Enter news update B: ")
    NEWS_AGENCY.notify(news_input_1, news_input_2)

    car_num_input = input("Enter car number: ")
    print("Selected Car Number:",
          f"kz {car_num_input} {''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3))} 13 ")

    print("--- New Services ---")
    print("Repair Requests:", repair_service.get_all_requests())
    custom_service_1.execute_service()
    custom_service_2.execute_service()