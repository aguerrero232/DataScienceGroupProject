import pandas as pd
import numpy as np
import scipy.stats
import math
import helper_functions

poke = pd.read_csv('../data/pokedex.csv')
separator = '---------------------------------------------------------------'
tab: str = "\t"

# Pokemon population stats

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

# Important values

# -- Number of Pokemon in population ---
num_pokemon = len(poke)
# ---------------------------------------

# --- Grouping pokemon by type -----------------------------------------------------------------------------------
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


# --- Statistics for each Pokemon Type -----------
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


# ---- sample constants --------------------
# size of pokemon sampled from population
sample_size = 100
# number of times we sample the population
repeat_n = 1000
# -------------------------------------------


# --- samples --------------------------------------------------------------------------------------
sample_attack = np.random.choice(attack, (sample_size, repeat_n), replace=True)
sample_attack_mean = pd.DataFrame(sample_attack).describe().loc['mean']  # getting mean of each col
# ---------------------------------------------------------------------------------------------------


# --- samples stats -----------------------------------
# sample attack stats
sample_attack_stats = sample_attack_mean.describe()
# ------------------------------------------------------


# --- Z score transformation ------------------------------------------------
# zscores and zscore stats for pokemon stat values, height(m), and weight(kg)
z_hp = helper_functions.z_score(hp)
z_hp_stats = z_hp.describe()
z_attack = helper_functions.z_score(attack)
z_attack_stats = z_attack.describe()
z_defense = helper_functions.z_score(defense)
z_defense_stats = z_defense.describe()
z_sp_attack = helper_functions.z_score(sp_attack)
z_sp_attack_stats = z_sp_attack.describe()
z_sp_defense = helper_functions.z_score(sp_defense)
z_sp_defense_stats = z_sp_defense.describe()
z_speed = helper_functions.z_score(speed)
z_speed_stats = z_speed.describe()
z_weight = helper_functions.z_score(weight)
z_weight_stats = z_weight.describe()
z_height = helper_functions.z_score(height)
z_height_stats = z_height.describe()
# sample attack zscore and stats
z_attack_s = helper_functions.z_score(sample_attack_mean)
z_attack_stats_s = z_attack_s.describe()
# ------------------------------------------------------------------------------


# --- log normal distributions -
# normal log scale height
log_h = np.log(height)
# normal log scale weight
log_w = np.log(weight)
# ------------------------------


# --- basic stats for different sets from the population ---
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


# --- Getting Dragon and Non Dragon Types and collecting their various statistics --
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


# --- probailities of height --------------------------
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


# --- three groups of pokemon attack stats ----------------------------------------------
measures_attack = pd.DataFrame(np.random.choice(attack, (300, 3), replace=True))
g1_stats = measures_attack[0].describe()
g2_stats = measures_attack[1].describe()
g3_stats = measures_attack[2].describe()
# --- SEM for 3 groups of pokemon attack stats  ->  std / sqrt(len(group))
SEM_attack = np.std(measures_attack, 0) / math.sqrt(measures_attack.shape[0])
# --- 95% Confidence Interval ----------------------------------------------------------
ci95_attack = SEM_attack * 1.96
# ---------------------------------------------------------------------------------------


# --- using different number of bins to display dragon height dist ---------------
b_num = 10
# data for dragons
bin10_d, freq10_d = helper_functions.my_hist_data(dragon_type_height, bins=b_num)
bin20_d, freq20_d = helper_functions.my_hist_data(dragon_type_height, bins=b_num * 2)
bin30_d, freq30_d = helper_functions.my_hist_data(dragon_type_height, bins=b_num * 3)
# data for not dragons
bin10_nd, freq10_nd = helper_functions.my_hist_data(not_dragon_type_height, bins=b_num)
bin20_nd, freq20_nd = helper_functions.my_hist_data(not_dragon_type_height, bins=b_num * 2)
bin30_nd, freq30_nd = helper_functions.my_hist_data(not_dragon_type_height, bins=b_num * 3)
# --------------------------------------------------------------------------------

# --- Trimming Height Data ---------------------------------------------------------------------------
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


# --- Filtering Height Data ------------------------------------------------------
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
