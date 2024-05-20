# Author   : Anshuman Agarwal
# Email    : anagarwal@umass.edu
# Spire ID : 34157323

def get_protein(order):
    order_list = list(order)
    protein = order_list[3]
    price = 0
    if protein=='chicken':
        price = 2.5
    elif protein=='steak':
        price = 3.5
    elif protein =='barbacoa':
        price = 3.5
    elif protein == "carnitas":
        price = 3
    elif protein == "veggies":
        price = 2.5
    else:
        price = 0
    return price

def get_rice(order):
    order_list2 = list(order)
    rice = order_list2[4]
    price = 0
    if rice == 'white':
        price = 2.5
    elif rice == 'brown':
        price = 3.5
    else:
        price = 0
    return price

def get_beans(order):
    order_list3 = list(order)
    beans = order_list3[5]
    price = 0
    if beans == 'black':
        price = 2.5
    elif beans == 'pinto':
        price = 2.5
    else:
        price = 0
    return price

def get_burrito(order):
    order_list4 = list(order)
    burrito = order_list4[6]
    price = 0
    if burrito:
        price = 2
    else:
        price = 0
    return price

def get_toppings(order):
    order_list5 = list(order)
    protein = order_list5[3]
    price = 0
    free = False
    if protein == 'veggies':
        free = True
    for i in range(7, len(order_list5)):
        if order_list5[i]=='guacamole':
            if free:
                price += 0
            else:
                price += 2.75
        elif order_list5[i]=='fajita veggies':
            if free:
                price += 0
            else:
                price += 2.5
        elif order_list5[i]=='tomato salsa':
            price += 2.5
        elif order_list5[i]=='chili corn salsa':
            price += 1.75
        elif order_list5[i]=='tomatillo green chili salsa':
            price += 2
        elif order_list5[i]=='sour cream':
            price += 2.5
        elif order_list5[i]=='cheese':
            price += 2
        elif order_list5[i]=='queso blanco':
            price += 2.75
        else:
            price += 0
    return price

def apply_discount(order,total_price):
    order_list6 = list(order)
    discount = order_list6[2]
    if discount == 'MAGIC':
        total_price = total_price - (total_price*0.05) 
    elif discount == 'SUNDAYFUNDAY':
        total_price = total_price - (total_price*0.10)
    elif discount == 'FLAT3':
        total_price = total_price - 3
    return total_price

def approximate_time(order):
    order_list7 = list(order)
    location = order_list7[1]
    time = 0
    if location == 'amherst':
        time = 15
    elif location == 'north amherst':
        time = 15
    elif location == 'south amherst':
        time = 15
    elif location == 'hadley':
        time = 15
    elif location == 'northampton':
        time = 30
    elif location == 'south hadley':
        time = 30
    elif location == 'belchertown':
        time = 30
    elif location == 'sunderland':
        time = 30
    elif location == 'holyoke':
        time = 45
    elif location == 'greenfield':
        time = 45
    elif location == 'deerfield':
        time = 45
    elif location == 'springfield':
        time = 45
    return time

def generate_invoice(order):
    order_list8 = list(order)
    toppings_list = []
    for i in range(7,len(order_list8)):
        toppings_list.append(order_list8[i])
    
    if order_list8[6]:
        burrito = 'Yes'
    else:
        burrito = 'No'
    
    subtotal = get_protein(order)+get_rice(order)+get_beans(order)+get_burrito(order)+get_toppings(order)
    money_saved = subtotal - (apply_discount(order,subtotal))

    print (f'Welcome to Chipotle Mexican Grill Hadley, {order_list8[0]}.')
    print('Your invoice is displayed below:')
    print(f'Protein: {order_list8[3]} - ${get_protein(order)}')
    print(f'Rice: {order_list8[4]} rice - ${get_rice(order)}')
    print(f'Beans: {order_list8[5]} beans - ${get_beans(order)}')
    print(f'Burrito: {burrito} - ${get_burrito(order)}')
    print(f'Toppings: {", ".join(toppings_list)} - ${get_toppings(order)}')
    print(f'Subtotal: ${subtotal}')
    print(f'Discount Code: {order_list8[2]}')
    print(f'Total: ${apply_discount(order,subtotal)}')
    print(f'You Save: ${money_saved}')
    print(f'Your order will be ready in {approximate_time(order)} minutes.')
    print('Enjoy your meal and have a good day!')


order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')
#print(get_protein(order1))
#print(get_protein(order2))
#print(get_rice(order1))
#print(get_rice(order2))
#print(get_beans(order1))
#print(get_beans(order2))
#print(get_burrito(order1))
#print(get_burrito(order2))
#print(get_toppings(order1))
#print(get_toppings(order2))
#print(apply_discount(order1, 17.25))
#print(apply_discount(order2, 23.25))
#print(approximate_time(order1))
#print(approximate_time(order2))
#generate_invoice(order1)
#generate_invoice(order2)