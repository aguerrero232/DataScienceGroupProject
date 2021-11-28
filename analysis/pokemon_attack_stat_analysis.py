import numpy as np
import matplotlib.pyplot as plt
import helper_functions
import loaddata

separator = '---------------------------------------------------------------'
tab: str = "\t"

print(f'{separator + separator}\n')

print(f'{tab * 10}- - - Pokemon Data Analysis - Attack Stat Analysis - - -')
print(f'{tab * 12}Group 18')

print(f'{separator + separator}\n')

print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')

print(f'{separator + separator}')

# plotting bell curve for pokemon attack distribution
curr_fig = "1"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Attack Stat Distribution - - -\n')

print(helper_functions.basic_stats_string(loaddata.attack_stats, "Attack"))

# plotting population mean
helper_functions.plot_hist(loaddata.attack, f"Figure {curr_fig}: Attack Stat Distribution", 'attack stat', 'frequency', 'blue', 'red', False)
plt.show()

print(f'{separator + separator}\n')


# plotting population mean (standardized)

curr_fig = "1b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Attack Stat Distribution (standardized) - - -\n')

print(helper_functions.basic_stats_string(loaddata.z_attack_stats, "Z Attack"))

helper_functions.plot_hist(loaddata.z_attack, f"Figure {curr_fig}: Attack Stat Distribution (standardized)",
                           'attack stat (Z Score)', 'frequency', 'blue', 'red', True)
plt.show()

print(f'{separator + separator}\n')


# Population Attack distribution standardized plot

curr_fig = "2"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Population raw attack value against standardized score - - -\n')

print(helper_functions.corr_compute(loaddata.attack, loaddata.z_attack, "Attack", "Z Attack"))

plt.xlabel('Attack (atk)')
plt.ylabel('Z-score (unit-less)')
plt.title('Figure 2: Population raw attack value against standardized score')
plt.scatter(loaddata.attack, loaddata.z_attack)
plt.show()

print(f'{separator + separator}\n')


# plotting sample Pokemon attack distribution

curr_fig = "3"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Sample Pokemon Attack Distribution - - -\n')
print(f'{tab * 4}Sample size = {loaddata.sample_size}, Repeated {loaddata.repeat_n}x\n')

print(helper_functions.basic_stats_string(loaddata.sample_attack_stats, "Attack"))

helper_functions.plot_hist(loaddata.sample_attack_mean, f'Figure {curr_fig}: Sample Pokemon Attack Distribution',
                           'attack', 'frequency', 'blue', 'red', False)
plt.show()

print(f'{separator + separator}\n')


# Plotting sample attack distribution (standardized)

curr_fig = "3b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Sample Pokemon Attack Distribution (standardized) - - -\n')
print(f'{tab * 4}Sample Size = {loaddata.sample_size}, Repeated {loaddata.repeat_n}x\n')

print(helper_functions.basic_stats_string(loaddata.z_attack_stats_s, "Z Attack"))

helper_functions.plot_hist(loaddata.z_attack_s, x_label='Z Attack', y_label='frequency',
                           title=f"Figure {curr_fig}: Sample Pokemon Attack Distribution (standardized)",
                           c='blue', tc='red', is_z_score=True)
plt.show()

print(f'{separator + separator}\n')

# Sample Attack against standardized plot

curr_fig = "4"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Sample Raw Attack value against standardized score - - -\n')
print(f'{tab * 4}Sample Size = {loaddata.sample_size}, Repeated {loaddata.repeat_n}x\n')

print(helper_functions.corr_compute(loaddata.sample_attack_mean, loaddata.z_attack_s, "Attack", "Z Attack"))

plt.xlabel('Attack (atk)')
plt.ylabel('Z-score (unit-less)')
plt.title(f'Figure {curr_fig}: Sample Raw Attack value against standardized score')
plt.scatter(loaddata.sample_attack_mean, loaddata.z_attack_s)
plt.show()

print(f'{separator + separator}\n')


# Mean and standard error of the mean of Atk stat for three groups of data

curr_fig = "5"

sem_str = ""
for x in range(len(loaddata.SEM_attack)):
    sem_str += f"{tab * 5}Group #{x + 1}: {round(loaddata.SEM_attack[x], 2)}\n"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Mean and SEM Atk stat for three groups of Pokemon - - -\n')
print(f'{tab * 4}Sample size per group = {loaddata.measures_attack.shape[0]}\n')

print(f'{tab * 4}Standard Error of the Mean:')
print(sem_str)

print(f"{tab * 9}- - - Attack Stats By Group - - -\n")
print(helper_functions.basic_stats_string(loaddata.g1_stats, "Attack (group 1)"))
print(helper_functions.basic_stats_string(loaddata.g2_stats, "Attack (group 2)"))
print(helper_functions.basic_stats_string(loaddata.g3_stats, "Attack (group 3)"))

plt.xlabel('Sample group')
plt.ylabel('Mean $\pm$ SEM (atk)')
plt.title(f'Figure {curr_fig}: Mean and SEM Atk stat for three groups of Pokemon')
plt.errorbar([1, 2, 3], np.mean(loaddata.measures_attack, 0), loaddata.SEM_attack)
plt.xticks([1, 2, 3])
plt.show()

print(f'{separator + separator}\n')


# calculating 95% Confidence interval for mean attack stats

curr_fig = "5b"

ci_95_str = ""
for x in range(len(loaddata.SEM_attack)):
    ci_95_str += f"{tab * 5}Group #{x + 1}: {round(loaddata.ci95_attack[x], 2)}\n"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: 95% Confidence Interval Attack stat for mean of 3 groups of Pokemon - - -\n')
print(f'{tab * 4}Sample size per group = {loaddata.measures_attack.shape[0]}\n')

print(f'{tab * 4}95% Confidence Interval Attack stat for mean of 3 groups:')
print(ci_95_str)

plt.xlabel('Sample Groups')
plt.ylabel('Mean and confidence interval (atk)')
plt.title(f"Figure {curr_fig}: 95% Confidence Interval")
plt.errorbar([1.05, 2.05, 3.05], np.mean(loaddata.measures_attack, 0), loaddata.SEM_attack)
plt.errorbar([1, 2, 3], np.mean(loaddata.measures_attack, 0), loaddata.ci95_attack)
plt.legend(('SEM', '95% CI'), loc=2)
plt.xticks([1, 2, 3])
plt.show()

print(f'{separator + separator}\n')
