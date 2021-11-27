# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import math
from sklearn import linear_model

poke = pd.read_csv('pokedex.csv')


## Usefull Functions (thank you professor Ruan!)
# %%
def zscore(data):
    m = np.mean(data)
    s = np.std(data)
    return ((data - m) / s)


# %%
def plotHist(data, title='histogram', xlabel='bin center', ylabel='frequency', c='blue', tc='red', is_zscore=False):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    mean_plt = np.mean(data)
    std_plt = np.std(data)

    if is_zscore:
        plt.title(title)
        # plot histogram and return counts containing frequency and bin center data
        counts = plt.hist(data, 20, color=c)
    else:
        plt.title(title)
        # plot histogram and return counts containing frequency and bin center data
        counts = plt.hist(data, 20, color=c)
        # text to be displayed on fig
        str_m = f'mean: {round(mean_plt, 3)}, std: {round(std_plt, 3)}'
        # location of text aligned with second bin center and half max frequency
        plt.annotate(str_m, [counts[1][1], np.max(counts[0]) / 2], color=tc)

    plt.show()


# %%
def myHistData(data, bins=20):
    counts = plt.hist(data, bins)
    plt.close()
    binCenter = (counts[1][1:] + counts[1][:-1]) / 2
    freq = counts[0] / len(data)
    return (binCenter, freq)


# %%
def plot_cdf(data, title="CDF", xlbl='x', ylbl='prob(value $\leq$ x)'):
    x = np.sort(data)
    size = len(data)
    y = (1 + np.arange(size)) / size
    plt.plot(x, y)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)  # between $$ is latex math mode
    plt.title(title)
    plt.show()
    return (x, y)


# %%
def normProbPlot(data, ylabel='Data', title='Normal probablity plot'):
    a = np.random.randn(len(data))
    plt.scatter(np.sort(a), np.sort(data))
    plt.xlabel('Standard Normal')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


# %%
## Pokemon population stats
total_points = poke['total_points']
hp = poke['hp']
speed = poke['speed']
attack = poke['attack']
sp_attack = poke['sp_attack']
defense = poke['defense']
sp_defense = poke['sp_defense']
height = poke['height_m']
weight = poke['weight_kg']

stat_values = poke[['pokedex_number',  'generation', 'name', 'type_1', 'type_2', 'height_m', 'weight_kg',
                    'ability_1', 'ability_2', 'ability_hidden',
                    'total_points', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed',
                    'is_sub_legendary', 'is_legendary', 'is_mythical']]

total_points_stats = total_points.describe()
hp_stats = hp.describe()
speed_stats = speed.describe()
attack_stats = attack.describe()
sp_attack_stats = sp_attack.describe()
defense_stats = defense.describe()
sp_defense_stats = sp_defense.describe()
height_stats = height.describe()
weight_stats = weight.describe()

# %%
## Grouping pokemon by type
# poke_important_data =
fire_types = stat_values.loc[(stat_values['type_1'] == "Fire") | (stat_values['type_2'] == "Fire")]
water_types = stat_values.loc[(stat_values['type_1'] == "Water") | (stat_values['type_2'] == "Water")]
grass_types = stat_values.loc[(stat_values['type_1'] == "Grass") | (stat_values['type_2'] == "Grass")]
electric_types = stat_values.loc[(stat_values['type_1'] == "Electric") | (stat_values['type_2'] == "Electric")]
normal_types = stat_values.loc[(stat_values['type_1'] == "Normal") | (stat_values['type_2'] == "Normal")]
ground_types = stat_values.loc[(stat_values['type_1'] == "Ground") | (stat_values['type_2'] == "Ground")]
rock_types = stat_values.loc[(stat_values['type_1'] == "Rock") | (stat_values['type_2'] == "Rock")]
steel_types = stat_values.loc[(stat_values['type_1'] == "Steel") | (stat_values['type_2'] == "Steel")]
ice_types = stat_values.loc[(stat_values['type_1'] == "Ice") | (stat_values['type_2'] == "Ice")]
flying_types = stat_values.loc[(stat_values['type_1'] == "Flying") | (stat_values['type_2'] == "Flying")]
fighting_types = stat_values.loc[(stat_values['type_1'] == "Fighting") | (stat_values['type_2'] == "Fighting")]
poison_types = stat_values.loc[(stat_values['type_1'] == "Poison") | (stat_values['type_2'] == "Poison")]
psychic_types = stat_values.loc[(stat_values['type_1'] == "Psychic") | (stat_values['type_2'] == "Psychic")]
bug_types = stat_values.loc[(stat_values['type_1'] == "Bug") | (stat_values['type_2'] == "Bug")]
ghost_types = stat_values.loc[(stat_values['type_1'] == "Ghost") | (stat_values['type_2'] == "Ghost")]
dark_types = stat_values.loc[(stat_values['type_1'] == "Dark") | (stat_values['type_2'] == "Dark")]
dragon_types = stat_values.loc[(stat_values['type_1'] == "Dragon") | (stat_values['type_2'] == "Dragon")]
fairy_types = stat_values.loc[(stat_values['type_1'] == "Fairy") | (stat_values['type_2'] == "Fairy")]

## Statistics for each type of Pokemon
stats_fire_types = fire_types.describe()
stats_water_types = water_types.describe()
stats_grass_types = grass_types.describe()
stats_electric_types = electric_types.describe()
stats_normal_types = normal_types.describe()
stats_ground_types = ground_types.describe()
stats_rock_types = rock_types.describe()
stats_steel_types = steel_types.describe()
stats_ice_types = ice_types.describe()
stats_flying_types = flying_types.describe()
stats_fighting_types = fighting_types.describe()
stats_poison_types = poison_types.describe()
stats_psychic_types = psychic_types.describe()
stats_bug_types = bug_types.describe()
stats_ghost_types = ghost_types.describe()
stats_dark_types = dark_types.describe()
stats_dragon_types = dragon_types.describe()
stats_fairy_types = fairy_types.describe()

# %%
## central limit theorem for attack of all pokemon
###  attack stat distributions
cl_attack = poke['attack']
### 100 samples, repeated 1000 times.
attack_sample = np.random.choice(cl_attack, (100, 1000), replace=True)
### sample mean of each column
attack_sample_mean = pd.DataFrame(attack_sample).describe().loc['mean']
# %%
## Z score transformation for attack stats
zs = zscore(cl_attack)
## Z score transformation for sampled attack stats
zs_s = zscore(attack_sample_mean)

# %%
### plotting bell curve for pokemon attack distribution
plt.figure()
### plotting population mean
plotHist(cl_attack, "Pokemon Attack Dist.", 'attack stat', 'frequency', 'blue', 'red', False)
plt.show()

# %%
### plotting population mean (standardized)
plt.figure()
plotHist(zs, "Pokemon Attack Dist. (Z-Score)", 'attack stat (Z Score)', 'frequency', 'blue', 'red', True)
plt.show()

# %%
## Population Attack against standardized plot
plt.scatter(cl_attack, zs)
plt.xlabel('Attack (atk)')
plt.ylabel('Z-score (unit-less)')
plt.title('Population Raw Attack value against standardized score')
plt.show()

# %%
### plotting bell curve for sample Pokemon attack distribution
plt.figure()
### plotting sample mean
plotHist(attack_sample_mean, 'Sample Pokemon Attack Dist. (sample size = 100, Repeated 1000x)', 'attack',
         'frequency', 'blue', 'red', False)
plt.show()

# %%
### plotting sample mean (standardized)
plt.figure()
plotHist(zs_s, "Sample Pokemon Attack Dist. (Z-Score)(ss = 100, Repeated 1000x)", 'attack stat (Z Score)', 'frequency',
         'blue', 'red', True)
plt.show()

# %%
## Sample Attack against standardized plot
plt.scatter(attack_sample_mean, zs_s)
plt.xlabel('Attack (atk)')
plt.ylabel('Z-score (unit-less)')
plt.title('Sample Raw Attack value against standardized score')
plt.show()

# %%
## Mean and standard error of the mean of Atk stat for three groups of data

measures = pd.DataFrame(np.random.choice(cl_attack, (300, 3), replace=True))
# SEM = std / sqrt(n)
SEM = np.std(measures, 0) / math.sqrt(measures.shape[0])

plt.errorbar([1, 2, 3], np.mean(measures, 0), SEM)
plt.xticks([1, 2, 3])
plt.xlabel('Sample group')
plt.ylabel('Mean $\pm$ SEM (atk)')
plt.title('Mean and SEM Atk stat for three groups of data (sample size = %d)' % measures.shape[0])
plt.show()

# %%
## calculating 95% Confidence interval for mean attack stats

plt.errorbar([1.05, 2.05, 3.05], np.mean(measures, 0), SEM)
plt.errorbar([1, 2, 3], np.mean(measures, 0), SEM * 1.96)
plt.xticks([1, 2, 3])
plt.xlabel('Sample group')
plt.ylabel('Mean and confidence interval (atk)')
plt.title('CI Atk stat for mean of 3 groups of data (sample size = %d)' % measures.shape[0])
plt.legend(('SEM', '95% CI'), loc=2)
plt.show()

# %%
## finding a correlation between hp and weight, speed and weight, height and weight, speed and hp, etc....
z_hp = zscore(hp)
z_speed = zscore(speed)
z_attack = zscore(attack)
z_sp_attack = zscore(sp_attack)
z_weight = zscore(weight)
z_height = zscore(height)

# corr hp / weight
# compute pearson correlation coefficient
pcc_hp_weight = weight.corr(hp, method='pearson')
# compute spearman correlation coefficient
scc_hp_weight = weight.corr(hp, method='spearman')
# compute kendal correlation coefficient
kcc_hp_weight = weight.corr(hp, method='kendall')

# corr speed / weight
# compute pearson correlation coefficient
pcc_speed_weight = weight.corr(speed, method='pearson')
# compute spearman correlation coefficient
scc_speed_weight = weight.corr(speed, method='spearman')
# compute kendal correlation coefficient
kcc_speed_weight = weight.corr(speed, method='kendall')

# corr height / weight
# compute pearson correlation coefficient
pcc_height_weight = weight.corr(height, method='pearson')
# compute spearman correlation coefficient
scc_height_weight = weight.corr(height, method='spearman')
# compute kendal correlation coefficient
kcc_height_weight = weight.corr(height, method='kendall')

# corr hp / speed
# compute pearson correlation coefficient
pcc_speed_hp = hp.corr(speed, method='pearson')
# compute spearman correlation coefficient
scc_speed_hp = hp.corr(speed, method='spearman')
# compute kendal correlation coefficient
kcc_speed_hp = hp.corr(speed, method='kendall')

# corr attack / sp_attak
# compute pearson correlation coefficient
pcc_atk_sp_atk = attack.corr(sp_attack, method='pearson')
# compute spearman correlation coefficient
scc_atk_sp_atk = attack.corr(sp_attack, method='spearman')
# compute kendal correlation coefficient
kcc_atk_sp_atk = attack.corr(sp_attack, method='kendall')

# %%
## Correlation between hp and weight
plt.scatter(hp, weight)
plt.title(
    f"Corr. HP and (kg) | Prsn CC={round(pcc_hp_weight, 2)}, Spm CC={round(scc_hp_weight, 2)}, Kend CC={round(kcc_hp_weight, 2)}")
plt.xlabel('HP')
plt.ylabel('Weight(kg)')
plt.show()

# %%
## Correlation between hp and weight (standardized)
plt.scatter(z_hp, z_weight)
plt.title(
    f"Corr. HP and (kg)| Prsn CC={round(pcc_hp_weight, 2)}, Spm CC={round(scc_hp_weight, 2)}, Kend CC={round(kcc_hp_weight, 2)}")
plt.xlabel('Z HP')
plt.ylabel('Z Weight(kg)')
plt.show()

# %%
## Correlation between speed and weight
plt.scatter(speed, weight)
plt.title(
    f"Corr. Speed and (kg)| Prsn CC={round(pcc_speed_weight, 2)}, Spm CC={round(scc_speed_weight, 2)}, Ken CC={round(kcc_speed_weight, 2)}")
plt.xlabel('Speed')
plt.ylabel('Weight(kg)')
plt.show()

# %%
## Correlation between speed and weight (standardized)
plt.scatter(z_speed, z_weight)
plt.title(
    f"Corr. Speed and (kg)| Prsn CC={round(pcc_speed_weight, 2)}, Spm CC={round(scc_speed_weight, 2)}, Kend CC={round(kcc_speed_weight, 2)}")
plt.xlabel('Z Speed')
plt.ylabel('Z Weight(kg)')
plt.show()

# %%
## Correlation between height and weight
plt.scatter(height, weight)
plt.title(
    f"Corr. (m) and (kg)| Prsn CC={round(pcc_height_weight, 2)}, Spm CC={round(scc_height_weight, 2)}, Kend CC={round(kcc_height_weight, 2)}")
plt.xlabel('Height(m)')
plt.ylabel('Weight(kg)')
plt.show()

# %%
## Correlation between height and weight (standardized)
plt.scatter(z_height, z_weight)
plt.title(
    f"Corr. (m) and (kg)| Prsn CC={round(pcc_height_weight, 2)}, Spm CC={round(scc_height_weight, 2)}, Kend CC={round(kcc_height_weight, 2)}")
plt.xlabel('Z Height(m)')
plt.ylabel('Z Weight(kg)')
plt.show()

# %%
## Correlation between speed and hp
plt.scatter(speed, hp)
plt.title(
    f"Corr. Speed and HP| Prsn CC={round(pcc_speed_hp, 2)}, Spm CC={round(scc_speed_hp, 2)}, Kend CC={round(kcc_speed_hp, 2)}")
plt.xlabel('Speed')
plt.ylabel('HP')
plt.show()

# %%
## Correlation between speed and hp (standardized)
plt.scatter(z_speed, z_hp)
plt.title(
    f"Corr. Speed and HP| Prsn CC={round(pcc_speed_hp, 2)}, Spm CC={round(scc_speed_hp, 2)}, Kend CC={round(kcc_speed_hp, 2)}")
plt.xlabel('Z Speed')
plt.ylabel('Z HP')
plt.show()

# %%
## Correlation between attack and special attack
plt.scatter(attack, sp_attack)
plt.title(
    f"Corr. Atk and SP.Atk | Prsn CC={round(pcc_atk_sp_atk, 2)}, Spm CC={round(scc_atk_sp_atk, 2)}, Kend CC={round(kcc_atk_sp_atk, 2)}")
plt.xlabel('Atack')
plt.ylabel('Special Attack')
plt.show()

# %%
## Correlation between attack and special attack (standardized)
plt.scatter(z_attack, z_sp_attack)
plt.title(
    f"Corr. Atk and SP.Atk | Prsn CC={round(pcc_atk_sp_atk, 2)}, Spm CC={round(scc_atk_sp_atk, 2)}, Kend CC={round(kcc_atk_sp_atk, 2)}")
plt.xlabel('Z Atack')
plt.ylabel('Z Special Attack')
plt.show()

# %%
## Getting Dragon and Non Dragon Types and collecting their various statistics

num_pokemon = len(poke)
cols = list(dragon_types.columns.values)

# already have list of all dragon types it is named dragon_types
dragon_type_height = dragon_types['height_m']
dragon_type_weight = dragon_types['weight_kg']
dragon_type_stat_values = dragon_types[cols[16:23]]

not_dragon_type = poke.loc[(poke['type_1'] != "Dragon") & (poke['type_2'] != "Dragon")]
not_dragon_type_height = not_dragon_type['height_m']
not_dragon_type_weight = not_dragon_type['weight_kg']
not_dragon_type_stat_values = not_dragon_type[cols[16:23]]

# %%
### Do Dragon Type Pokemon tend to be taller than all Pokemon? Non Dragon Type Pokemon?

# %%
## Displaying height(m) distribution of all Pokemon
counts = plt.hist(height, bins=100)
plt.xlabel('Height (m)')
plt.ylabel('Frequency')
plt.title('Pokemon Height Distribution')
plt.show()

# %%
## PMF For height(m) of all Pokemon
bin_center = (counts[1][1:] + counts[1][:-1]) / 2
plt.bar(bin_center, (counts[0] / sum(counts[0])), width=.2)
plt.xlabel('Pokemon Height (m)')
plt.ylabel('Probability')
plt.title('PMF: for height of all Pokemon')
plt.show()

# %%
## Displaying height(m) distribution of all Dragon Type Pokemon
counts_d = plt.hist(dragon_type_height, bins=100)
plt.xlabel('Height (m)')
plt.ylabel('Frequency')
plt.title('Dragon Type Pokemon Height Distribution')
plt.show()

# %%
## PMF for height(m) of all Dragon Pokemon
bin_center_d = (counts_d[1][1:] + counts_d[1][:-1]) / 2
plt.bar(bin_center_d, (counts_d[0] / sum(counts_d[0])), width=.2)
plt.xlabel('Pokemon Height (m)')
plt.ylabel('Probability')
plt.title('PMF: for height of all Dragon Type Pokemon')
plt.show()

# %%
## Displaying height(m) distribution of all Non Dragon Type Pokemon
counts_nd = plt.hist(not_dragon_type_height, bins=100)
plt.xlabel('Height (m)')
plt.ylabel('Frequency')
plt.title('Non Dragon Type Pokemon Height Distribution')
plt.show()

# %%
## PMF for height(m) of all Non Dragon Type Pokemon
bin_center_nd = (counts_nd[1][1:] + counts_nd[1][:-1]) / 2
plt.bar(bin_center_nd, (counts_nd[0] / sum(counts_nd[0])), width=.2)
plt.xlabel('Pokemon Height (m)')
plt.ylabel('Probability')
plt.title('PMF: for height of all Non Dragon Type Pokemon')
plt.show()

# %%
## PMF For height of Dragon vs all Pokemon
# line graph
plt.title("PMF: Height of Dragon vs all Pokemon")
plt.plot(bin_center_d, counts_d[0] / len(dragon_types), '-o',
         bin_center, counts[0] / num_pokemon, '-+')
plt.xlabel('Height')
plt.ylabel('Probability')
plt.legend(('Dragon Type', 'All Pokemon'))
plt.show()

# %%
## PMF For height of Dragon vs Not Dragon Pokemon
# line graph
plt.title("PMF: Height of Dragon vs Not Dragon Type Pokemon")
plt.plot(bin_center_d, counts_d[0] / len(dragon_types), '-o',
         bin_center_nd, counts_nd[0] / len(not_dragon_type), '-+')
plt.xlabel('Height')
plt.ylabel('Probability')
plt.legend(('Dragon Type', 'Not Dragon Type'))

plt.show()

# %%
## t-test
## going up means more likely to be a Dragon
plt.bar(bin_center_nd, counts_d[0] / len(dragon_types) - counts_nd[0] / len(not_dragon_type))
plt.title("T-Test: Do Dragon Types tend to be taller than Non Dragon Types")
plt.xlabel('Height (m)')
plt.ylabel('P[Dragon] - P[Not Dragon]')
plt.show()

# %%
## Cumulative distribution function (CDF) probability that its behind the curve at the given value

n_dragon_type = len(dragon_types)
n_not_dragon_type = len(not_dragon_type)
dragon_heights_sorted = np.sort(dragon_type_height)
not_dragon_heights_sorted = np.sort(not_dragon_type_height)
d = scipy.stats.norm.cdf(dragon_heights_sorted)
n_d = scipy.stats.norm.cdf(not_dragon_heights_sorted)

plt.plot(dragon_heights_sorted, d, '-b')
plt.plot(not_dragon_heights_sorted, n_d, 'r--')
plt.title("CDF: Dragon Type vs Not Dragon Type Pokemon Height")
plt.legend(('Dragon Type', 'Not Dragon Type'))
plt.xlabel('Height')
plt.ylabel('Probability (Height)')
plt.show()

# %%
## CDF plot using sort function - Dragon Types
prob = (np.arange(len(dragon_type_height)) + 1) / len(dragon_type_height)
plt.plot(np.sort(dragon_type_height), prob)
plt.title("CDF: Dragon Type Height")
plt.xlabel('Height (m)')
plt.ylabel('P(height $\leq$ x)')
plt.show()

#%%
## CDF plot using sort function - Not Dragon Types
prob = (np.arange(len(not_dragon_type_height)) + 1) / len(not_dragon_type_height)
plt.plot(np.sort(not_dragon_type_height), prob)
plt.title("CDF: Non Dragon Type Height")
plt.xlabel('Height (m)')
plt.ylabel('P(height $\leq$ x)')
plt.show()

# %%
## PMF vs CDF of dragon types for 10,20,30 bins
bin10, freq10 = myHistData(dragon_type_height, bins=10)
bin20, freq20 = myHistData(dragon_type_height, bins=20)
bin30, freq30 = myHistData(dragon_type_height, bins=30)

plt.title("PMF vs CDF for Dragon Type Height")
plt.plot(bin10, freq10, '-*', bin20, freq20, ':o', bin30, freq30, '-.v')
plt.legend(('10 bins', '20 bins', '30 bins'))
plt.xlabel('Height')
plt.ylabel('Probability (height)')
plt.show()

# %%
## Using standard normal distrubtion for quick probabilty estimation for all pokemon heights (m) and weights (kg)
print(f"Using standard normal distrubtion for quick probabilty estimation for all pokemon heights (m) and weights (kg)")

# %%
### how many Pokemon heights are less than 7 meters
print("how many Pokemon heights are less than 7 meters")
p = scipy.stats.norm.cdf(4.10475)
expected = p * len(height)
observed = (height < 7).sum()
print(f'# expected: {round(expected)}/{len(height)}')
print(f'# observed: {observed}/{len(height)}')
print("\n")

# %%
### How many heights are between 1.27 and 5.5 meters?
p = scipy.stats.norm.cdf(3.02968) - scipy.stats.norm.cdf(-0.00201)
expected = p * len(height)
observed = ((height < 5.5) & (height > 1.27)).sum()
print("How many Pokemon are between 1.27 and 5.5 meters?")
print(f'# expected: {round(expected)}/{len(height)}')
print(f'# observed: {observed}/{len(height)}')
print("\n")

# %%
### How many heights are greater than 2 meters?
p = 1 - scipy.stats.norm.cdf(0.52119)
expected = p * len(height)
observed = (height > 2).sum()
print("How many Pokemon are taller than than 2 meters?")
print(f'# expected: {round(expected)}/{len(height)}')
print(f'# observed: {observed}/{len(height)}')
print("\n")

# %%
### What percentage of the Pokemon population is between 1 and 2 meters?
test_high = 2
test_low = 1
std_dev_h = height_stats.loc['std']
mean_h = height_stats.loc['mean']

print("What percentage of the Pokemon population is between 1 and 2 meters?")
# more accurate estimate than just regular min and max (getting zscore of test_high and test_low)
high = (test_high - mean_h) / std_dev_h
low = (test_low - mean_h) / std_dev_h

p = scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low)
print(f'-->: {round((100 * p), 2)}%')
print("\n")

# %%
### What percentage of the Pokemon population is heavier than 50kg?
test_low = 50
std_dev_w = weight_stats.loc['std']
mean_w = weight_stats.loc['mean']

print("What percentage of the Pokemon population is heavier than 50kg?")
# more accurate estimate than just regular min and max
low = (test_low - mean_w) / std_dev_w

p = 1 - scipy.stats.norm.cdf(low)
print(f'-->: {round((100 * p), 2)}%')
print("\n")

# %%
### what percentage of the Pokemon population is heavier than 100kg?
test_low = 100
std_dev_w = weight_stats.loc['std']
mean_w = weight_stats.loc['mean']
print("What percentage of the Pokemon population is heavier than 100kg?")
# more accurate estimate than just regular min and max
low = (test_low - mean_w) / std_dev_w
p = 1 - scipy.stats.norm.cdf(low)
print(f'-->: {round((100 * p), 2)}%')
print("\n")

# %%
## Verifying estimations with real data

# %%
### What percentage of Pokemon are taller than 2.66807m

mean_h = height_stats.loc['mean']
std_dev_h = height_stats.loc['std']

test_low = mean_h + std_dev_h
low = (test_low - mean_h) / std_dev_h
p2 = 1 - scipy.stats.norm.cdf(low)

n = (height > test_low).sum()
p = n / len(height)

print(f"What percentage of Pokemon are taller than {round(test_low, 2)}m  (mean + (1 std.dev))")
print(f'Actual: {n}/{len(height)} = {round(100 * p, 3)}%')
print(f'Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'standardized: {round((100 * p2), 3)}%')
print("\n")

# %%
### What percentage of Dragon Pokemon are taller than 2.66807m
test_low = mean_h + std_dev_h

mean_dragon_h = stats_dragon_types['height_m'].loc['mean']
std_dev_dragon_h = stats_dragon_types['height_m'].loc['std']

low = (test_low - mean_dragon_h) / std_dev_dragon_h
p2 = 1 - scipy.stats.norm.cdf(low)

n = (dragon_type_height > 2.66807).sum()
p = n / len(dragon_type_height)

print(f"What percentage of Dragon Pokemon are taller than {round(test_low, 2)}m  (pop_mean + pop_std.dev.)")
print(f'Actual: {n}/{len(dragon_type_height)} = {round(100 * p, 3)}%')
print(f'Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'standardized: {round((100 * p2), 3)}%')
print("\n")

# %%
### What percentage of Pokemon are heavier than 75kg

n = (weight > 75).sum()
p = n / len(weight)
print("What percentage of Pokemon are heavier than 75kg")
print(f'Actual: {n}/{len(weight)} = {round(100 * p, 3)}%')
print(f'Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print("\n")

# %%
### What percentage of Dragon Pokemon are heavier than 75kg

n = (dragon_type_weight > 75).sum()
p = n / len(dragon_type_weight)
print("What percentage of Dragon Type Pokemon are heavier than 75kg")
print(f'Actual: {n}/{len(dragon_type_weight)} = {round(100 * p, 3)}%')
print(f'Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print("\n")

# %%
## *What is happening????*

# %%
## Normal Probability of pokemon heights
### Normal probablity plot

# %%
### Is Pokemon data actually normally distributed?

plotHist(height, "Distribution of Pokemon Height(m) ", "Height(m)", "Frequency")
normProbPlot(height, ylabel='Height(m)', title='Normal probablity plot of Pokemon Heights(m)')

# %%
## normal log scale height
log_h = np.log(height)
plotHist(log_h, xlabel='log(m)', title='Distribution of Pokemon Height log(m)')
normProbPlot(log_h, ylabel='log(m)', title='Normal probablity plot of Pokemon Height log(m)')
plot_cdf(height, title="Pokemon Height(m) CDF", xlbl='Height(m)', ylbl='prob(value $\leq$ height)')

# %%
### Trimming Data
h2 = height[(height > .1) & (height < 2.33)]
print('Removed %d / %d = %.2f %% of cases' % (
    len(height) - len(h2), len(height), (len(height) - len(h2)) / len(height) * 100))
plotHist(h2, 'Trimmed Pokemon Heights(m) (trimmed (height > .1) & (height < 2.33)', 'Height(m)')
normProbPlot(h2, ylabel='trimmed Heights(m)', title='Normal probablity plot of Pokemon Heights(m) (trimmed)')

# %%
### Filtering data
counts = np.unique(h2, return_counts=True)
# filter heights here, we want their frequency to be more than 5
filtered = np.array(counts)[:, counts[1] > 5]

plt.title("Filtered and Trimmed Pokemon Height Distribution")
plt.bar(filtered[0], filtered[1])
plt.xlabel("Height(m)")
plt.ylabel("Frequency")
plt.show()

# %%
##### What percentage of the Pokemon population is between .5m and 2m? (trimmed)
test_low = .5
test_high = 2

n = ((h2 < test_high) & (h2 > test_low)).sum()
p = n / len(h2)

high = (test_high - h2.mean()) / h2.std()
low = (test_low - h2.mean()) / h2.std()

#
#   value is area under the curve behind given point on cdf plot
#
#   to find area between you just subtract high-low
#

print(f"What percentage of the Pokemon population is between {test_low} and {test_high}? (trimmed)")
print(f'Answer: {n} / {len(h2)} = {round((100 * p), 3)}%')
print(f'Theory: {round((100 * (scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low))), 3)}%')

# %%
### Plotting weight distribution
plotHist(weight, 'Distribution of Pokemon weight(kg)')
normProbPlot(weight, ylabel='Weight (kg)', title='Normal Probablity plot of Pokemon weight(kg)')
# %%
## noraml log scale weight
log_w = np.log(weight)
plotHist(log_w, xlabel='log(kg)', title='Distribution of Pokemon Weight log(kg)')
normProbPlot(log_w, ylabel='log(kg)', title='Normal probablity plot of Pokemon Weight log(kg)')
plot_cdf(weight, title="Pokemon Weight(kg) CDF", xlbl='Weight(kg)', ylbl='prob(value $\leq$ weight)')

# %%
separator = '---------------------------------------------------------------'
pcc_height_weight = weight.corr(height, method='pearson')
pcc_log_height_weight = log_h.corr(weight, method='pearson')
pcc_log_height_log_weight = log_h.corr(log_w, method='pearson')
scc_height_weight = weight.corr(height, method='spearman')
scc_log_height_weight = log_h.corr(weight, method='spearman')
scc_log_height_log_weight = log_h.corr(log_w, method='spearman')

print(f'{separator}')
print(f'Pearson Correlation between Height and Weight is: {round(pcc_height_weight, 3)}')
print(f'Pearson Correlation between log(Height) and Weight is: {round(pcc_log_height_weight, 3)}')
print(f'Pearson Correlation between log(Height) and log(Weight) is: {round(pcc_log_height_log_weight, 3)}')
print(f'{separator}')
print(f'Spearman Correlation between Height and Weight is: {round(scc_height_weight, 3)}')
print(f'Spearman Correlation between log(Height) and Weight is: {round(scc_log_height_weight, 3)}')
print(f'Spearman Correlation between log(Height) and log(Weight) is: {round(scc_log_height_log_weight, 3)}')

# %%


dragon_types.boxplot()

plt.show()

# %%
# you can also read in by the chunk size incase your data set is extremely large
#  example:
#  for df in pd.read_csv("pokemon_data.csv", chunksize=5)
#       results = df.groupby(['Type 1']).count()
#
#       new_df = pd.concat([new_df, results])

# %%
#  printing certain column elements
# print(poke[['Name', 'Type 1', '#']])

# %%
# sort by col value, here we are sorting first by type 1 in order a->z then speed highest -> lowest
# poke.sort_values(['Type 1', 'Speed'], ascending=[1, 1])

# %%
# finds location that matched; here we find all pokemon with type 1 of fire
# print(poke.loc[poke['Type 1'] == "Fire" ] )

# %%
# # creating a new col of base stat totals
# poke["Stat Total"] = poke.iloc[:, 4:10].sum(axis=1)  #poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']
# cols = list(poke.columns.values)
# poke = poke[cols[0:10] + [cols[-1]] + cols[10:12]]
# modified = poke.to_csv('modified_pokemon.csv', index=False)
# print(count_type1)

# %%
# remove a collum
# poke = poke.drop(columns=["Stat Total"])
# print(poke.head(5))

# %%
# grouping by type1 with average attack
# type1_atk = poke[['Type 1', 'Attack']]
# avg_attack_by_type1 = type1_atk.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
# avg_attack_by_type1.rename(columns={'Attack': 'Avg. Atk.'}, inplace=True)
# avg_attack_by_type1.plot(kind='bar')
# plt.show()

# %%
## fire types data analytics
# gen1_fire = fire_types.loc[fire_types['generation'] == 1]
# gen2_fire = fire_types.loc[fire_types['generation'] == 2]
# gen3_fire = fire_types.loc[fire_types['generation'] == 3]
# gen4_fire = fire_types.loc[fire_types['generation'] == 4]
# gen5_fire = fire_types.loc[fire_types['generation'] == 5]
# gen6_fire = fire_types.loc[fire_types['generation'] == 6]
# gen7_fire = fire_types.loc[fire_types['generation'] == 7]
# gen8_fire = fire_types.loc[fire_types['generation'] == 8]
#
# stats_gen1_fire = gen1_fire.describe()
# stats_gen2_fire = gen2_fire.describe()
# stats_gen3_fire = gen3_fire.describe()
# stats_gen4_fire = gen4_fire.describe()
# stats_gen5_fire = gen5_fire.describe()
# stats_gen6_fire = gen6_fire.describe()
# stats_gen7_fire = gen7_fire.describe()
# stats_gen8_fire = gen8_fire.describe()
