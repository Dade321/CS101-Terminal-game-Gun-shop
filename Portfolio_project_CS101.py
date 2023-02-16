import os
import random
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
    def add_to_stock(self, market_prices, supplier_stock) -> None:
        exit_store = 0;
        while exit_store == 0:
            print("\nWhaddya need?");
            for key, value in supplier_stock.items():
                print(str(value) + " × " + key + " for " + str(market_prices[key]) + " each");
            add_to_stock_action = input("(Buy/Exit)?");
            if add_to_stock_action.lower() == "buy":
                print("Your current budget is: " + str(Store.store_budget) + ". What would you like to buy?");
                add_to_stock_buy = input();
                try:
                    gun_cost = market_prices[add_to_stock_buy.capitalize()];
                except Exception:
                    print("\nSorry I don't have this gun.")
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
                            print("\nSorry you can't afford that much.")
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
                        print("\nSee you later, call anytime")
                    elif exit_store_check.lower() == "n":
                        break
                    else:
                        pass       
    #Defining method for checking store name, stock, reputation
    def check_status(self) -> None:
        print("\nYou are a proud owner of a gun store called {name}. Your current budget is {budget}. You currently have these items in stock:".format(name = self.store_name, budget = Store.store_budget))
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
    preference_dict = {"Pistol":0.5, "Shotgun":0.5, "Machine gun":0.5, "Sub-machine gun":0.5, "Hunting knife":0.5};
    preference_list = [];
    customer_budget = 1.0;
#    customer_needs  = {"Pistol":0, "Shotgun":0, "Machine gun":0, "Sub-machine gun":0, "Hunting knife":0};
    def __init__(self) -> None:
        pass
    def set_preference(self):
        for key in Customer.preference_dict.keys():
            preference_value = random.uniform(0.0, 1.0);
            Customer.preference_dict[key] = preference_value;
        for key, value in Customer.preference_dict.items():
            Customer.preference_list.append([key, value]);
        Customer.preference_list.sort(key=lambda x: x[1], reverse=True);
    def set_customer_budget(self, market_prices):
        machine_gun_price = market_prices["Machine gun"];
        Customer.customer_budget = machine_gun_price + machine_gun_price/100*random.randint(-50, 50); 
    def express_prefferences(self):
        expression = "Hy, I am looking for a {}. ({}%)\nA {} would work aswell.({}%)\nAnd maybe you have a {} too?({}%)"
        print(expression.format(Customer.preference_list[0][0], int(Customer.preference_list[0][1] * 100), Customer.preference_list[1][0],  int(Customer.preference_list[1][1] * 100), Customer.preference_list[2][0],  int(Customer.preference_list[2][1] * 100)))
        Customer.preference_list = [];
    def check_preference(self, key):
        print("Would you be intereseted in a " + key + "?");
        if Customer.preference_dict[key] >= 0.9:
            print("Sure! That would be great.(" + str(int(Customer.preference_dict[key] *100)) + "%)\n")
        elif Customer.preference_dict[key] < 0.9 and Customer.preference_dict[key] >= 0.6:
            print("Yeah, why not.(" + str(int(Customer.preference_dict[key]) *100) + "%)\n")
        elif Customer.preference_dict[key] < 0.6 and Customer.preference_dict[key] >= 0.3:
            print("Well, might aswell. For a good price(" + str(int(Customer.preference_dict[key] *100)) + "%)\n")
        elif Customer.preference_dict[key] < 0.3:
            print("Not really.(" + str(int(Customer.preference_dict[key] *100)) + "%)\n")


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
print("You stand in front of your new store. You decide you gonna call it:\n");
store_name = input();
new_store = Store(store_name);
print("\n" + store_name + " sounds about right. You step inside. After a quick assesment you realize that everything seems to be in order and ready for bussines altough the stores inventory is completly empty. You call your gun supplier");
gun_supplier = Supplier();
continue_dialog = input("'Enter to continue'");
print("\nWhat's up? It's been a while. Whaddya need?");
gun_supplier.check_stock()
continue_dialog = input("'Enter to continue'");
print("\nAhh, what the hell. I'll make you a discount, 10% off, for old times sake. Just this time though.")
gun_market = Market();
gun_market.change_all_prices(-10);
new_store.add_to_stock(gun_market.market_prices, gun_supplier.supplier_stock);
new_store.check_status();
continue_dialog = input("'Enter to continue'");

day_counter = 0;
#Main loop
while True:
    #Defining actions the player can take
    player_action = input("\nYou decide to:\n(Check) shop status, stock\n(Call) supplier\n(Open) shop\n")
    if player_action.lower() == "check":
        new_store.check_status();
    elif player_action.lower() == "call":
        new_store.add_to_stock(gun_market.market_prices, gun_supplier.supplier_stock);
    elif player_action.lower() == "open":
        print("\nYou open the shop for today");
        continue_dialog = input("'Enter to continue'\n");
        print("You open for bussines and wait for a next customer. It's day " + str(day_counter) + ".")
        while True:
            print("\nA customer walks in.\n")
            next_customer = 0;
            customer_1 = Customer();
            customer_1.set_preference();
            customer_1.set_customer_budget(gun_market.market_prices);
            customer_1.express_prefferences();
            while True:
                if next_customer == 1:
                    break
                print("(Check) if the customer prefers a gun\n(Offer) a gun\nTell the customer that you can't (help) him");
                player_action = input();
                if player_action.lower() == "check":
                    while True:
                        gun_offer = input("Which gun would you like to check with the customer?")
                        gun_offer = gun_offer.capitalize()
                        try:
                            customer_1.preference_dict[gun_offer]
                        except Exception:
                            continue
                        else:
                            customer_1.check_preference(gun_offer)
                            break
                elif player_action.lower() == "offer":
                    while True:
                        pass
                elif player_action.lower() == "help":
                    while True:
                        player_action = input("Are you sure? (y/n)");
                        if player_action.lower() == "y":
                            print("That's fine I'll check the other stores.");
                            next_customer = 1;
                            continue_dialog = input("'Enter to continue'\n");
                            break
                        elif player_action.lower() == "n":
                            break
                        else:
                            continue
                else:
                    continue
    elif player_action.lower() == "quit":
        break
    else:
        continue