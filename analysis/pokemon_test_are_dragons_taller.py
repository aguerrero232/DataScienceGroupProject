import matplotlib.pyplot as plt
import scipy.stats
import helper_functions
import loaddata


separator = '---------------------------------------------------------------'
tab: str = "\t"
# Do Dragon Type Pokemon tend to be taller than all Pokemon? Non Dragon Type Pokemon?
dh_null_hypothesis = "Dragon Type Pokemon tend to be taller than Non Dragon Type Pokemon."


# ----------------------------------------------------------------------------------
print(f'{separator + separator}')
print(f'{tab * 11}- - - Pokemon Data Analysis - - -')
print(f'{tab * 14}Group 18')
print(f'{separator + separator}\n')
print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')
print(f'{separator + separator}')
print(f'{separator + separator}\n')
print(f'{tab * 3}Do Dragon Type Pokemon tend to be taller than Non Dragon Type Pokemon?\n')
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Dragon Type Pokemon
# Displaying height(m) distribution of all Dragon Type Pokemon
curr_fig = "1"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Height(m) distribution of Dragon Type Pokemon - - -\n')
print(helper_functions.basic_stats_string(loaddata.dragon_type_height.describe(), "Height(m)"))
plt.xlabel('Height(m)')
plt.ylabel('Frequency')
plt.title(f'Figure {curr_fig}: Height(m) distribution of Dragon Type Pokemon')
counts_d = plt.hist(loaddata.dragon_type_height, bins=100)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# PMF for height(m) of all Dragon Pokemon
curr_fig = "1b"
bin_center_d = (counts_d[1][1:] + counts_d[1][:-1]) / 2
dragon_h_pmf = counts_d[0] / len(loaddata.dragon_types)
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of Dragon Type Pokemon - - -\n')
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.title(f'Figure {curr_fig}: PMF: Height(m) of Dragon Type Pokemon')
plt.bar(bin_center_d, dragon_h_pmf, width=.2)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# CDF plot using sort function - Dragon Types
curr_fig = "1c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: CDF: Height(m) of Dragon Type Pokemon - - -\n')
print(helper_functions.basic_stats_string(loaddata.prob_h_d_stats, "Probability ( Height(m) <= x)"))
plt.xlabel('Height(m)')
plt.ylabel('P(height $\leq$ x)')
plt.title(f"Figure {curr_fig}: CDF: Height(m) of Dragon Type Pokemon")
plt.plot(loaddata.dragon_heights_sorted, loaddata.prob_h_d)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# PMF vs CDF of dragon types for 10,20,30 bins
curr_fig = "1d"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF vs CDF Height(m) of Dragon Type Pokemon - - -\n')
plt.xlabel('Height(m)')
plt.ylabel('Probability (Height(m))')
plt.title(f"Figure {curr_fig}: PMF vs CDF Height(m) of Dragon Type Pokemon")
plt.plot(loaddata.bin10_d, loaddata.freq10_d, '-*',
         loaddata.bin20_d, loaddata.freq20_d, ':o',
         loaddata.bin30_d, loaddata.freq30_d, '-.v')
plt.legend(('10 bins', '20 bins', '30 bins'))
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Non Dragon Type Pokemon
# Displaying height(m) distribution of all Non Dragon Type Pokemon
curr_fig = "2"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Height(m) distribution of Non Dragon Type Pokemon - - -\n')
print(helper_functions.basic_stats_string(loaddata.not_dragon_type_height.describe(), "Height(m)"))
plt.xlabel('Height(m)')
plt.ylabel('Frequency')
plt.title(f' Figure {curr_fig}: Height(m) distribution of Non Dragon Type Pokemon')
counts_nd = plt.hist(loaddata.not_dragon_type_height, bins=100)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# PMF for height(m) of all Non Dragon Type Pokemon
curr_fig = "2b"
bin_center_nd = (counts_nd[1][1:] + counts_nd[1][:-1]) / 2
non_dragon_h_pmf = counts_nd[0] / sum(counts_nd[0])
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of Non Dragon Type Pokemon - - -\n')
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.title(f'Figure {curr_fig}: PMF: Height(m) of Non Dragon Type Pokemon')
plt.bar(bin_center_nd, non_dragon_h_pmf, width=.2)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# CDF plot using sort function - Non Dragon Types
curr_fig = "2c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: CDF: Height(m) of Non Dragon Type Pokemon - - -\n')
print(helper_functions.basic_stats_string(loaddata.prob_h_nd_stats, "Probability ( Height(m) <= x)"))
plt.xlabel('Height(m)')
plt.ylabel('P(height $\leq$ x)')
plt.title(f"Figure {curr_fig}: CDF: Height(m) of Non Dragon Type Pokemon")
plt.plot(loaddata.not_dragon_heights_sorted, loaddata.prob_h_nd)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# PMF vs CDF of dragon types for 10,20,30 bins
curr_fig = "2d"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF vs CDF Height(m) of Non Dragon Type Pokemon - - -\n')
plt.xlabel('Height(m)')
plt.ylabel('Probability (Height(m))')
plt.title(f"Figure {curr_fig}: PMF vs CDF Height(m) of Non Dragon Type Pokemon")
plt.plot(loaddata.bin10_nd, loaddata.freq10_nd, '-*',
         loaddata.bin20_nd, loaddata.freq20_nd, ':o',
         loaddata.bin30_nd, loaddata.freq30_nd, '-.v')
plt.legend(('10 bins', '20 bins', '30 bins'))
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# PMF For height of Dragon vs Not Dragon Pokemon
curr_fig = "3"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of Dragon vs Non Dragon Type Pokemon - - -\n')
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.title(f"Figure {curr_fig}: PMF: Height(m) of Dragon vs Non Dragon Type Pokemon")
plt.plot(bin_center_d, counts_d[0] / len(loaddata.dragon_types), '-o',
         bin_center_nd, counts_nd[0] / len(loaddata.not_dragon_type), '-+')
plt.legend(('Dragon Type', 'Not Dragon Type'))
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# t-test going up means more likely to be a Dragon
curr_fig = "4"
d_c_test = counts_d[0] / len(loaddata.dragon_types)
nd_c_test = counts_nd[0] / len(loaddata.not_dragon_type)
t_test_dragon_height = d_c_test - nd_c_test
t_test_dh_t_val = scipy.stats.ttest_ind(d_c_test, nd_c_test)
t_test_dh_statistic_val = t_test_dh_t_val.statistic
t_test_dh_p_val = t_test_dh_t_val.pvalue
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: T-Test: Do Dragon Types tend to be taller than Non Dragon Types - - -\n')
print(f'{tab * 4}T Test Values:')
print(f'{tab * 5}Statistic: {round(t_test_dh_statistic_val, 3)}\n{tab * 5}P Value: {round(t_test_dh_p_val, 3)}\n')
if t_test_dh_p_val > .05:
    print(f"{tab * 4}Accept the null Hypothesis!")
else:
    print(f"{tab * 4}Reject the null Hypothesis!")
print(f"{tab * 5}{dh_null_hypothesis}\n")
plt.xlabel(f'Height(m)')
plt.ylabel(f'P[Dragon] - P[Not Dragon]')
plt.title(f"Figure {curr_fig}: Do Dragon Types tend to be taller than Non Dragon Types")
plt.bar(bin_center_nd, t_test_dragon_height)
plt.show()
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------
