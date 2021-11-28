import matplotlib.pyplot as plt
import loaddata

separator = '---------------------------------------------------------------'
tab: str = "\t"

print(f'{separator + separator}\n')

print(f'{tab * 7}- - - Pokemon Data Analysis - Pokemon Linear Regression - - -')
print(f'{tab * 14}Group 18\n')

print(f'{separator + separator}\n')

print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')

print(f'{separator + separator}')

print(f"{tab*2}Looking at Dragon Type data!")

curr_fig = "1"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: - - -\n')

loaddata.dragon_types[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].boxplot()
plt.show()

print(f'{separator + separator}\n')

curr_fig = "1b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: - - -\n')

loaddata.dragon_types[['height_m', 'weight_kg']].boxplot()
plt.show()

print(f'{separator + separator}\n')


curr_fig = "1c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: - - -\n')

loaddata.dragon_types[['height_m']].boxplot()
plt.show()

print(f'{separator + separator}\n')
