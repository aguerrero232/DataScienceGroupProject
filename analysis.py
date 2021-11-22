# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import math

poke = pd.read_csv('pokedex.csv')

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
        str_m = f'mean: {round(mean_plt,3)}, std: {round(std_plt,3)}'
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

#%%
## pokemon stats

total_points = poke['total_points']
hp = poke['hp']
speed = poke['speed']
attack = poke['attack']
sp_attack = poke['sp_attack']
defense = poke['defense']
sp_defense = poke['sp_defense']
height = poke['height_m']
weight = poke['weight_kg']

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

## grouping pokemon by type
fire_types = poke.loc[(poke['type_1'] == "Fire") | (poke['type_2'] == "Fire")]
water_types = poke.loc[(poke['type_1'] == "Water") | (poke['type_2'] == "Water")]
grass_types = poke.loc[(poke['type_1'] == "Grass") | (poke['type_2'] == "Grass")]
electric_types = poke.loc[(poke['type_1'] == "Electric") | (poke['type_2'] == "Electric")]
normal_types = poke.loc[(poke['type_1'] == "Normal") | (poke['type_2'] == "Normal")]
ground_types = poke.loc[(poke['type_1'] == "Ground") | (poke['type_2'] == "Ground")]
rock_types = poke.loc[(poke['type_1'] == "Rock") | (poke['type_2'] == "Rock")]
steel_types = poke.loc[(poke['type_1'] == "Steel") | (poke['type_2'] == "Steel")]
ice_types = poke.loc[(poke['type_1'] == "Ice") | (poke['type_2'] == "Ice")]
flying_types = poke.loc[(poke['type_1'] == "Flying") | (poke['type_2'] == "Flying")]
fighting_types = poke.loc[(poke['type_1'] == "Fighting") | (poke['type_2'] == "Fighting")]
poison_types = poke.loc[(poke['type_1'] == "Poison") | (poke['type_2'] == "Poison")]
psychic_types = poke.loc[(poke['type_1'] == "Psychic") | (poke['type_2'] == "Psychic")]
bug_types = poke.loc[(poke['type_1'] == "Bug") | (poke['type_2'] == "Bug")]
ghost_types = poke.loc[(poke['type_1'] == "Ghost") | (poke['type_2'] == "Ghost")]
dark_types = poke.loc[(poke['type_1'] == "Dark") | (poke['type_2'] == "Dark")]
dragon_types = poke.loc[(poke['type_1'] == "Dragon") | (poke['type_2'] == "Dragon")]
fairy_types = poke.loc[(poke['type_1'] == "Fairy") | (poke['type_2'] == "Fairy")]

stats_fire_types = fire_types.describe()

# stats_water_types = water_types.describe()

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

# %%
## central limit theorem for attack of all pokemon

#  attack stat distributions
cl_attack = poke['attack']

# 100 samples, repeated 1000 times.
attack_sample = np.random.choice(cl_attack, (100, 1000), replace=True)

# sample mean of each column
attack_sample_mean = pd.DataFrame(attack_sample).describe().loc['mean']

# plotting bell curve for pokemon attack distribution
plt.figure()

# plotting population mean
plotHist(cl_attack, "Pokemon Attack stat Distribution", 'attack stat', 'frequency', 'blue', 'red', False)

# plotting sample mean
plotHist(attack_sample_mean, 'Distribution of Attack Sample Mean(sample size = 100, Repeated 1000x)', 'attack',
         'frequency', 'blue', 'red', False)

# plt.hist(sampleMean)
plt.show()

# %%
## Z score transformation for attack stats
m = np.mean(cl_attack)
s = np.std(cl_attack)

zs = zscore(cl_attack)

# plotting population mean
plotHist(zs, "Pokemon Attack stat Distribution", 'attack stat Z Score', 'frequency', 'blue', 'red', True)
plt.show()
# %%
## original Attack against standardized plot
plt.scatter(cl_attack, zs)
plt.xlabel('Attack (atk)')
plt.ylabel('Z-score (unit-less)')
plt.title('Raw Attack value against standardized score')
plt.show()

# %%
##  Mean and standard error of the mean of Atk stat for three groups of data

measures = pd.DataFrame(np.random.choice(cl_attack, (300, 3), replace=True))
# SEM = std / sqrt(n)
SEM = np.std(measures, 0) / math.sqrt(measures.shape[0])

plt.errorbar([1, 2, 3], np.mean(measures, 0), SEM)
plt.xticks([1, 2, 3])
plt.xlabel('Sample group')
plt.ylabel('Mean $\pm$ SEM')
plt.title('Mean and SEM Atk stat for three groups of data (sample size = %d)' % measures.shape[0])
plt.show()

# %%
## calculating 95% Confidence interval for mean attack stats

plt.errorbar([1.05, 2.05, 3.05], np.mean(measures, 0), SEM)
plt.errorbar([1, 2, 3], np.mean(measures, 0), SEM * 1.96)
plt.xticks([1, 2, 3])
plt.xlabel('Sample group')
plt.ylabel('Mean and confidence interval')
plt.title('CI Atk stat for mean of 3 groups of data (sample size = %d)' % measures.shape[0])
plt.legend(('SEM', '95% CI'), loc=2)
plt.show()

#%%
## finding a correlation between hp and weight
z_hp = zscore(hp)
z_weight = zscore(weight)

# compute pearson correlation coefficient;
pcc_hp_weight = hp.corr(weight, method='pearson')

# compute spearman correlation coefficient;
scc_hp_weight = hp.corr(weight, method='spearman')

# compute kendal correlation coefficient;
kcc_hp_weight = hp.corr(weight, method='kendall')


#%%
## display correlation between hp and weight
plt.scatter(z_hp, z_weight)
plt.title(f"Corr HP/Weight| Pearson CC={round(pcc_hp_weight, 2)}, Spearman CC={round(scc_hp_weight, 2)}, Kendall CC={round(kcc_hp_weight, 2)}")
plt.xlabel('Z HP')
plt.ylabel('Z Weight')
plt.show()


#%%
## Getting Dragon and Non Dragon Types and collecting their heights
not_dragon_type = poke.loc[(poke['type_1'] != "Dragon") & (poke['type_2'] != "Dragon")]
num_pokemon = len(poke)
not_dragon_type_height = not_dragon_type['height_m']
dragon_type_height = dragon_types['height_m']


#%%
## Displaying height (m) distribution
counts = plt.hist(height, bins=100)
plt.xlabel('Height (m)')
plt.ylabel('Frequency')
plt.title('Pokemon Height Distribution')
plt.show()

#%%
## PMF For height of all Pokemon

bin_center = (counts[1][1:]+counts[1][:-1])/2
plt.bar(bin_center, (counts[0]/sum(counts[0])), width=.2)
plt.xlabel('Pokemon Height (m)')
plt.ylabel('Probability')
plt.title('PMF for Height of Pokemon')
plt.show()

# print('bin bondaries: ', counts[1])
# print('len(bin bondaries): ', len(counts[1]))
# print('counts: ', counts[0])
# print('len(counts): ', len(counts[0]))
#%%
## PMF For height of Dragon vs Not Dragon Pokemon
dragon_counts = plt.hist(dragon_type_height, bins=counts[1])
plt.close() # do not show fig; we just need counts from the hist func
not_dragon_counts = plt.hist(not_dragon_type_height, bins=counts[1])
plt.close() # do not show fig; we just need counts from the hist func

# line graph
plt.title("PMF Height of Dragon vs Not Dragon Type Pokemon")
plt.plot(bin_center, dragon_counts[0]/len(dragon_types), '-o',
         bin_center, not_dragon_counts[0]/len(not_dragon_type), '-+')
plt.xlabel('Height')
plt.ylabel('Probability')
plt.legend(('Dragon Type', 'Not Dragon Type'))

plt.show()

#%%
## Forgot what this type of graph is called but shows the probability dist (going down = more likely to be not Dragon
## and going up means more likely to be a Dragon)
plt.bar(bin_center, dragon_counts[0]/len(dragon_types) - not_dragon_counts[0]/len(not_dragon_type))
plt.xlabel('Height (m)')
plt.ylabel('P[Dragon] - P[Not Dragon]')
plt.show()


#%%
## Cumulative distribution function (CDF) probability that its behind the curve at the given bvalue

n_dragon_type = len(dragon_types)
n_not_dragon_type = len(not_dragon_type)
dragon_heights_sorted = np.sort(dragon_type_height)
not_dragon_heights_sorted = np.sort(not_dragon_type_height)
d = scipy.stats.norm.cdf(dragon_heights_sorted)
n_d = scipy.stats.norm.cdf(not_dragon_heights_sorted)

plt.plot(dragon_heights_sorted, d, '-b')
plt.plot(not_dragon_heights_sorted, n_d, 'r--')
plt.title("CDF Dragon Type vs Not Dragon Type Pokemon Height")
plt.legend(('Dragon Type', 'Not Dragon Type'))
plt.xlabel('Height')
plt.ylabel('Probability (Height)')
plt.show()

#%%
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

#%%
## CDF plot using sort function
prob = (np.arange(len(dragon_type_height))+1)/len(dragon_type_height)
plt.plot(np.sort(dragon_type_height), prob)
plt.title("CDF Dragon Type Height")
plt.xlabel('Height (m)')
plt.ylabel('P(height $\leq$ x)')
plt.show()

# %%
## Using standard normal distrubtion for quick probabilty estimation for all pokemon heights (m) and weights (kg)
print(height_stats)
print("\n")
### how many heights are less than 7 meters
p = scipy.stats.norm.cdf(7)
expected = p * len(height)
observed = (height < 7).sum()
print('# expected: %d / %d' % (expected, len(height)))
print('# observed: %d / %d' % (observed, len(height)))

#%%
### How many heights are between 2 and 15 meters?
p = scipy.stats.norm.cdf(15) - scipy.stats.norm.cdf(2)
expected = p * len(height)
observed = ((height < 15) & (height > 2)).sum()

print('# expected: %d / %d' % (expected, len(height)))
print('# observed: %d / %d' % (observed, len(height)))

#%%
### How many heights are greater than 2 meters?
p = 1 - scipy.stats.norm.cdf(2)

expected = p * len(height)
observed = (height > 2).sum()

print('# expected: %d / %d' % (expected, len(height)))
print('# observed: %d / %d' % (observed, len(height)))

#%%
### What percentage of the Pokemon population is between 1 and 2 meters?

test_high = 2
test_low = 1

std_dev_h = height_stats.loc['std']
mean_h = height_stats.loc['mean']

# more accurate estimate than just regular min and max
high = (test_high - mean_h) / std_dev_h
low = (test_low - mean_h) / std_dev_h
p = scipy.stats.norm.cdf(high) - scipy.stats.norm.cdf(low)
print('Answer: %.2f %%' % (100 * p))

#%%
### what percentage of the Pokemon population is heavier than 50kg?

test_low = 50

std_dev_w = weight_stats.loc['std']
mean_w = weight_stats.loc['mean']

# more accurate estimate than just regular min and max
low = (test_low - mean_w) / std_dev_w
p = 1 - scipy.stats.norm.cdf(low)
print('Answer: %.2f %%' % (100 * p))
#%%
### what percentage of the Pokemon population is heavier than 100kg?
test_low = 100

std_dev_w = weight_stats.loc['std']
mean_w = weight_stats.loc['mean']

# more accurate estimate than just regular min and max
low = (test_low - mean_w) / std_dev_w
p = 1 - scipy.stats.norm.cdf(low)
print('Answer: %.2f %%' % (100 * p))

#%%
## Verifying estimations with real data
### What percentage of Pokemon are taller than 2.66807m


n = (height > 2.66807).sum()
p = n / len(height)
print(f'Actual: {n}/{len(height)} = {round( 100*p ,3) }%')
print(f'Theory: {round( (100 * (1 - scipy.stats.norm.cdf(1))) ,3)}%')

#%%
### What percentage of Pokemon are heavier than 75kg

n = (weight > 75).sum()
p = n / len(weight)
print(f'Actual: {n}/{len(weight)} = {round( 100*p ,3) }%')
print(f'Theory: {round( (100*(1 - scipy.stats.norm.cdf(4))) ,3)}%')

#%%
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
