import pandas as pd
import numpy as np
import scipy.stats
import math
import helper_functions

stat_cols = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']
physical_attr_cols = ['height_m', 'weight_kg']
separator = '---------------------------------------------------------------'
tab: str = "\t"

all_pokemon = pd.read_csv('../data/pokedex.csv').dropna(subset=(stat_cols + physical_attr_cols))

# ------------------------------------------------------------------------------------------------------------
# things well def need, gonna use this since its easy to use for just these cols
stat_values = all_pokemon[['pokedex_number', 'generation', 'name', 'type_1', 'type_2', 'height_m', 'weight_kg',
                           'ability_1', 'ability_2', 'ability_hidden',
                           'total_points', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed',
                           'is_sub_legendary', 'is_legendary', 'is_mythical']]
# ------------------------------------------------------------------------------------------------------------


# --- column labels for Pokemon ----------------------------------------------------------------
cols = list(stat_values.columns.values)  # name of colums in type dataframes
total_attr = len(cols)  # count of col labels
# ------------------------------------------------------------------------------------------------


# --- z score column labels for Pokemon ----------------------------------------------------------------------------
z_cols = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'total_points', 'weight_kg', 'height_m']
study_attr = len(z_cols)  # count of z col labels
# ------------------------------------------------------------------------------------------------------------------


# -- Number of Pokemon in population ---
num_pokemon = len(all_pokemon)
# ---------------------------------------


# ---------------------------------------
# Pokemon population relevant categories
total_points = all_pokemon['total_points']
hp = all_pokemon['hp']
speed = all_pokemon['speed']
attack = all_pokemon['attack']
sp_attack = all_pokemon['sp_attack']
defense = all_pokemon['defense']
sp_defense = all_pokemon['sp_defense']
height = all_pokemon['height_m']
weight = all_pokemon['weight_kg']
# ---------------------------------------


# --- Pokemon Pop Stats by category ------------
total_points_stats = total_points.describe()
hp_stats = hp.describe()
speed_stats = speed.describe()
attack_stats = attack.describe()
sp_attack_stats = sp_attack.describe()
defense_stats = defense.describe()
sp_defense_stats = sp_defense.describe()
height_stats = height.describe()
weight_stats = weight.describe()
# --------------------------------------------


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


# --- Z score transformation ------------------------------------------------
# zscores and zscore stats for pokemon stat values, height(m), and weight(kg)
z_total_points = helper_functions.z_score(total_points)
z_total_points_stats = z_total_points.describe()
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
# pokemon z scores
z_pokemon = helper_functions.z_score(all_pokemon[z_cols])
# pokemon type z scores
z_fire = helper_functions.z_score(fire_types[z_cols])
z_water = helper_functions.z_score(water_types[z_cols])
z_grass = helper_functions.z_score(grass_types[z_cols])

z_electric = helper_functions.z_score(electric_types[z_cols])
z_psychic = helper_functions.z_score(psychic_types[z_cols])
z_ghost = helper_functions.z_score(ghost_types[z_cols])

z_normal = helper_functions.z_score(normal_types[z_cols])
z_fighting = helper_functions.z_score(fighting_types[z_cols])
z_ice = helper_functions.z_score(ice_types[z_cols])

z_dark = helper_functions.z_score(dark_types[z_cols])
z_fairy = helper_functions.z_score(fairy_types[z_cols])
z_poison = helper_functions.z_score(poison_types[z_cols])

z_ground = helper_functions.z_score(ground_types[z_cols])
z_rock = helper_functions.z_score(rock_types[z_cols])
z_steel = helper_functions.z_score(steel_types[z_cols])

z_bug = helper_functions.z_score(bug_types[z_cols])
z_flying = helper_functions.z_score(flying_types[z_cols])
z_dragon = helper_functions.z_score(dragon_types[z_cols])
# ------------------------------------------------------------------------------


# ---- sample constants --------------------
# size of pokemon sampled from population
sample_size = 100
# number of times we sample the population
repeat_n = 1000
# -------------------------------------------


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
# dragon types
# already have list of all dragon types it is named dragon_types
dragon_type_height = dragon_types['height_m']
dragon_type_weight = dragon_types['weight_kg']
dragon_type_stat_values = dragon_types[cols[16:23]]
n_dragon_type = len(dragon_types)
dragon_heights_sorted = np.sort(dragon_type_height)
d_cdf = scipy.stats.norm.cdf(dragon_heights_sorted)
# non dragon types
not_dragon_type = all_pokemon.loc[(all_pokemon['type_1'] != "Dragon") & (all_pokemon['type_2'] != "Dragon")]
not_dragon_type_height = not_dragon_type['height_m']
not_dragon_type_weight = not_dragon_type['weight_kg']
not_dragon_type_stat_values = not_dragon_type[cols[16:23]]
n_not_dragon_type = len(not_dragon_type)
not_dragon_heights_sorted = np.sort(not_dragon_type_height)
n_d_cdf = scipy.stats.norm.cdf(not_dragon_heights_sorted)
# ----------------------------------------------------------------------------------


# --- Probabilities of height and weight -------------------------------------------------------------
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
# --------------------------------------------------------------------------------------------------


# --- using different number of bins to display dragon/non dragon height dist --------------------------
b_num = 10
# data for dragons
bin10_d, freq10_d = helper_functions.my_hist_data(dragon_type_height, bins=b_num)
bin20_d, freq20_d = helper_functions.my_hist_data(dragon_type_height, bins=b_num * 2)
bin30_d, freq30_d = helper_functions.my_hist_data(dragon_type_height, bins=b_num * 3)
# data for not dragons
bin10_nd, freq10_nd = helper_functions.my_hist_data(not_dragon_type_height, bins=b_num)
bin20_nd, freq20_nd = helper_functions.my_hist_data(not_dragon_type_height, bins=b_num * 2)
bin30_nd, freq30_nd = helper_functions.my_hist_data(not_dragon_type_height, bins=b_num * 3)
# ------------------------------------------------------------------------------------------------------


# --- Trimming Height Data ---------------------------------------------------------------------------
height_trim_low = .1
height_trim_high = 2.33

h2 = height[(height > height_trim_low) & (height < height_trim_high)]  # trimmed height

pokemon_trimmed_heights = all_pokemon[(all_pokemon['height_m'] > height_trim_low) &
                                      (all_pokemon['height_m'] < height_trim_high)]

z_pokemon_trimmed_height = helper_functions.z_score(pokemon_trimmed_heights)

prob_h_trim = (np.arange(len(h2)) + 1) / len(h2)
prob_h_trim_stats = pd.Series(prob_h_trim).describe()

trim_data_h = f"{tab * 4}Trimmed extreme Height(m) from Pokemon data\n" + \
              f'{tab * 5}min height = {height_trim_low}(m), max height = {height_trim_high}(m)\n' + \
              f'{tab * 5}Removed {num_pokemon - len(h2)} / {num_pokemon} = ' + \
              f'{round(((num_pokemon - len(h2)) / num_pokemon) * 100, 2)}% of cases\n' + \
              f'{tab * 5}{len(pokemon_trimmed_heights)} Pokemon Remain\n'
# -----------------------------------------------------------------------------------------------------


# --- Trimming Weight Data ---------------------------------------------------------------------------
weight_trim_low = 1
weight_trim_high = 300

# trimmed weight
pokemon_trimmed_weights = all_pokemon[(all_pokemon['weight_kg'] > weight_trim_low) &
                                      (all_pokemon['weight_kg'] < weight_trim_high)]

z_pokemon_trimmed_weight = helper_functions.z_score(pokemon_trimmed_weights)

prob_w_trim = (np.arange(len(pokemon_trimmed_weights[['weight_kg']])) + 1) / len(pokemon_trimmed_weights)
prob_w_trim_stats = pd.Series(prob_h_trim).describe()

trim_data_w = f"{tab * 4}Trimmed extreme Weight(kg) from Pokemon data\n" + \
              f'{tab * 5}min weight = {weight_trim_low}(kg), max weight = {weight_trim_high}(kg)\n' + \
              f'{tab * 5}Removed {num_pokemon - len(pokemon_trimmed_weights)} / {num_pokemon} = ' + \
              f'{round(((num_pokemon - len(pokemon_trimmed_weights)) / num_pokemon) * 100, 2)}% of cases\n' + \
              f'{tab * 5}{len(pokemon_trimmed_weights)} Pokemon Remain\n'
# -----------------------------------------------------------------------------------------------------


# --- Trimming Height and Weight Data ---------------------------------------------------------------------------
# trimmed height and weight
pokemon_trimmed_height_and_weight = all_pokemon[(all_pokemon['weight_kg'] > weight_trim_low) &
                                                (all_pokemon['weight_kg'] < weight_trim_high) &
                                                (all_pokemon['height_m'] > height_trim_low) &
                                                (all_pokemon['height_m'] < height_trim_high)]

z_pokemon_trimmed_height_and_weight = helper_functions.z_score(pokemon_trimmed_height_and_weight)

trim_data_h_w = f"{tab * 4}Trimmed extreme Height(m) and Weight(kg) from Pokemon data!\n" + \
                f'{tab * 5}min height = {height_trim_low}(m), max height = {height_trim_high}(m)\n' + \
                f'{tab * 5}min weight = {weight_trim_low}(kg), max weight = {weight_trim_high}(kg)\n' + \
                f'{tab * 5}Removed {num_pokemon - len(pokemon_trimmed_height_and_weight)} / {num_pokemon} = ' + \
                f'{round(((num_pokemon - len(pokemon_trimmed_height_and_weight)) / num_pokemon) * 100, 2)}%' \
                f' of cases\n' + \
                f'{tab * 5}{len(pokemon_trimmed_height_and_weight)} Pokemon Remain\n'
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
