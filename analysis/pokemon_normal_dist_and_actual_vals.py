import scipy.stats
import loaddata


separator = '---------------------------------------------------------------'
tab: str = "\t"


# ----------------------------------------------------------------------------------
print(f'{separator + separator}\n')
print(f'{tab * 4}- - - Pokemon Data Analysis - Normal Distribution and Verification with real data - - -\n')
print(f'{tab * 14}Group 18\n')
print(f'{separator + separator}\n')
print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')
print(f'{separator + separator}\n')
# Using standard normal distribution for quick probability estimation for all pokemon heights (m) and weights (kg)
print(f'{separator + separator}\n')
print(f"\n{tab * 2}Using standard normal distribution for quick probability estimation for all pokemon Heights(m) and "
      f"Weights(kg).\n")
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# how many Pokemon heights are less than 7 meters
test_high = 7
high = (test_high - loaddata.mean_h) / loaddata.std_dev_h
p = scipy.stats.norm.cdf(high)
expected = p * len(loaddata.height)
observed = (loaddata.height < 7).sum()

print(f"{tab * 4}how many Pokemon heights are less than 7 meters\n")
print(f'{tab * 5}# expected: {round(expected)}/{len(loaddata.height)}')
print(f'{tab * 5}# observed: {observed}/{len(loaddata.height)}')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# How many heights are between 1.27 and 5.5 meters?
test_low = 1.27
test_high = 5.5
# get z score of desired heights
low = (test_low - loaddata.mean_h) / loaddata.std_dev_h
high = (test_high - loaddata.mean_h) / loaddata.std_dev_h
p = scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low)
expected = p * len(loaddata.height)
observed = ((loaddata.height < 5.5) & (loaddata.height > 1.27)).sum()
print(f"{tab * 4}How many Pokemon are between 1.27 and 5.5 meters?\n")
print(f'{tab * 5}# expected: {round(expected)}/{len(loaddata.height)}')
print(f'{tab * 5}# observed: {observed}/{len(loaddata.height)}')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# How many heights are greater than 2 meters?
test_low = 2
low = (test_low - loaddata.mean_h) / loaddata.std_dev_h
p = 1 - scipy.stats.norm.cdf(low)
expected = p * len(loaddata.height)
observed = (loaddata.height > 2).sum()
print(f"{tab * 4}How many Pokemon are taller than than 2 meters?\n")
print(f'{tab * 5}# expected: {round(expected)}/{len(loaddata.height)}')
print(f'{tab * 5}# observed: {observed}/{len(loaddata.height)}')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# What percentage of the Pokemon population is between 1 and 2 meters?
test_high = 2
test_low = 1
high = (test_high - loaddata.mean_h) / loaddata.std_dev_h
low = (test_low - loaddata.mean_h) / loaddata.std_dev_h
p = scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low)
print(f"{tab * 4}What percentage of the Pokemon population is between {test_low} and {test_high} meters?\n")
print(f'{tab * 5}-->: {round((100 * p), 2)}%')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# What percentage of the Pokemon population is heavier than 50kg?
test_low = 50
low = (test_low - loaddata.mean_w) / loaddata.std_dev_w
p = 1 - scipy.stats.norm.cdf(low)
print(f"{tab * 4}What percentage of the Pokemon population is heavier than  {test_low}kg?\n")
print(f'{tab * 5}-->: {round((100 * p), 2)}%')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# what percentage of the Pokemon population is heavier than 100kg?
test_low = 100
# more accurate estimate than just regular min and max
low = (test_low - loaddata.mean_w) / loaddata.std_dev_w
p = 1 - scipy.stats.norm.cdf(low)
print(f"{tab * 4}What percentage of the Pokemon population is heavier than {test_low}kg?\n")
print(f'{tab * 5}-->: {round((100 * p), 2)}%')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Verifying estimations with real data
print(f'{separator + separator}\n')
print(f"{tab * 10}Verifying estimations with real data\n")
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# What percentage of Pokemon are taller than 2.66807m (mean + (1 std_dev))
test_low = loaddata.mean_h + loaddata.std_dev_h
n = (loaddata.height > test_low).sum()
p = n / len(loaddata.height)
low = (test_low - loaddata.mean_h) / loaddata.std_dev_h
p2 = 1 - scipy.stats.norm.cdf(low)
print(f"{tab * 4}What percentage of Pokemon are taller than {round(test_low, 2)}m  (mean + (1 std.dev))\n")
print(f'{tab * 5}Actual: {n}/{len(loaddata.height)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# What percentage of Dragon Pokemon are taller than 2.66807m  (pop_mean + (1 pop_std_dev))
test_low = loaddata.mean_h + loaddata.std_dev_h
n = (loaddata.dragon_type_height > test_low).sum()
p = n / len(loaddata.dragon_type_height)
low = (test_low - loaddata.mean_dragon_h) / loaddata.std_dev_dragon_h
p2 = 1 - scipy.stats.norm.cdf(low)
print(f"{tab * 4}What percentage of Dragon Pokemon are taller than {round(test_low, 2)}m  (pop_mean + pop_std.dev.)\n")
print(f'{tab * 5}Actual: {n}/{len(loaddata.dragon_type_height)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# What percentage of Pokemon are heavier than 75kg
test_low = 75
n = (loaddata.weight > test_low).sum()
p = n / len(loaddata.weight)
low = (test_low - loaddata.mean_w) / loaddata.std_dev_w
p2 = 1 - scipy.stats.norm.cdf(low)
print(f"{tab * 4}What percentage of Pokemon are heavier than {test_low}kg\n")
print(f'{tab * 5}Actual: {n}/{len(loaddata.weight)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# What percentage of Dragon Pokemon are heavier than 75kg
test_low = 75
n = (loaddata.dragon_type_weight > test_low).sum()
p = n / len(loaddata.dragon_type_weight)
low = (test_low - loaddata.mean_dragon_w) / loaddata.std_dev_dragon_w
p2 = 1 - scipy.stats.norm.cdf(low)
print(f"{tab * 4}What percentage of Dragon Type Pokemon are heavier than {test_low}kg\n")
print(f'{tab * 5}Actual: {n}/{len(loaddata.dragon_type_weight)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')
print("\n")
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# What percentage of the Pokemon population is between .5m and 2m? (trimmed)
test_low = .5
test_high = 2
n = ((loaddata.h2 < test_high) & (loaddata.h2 > test_low)).sum()
p = n / len(loaddata.h2)
high = (test_high - loaddata.h2.mean()) / loaddata.h2.std()
low = (test_low - loaddata.h2.mean()) / loaddata.h2.std()
#
#   value is area under the curve behind given point on cdf plot
#
#   to find area between you just subtract high-low
#
print(f"{tab * 4}What percentage of Pokemon Heights(m) are between {test_low}m and {test_high}m? (trimmed)\n")
print(loaddata.trim_data)
print(f'{tab * 5}Answer: {n} / {len(loaddata.h2)} = {round((100 * p), 3)}%')
print(f'{tab * 5}Theory: {round((100 * (scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low))), 3)}%\n')
print(f'{separator + separator}\n')
# ----------------------------------------------------------------------------------
