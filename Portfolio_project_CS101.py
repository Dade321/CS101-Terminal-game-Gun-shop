import os
os.system('cls') 

#Defining main store class
class Store:
    #Starting stock, budget and reputation
    current_stock = {"Pistol":0, "Shotgun":0, "Machine gun":0, "Sub-machine gun":0, "Hunting knife":0};
    store_budget = 2000;
    reputation = 0;
    #Initializing new store
    def __init__(self, store_name) -> None:
        self.store_name =store_name;
    #Defining method for repleneshing stock
    def add_to_stock(self, market_prices) -> None:
        exit_store = 0;
        while exit_store == 0:
            add_to_stock_action = input("(Buy/Exit)?");
            if add_to_stock_action.lower() == "buy":
                print("Your current budget is: " + str(Store.store_budget) + ". What would you like to buy?");
                add_to_stock_buy = input();
                try:
                    gun_cost = market_prices[add_to_stock_buy.capitalize()];
                except Exception:
                    print("Sorry I don't have this gun.")
                else:
                    affordable_amount = int((Store.store_budget - Store.store_budget % gun_cost)/gun_cost);
                    print("One " + str(add_to_stock_buy.capitalize()) + " costs " + str(gun_cost) + ". With your current budget you can buy " + str(affordable_amount) + ". How much do you need?");
                    amount_to_buy = input();
                    try:
                       int(amount_to_buy) + 1;
                    except Exception:
                        print("Enter an amount") ;
                    else:
                        if int(amount_to_buy) > affordable_amount:
                            print("Sorry you can't afford that much.")
                        else:
                            Store.store_budget -= int(amount_to_buy) * gun_cost;
                            Store.current_stock[add_to_stock_buy.capitalize()] += int(amount_to_buy);
                            print("You now have:")
                            for key, value in Store.current_stock.items():
                                print(str(value) + " × " + key)
            elif add_to_stock_action.lower() == "exit":
                while exit_store == 0:
                    exit_store_check = input("Are you sure you want to exit? (y/n)")
                    if exit_store_check.lower() == "y":
                        exit_store = 1;
                        print("See you later, call anytime")
                    elif exit_store_check.lower() == "n":
                        break
                    else:
                        pass       
    #Defining method for checking store name, stock, reputation
    def check_status(self) -> None:
        print("You are a proud owner of a gun store called {name}. Your current budget is {budget}. You currently have these items in stock:".format(name = self.store_name, budget = Store.store_budget))
        for key, value in Store.current_stock.items():
            print(str(value) + " × " + key)
    #Defining method for setting gun prices
    #Defining method for checking store budget, income, profit

#Defining gun supplier class
class Supplier:
    #Defining suppliers initial stock
    supplier_stock = {"Pistol":10, "Shotgun":10, "Machine gun":10, "Sub-machine gun":10, "Hunting knife":10};
    def __init__(self) -> None:
        pass
    #Defining a method for checking stock
    def check_stock(self) -> None:
        for key, value in Supplier.supplier_stock.items():
            print(str(value) + " × " + key + " for " + str(Market.market_prices[key]) + " each")

#Defining Customer class
class Customer:
    def __init__(self, customer_budget, preference, needs) -> None:
        self.customer_budget = customer_budget;
        self.preference = preference;
        self.needs = needs;

#Defining market class
class Market:
    #pistol, shotgun, machine_gun, sub_machine_gun, hunting_knife;
    market_prices = {"Pistol":200.0, "Shotgun":300.0, "Machine gun":1000.0, "Sub-machine gun":700.0, "Hunting knife":100.0};
    def __init__(self) -> None:
        pass
    def change_all_prices(self, change) -> None:
        for key, value in Market.market_prices.items():
            Market.market_prices[key] = value + (value/100*change);

#Intro sequance
print("You stand in front of your new store. You decide you gonna call it:");
store_name = input();
new_store = Store(store_name);
print(store_name + " sounds about right. You step inside. After a quick assesment you realize that everything seems to be in order and ready for bussines altough the stores inventory is completly empty. You call your gun supplier");
gun_supplier = Supplier();
continue_dialog = input("'Enter to continue'");
print("What's up? It's been a while. Whatcha need?");
gun_supplier.check_stock()
continue_dialog = input("'Enter to continue'");
print("Ahh, what the hell. I'll make you a discount, 10% off, for old times sake. Just this time though")
gun_market = Market();
gun_market.change_all_prices(-10);
gun_supplier.check_stock();
new_store.add_to_stock(gun_market.market_prices);
new_store.check_status();
continue_dialog = input("'Enter to continue'");

#Main loop
while True:
    #Defining actions the player can take
    player_action = input("You decide to:\n(Check) shop status, stock\n(Call) supplier\n(Open) shop\n")
    if player_action.lower == "check":
        new_store.check_stock();
    elif player_action.lower == "call":
        new_store.add_to_stock(gun_market.market_prices);
    elif player_action.lower == "open":
        print("You open the shop for today")
    else:
        continue
    break