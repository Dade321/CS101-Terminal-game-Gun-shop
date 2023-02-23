import os
import random
os.system('cls') 

#Additional functions
def linear_interpolation(x1, x2, y1, y2, x):
    return y1 - abs(x1-x)*abs(y1-y2)/abs(x1-x2)

#Main classess

class Store:
    #Starting stock, budget
    current_stock = {"Pistol":3, "Shotgun":1, "Machine gun":0, "Sub-machine gun":0, "Hunting knife":3};
    store_budget = 1000;

    #Initializing class
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


class Supplier:
    #Defining suppliers initial stock
    supplier_stock = {"Pistol":10, "Shotgun":10, "Machine gun":10, "Sub-machine gun":10, "Hunting knife":10};

    #Initializing class
    def __init__(self) -> None:
        pass
    
    #Defining a method for checking stock
    def check_stock(self) -> None:
        for key, value in Supplier.supplier_stock.items():
            print(str(value) + " × " + key + " for " + str(Market.market_prices[key]) + " each")


class Customer:
    #Customers preference dictionary and lists, items which sale is being attempted price dictionary and chance of sale dictionary with discount as a key and customers budget
    preference_dict = {"Pistol":0.5, "Shotgun":0.5, "Machine gun":0.5, "Sub-machine gun":0.5, "Hunting knife":0.5};
    preference_list = [];
    altered_price_dict = {-50:0, -40:0, -30:0, -20:0, -10:0, 0:0, 10:0, 20:0, 30:0, 40:0, 50:0};
    chance_of_sale_dict = {-50:0, -40:0, -30:0, -20:0, -10:0, 0:0, 10:0, 20:0, 30:0, 40:0, 50:0};
    customer_budget = 1.0;

    #Initializes class
    def __init__(self) -> None:
        pass

    #Sets customers prference(percentage from 0 to 100), stores them in a preference dictionary and in a sorted preference list
    def set_preference(self) -> None:
        Customer.preference_list = [];
        for key in Customer.preference_dict.keys():
            preference_value = random.uniform(0.0, 1.0);
            Customer.preference_dict[key] = preference_value;
        for key, value in Customer.preference_dict.items():
            Customer.preference_list.append([key, value]);
        Customer.preference_list.sort(key=lambda x: x[1], reverse=True);
    
    #Sets customer budget. Budget is set by taking a Machine guns price and adding percentage from -50 to 50
    def set_customer_budget(self, market_prices) -> None:
        machine_gun_price = market_prices["Machine gun"];
        Customer.customer_budget = int(machine_gun_price + machine_gun_price/100*random.randint(-50, 50)); 
    
    #Prints customers preferences
    def express_prefferences(self) -> None:
        expression = "\nI am looking for a {}. ({}%)\nA {} would work aswell.({}%)\nAnd maybe you have a {} too?({}%)"
        print(expression.format(Customer.preference_list[0][0], int(Customer.preference_list[0][1] * 100), Customer.preference_list[1][0],  int(Customer.preference_list[1][1] * 100), Customer.preference_list[2][0],  int(Customer.preference_list[2][1] * 100)))
        print("Customers budget " + str(Customer.customer_budget))
    
    #Method for checking customers preference for a particular item.
    def check_preference(self, key) -> None:
        print("\nWould you be intereseted in a " + key + "?");
        if Customer.preference_dict[key] >= 0.9:
            percentage = str(int(Customer.preference_dict[key]*100))
            print("Sure! That would be great.(" + percentage + "%)\n")
            #print(Customer.preference_dict[key]*100)
        elif Customer.preference_dict[key] < 0.9 and Customer.preference_dict[key] >= 0.6:
            percentage = str(int(Customer.preference_dict[key]*100))
            print("Yeah, why not.(" + percentage + "%)\n")
            #print(Customer.preference_dict[key]*100)
        elif Customer.preference_dict[key] < 0.6 and Customer.preference_dict[key] >= 0.3:
            percentage = str(int(Customer.preference_dict[key]*100))
            print("Well, might aswell. For a good price(" + percentage + "%)\n")
            #print(Customer.preference_dict[key] *100)
        elif Customer.preference_dict[key] < 0.3:
            percentage = str(int(Customer.preference_dict[key]*100))
            print("Not really.(" + percentage + "%)\n")
            #print(Customer.preference_dict[key]*100)

    #Calculates a chance of sale and prints it
    def check_chance_of_sale(self, market_prices, key) -> None:
        market_price = market_prices[key];
        chance_of_sale_p20 = Customer.preference_dict[key] * 100;
        price_change = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50];
        lowest_change = price_change[0];
        chance_of_sale = [chance_of_sale_p20 + 50, 1, 2, 3, 4, 5, 6, chance_of_sale_p20, 8, 9, chance_of_sale_p20 - 50];
        for index in chance_of_sale[1:7]:
            chance_of_sale[index] = linear_interpolation(-50, 20, chance_of_sale[0], chance_of_sale[7], price_change[index]);
        for index in chance_of_sale[8:10]:
            chance_of_sale[index] = linear_interpolation(20, 50, chance_of_sale[7], chance_of_sale[10], price_change[index]);
        for chance in chance_of_sale:
            if lowest_change != 0:
                altered_price = int(market_price + market_price/100*lowest_change);
                Customer.altered_price_dict[lowest_change] = altered_price;
                Customer.chance_of_sale_dict[lowest_change] = int(chance);
                print("Offer " + str(lowest_change) + "%. For a price of " + str(altered_price) + ".(" + str(int(chance)) + "%)" );
                lowest_change += 10;
            else:
                Customer.altered_price_dict[lowest_change] = int(market_price);
                Customer.chance_of_sale_dict[lowest_change] = int(chance);
                print("Offer " + str(lowest_change) + "%. For a price of " + str(int(market_price)) + ".(" + str(int(chance)) + ")" );
                lowest_change += 10;
    
    #Checks if a sale attempt was successful, transfers credits from customer to a store and substracts any sold weapons from stores stock 
    def attempt_sale(self, gun, price, chance_of_sale) -> None:
        print("\nYou offer a " + gun + " for " + str(price));
        print("The customer checks his budget and thinks a bit")
        input("'Enter to continue'");
        random_number = random.random() * 100;
        if random_number <= chance_of_sale and Customer.customer_budget >= price:
            print("\nSounds like a deal!\n")
            Customer.customer_budget -= price;
            Store.store_budget += price;
            Store.current_stock[gun] -= 1;
            Customer.preference_dict[gun] = 0.0;
            Customer.preference_list = []
            for key, value in Customer.preference_dict.items():
                Customer.preference_list.append([key, value]);
            Customer.preference_list.sort(key=lambda x: x[1], reverse=True);
        elif random_number <= chance_of_sale:
            print("\nSounds great, but I am afraid I can't afford it. Would you agree on " + str(Customer.customer_budget) + "? (y/n)")
            while True:
                player_response = input()
                if player_response.lower() == "y":
                    Customer.customer_budget = 0;
                    Store.store_budget += Customer.customer_budget;
                    Store.current_stock[gun] -= 1;
                    print("Great! Thanks a lot")
                    break
                elif player_response.lower() == "n":
                    print("Oh well.\n")
                    break
                else:
                    continue
        else:
            print("That won't work for me\n")
            Customer.preference_dict[gun] = Customer.preference_dict[gun]/4;
            Customer.preference_list = []
            for key, value in Customer.preference_dict.items():
                Customer.preference_list.append([key, value]);
            Customer.preference_list.sort(key=lambda x: x[1], reverse=True);


class Market:
    #pistol, shotgun, machine_gun, sub_machine_gun, hunting_knife;
    base_market_prices = {"Pistol":200.0, "Shotgun":300.0, "Machine gun":1000.0, "Sub-machine gun":700.0, "Hunting knife":100.0};
    market_prices = {"Pistol":200.0, "Shotgun":300.0, "Machine gun":1000.0, "Sub-machine gun":700.0, "Hunting knife":100.0};

    #Initialize class
    def __init__(self) -> None:
        pass

    #Change all gun prices by a set percentage
    def change_all_prices(self, change) -> None:
        for key, value in Market.market_prices.items():
            Market.market_prices[key] = value + (value/100*change);
    
    #Alter all gun prices by a random percentage after each day
    def alter_prices(self) -> None:
        for key, value in Market.base_market_prices.items():
            Market.market_prices[key] = int(value + (value/100*random.randint(-20, 20)));
    
    #Prints current market prices
    def check_prices(self) -> None:
        print("")
        for key, value in Market.market_prices.items():
            print(str(key) + "- " + str(value))

#Intro sequance
print("You stand in front of your new store. You decide you gonna call it:\n");
store_name = input();
customer_1 = Customer();
new_store = Store(store_name);
new_store.check_status();
print("\n" + store_name + " sounds about right. You step inside. After a quick assesment you realize that everything seems to be in order and ready for bussiness altough the stores inventory seems a little empty. You call your gun supplier");
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

day_counter = 1;
alter_prices = 1;
#Main loop
while True:
    customer_count = 0;
    if alter_prices == 1:
        gun_market.alter_prices()
        alter_prices = 0
    print("\nYou still have some time today")
    #Defining actions the player can take
    player_action = input("\nYou decide to:\n(Check) shop status, stock\n(Call) supplier\nGo home and (Open) shop in the morning\n")
    if player_action.lower() == "check":
        new_store.check_status();
    elif player_action.lower() == "call":
        new_store.add_to_stock(gun_market.market_prices, gun_supplier.supplier_stock);
    elif player_action.lower() == "open":
        print("\nYou return in the morning and open for bussines. It's day " + str(day_counter) + ".")
        day_counter += 1;
        alter_prices = 1;
        continue_dialog = input("'Enter to continue'\n");
        while True:
            if customer_count == 3:
                print("It seems there won't be anymore customers today, you decide to close shop")
                break
            print("\nA customer walks in.")
            customer_count += 1;
            next_customer = 0;
            customer_1.set_preference();
            customer_1.set_customer_budget(gun_market.market_prices);
            while True:
                go_back = 0;
                if next_customer == 1:
                    print("\nYou wait for another customer")
                    continue_dialog = input("'Enter to continue'\n");
                    break
                customer_1.express_prefferences();
                print("\nYou decide to:\nCheck stores current (stock)\nCheck current market (prices)\n(Check) if the customer preffers a gun\n(Offer) a gun\nTell the customer that you can't help him and wait for a (next) customer");
                player_action = input();
                if player_action.lower() == "check":
                    while True:
                        gun_check = input("\nWhich gun would you like to check with the customer?")
                        gun_check = gun_check.capitalize()
                        try:
                            customer_1.preference_dict[gun_check]
                        except Exception:
                            continue
                        else:
                            customer_1.check_preference(gun_check)
                            break
                elif player_action.lower() == "stock":
                    new_store.check_status();
                elif player_action.lower() == "prices":
                    gun_market.check_prices()
                elif player_action.lower() == "offer":
                    while True:
                        if go_back == 1:
                            break
                        gun_offer = input("\nWhich gun would you like to offer to the customer?")
                        gun_offer = gun_offer.capitalize()
                        if gun_offer not in new_store.current_stock or new_store.current_stock[gun_offer] == 0:
                            print("You don't have this item in stock")
                            break
                        try:
                            customer_1.preference_dict[gun_offer]
                        except Exception:
                            continue
                        else:

                            while True:
                                print("The current market price for this gun: " + str(int(gun_market.market_prices[gun_offer])) + ".")
                                print("How much would you like to alter the price?")
                                customer_1.check_chance_of_sale(gun_market.market_prices, gun_offer)
                                print("\nYou decide to:\nAttempt a sale(choose price change)\nOffer a (different) gun\nGo (back)");
                                player_action = input();
                                try:
                                    int(player_action);
                                except ValueError:
                                    if player_action.lower() == "different":
                                        break
                                    elif player_action.lower() == "back":
                                        go_back = 1;
                                        break
                                    else:
                                        continue
                                else:
                                    if int(player_action) in customer_1.altered_price_dict:
                                        customer_1.attempt_sale(gun_offer, customer_1.altered_price_dict[int(player_action)], customer_1.chance_of_sale_dict[int(player_action)])
                                    if customer_1.customer_budget == 0:
                                        print("Looks like am all out of cash. Thanks again.")
                                        next_customer = 1
                                        go_back = 1
                                        break
                                    go_back = 1
                                    break

                elif player_action.lower() == "next":
                    while True:
                        player_action = input("\nAre you sure? (y/n)");
                        if player_action.lower() == "y":
                            print("That's fine I'll check the other stores.");
                            print("Customer walks out of the store")
                            next_customer = 1;
                            continue_dialog = input("'Enter to continue'");
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