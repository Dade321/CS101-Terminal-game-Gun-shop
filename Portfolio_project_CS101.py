#Defining main store class
class Store:
    #Starting stock, budget and reputation
    current_stock = [];
    store_budget = 0;
    reputation = 0;
    #Initializing new store
    def __init__(self, store_name) -> None:
        self.store_name =store_name;

#Defining gun supplier class
class Supplier:
    #Defining suppliers initial stock
    supplier_stock = {"Pistol":10, "Shotgun":10, "Machine gun":10, "Sub-machine gun":10, "Hunting knife":10}
    def __init__(self) -> None:
        pass

#Defining Customer class
class Customer:
    def __init__(self, customer_budget, preference, needs) -> None:
        self.customer_budget = customer_budget;
        self.preference = preference;
        self.needs = needs;

#Defining market class
class Market:
    pistol_cost = 200;
    shotgun_cost = 300;
    machine_gun_cost = 1000;
    sub_machine_gun_cost = 700;
    hunting_knife = 100;
    def __init__(self) -> None:
        pass