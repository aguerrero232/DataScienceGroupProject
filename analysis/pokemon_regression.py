import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import loaddata
import helper_functions
from sklearn import linear_model


separator = '---------------------------------------------------------------'
tab: str = "\t"


# ----------------------------------------------------------------------------------
print(f'{separator + separator}\n')
print(f'{tab * 7}- - - Pokemon Data Analysis - Pokemon Linear Regression - - -')
print(f'{tab * 14}Group 18\n')
print(f'{separator + separator}\n')
print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')
print(f'{separator + separator}\n')
print(f"{tab*2}Looking at Dragon Type data!\n")
print(f'{separator + separator}\n')
print(helper_functions.data_set_stats(loaddata.dragon_types, "Dragon Type"))
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = "1"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Dragon Type Stat Points - - -\n')
loaddata.dragon_types[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].boxplot()
plt.title(f"Figure {curr_fig}: Dragon Type Stat Point Data")
plt.show()
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = "1b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Dragon Type Stat Point Data (standardized) - - -\n')
loaddata.z_dragons[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].boxplot()
plt.title(f"Figure {curr_fig}: Dragon Type Stat Point Data (standardized)")
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = "1c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Dragon Type Height(m) - - -\n')
loaddata.dragon_types[['height_m']].boxplot()
plt.title(f"Figure {curr_fig}: Dragon Type Height(m)")
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = "1d"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Dragon Type Weight(kg) - - -\n')
loaddata.dragon_types[['weight_kg']].boxplot()
plt.title(f"Figure {curr_fig}: Dragon Type Weight(m)")
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = "1e"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Dragon Type Height(m) and Weight(kg) (standardized) - - -\n')
loaddata.dragon_types[['height_m', 'weight_kg']].boxplot()
plt.title(f"Figure {curr_fig}: Dragon Type Height(m) and Weight(kg)")
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------

