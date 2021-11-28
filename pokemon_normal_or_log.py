import matplotlib.pyplot as plt
import helper_functions
import loaddata
import pandas as pd

separator = '---------------------------------------------------------------'
tab: str = "\t"

print(f'{separator + separator}\n')

print(f'{tab * 7}- - - Pokemon Data Analysis - Normal or Log? - - -')
print(f'{tab * 14}Group 18\n')

print(f'{separator + separator}\n')

print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')

print(f'{separator + separator}')

# Is Pokemon data actually normally distributed?
# Normal Probability of pokemon heights

print(f'{separator + separator}\n')
print(f'{tab * 2}Normal and Log Distributions of pokemon heights and weights. '
      f'Are Pokemon heights, and weights normally distributed?\n')

print(f'{separator + separator}\n')

curr_fig = "1"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Distribution of Pokemon Height(m) - - -\n')
print(f'{tab * 4}Same as Figure 11! It is here for easier reference.')
print(helper_functions.basic_stats_string(loaddata.height_stats, "Height(m)"))

helper_functions.plot_hist(loaddata.height, title=f"Figure {curr_fig}: Normal Distribution of Pokemon Height(m)",
                           x_label="Height(m)", y_label="Frequency", bins=100)

plt.show()

print(f'{separator + separator}\n')


curr_fig = "1b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal probability of Pokemon Heights(m) - - -\n')

helper_functions.plot_norm_prob(loaddata.height, y_label='Height(m)',
                                title=f'Figure {curr_fig}: Normal probability of Pokemon Heights(m)')
plt.show()

print(f'{separator + separator}\n')


curr_fig = "1c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal CDF of Pokemon Heights(m) - - -\n')
print(helper_functions.basic_stats_string(loaddata.prob_h_stats, f"Probability(value <= Height(m)))"))

_, _ = helper_functions.plot_cdf(loaddata.height, title=f"Figure {curr_fig}: Normal CDF of Pokemon Heights(m)",
                                 x_label='Height(m)', y_label='prob(value $\leq$ height)')
plt.show()

print(f'{separator + separator}\n')


curr_fig = "2"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal distribution of Pokemon Height(m) - - -\n')
print(helper_functions.basic_stats_string(loaddata.log_h.describe(), "log(Height(m))"))

helper_functions.plot_hist(loaddata.log_h, title=f'Figure {curr_fig}: Log Normal distribution of Pokemon Height(m)',
                           x_label='log(Height(m))', bins=20)
plt.show()

print(f'{separator + separator}\n')


curr_fig = "2b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal probablity plot of Pokemon Height(m) - - -\n')

helper_functions.plot_norm_prob(loaddata.log_h, y_label='log(Height(m))',
                                title=f'Figure {curr_fig}: Log Normal probablity plot of Pokemon Height(m)')
plt.show()

print(f'{separator + separator}\n')


curr_fig = "2c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal CDF of Pokemon Height(m) - - -\n')

_, frequencies = helper_functions.plot_cdf(loaddata.log_h,
                                           title=f"Figure {curr_fig}: Log Normal CDF of Pokemon Height(m)",
                                           x_label='log(Height(m))', y_label='Prob(value $\leq$ log(Height))')
plt.show()

freq_stats = pd.Series(frequencies).describe()
print(helper_functions.basic_stats_string(freq_stats, f"Probability(value <= log(Height(m)))"))

print(f'{separator + separator}\n')

# Plotting weight distribution

curr_fig = "3"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal distribution of Pokemon Weight(kg) - - -\n')
print(helper_functions.basic_stats_string(loaddata.weight_stats, "Weight(kg)"))

helper_functions.plot_hist(loaddata.weight, f"Figure {curr_fig}: Normal distribution of Pokemon Weight(kg)",
                           x_label="Weight(kg)")
plt.show()

print(f'{separator + separator}\n')


curr_fig = "3b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal probablity plot of Pokemon Weight(kg) - - -\n')

helper_functions.plot_norm_prob(loaddata.weight, y_label='Weight(kg)',
                                title=f'Figure {curr_fig}: Normal probablity plot of Pokemon Weight(kg)')
plt.show()

print(f'{separator + separator}\n')


curr_fig = "3c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal CDF of Pokemon Weight(kg) - - -\n')
print(helper_functions.basic_stats_string(loaddata.prob_w_stats, f"Probability(value <= Weight(kg)))"))

_, _ = helper_functions.plot_cdf(loaddata.height,
                                 title=f"Figure {curr_fig}: Normal CDF of Pokemon Weight(kg)",
                                 x_label='Weight(kg)', y_label='prob(value $\leq$ weight)')
plt.show()

print(f'{separator + separator}\n')

curr_fig = "4"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal distribution of Pokemon Weight(kg) - - -\n')
print(helper_functions.basic_stats_string(loaddata.log_w.describe(), "log(Weight(kg))"))

helper_functions.plot_hist(loaddata.log_w, x_label='log(kg)',
                           title=f'Figure {curr_fig}: Log Normal distribution of Pokemon Weight(kg)')
plt.show()

print(f'{separator + separator}\n')


curr_fig = "4b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal probablity plot of Pokemon Weight(kg) - - -\n')

helper_functions.plot_norm_prob(loaddata.log_w, y_label='log(Weight(kg))',
                                title=f'Figure {curr_fig}: Log Normal probablity plot of Pokemon Weight(kg)')
plt.show()

print(f'{separator + separator}\n')


curr_fig = "4c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal CDF of Pokemon Weight(kg) - - -\n')

_, frequencies = helper_functions.plot_cdf(loaddata.log_w, x_label='Weight(kg)', y_label='prob(value $\leq$ weight)',
                                           title=f"Figure {curr_fig}: Log Normal CDF of Pokemon Weight(kg)")

plt.show()

freq_stats = pd.Series(frequencies).describe()
print(helper_functions.basic_stats_string(freq_stats, f"Probability(value <= log(Weight(kg)))"))
