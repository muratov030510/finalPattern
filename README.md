# finalPattern

Overview
This project comprises various car service functionalities implemented using Python. Each service follows different design patterns for modularity, flexibility, and extensibility.

Features
Car Repair Service (Singleton)
Description: Manages repair requests for cars.
Implementation: Utilizes the Singleton pattern to ensure a single instance of the service throughout the application.
Usage: Use CarRepairService to add and retrieve repair requests.
Additional Car Services (Factory)
Description: Creates various additional car services based on specific types.
Implementation: Utilizes the Factory pattern to instantiate different service objects.
Usage: Create additional services such as CustomService1, CustomService2, or default services using AdditionalServiceFactory.
Mass Measurement Services
Description: Allows measurement conversions between pounds (lb) and kilograms (kg).
Implementation: Provides classes LB, KG, and KGAdapter for handling mass conversions.
Usage: Utilize LB for pounds, KG for kilograms, and KGAdapter to adapt kg to lb.
Car Wash Services
Description: Provides cost calculations for different types of car wash services.
Implementation: Includes classes like Sedan, Crossover, and decorators FullServiceCarWash and SelfServiceCarWash.
Usage: Calculate costs using different wash services for sedan and crossover cars.
News Notification Services (Observer)
Description: Notifies subscribers about news updates.
Implementation: Utilizes the Observer pattern with Publisher, NewsAgency, and Subscriber classes.
Usage: Register subscribers, notify about news updates, and handle subscriber updates.
Car Number Service (Strategy)
Description: Generates various car number sequences.
Implementation: Employs the Strategy pattern with CarNumberStrategy and its various concrete strategies.
Usage: Choose different strategies to generate car number sequences.
How to Use
Setup:

Clone the repository: git clone <repository-url>
Navigate to the project directory.
Run:

Execute python filename.py.
Follow the prompts for inputs as required for different services.
Testing:

Modify code for different inputs or add new services as needed.
Ensure proper functionality by testing different scenarios.
Contributors:
Muratov Bakhromkhon
