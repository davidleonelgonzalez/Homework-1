import math

height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
wall_area = width * height
print('Wall area:', wall_area, 'square feet')

paint_color = {'red': 35, 'blue': 25, 'green': 25}


paint_needed = wall_area / 350
cans_needed = math.ceil(paint_needed)

print('Paint needed: {:.2f} gallons'.format(paint_needed))
print('Cans needed:', str(cans_needed), 'can(s)\n')

color_of_paint = input('Choose a color to paint the wall:\n')

paint_cost = cans_needed * paint_color[color_of_paint.lower()]
print('Cost of purchasing', str(color_of_paint), 'paint: $'+str(paint_cost))
