
def cost_daily_summary(the_file):
    """Imputting file from Records^"""

    for line in the_file:
        """Remove | from lines to create string list"""
        words = line.split('|')
        """Assign variables to strings in list"""
        melon = words[0] 
        quantity = words[1]
        quantity = int(quantity)
        cost = words[2]
        cost = float(cost)
        """ Using Quantity of melons and multiplying cost of each for total price"""
        total_cost = (quantity * cost)
        print(f'Delivered {quantity} {melon} for total of ${total_cost}')

# print('Day 1')
# cost_daily_summary(open("um-deliveries-day-1.txt"))
print('Day 2')
cost_daily_summary(open("um-deliveries-day-2.txt"))
# print('Day 3')
# cost_daily_summary(open("um-deliveries-day-3.txt"))



