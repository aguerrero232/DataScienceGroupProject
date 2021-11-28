import matplotlib.pyplot as plt
import helper_functions
import loaddata


separator = '---------------------------------------------------------------'
tab: str = "\t"


# ----------------------------------------------------------------------------------
print(f'{separator + separator}\n')
print(f'{tab * 7}- - - Pokemon Data Analysis - Finding Correlations - - -')
print(f'{tab * 12}Group 18')
print(f'{separator + separator}\n')
print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')
print(f'{separator + separator}')
# finding a correlation between hp and weight, speed and weight, height and weight, speed and hp, etc....
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between hp and weight
curr_fig = "1"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Hp and Weight(kg) - - -\n')
print(helper_functions.corr_compute(loaddata.hp, loaddata.weight, "Hp", "Weight(kg)"))
plt.xlabel('HP')
plt.ylabel('Weight(kg)')
plt.title(f"Figure {curr_fig}: Correlation between Hp and Weight(kg)")
plt.scatter(loaddata.hp, loaddata.weight)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between hp and weight (standardized)
curr_fig = "1b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Hp and Weight(kg) (standardized) - - -\n')
print(helper_functions.corr_compute(loaddata.z_hp, loaddata.z_weight, "Z Hp", "Z Weight(kg)", "(standardized)"))
plt.xlabel('Z HP')
plt.ylabel('Z Weight(kg)')
plt.title(f'Figure {curr_fig}: Correlation between Hp and Weight(kg) (standardized)')
plt.scatter(loaddata.z_hp, loaddata.z_weight)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between speed and weight
curr_fig = "2"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Weight(kg) - - -\n')
print(helper_functions.corr_compute(loaddata.speed, loaddata.weight, "Speed", "Weight(kg)"))
plt.xlabel('Speed')
plt.ylabel('Weight(kg)')
plt.title(f'Figure {curr_fig}: Correlation between Speed and Weight(kg)')
plt.scatter(loaddata.speed, loaddata.weight)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between speed and weight (standardized)
curr_fig = '2b'
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Weight(kg) (standardized) - - -\n')
print(helper_functions.corr_compute(loaddata.z_speed, loaddata.z_weight, "Z Speed", "Z Weight(kg)", "(standardized)"))
plt.xlabel('Z Speed')
plt.ylabel('Z Weight(kg)')
plt.title(f'Figure {curr_fig}: Correlation between Speed and Weight(kg) (standardized)')
plt.scatter(loaddata.z_speed, loaddata.z_weight)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between speed and hp
curr_fig = "3"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Hp - - -\n')
print(helper_functions.corr_compute(loaddata.speed, loaddata.hp, "Speed", "Hp"))
plt.xlabel('Speed')
plt.ylabel('HP')
plt.title(f"Figure {curr_fig}: Correlation between Speed and Hp")
plt.scatter(loaddata.speed, loaddata.hp)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between speed and hp (standardized)
curr_fig = "3b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Hp (standardized) - - -\n')
print(helper_functions.corr_compute(loaddata.z_speed, loaddata.z_hp, "Z Speed", "Z Hp", "(standardized)"))
plt.xlabel('Z Speed')
plt.ylabel('Z HP')
plt.title(f"Figure {curr_fig}: Correlation between Speed and Hp (standardized)")
plt.scatter(loaddata.z_speed, loaddata.z_hp)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between attack and special attack
curr_fig = "4"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Attack and Special Attack - - -\n')
print(helper_functions.corr_compute(loaddata.attack, loaddata.sp_attack, "Attack", "Special Attack"))
plt.xlabel('Atack')
plt.ylabel('Special Attack')
plt.title(f"Figure {curr_fig}: Correlation between Attack and Special Attack")
plt.scatter(loaddata.attack, loaddata.sp_attack)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between attack and special attack (standardized)
curr_fig = "4b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Attack and Special Attack (standardized) - - -\n')
print(helper_functions.corr_compute(loaddata.z_attack, loaddata.z_sp_attack, "Z Attack", "Z Special Attack", "(standardized)"))
plt.xlabel('Z Atack')
plt.ylabel('Z Special Attack')
plt.title(f"Figure {curr_fig}: Correlation between Attack and Special Attack (standardized)")
plt.scatter(loaddata.z_attack, loaddata.z_sp_attack)
plt.show()
# Calculating Correlation between Pokemon Height(m) and Weight(kg). (normal and log normal)
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Correlation between height and weight
curr_fig = "5"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Height(m) and Weight(kg) - - -\n')
print(helper_functions.corr_compute(loaddata.height, loaddata.weight, "Height(m)", "Weight(kg)"))
plt.xlabel('Height(m)')
plt.ylabel('Weight(kg)')
plt.title(f"Figure {curr_fig}: Correlation between Height(m) and Weight(kg)")
plt.scatter(loaddata.height, loaddata.weight)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = "5b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Height(m) and Weight(kg) (standardized) - - -\n')
print(helper_functions.corr_compute(loaddata.z_height, loaddata.z_weight, "Z Height", "Z Weight(kg)", "(standardized)"))
plt.xlabel('Z Height(m)')
plt.ylabel('Z Weight(kg)')
plt.title(f"Figure {curr_fig}: Correlation between Height(m) and Weight(kg) (standardized)")
plt.scatter(loaddata.z_height, loaddata.z_weight)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = "5c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between log(Height(m)) and Weight(kg) - - -\n')
print(helper_functions.corr_compute(loaddata.log_h, loaddata.weight, "log(Height(m))", "Weight(kg)"))
plt.xlabel('log(Height(m))')
plt.ylabel('Weight(kg)')
plt.title(f"Figure {curr_fig}: Correlation between log(Height(m)) and Weight(kg)")
plt.scatter(loaddata.log_h, loaddata.weight)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
curr_fig = '5d'
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between log(Height(m)) and log(Weight(kg)) - - -\n')
print(helper_functions.corr_compute(loaddata.log_h, loaddata.log_w, "log(Height(m))", "log(Weight(kg))"))
plt.xlabel('log(Height(m))')
plt.ylabel('log(Weight(kg))')
plt.title(f"Figure {curr_fig}: Correlation between log(Height(m)) and log(Weight(kg))")
plt.scatter(loaddata.log_h, loaddata.log_w)
plt.show()
print(f'{separator + separator}\n')
