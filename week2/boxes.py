import math

quantity=int(input('Enter the number of items: '))

capacity=int(input('Enter the number of items per box: '))

boxes=math.ceil(quantity/capacity)

print(f'For {quantity} items, packing {capacity} items in each box, your will need {boxes} boxes. ')