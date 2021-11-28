# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import math
from sklearn import linear_model

poke = pd.read_csv('pokedex.csv')
separator = '---------------------------------------------------------------'
tab = "\t"


# %%
print(f'{separator + separator}')

print(f'{tab * 11}- - - Pokemon Data Analysis - - -')
print(f'{tab * 14}Group 18')

print(f'{separator + separator}\n')
print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
      f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
      f'{tab * 14}Thank you!\n')
print(f'{separator + separator}')


# %%
def z_score(data):
    m = np.mean(data)
    s = np.std(data)
    return ((data - m) / s)


# %%
def plot_hist(data, title='histogram', xlabel='bin center', ylabel='frequency', c='blue', tc='red',
              is_zscore=False, bins=20):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    mean_plt = np.mean(data)
    std_plt = np.std(data)

    if is_zscore:
        plt.title(title)
        # plot histogram and return counts containing frequency and bin center data
        counts = plt.hist(data, bins, color=c)
    else:
        plt.title(title)
        # plot histogram and return counts containing frequency and bin center data
        counts = plt.hist(data, bins, color=c)
        # text to be displayed on fig
        str_m = f'mean: {round(mean_plt, 3)}, std: {round(std_plt, 3)}'
        # location of text aligned with second bin center and half max frequency
        plt.annotate(str_m, [counts[1][1], np.max(counts[0]) / 2], color=tc)


# %%
def plot_norm_prob(data, ylabel='Data', title='Normal probablity plot'):
    a = np.random.randn(len(data))
    plt.scatter(np.sort(a), np.sort(data))
    plt.xlabel('Standard Normal')
    plt.ylabel(ylabel)
    plt.title(title)


# %%
def plot_cdf(data, title="CDF", xlbl='x', ylbl='prob(value $\leq$ x)'):
    x = np.sort(data)
    size = len(data)
    y = (1 + np.arange(size)) / size
    plt.plot(x, y)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)  # between $$ is latex math mode
    plt.title(title)
    return (x, y)


# %%
def my_hist_data(data, bins=20):
    counts = plt.hist(data, bins)
    plt.close()
    binCenter = (counts[1][1:] + counts[1][:-1]) / 2
    freq = counts[0] / len(data)
    return (binCenter, freq)


# %%
def corr_compute(x, y, xlbl='x', ylbl='y', modified=""):
    # corr x / y
    # compute pearson correlation coefficient
    pcc = x.corr(y, method='pearson')
    # compute spearman correlation coefficient
    scc = x.corr(y, method='spearman')
    # compute kendal correlation coefficient
    kcc = x.corr(y, method='kendall')

    corr_data = f"{tab * 4}Corelation between {xlbl} and {ylbl} {modified}\n" + \
                f"{tab * 5}Pearson CC = {round(pcc, 2)}\n" + \
                f"{tab * 5}Spearman CC = {round(scc, 2)}\n" + \
                f"{tab * 5}Kendall CC = {round(kcc, 2)}\n"
    return corr_data


# %%
def basic_stats_string(x_stats, xlbl='x'):
    # output string
    stats_string = f"{tab * 4}{xlbl} Statistics:\n" \
                   f"{tab * 5}Standard Deviation: {round(x_stats.loc['std'], 2)}\n" + \
                   f"{tab * 5}Mean: {round(x_stats.loc['mean'], 2)}\n" + \
                   f"{tab * 5}Min: {round(x_stats.loc['min'], 2)}\n" + \
                   f"{tab * 5}Max: {round(x_stats.loc['max'], 2)}\n"
    return stats_string


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

# things well def need, gonna use this since its easy to use for just these cols
stat_values = poke[['pokedex_number', 'generation', 'name', 'type_1', 'type_2', 'height_m', 'weight_kg',
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
### Important values

## -- Number of Pokemon in population ---
num_pokemon = len(poke)
# ---------------------------------------

## --- Grouping pokemon by type -----------------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------------------------------------


## --- Statistics for each Pokemon Type -----------
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
# -------------------------------------------------


## ---- sample constants --------------------
# size of pokemon sampled from population
sample_size = 100
# number of times we sample the population
repeat_n = 1000
# -------------------------------------------


## --- samples --------------------------------------------------------------------------------------
sample_attack = np.random.choice(attack, (sample_size, repeat_n), replace=True)
sample_attack_mean = pd.DataFrame(sample_attack).describe().loc['mean']  # getting mean of each col
# ---------------------------------------------------------------------------------------------------


## --- samples stats -----------------------------------
# sample attack stats
sample_attack_stats = sample_attack_mean.describe()
# ------------------------------------------------------


## --- Z score transformation ------------------------------------------------
# zscores and zscore stats for pokemon stat values, height(m), and weight(kg)
z_hp = z_score(hp)
z_hp_stats = z_hp.describe()
z_attack = z_score(attack)
z_attack_stats = z_attack.describe()
z_defense = z_score(defense)
z_defense_stats = z_defense.describe()
z_sp_attack = z_score(sp_attack)
z_sp_attack_stats = z_sp_attack.describe()
z_sp_defense = z_score(sp_defense)
z_sp_defense_stats = z_sp_defense.describe()
z_speed = z_score(speed)
z_speed_stats = z_speed.describe()
z_weight = z_score(weight)
z_weight_stats = z_weight.describe()
z_height = z_score(height)
z_height_stats = z_height.describe()
# sample attack zscore and stats
z_attack_s = z_score(sample_attack_mean)
z_attack_stats_s = z_attack_s.describe()
# ------------------------------------------------------------------------------


## --- log normal distributions -
# normal log scale height
log_h = np.log(height)
# normal log scale weight
log_w = np.log(weight)
# ------------------------------


## --- basic stats for different sets from the population ---
# Pokemon height mean and std dev
mean_h = height_stats.loc['mean']
std_dev_h = height_stats.loc['std']
# Pokemon weight mean and std dev
mean_w = weight_stats.loc['mean']
std_dev_w = weight_stats.loc['std']
# Dragon Type Pokemon height mean and std dev
mean_dragon_h = stats_dragon_types['height_m'].loc['mean']
std_dev_dragon_h = stats_dragon_types['height_m'].loc['std']
# Dragon Type Pokemon weight mean and std dev
mean_dragon_w = stats_dragon_types['weight_kg'].loc['mean']
std_dev_dragon_w = stats_dragon_types['weight_kg'].loc['std']
# ------------------------------------------------------------


## --- Getting Dragon and Non Dragon Types and collecting their various statistics --
cols = list(dragon_types.columns.values)  # name of colums in type dataframes
# dragon types
# already have list of all dragon types it is named dragon_types
dragon_type_height = dragon_types['height_m']
dragon_type_weight = dragon_types['weight_kg']
dragon_type_stat_values = dragon_types[cols[16:23]]
n_dragon_type = len(dragon_types)
dragon_heights_sorted = np.sort(dragon_type_height)
d_cdf = scipy.stats.norm.cdf(dragon_heights_sorted)
# non dragon types
not_dragon_type = poke.loc[(poke['type_1'] != "Dragon") & (poke['type_2'] != "Dragon")]
not_dragon_type_height = not_dragon_type['height_m']
not_dragon_type_weight = not_dragon_type['weight_kg']
not_dragon_type_stat_values = not_dragon_type[cols[16:23]]
n_not_dragon_type = len(not_dragon_type)
not_dragon_heights_sorted = np.sort(not_dragon_type_height)
n_d_cdf = scipy.stats.norm.cdf(not_dragon_heights_sorted)
# ----------------------------------------------------------------------------------


## --- probailities of height --------------------------
# height
prob_h = (np.arange(len(height)) + 1) / len(height)
prob_h_stats = pd.Series(prob_h).describe()
# weight
prob_w = (np.arange(len(weight)) + 1) / len(height)
prob_w_stats = pd.Series(prob_w).describe()
# height prob dragon
prob_h_d = (np.arange(len(dragon_type_height)) + 1) / len(dragon_type_height)
prob_h_d_stats = pd.Series(prob_h_d).describe()
# height prob non dragons
prob_h_nd = (np.arange(len(not_dragon_type_height)) + 1) / len(not_dragon_type_height)
prob_h_nd_stats = pd.Series(prob_h_nd).describe()
# ------------------------------------------------------


## --- three groups of pokemon attack stats ----------------------------------------------
measures_attack = pd.DataFrame(np.random.choice(attack, (300, 3), replace=True))
g1_stats = measures_attack[0].describe()
g2_stats = measures_attack[1].describe()
g3_stats = measures_attack[2].describe()
## --- SEM for 3 groups of pokemon attack stats  ->  std / sqrt(len(group))
SEM_attack = np.std(measures_attack, 0) / math.sqrt(measures_attack.shape[0])
## --- 95% Confidence Interval ----------------------------------------------------------
ci95_attack = SEM_attack * 1.96
# ---------------------------------------------------------------------------------------


## --- Trimming Height Data ---------------------------------------------------------------------------
height_trim_low = .1
height_trim_high = 2.33

h2 = height[(height > height_trim_low) & (height < height_trim_high)]  # trimmed height

prob_h_trim = (np.arange(len(h2)) + 1) / len(h2)
prob_h_trim_stats = pd.Series(prob_h_trim).describe()

trim_data = f"{tab * 4}Trimmed extremes from Pokemon Height(m) data\n" + \
            f'{tab * 5}min height = {height_trim_low}(m), max height = {height_trim_high}(m)\n' + \
            f'{tab * 5}Removed {len(height) - len(h2)} / {len(height)} = ' + \
            f'{round(((len(height) - len(h2)) / len(height)) * 100, 2)}% of cases\n' + \
            f'{tab * 5}{len(h2)} Pokemon Remain\n'
# -----------------------------------------------------------------------------------------------------

## --- Filtering Height Data ------------------------------------------------------
min_freq = 9
height_counts = np.unique(h2, return_counts=True)
# filter heights here, we want their frequency to be more than 5
filtered_heights = np.array(height_counts)[:, height_counts[1] > min_freq]
total_filtered_num = int(filtered_heights[1].sum())
num_removed_filter_h = len(h2) - total_filtered_num
filter_freq_data_stats = pd.Series(filtered_heights[1]).describe()

filter_data = f"{tab * 4}Filtered Pokemon Heights(m).\n" + \
              f"{tab * 5}Removed Heights(m) that occur less than {min_freq}x\n" \
              f'{tab * 5}Removed {num_removed_filter_h} / {len(h2)} = ' + \
              f'{round(((num_removed_filter_h / len(h2)) * 100), 2)}% of cases\n' + \
              f'{tab * 5}{total_filtered_num} Pokemon Remain\n'
# ----------------------------------------------------------------------------------


# %%
### plotting bell curve for pokemon attack distribution

curr_fig = "1"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Attack Stat Distribution - - -\n')
print(basic_stats_string(attack_stats, "Attack"))

plt.figure()
### plotting population mean
plot_hist(attack, f"Figure {curr_fig}: Attack Stat Distribution", 'attack stat', 'frequency', 'blue', 'red', False)
plt.show()

print(f'{separator + separator}\n')

# %%
### plotting population mean (standardized)

curr_fig = "1b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Attack Stat Distribution (standardized) - - -\n')
print(basic_stats_string(z_attack_stats, "Z Attack"))

plt.figure()
plot_hist(z_attack, f"Figure {curr_fig}: Attack Stat Distribution (standardized)", 'attack stat (Z Score)', 'frequency', 'blue',
          'red', True)
plt.show()

print(f'{separator + separator}\n')



# %%
## Population Attack distribution standardized plot

curr_fig = "2"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Population raw attack value against standardized score - - -\n')
print(corr_compute(attack, z_attack, "Attack", "Z Attack"))

plt.figure()
plt.scatter(attack, z_attack)
plt.xlabel('Attack (atk)')
plt.ylabel('Z-score (unit-less)')
plt.title('Figure 2: Population raw attack value against standardized score')
plt.show()

print(f'{separator + separator}\n')

# %%
### plotting sample Pokemon attack distribution

curr_fig = "3"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Sample Pokemon Attack Distribution - - -\n')
print(f'{tab * 4}Sample size = {sample_size}, Repeated {repeat_n}x\n')
print(basic_stats_string(sample_attack_stats, "Attack"))

plt.figure()
plot_hist(sample_attack_mean, f'Figure {curr_fig}: Sample Pokemon Attack Distribution', 'attack',
          'frequency', 'blue', 'red', False)
plt.show()

print(f'{separator + separator}\n')

# %%
### Plotting sample attack distribution (standardized)

curr_fig = "3b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Sample Pokemon Attack Distribution (standardized) - - -\n')
print(f'{tab * 4}Sample Size = {sample_size}, Repeated {repeat_n}x\n')
print(basic_stats_string(z_attack_stats_s, "Z Attack"))

plt.figure()
plot_hist(z_attack_s, f"Figure {curr_fig}: Sample Pokemon Attack Distribution (standardized)", 'Z Attack', 'frequency',
          'blue', 'red', True)
plt.show()

print(f'{separator + separator}\n')


# %%
## Sample Attack against standardized plot

curr_fig = "4"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Sample Raw Attack value against standardized score - - -\n')
print(f'{tab * 4}Sample Size = {sample_size}, Repeated {repeat_n}x\n')
print(corr_compute(sample_attack_mean, z_attack_s, "Attack", "Z Attack"))

plt.figure()
plt.scatter(sample_attack_mean, z_attack_s)
plt.xlabel('Attack (atk)')
plt.ylabel('Z-score (unit-less)')
plt.title(f'Figure {curr_fig}: Sample Raw Attack value against standardized score')
plt.show()

print(f'{separator + separator}\n')

# %%
## Mean and standard error of the mean of Atk stat for three groups of data

curr_fig = "5"

sem_str = ""
for x in range(len(SEM_attack)):
    sem_str += f"{tab * 5}Group #{x + 1}: {round(SEM_attack[x], 2)}\n"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Mean and SEM Atk stat for three groups of Pokemon - - -\n')
print(f'{tab * 4}Sample size per group = {measures_attack.shape[0]}\n')
print(f'{tab * 4}Standard Error of the Mean:')
print(sem_str)

print(f"{tab * 9}- - - Attack Stats By Group - - -\n")
print(basic_stats_string(g1_stats, "Attack (group 1)"))
print(basic_stats_string(g2_stats, "Attack (group 2)"))
print(basic_stats_string(g3_stats, "Attack (group 3)"))

plt.figure()
plt.errorbar([1, 2, 3], np.mean(measures_attack, 0), SEM_attack)
plt.xticks([1, 2, 3])
plt.xlabel('Sample group')
plt.ylabel('Mean $\pm$ SEM (atk)')
plt.title(f'Figure {curr_fig}: Mean and SEM Atk stat for three groups of Pokemon')
plt.show()

print(f'{separator + separator}\n')

# %%
## calculating 95% Confidence interval for mean attack stats

curr_fig = "5b"

ci_95_str = ""
for x in range(len(SEM_attack)):
    ci_95_str += f"{tab * 5}Group #{x + 1}: {round(ci95_attack[x], 2)}\n"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: 95% Confidence Interval Attack stat for mean of 3 groups of Pokemon - - -\n')
print(f'{tab * 4}Sample size per group = {measures_attack.shape[0]}\n')
print(f'{tab * 4}95% Confidence Interval Attack stat for mean of 3 groups:')
print(ci_95_str)

plt.figure()
plt.errorbar([1.05, 2.05, 3.05], np.mean(measures_attack, 0), SEM_attack)
plt.errorbar([1, 2, 3], np.mean(measures_attack, 0), ci95_attack)
plt.xticks([1, 2, 3])
plt.xlabel('Sample Groups')
plt.ylabel('Mean and confidence interval (atk)')
plt.title(f"Figure {curr_fig}: 95% Confidence Interval")
plt.legend(('SEM', '95% CI'), loc=2)
plt.show()

print(f'{separator + separator}\n')

# %%
## finding a correlation between hp and weight, speed and weight, height and weight, speed and hp, etc....

## Correlation between hp and weight

curr_fig = "6"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Hp and Weight(kg) - - -\n')

print(corr_compute(hp, weight, "Hp", "Weight(kg)"))

plt.figure()
plt.scatter(hp, weight)
plt.title(f"Figure {curr_fig}: Correlation between Hp and Weight(kg)")
plt.xlabel('HP')
plt.ylabel('Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between hp and weight (standardized)

curr_fig = "6b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Hp and Weight(kg) (standardized) - - -\n')
print(corr_compute(z_hp, z_weight, "Z Hp", "Z Weight(kg)", "(standardized)"))

plt.figure()
plt.scatter(z_hp, z_weight)
plt.title(f'Figure {curr_fig}: Correlation between Hp and Weight(kg) (standardized)')
plt.xlabel('Z HP')
plt.ylabel('Z Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between speed and weight

curr_fig = "7"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Weight(kg) - - -\n')

print(corr_compute(speed, weight, "Speed", "Weight(kg)"))

plt.figure()
plt.scatter(speed, weight)
plt.title(f'Figure {curr_fig}: Correlation between Speed and Weight(kg)')
plt.xlabel('Speed')
plt.ylabel('Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between speed and weight (standardized)

curr_fig = '7b'

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Weight(kg) (standardized) - - -\n')
print(corr_compute(z_speed, z_weight, "Z Speed", "Z Weight(kg)", "(standardized)"))

plt.figure()
plt.scatter(z_speed, z_weight)
plt.title(f'Figure {curr_fig}: Correlation between Speed and Weight(kg) (standardized)')
plt.xlabel('Z Speed')
plt.ylabel('Z Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between height and weight

curr_fig = "8"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Height(m) and Weight(kg) - - -\n')

print(corr_compute(height, weight, "Height(m)", "Weight(kg)"))

plt.figure()
plt.scatter(height, weight)
plt.title(f"Figure {curr_fig}: Correlation between Height(m) and Weight(kg)")
plt.xlabel('Height(m)')
plt.ylabel('Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between height and weight (standardized)

curr_fig = "8b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Height(m) and Weight(kg) (standardized) - - -\n')

print(corr_compute(z_height, z_weight, "Z Height", "Z Weight(kg)", "(standardized)"))

plt.figure()
plt.scatter(z_height, z_weight)
plt.title(f"Figure {curr_fig}: Correlation between Height(m) and Weight(kg) (standardized)")
plt.xlabel('Z Height(m)')
plt.ylabel('Z Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between speed and hp

curr_fig = "9"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Hp - - -\n')

print(corr_compute(speed, hp, "Speed", "Hp"))

plt.figure()
plt.scatter(speed, hp)
plt.title(f"Figure {curr_fig}: Correlation between Speed and Hp")
plt.xlabel('Speed')
plt.ylabel('HP')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between speed and hp (standardized)

curr_fig = "9b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Speed and Hp (standardized) - - -\n')

print(corr_compute(z_speed, z_hp, "Z Speed", "Z Hp", "(standardized)"))

plt.figure()
plt.scatter(z_speed, z_hp)
plt.title(f"Figure {curr_fig}: Correlation between Speed and Hp (standardized)")
plt.xlabel('Z Speed')
plt.ylabel('Z HP')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between attack and special attack

curr_fig = "10"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Attack and Special Attack - - -\n')
print(corr_compute(attack, sp_attack, "Attack", "Special Attack"))

plt.figure()
plt.scatter(attack, sp_attack)
plt.title(f"Figure {curr_fig}: Correlation between Attack and Special Attack")
plt.xlabel('Atack')
plt.ylabel('Special Attack')
plt.show()

print(f'{separator + separator}\n')

# %%
## Correlation between attack and special attack (standardized)

curr_fig = "10b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Correlation between Attack and Special Attack (standardized) - - -\n')
print(corr_compute(z_attack, z_sp_attack, "Z Attack", "Z Special Attack", "(standardized)"))

plt.figure()
plt.scatter(z_attack, z_sp_attack)
plt.title(f"Figure {curr_fig}: Correlation between Attack and Special Attack (standardized)")
plt.xlabel('Z Atack')
plt.ylabel('Z Special Attack')
plt.show()

print(f'{separator + separator}\n')

# %%
### Do Dragon Type Pokemon tend to be taller than all Pokemon? Non Dragon Type Pokemon?
dh_null_hypothesis = "Assume Dragon Type Pokemon tend to be taller than all Pokemon, and Non Dragon Type Pokemon."

print(f'{separator + separator}\n')
print(f'{tab * 3}Do Dragon Type Pokemon tend to be taller than all Pokemon?  What about just'
      f' Non Dragon Type Pokemon?\n')
print(f'{separator + separator}\n')

# %%
### All Types of Pokemon
## Displaying height(m) distribution of all Pokemon

curr_fig = "11"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Height(m) distribution of all Pokemon - - -\n')
print(basic_stats_string(height_stats, "Height(m)"))

plt.figure()
# storing frequencies of different heights of all pokemon here
counts_a = plt.hist(height, bins=100)
plt.xlabel('Height(m)')
plt.ylabel('Frequency')
plt.title(f'Figure {curr_fig}: Height(m) distribution of all Pokemon')
plt.show()

print(f'{separator + separator}\n')

# %%

curr_fig = "11b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of all Pokemon - - -\n')

## PMF For height(m) of all Pokemon
bin_center = (counts_a[1][1:] + counts_a[1][:-1]) / 2
pmf_val = counts_a[0] / sum(counts_a[0])

plt.figure()
plt.bar(bin_center, pmf_val, width=.2)
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.title(f'Figure {curr_fig}: PMF: Height(m) of all Pokemon')
plt.show()

print(f'{separator + separator}\n')

# %%
### Dragon Type Pokemon
## Displaying height(m) distribution of all Dragon Type Pokemon

curr_fig = "12"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Height(m) distribution of Dragon Type Pokemon - - -\n')
print(basic_stats_string(dragon_type_height.describe(), "Height(m)"))

plt.figure()
# storing frequencies of different heights of dragon type pokemon here
counts_d = plt.hist(dragon_type_height, bins=100)
plt.xlabel('Height(m)')
plt.ylabel('Frequency')
plt.title(f'Figure {curr_fig}: Height(m) distribution of Dragon Type Pokemon')
plt.show()

print(f'{separator + separator}\n')

# %%
## PMF for height(m) of all Dragon Pokemon

curr_fig = "12b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of Dragon Type Pokemon - - -\n')

bin_center_d = (counts_d[1][1:] + counts_d[1][:-1]) / 2
pmf_val_d = counts_d[0] / sum(counts_d[0])

plt.figure()
plt.bar(bin_center_d, pmf_val_d, width=.2)
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.title(f'Figure {curr_fig}: PMF: Height(m) of Dragon Type Pokemon')
plt.show()

print(f'{separator + separator}\n')

# %%
## CDF plot using sort function - Dragon Types

curr_fig = "12c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: CDF: Height(m) of Dragon Type Pokemon - - -\n')
print(basic_stats_string(prob_h_d_stats, "Probability ( Height(m) <= x)"))

plt.figure()
plt.plot(dragon_heights_sorted, prob_h_d)
plt.title(f"Figure {curr_fig}: CDF: Height(m) of Dragon Type Pokemon")
plt.xlabel('Height(m)')
plt.ylabel('P(height $\leq$ x)')
plt.show()

print(f'{separator + separator}\n')


# %%
## PMF vs CDF of dragon types for 10,20,30 bins

curr_fig = "12d"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF vs CDF Height(m) of Dragon Type Pokemon - - -\n')

b_num = 10
bin10, freq10 = my_hist_data(dragon_type_height, bins=b_num)
bin20, freq20 = my_hist_data(dragon_type_height, bins=b_num * 2)
bin30, freq30 = my_hist_data(dragon_type_height, bins=b_num * 3)

plt.figure()
plt.title(f"Figure {curr_fig}: PMF vs CDF Height(m) of Dragon Type Pokemon")
plt.plot(bin10, freq10, '-*')
plt.plot(bin20, freq20, ':o')
plt.plot(bin30, freq30, '-.v')
plt.legend(('10 bins', '20 bins', '30 bins'))
plt.xlabel('Height(m)')
plt.ylabel('Probability (Height(m))')
plt.show()

print(f'{separator + separator}\n')
# %%
### Non Dragon Type Pokemon
## Displaying height(m) distribution of all Non Dragon Type Pokemon

curr_fig = "13"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Height(m) distribution of Non Dragon Type Pokemon - - -\n')
print(basic_stats_string(not_dragon_type_height.describe(), "Height(m)"))

plt.figure()
# storing frequencies of different heights of non dragon type pokemon here
counts_nd = plt.hist(not_dragon_type_height, bins=100)
plt.xlabel('Height(m)')
plt.ylabel('Frequency')
plt.title(f' Figure {curr_fig}: Height(m) distribution of Non Dragon Type Pokemon')
plt.show()

print(f'{separator + separator}\n')

# %%
## PMF for height(m) of all Non Dragon Type Pokemon

curr_fig = "13b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of Non Dragon Type Pokemon - - -\n')

bin_center_nd = (counts_nd[1][1:] + counts_nd[1][:-1]) / 2
pmf_val_nd = counts_nd[0] / sum(counts_nd[0])

plt.figure()
plt.bar(bin_center_nd, pmf_val_nd, width=.2)
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.title(f'Figure {curr_fig}: PMF: Height(m) of Non Dragon Type Pokemon')
plt.show()

print(f'{separator + separator}\n')

# %%
## CDF plot using sort function - Non Dragon Types

curr_fig = "13c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: CDF: Height(m) of Non Dragon Type Pokemon - - -\n')
print(basic_stats_string(prob_h_nd_stats, "Probability ( Height(m) <= x)"))

plt.figure()
plt.plot(not_dragon_heights_sorted, prob_h_nd)
plt.title(f"Figure {curr_fig}: CDF: Height(m) of Non Dragon Type Pokemon")
plt.xlabel('Height(m)')
plt.ylabel('P(height $\leq$ x)')
plt.show()

print(f'{separator + separator}\n')

# %%
## Calculating CDF Dragon vs Non Dragon Types Height(m)

curr_fig = "14"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: CDF: Height(m) of Dragon vs Non Dragon Type Pokemon - - -\n')

plt.figure()
plt.plot(dragon_heights_sorted, d_cdf, '-b',
         not_dragon_heights_sorted, n_d_cdf, 'r--')

plt.title(f"Figure {curr_fig}: CDF: Height(m) of Dragon vs Non Dragon Type Pokemon")
plt.legend(('Dragon Type', 'Not Dragon Type'))

plt.xlabel('Height(m)')
plt.ylabel('Probability (Height(m))')
plt.show()

print(f'{separator + separator}\n')

# %%
## PMF For height of Dragon vs all Pokemon

curr_fig = "15"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of Dragon vs all Pokemon - - -\n')

plt.figure()
plt.title(f"Figure {curr_fig}: PMF: Height(m) of Dragon vs all Pokemon")
plt.plot(bin_center_d, counts_d[0] / len(dragon_types), '-o')
plt.plot(bin_center, counts_a[0] / num_pokemon, '-+')
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.legend(('Dragon Type', 'All Pokemon'))
plt.show()

print(f'{separator + separator}\n')

# %%
## PMF For height of Dragon vs Not Dragon Pokemon

curr_fig = "16"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: PMF: Height(m) of Dragon vs Non Dragon Type Pokemon - - -\n')

plt.figure()
plt.title(f"Figure {curr_fig}: PMF: Height(m) of Dragon vs Non Dragon Type Pokemon")
plt.plot(bin_center_d, counts_d[0] / len(dragon_types), '-o')
plt.plot(bin_center_nd, counts_nd[0] / len(not_dragon_type), '-+')
plt.xlabel('Height(m)')
plt.ylabel('Probability')
plt.legend(('Dragon Type', 'Not Dragon Type'))
plt.show()

print(f'{separator + separator}\n')

# %%
## t-test going up means more likely to be a Dragon

d_c_test = counts_d[0] / len(dragon_types)
nd_c_test = counts_nd[0] / len(not_dragon_type)
ttest_dragon_height = d_c_test - nd_c_test
ttdh_tval = scipy.stats.ttest_ind(d_c_test, nd_c_test)
ttdh_statisticval = ttdh_tval.statistic
ttdh_pval = ttdh_tval.pvalue

curr_fig = "17"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: T-Test: Do Dragon Types tend to be taller than Non Dragon Types - - -\n')

print(f'{tab * 4}T Test Values:')
print(f'{tab * 5}Statistic: {round(ttdh_statisticval, 3)}\n{tab * 5}P Value: {round(ttdh_pval, 3)}\n')

if ttdh_pval > .05:
    print(f"{tab * 4}Accept the null Hypothesis!")
else:
    print(f"{tab * 4}Reject the null Hypothesis!")

print(f"{tab * 5}{dh_null_hypothesis}\n")

plt.figure()

plt.bar(bin_center_nd, ttest_dragon_height)
plt.title(f"Figure {curr_fig}: Do Dragon Types tend to be taller than Non Dragon Types")
plt.xlabel(f'Height(m)')
plt.ylabel(f'P[Dragon] - P[Not Dragon]')

plt.show()

print(f'{separator + separator}\n')

# %%
### Is Pokemon data actually normally distributed?

## Normal Probability of pokemon heights

print(f'{separator + separator}\n')
print(f'{tab * 2}Normal Probability of pokemon heights, Is Pokemon data actually normally distributed?\n')

curr_fig = "18"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Distribution of Pokemon Height(m) - - -\n')
print(f'{tab * 4}Same as Figure 11! It is here for easier reference.')
print(basic_stats_string(height_stats, "Height(m)"))

plt.figure()

plot_hist(height, title="Figure {curr_fig}: Normal Distribution of Pokemon Height(m)", xlabel="Height(m)",
          ylabel="Frequency", bins=100)

plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "18b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal probablity of Pokemon Heights(m) - - -\n')

plt.figure()
plot_norm_prob(height, ylabel='Height(m)', title='Figure {curr_fig}: Normal probablity of Pokemon Heights(m)')
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "18c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal CDF of Pokemon Heights(m) - - -\n')
print(basic_stats_string(prob_h_stats, f"Probability(value <= Height(m)))"))

plt.figure()
plot_cdf(height, title=f"Figure {curr_fig}: Normal CDF of Pokemon Heights(m)", xlbl='Height(m)',
         ylbl='prob(value $\leq$ height)')
plt.show()

print(f'{separator + separator}\n')

# %%

curr_fig = "19"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal Distribution of Pokemon Height(m) (trimmed)- - -\n')
print(trim_data)
print(basic_stats_string(h2.describe(), "Height(m)"))

plt.figure()
plot_hist(h2, 'Figure {curr_fig}: Normal Distribution of Pokemon Height(m) (trimmed)', 'Height(m)')
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "19b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal probablity of Pokemon Height(m) (trimmed) - - -\n')
print(trim_data)

plt.figure()
plot_norm_prob(h2, ylabel='trimmed Heights(m)', title=f'Figure {curr_fig}: Normal probablity of Pokemon Height(m) (trimmed)')
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "19c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal CDF of Pokemon Height(m) (trimmed) - - -\n')
print(trim_data)
print(basic_stats_string(prob_h_trim_stats, f"Probability(value <=  Height(m)) (trimmed)"))

plt.figure()
plot_cdf(h2, title=f"Figure {curr_fig}: Normal CDF of Pokemon Height(m) (trimmed)", xlbl='Height(m)',
         ylbl='prob(value $\leq$ height)')
plt.show()

print(f'{separator + separator}\n')

# %%

curr_fig = "20"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal Distribution of Pokemon Height(m) (trimmed) (filtered) - - -\n')
print(trim_data)
print(filter_data)
print(basic_stats_string(filter_freq_data_stats, "Height(m) Frequencies (trimmed) (filtered)"))

plt.figure()
plt.title(f"Figure {curr_fig}: Normal Distribution of Pokemon Height(m) (trimmed) (filtered)")
plt.bar(filtered_heights[0], filtered_heights[1])
plt.xlabel("Height(m)")
plt.ylabel("Frequency")
plt.show()

print(f'{separator + separator}\n')

# %%

curr_fig = "21"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal distribution of Pokemon Height(m) - - -\n')
print(basic_stats_string(log_h.describe(), "log(Height(m))"))

plt.figure()
plot_hist(log_h, title=f'Figure {curr_fig}: Log Normal distribution of Pokemon Height(m)', xlabel='log(Height(m))', bins=20)
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "21b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal probablity plot of Pokemon Height(m) - - -\n')

plt.figure()

plot_norm_prob(log_h, title=f'Figure {curr_fig}: Log Normal probablity plot of Pokemon Height(m)', ylabel='log(Height(m))')

plt.show()

print(f'{separator + separator}\n')

# %%

curr_fig = "21c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: log Normal CDF of Pokemon Height(m) - - -\n')

plt.figure()
_, frequencies = plot_cdf(log_h, title="Figure {curr_fig}: log Normal CDF of Pokemon Height(m)", xlbl='log(Height(m))',
                             ylbl='Prob(value $\leq$ log(Height))')
plt.show()

freq_stats = pd.Series(frequencies).describe()
print(basic_stats_string(freq_stats, f"Probability(value <= log(Height(m)))"))

print(f'{separator + separator}\n')

# %%
### Plotting weight distribution

curr_fig = "22"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal distribution of Pokemon Weight(kg) - - -\n')
print(basic_stats_string(weight_stats, "Weight(kg)"))
plt.figure()
plot_hist(weight, f"Figure {curr_fig}: Normal distribution of Pokemon Weight(kg)", xlabel="Weight(kg)")
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "22b"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal probablity plot of Pokemon Weight(kg) - - -\n')

plt.figure()
plot_norm_prob(weight, ylabel='Weight(kg)', title=f'Figure {curr_fig}: Normal probablity plot of Pokemon Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "22c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Normal CDF of Pokemon Weight(kg) - - -\n')
print(basic_stats_string(prob_w_stats, f"Probability(value <= Weight(kg)))"))

plt.figure()
plot_cdf(height, title=f"Figure {curr_fig}: Normal CDF of Pokemon Weight(kg)", xlbl='Weight(kg)',
         ylbl='prob(value $\leq$ weight)')
plt.show()

print(f'{separator + separator}\n')
# %%

curr_fig = "23"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal distribution of Pokemon Heights(m) - - -\n')
print(basic_stats_string(log_w.describe(), "log(Weight(kg))"))

plt.figure()
plot_hist(log_w, xlabel='log(kg)', title=f'Figure {curr_fig}: Log Normal distribution of Pokemon Heights(m)')
plt.show()

print(f'{separator + separator}\n')

# %%

curr_fig = "23b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure 24b: Log Normal probablity plot of Pokemon Weight(kg) - - -\n')

plt.figure()
plot_norm_prob(log_w, ylabel='log(Weight(kg))', title='Figure 24b: Log Normal probablity plot of Pokemon Weight(kg)')
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "23c"
print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: Log Normal CDF of Pokemon Weight(kg) - - -\n')

plt.figure()

_, frequencies = plot_cdf(log_w, title=f"Figure {curr_fig}: Log Normal CDF of Pokemon Weight(kg)", xlbl='Weight(kg)',
                                   ylbl='prob(value $\leq$ weight)')

plt.show()

freq_stats = pd.Series(frequencies).describe()
print(basic_stats_string(freq_stats, f"Probability(value <= log(Weight(kg)))"))

print(f'{separator + separator}\n')

# %%

curr_fig = "24"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: - - -\n')

plt.figure()

dragon_types[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].boxplot()

plt.show()

print(f'{separator + separator}\n')
# %%

curr_fig = "24b"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: - - -\n')

plt.figure()
dragon_types[['weight_kg']].boxplot()
plt.show()

print(f'{separator + separator}\n')

# %%
curr_fig = "24c"

print(f'{separator + separator}\n')
print(f'{tab * 6}- - - Figure {curr_fig}: - - -\n')

plt.figure()
dragon_types[['height_m']].boxplot()
plt.show()

print(f'{separator + separator}\n')

# %%
## Calculating Correlation between Pokemon Height(m) and Weight(kg). (normal and log normal)

print(f'{separator + separator}\n')

print(f'{tab * 5}Calculating Correlation between Pokemon Height(m) and Weight(kg). (normal and log normal)\n')
print(f'{separator + separator}\n')

print(corr_compute(height, weight, "Height(m)", "Weight(kg)"))
print(corr_compute(log_h, weight, "log(Height(m))", "Weight(kg)"))
print(corr_compute(height, log_w, "Height(m)", "log(Weight(kg))"))
print(corr_compute(log_h, log_w, "log(Height(m))", "log(Weight(kg))"))

print(f'{separator + separator}\n')

# %%
## Using standard normal distrubtion for quick probabilty estimation for all pokemon heights (m) and weights (kg)

print(f'{separator + separator}\n')
print(f"\n{tab * 2}Using standard normal distrubtion for quick probabilty estimation for all pokemon Heights(m) and "
      f"Weights(kg).\n")
print(f'{separator + separator}\n')

# %%
### how many Pokemon heights are less than 7 meters

test_high = 7
high = (test_high - mean_h) / std_dev_h
p = scipy.stats.norm.cdf(high)

expected = p * len(height)
observed = (height < 7).sum()

print(f"{tab * 4}how many Pokemon heights are less than 7 meters\n")
print(f'{tab * 5}# expected: {round(expected)}/{len(height)}')
print(f'{tab * 5}# observed: {observed}/{len(height)}')
print("\n")

# %%
### How many heights are between 1.27 and 5.5 meters?

test_low = 1.27
test_high = 5.5

# get zcore of desired heights
low = (test_low - mean_h) / std_dev_h
high = (test_high - mean_h) / std_dev_h

p = scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low)
expected = p * len(height)
observed = ((height < 5.5) & (height > 1.27)).sum()

print(f"{tab * 4}How many Pokemon are between 1.27 and 5.5 meters?\n")
print(f'{tab * 5}# expected: {round(expected)}/{len(height)}')
print(f'{tab * 5}# observed: {observed}/{len(height)}')
print("\n")

# %%
### How many heights are greater than 2 meters?

test_low = 2
low = (test_low - mean_h) / std_dev_h

p = 1 - scipy.stats.norm.cdf(low)
expected = p * len(height)
observed = (height > 2).sum()

print(f"{tab * 4}How many Pokemon are taller than than 2 meters?\n")
print(f'{tab * 5}# expected: {round(expected)}/{len(height)}')
print(f'{tab * 5}# observed: {observed}/{len(height)}')
print("\n")

# %%
### What percentage of the Pokemon population is between 1 and 2 meters?

test_high = 2
test_low = 1
high = (test_high - mean_h) / std_dev_h
low = (test_low - mean_h) / std_dev_h

p = scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low)

print(f"{tab * 4}What percentage of the Pokemon population is between {test_low} and {test_high} meters?\n")
print(f'{tab * 5}-->: {round((100 * p), 2)}%')
print("\n")

# %%
### What percentage of the Pokemon population is heavier than 50kg?

test_low = 50
low = (test_low - mean_w) / std_dev_w
p = 1 - scipy.stats.norm.cdf(low)

print(f"{tab * 4}What percentage of the Pokemon population is heavier than  {test_low}kg?\n")
print(f'{tab * 5}-->: {round((100 * p), 2)}%')
print("\n")

# %%
### what percentage of the Pokemon population is heavier than 100kg?

test_low = 100
# more accurate estimate than just regular min and max
low = (test_low - mean_w) / std_dev_w
p = 1 - scipy.stats.norm.cdf(low)

print(f"{tab * 4}What percentage of the Pokemon population is heavier than {test_low}kg?\n")
print(f'{tab * 5}-->: {round((100 * p), 2)}%')
print("\n")
print(f'{separator + separator}\n')

# %%
## Verifying estimations with real data
print(f'{separator + separator}\n')
print(f"{tab * 10}Verifying estimations with real data\n")
print(f'{separator + separator}\n')

# %%
### What percentage of Pokemon are taller than 2.66807m (mean + (1 std_dev))

test_low = mean_h + std_dev_h
n = (height > test_low).sum()
p = n / len(height)

low = (test_low - mean_h) / std_dev_h
p2 = 1 - scipy.stats.norm.cdf(low)

print(f"{tab * 4}What percentage of Pokemon are taller than {round(test_low, 2)}m  (mean + (1 std.dev))\n")
print(f'{tab * 5}Actual: {n}/{len(height)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')
print("\n")

# %%
### What percentage of Dragon Pokemon are taller than 2.66807m  (pop_mean + (1 pop_std_dev))

test_low = mean_h + std_dev_h
n = (dragon_type_height > test_low).sum()
p = n / len(dragon_type_height)

low = (test_low - mean_dragon_h) / std_dev_dragon_h
p2 = 1 - scipy.stats.norm.cdf(low)

print(f"{tab * 4}What percentage of Dragon Pokemon are taller than {round(test_low, 2)}m  (pop_mean + pop_std.dev.)\n")
print(f'{tab * 5}Actual: {n}/{len(dragon_type_height)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')
print("\n")

# %%
### What percentage of Pokemon are heavier than 75kg

test_low = 75
n = (weight > test_low).sum()
p = n / len(weight)

low = (test_low - mean_w) / std_dev_w
p2 = 1 - scipy.stats.norm.cdf(low)

print(f"{tab * 4}What percentage of Pokemon are heavier than {test_low}kg\n")
print(f'{tab * 5}Actual: {n}/{len(weight)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')

print("\n")

# %%
### What percentage of Dragon Pokemon are heavier than 75kg

test_low = 75

n = (dragon_type_weight > test_low).sum()
p = n / len(dragon_type_weight)

low = (test_low - mean_dragon_w) / std_dev_dragon_w
p2 = 1 - scipy.stats.norm.cdf(low)

print(f"{tab * 4}What percentage of Dragon Type Pokemon are heavier than {test_low}kg\n")
print(f'{tab * 5}Actual: {n}/{len(dragon_type_weight)} = {round(100 * p, 3)}%')
print(f'{tab * 5}Theory: {round((100 * (1 - scipy.stats.norm.cdf(p))), 3)}%')
print(f'{tab * 5}Theory standardized: {round((100 * p2), 3)}%')
print("\n")

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

print(f"{tab * 4}What percentage of the Pokemon population is between {test_low} and {test_high}? (trimmed)\n")
print(f'{tab * 5}Answer: {n} / {len(h2)} = {round((100 * p), 3)}%')
print(f'{tab * 5}Theory: {round((100 * (scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low))), 3)}%\n')

# %%
print(f'{separator + separator}\n')
# sort by col value, here we are sorting first by type 1 in order a->z then speed highest -> lowest
# poke.sort_values(['Type 1', 'Speed'], ascending=[1, 1])


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
