#David Gonzalez
#1630338
lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
serving = float(input('How many servings does this make?\n'))
print()
print('Lemonade ingredients - yields %.2f servings'%(serving))
print('%.2f cup(s) lemon juice'%(lemon_juice))
print('%.2f cup(s) water'%(water))
print('%.2f cup(s) agave nectar\n'%(agave_nectar))

num_serving = float(input('How many servings would you like to make?\n'))
print()
lemon_juice_cups1 = lemon_juice / serving
water_cups1 = water / serving
agave_nectar_cups1 = agave_nectar / serving

lemon_juice_needed = lemon_juice_cups1 * num_serving
water_needed = water_cups1 * num_serving
agave_nectar_needed = agave_nectar_cups1 * num_serving

print('Lemonade ingredients - yields %.2f servings'%(num_serving))
print('%.2f cup(s) lemon juice'%(lemon_juice_needed))
print('%.2f cup(s) water'%(water_needed))
print('%.2f cup(s) agave nectar'%(agave_nectar_needed))
print()
print('Lemonade ingredients - yields', str('{:.2f}'.format(num_serving)), 'servings')
print(str('{:.2f}'.format(lemon_juice_needed / 16)), 'gallon(s) lemon juice')
print(str('{:.2f}'.format(water_needed / 16)), 'gallon(s) water')
print(str('{:.2f}'.format(agave_nectar_needed / 16)),'gallon(s) agave nectar')
