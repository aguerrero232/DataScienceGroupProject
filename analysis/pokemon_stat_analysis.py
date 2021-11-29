import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import helper_functions
import loaddata


separator = '---------------------------------------------------------------'
tab: str = "\t"


def stat_analysis(stat_name, stat_values, z_stat_values, stat_value_stats, z_stat_value_stats):
    # ----------------------------------------------------------------------------------
    print(f'{separator + separator}\n')
    print(f'{tab * 10}- - - Pokemon Data Analysis - {stat_name} Stat Analysis - - -')
    print(f'{tab * 12}Group 18')
    print(f'{separator + separator}\n')
    print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
          f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
          f'{tab * 14}Thank you!\n')
    print(f'{separator + separator}')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # plotting bell curve for pokemon stat distribution
    curr_fig = "1"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: {stat_name} Stat Distribution - - -\n')
    print(helper_functions.basic_stats_string(stat_value_stats, stat_name))
    helper_functions.plot_hist(stat_values, f"Figure {curr_fig}: {stat_name} Stat Distribution", stat_name,
                               'frequency', 'blue', 'red', False)
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # plotting stat dist. (standardized)
    curr_fig = "1b"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: {stat_name} Stat Distribution (standardized) - - -\n')
    print(helper_functions.basic_stats_string(z_stat_value_stats, f"Z {stat_name}"))
    helper_functions.plot_hist(z_stat_values, f"Figure {curr_fig}: {stat_name} Stat Distribution (standardized)",
                               F'Z {stat_name}', 'frequency', 'blue', 'red', True)
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # Population Stat distribution standardized plot
    curr_fig = "2"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: Population raw {stat_name} value against standardized score - - -\n')
    print(helper_functions.corr_compute(stat_values, z_stat_values, f"{stat_name}", f"Z {stat_name}"))
    plt.xlabel(f'{stat_name}')
    plt.ylabel('Z-score (unit-less)')
    plt.title(f'Figure 2: Population raw {stat_name} value against standardized score')
    plt.scatter(stat_values, z_stat_values)
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # --- three groups of pokemon attack stats ----------------------------------------------
    stat_measures = pd.DataFrame(np.random.choice(stat_values, (300, 3), replace=True))

    g1_stats = stat_measures[0].describe()
    g2_stats = stat_measures[1].describe()
    g3_stats = stat_measures[2].describe()

    # --- SEM for 3 groups of pokemon stats  ->  std / sqrt(len(group))
    stat_sem = np.std(stat_measures, 0) / math.sqrt(stat_measures.shape[0])
    # --- 95% Confidence Interval ----------------------------------------------------------
    stat_ci95 = stat_sem * 1.96
    # ---------------------------------------------------------------------------------------

    # --- samples --------------------------------------------------------------------------------------
    stat_sample = np.random.choice(stat_values, (loaddata.sample_size, loaddata.repeat_n), replace=True)
    stat_sample_mean = pd.DataFrame(stat_sample).describe().loc['mean']  # getting mean of each col
    # ---------------------------------------------------------------------------------------------------

    # --- samples stats -----------------------------------
    stat_sample_stats = stat_sample_mean.describe()
    # sample zscore and stats
    z_stat_sample = helper_functions.z_score(stat_sample_mean)
    z_stat_sample_stats = z_stat_sample.describe()
    # ------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # plotting sample Pokemon attack distribution
    curr_fig = "3"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: Sample Pokemon {stat_name} Distribution - - -\n')
    print(f'{tab * 4}Sample size = {loaddata.sample_size}, Repeated {loaddata.repeat_n}x\n')
    print(helper_functions.basic_stats_string(stat_sample_stats, stat_name))
    helper_functions.plot_hist(stat_sample_mean, f'Figure {curr_fig}: Sample Pokemon {stat_name} Distribution',
                               f'{stat_name}', 'frequency', 'blue', 'red', False)
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # Plotting sample attack distribution (standardized)
    curr_fig = "3b"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: Sample Pokemon {stat_name} Distribution (standardized) - - -\n')
    print(f'{tab * 4}Sample Size = {loaddata.sample_size}, Repeated {loaddata.repeat_n}x\n')
    print(helper_functions.basic_stats_string(z_stat_sample_stats, f"Z {stat_name}"))

    helper_functions.plot_hist(z_stat_sample, x_label=f'Z {stat_name}', y_label='frequency',
                               title=f"Figure {curr_fig}: Sample Pokemon {stat_name} Distribution (standardized)",
                               c='blue', tc='red', is_z_score=True)
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # Sample Attack against standardized plot
    curr_fig = "4"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: Sample Raw {stat_name} value against standardized score - - -\n')
    print(f'{tab * 4}Sample Size = {loaddata.sample_size}, Repeated {loaddata.repeat_n}x\n')
    print(helper_functions.corr_compute(stat_sample_mean, z_stat_sample, f"{stat_name}", f"Z {stat_name}"))
    plt.xlabel(f'{stat_name}')
    plt.ylabel('Z-score (unit-less)')
    plt.title(f'Figure {curr_fig}: Sample Raw {stat_name} value against standardized score')
    plt.scatter(stat_sample_mean, z_stat_sample)
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # Mean and standard error of the mean of Atk stat for three groups of data
    curr_fig = "5"
    sem_str = ""
    for x in range(len(stat_sem)):
        sem_str += f"{tab * 5}Group #{x + 1}: {round(stat_sem[x], 2)}\n"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: Mean and SEM {stat_name} stat for three groups of Pokemon - - -\n')
    print(f'{tab * 4}Sample size per group = {stat_measures.shape[0]}\n')
    print(f'{tab * 4}Standard Error of the Mean:')
    print(sem_str)
    print(f"{tab * 9}- - - {stat_name} Stats By Group - - -\n")
    print(helper_functions.basic_stats_string(g1_stats, f"{stat_name} (group 1)"))
    print(helper_functions.basic_stats_string(g2_stats, f"{stat_name} (group 2)"))
    print(helper_functions.basic_stats_string(g3_stats, f"{stat_name} (group 3)"))
    plt.xlabel('Sample group')
    plt.ylabel(f'Mean $\pm$ SEM ({stat_name.lower()})')
    plt.title(f'Figure {curr_fig}: Mean and SEM {stat_name} stat for three groups of Pokemon')
    plt.errorbar([1, 2, 3], np.mean(stat_measures, 0), stat_sem)
    plt.xticks([1, 2, 3])
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # calculating 95% Confidence interval for mean selected stats
    curr_fig = "5b"
    ci_95_str = ""
    for x in range(len(stat_sem)):
        ci_95_str += f"{tab * 5}Group #{x + 1}: {round(stat_ci95[x], 2)}\n"
    print(f'{separator + separator}\n')
    print(f'{tab * 6}- - - Figure {curr_fig}: 95% Confidence Interval {stat_name} stat in mean '
          f'of 3 groups of Pokemon - - -\n')
    print(f'{tab * 4}Sample size per group = {stat_measures.shape[0]}\n')
    print(f'{tab * 4}95% Confidence Interval {stat_name} stat for mean of 3 groups:')
    print(ci_95_str)
    plt.xlabel('Sample Groups')
    plt.ylabel(f'Mean, SEM, & 95% CI ({stat_name})')
    plt.title(f"Figure {curr_fig}: 95% Confidence Interval for {stat_name} stat.")
    plt.errorbar([1.05, 2.05, 3.05], np.mean(stat_measures, 0), stat_sem)
    plt.errorbar([1, 2, 3], np.mean(stat_measures, 0), stat_ci95)
    plt.legend(('SEM', '95% CI'), loc=2)
    plt.xticks([1, 2, 3])
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------
    return
