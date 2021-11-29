import numpy as np
import scipy.stats
import loaddata

separator = '---------------------------------------------------------------'
tab: str = "\t"


def less_than_high(stat_values, mean, std_dev, test_high, set_name, stat_name, set_type, unit=''):
    # how many Pokemon VALs are less than high_val?
    high = (test_high - mean) / std_dev
    p = scipy.stats.norm.cdf(high)
    expected = p * len(stat_values)
    observed = (stat_values < test_high).sum()

    print(f"{tab * 4}How many {set_type}{set_name} {stat_name} are less than {test_high}{unit}?\n")
    print(f'{tab * 5}# expected: {round(expected)}/{len(stat_values)}')
    print(f'{tab * 5}# observed: {observed}/{len(stat_values)}')
    print(f'{tab * 5}-->: {round((100 * p), 2)}%')
    print("\n")


def more_than_low(stat_values, mean, std_dev, test_low, set_name, stat_name, set_type, unit=''):
    # How many VALs are greater than low_val?
    low = (test_low - mean) / std_dev
    p = 1 - scipy.stats.norm.cdf(low)
    expected = p * len(stat_values)
    observed = (stat_values > test_low).sum()
    print(f"{tab * 4}How many {set_type}{set_name} {stat_name} are more than {test_low}{unit}?\n")
    print(f'{tab * 5}# expected: {round(expected)}/{len(stat_values)}')
    print(f'{tab * 5}# observed: {observed}/{len(stat_values)}')
    print(f'{tab * 5}-->: {round((100 * p), 2)}%')
    print("\n")


def between_low_and_high(stat_values, mean, std_dev, test_low, test_high, set_name, stat_name, set_type, unit=''):
    # How many VALs are between low_val and high_val ?
    # get z score of desired values
    low = (test_low - mean) / std_dev
    high = (test_high - mean) / std_dev
    p = scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low)
    expected = p * len(stat_values)
    observed = ((stat_values < test_high) & (stat_values > test_low)).sum()

    print(f"{tab * 4}How many {set_type}{set_name} {stat_name} are between {test_low}{unit} and {test_high}{unit}?\n")
    print(f'{tab * 5}# expected: {round(expected)}/{len(stat_values)}')
    print(f'{tab * 5}# observed: {observed}/{len(stat_values)}')
    print(f'{tab * 5}-->: {round((100 * p), 2)}%')
    print("\n")


def run_normal_dist_vs_actual(stat_values, stat_stats, test_bounds=(0, 50), set_name='Pokemon', stat_name='', unit='',
                              modifier='', set_type=''):
    # ----------------------------------------------------------------------------------
    print(f'{separator + separator}\n')
    print(
        f'{tab * 4}- - - Pokemon Data Analysis - Normal Distribution and Verification with real data {modifier} - - -\n')
    print(f'{tab * 14}Group 18\n')
    print(f'{separator + separator}\n')
    print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
          f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
          f'{tab * 14}Thank you!\n')
    print(f'{separator + separator}\n')
    # Using standard normal distribution for quick probability estimation for all pokemon heights (m) and weights (kg)
    print(f'{separator + separator}\n')
    print(
        f"\n{tab * 3}Using standard normal distribution for quick probability estimation of {set_type}{set_name} {stat_name}{unit} {modifier}\n")
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    mean = stat_stats.loc['mean']
    std_dev = stat_stats['std']

    for stuff in range(0, 3):
        low, high = round(np.random.uniform(test_bounds[0], test_bounds[1] / 3), 2), round(
            np.random.uniform((test_bounds[1] / 3), test_bounds[1]), 2)
        less_than_high(stat_values, mean, std_dev, high, set_name, stat_name, set_type, unit)
        more_than_low(stat_values, mean, std_dev, low, set_name, stat_name, set_type, unit)
        between_low_and_high(stat_values, mean, std_dev, low, high, set_name, stat_name, set_type, unit)

    print(f'{separator + separator}\n')
    return
