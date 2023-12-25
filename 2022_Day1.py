def format_list(inventory):
    formatted_inventory = inventory.replace(" ", ",")
    formatted_inventory2 = formatted_inventory.split(",,")
    formatted_inventory3 = []
    for food in formatted_inventory2:
        formatted_inventory3.append(food.split(","))
    full_inventory = [list(map(int, lst)) for lst in formatted_inventory3]
    return full_inventory
    
def calory_count(inventory_list):
    totals = []
    for i in inventory_list:
        totals.append(sum(i))
    totals.sort()
    return totals
   

inventory = input('Copy/paste the elf inventory pls: ')
inventory_list = format_list(inventory)
totals = calory_count(inventory_list)
#print(totals)
#print(f'This is the elf inventory: {inventory_list}')
print(f'The biggest calory count by a single elf is: {totals[-1]}')
print(f'The total calory count of the three calory-richest elves is: {totals[-1] + totals[-2] + totals[-3]}')