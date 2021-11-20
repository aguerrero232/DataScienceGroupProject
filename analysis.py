#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
poke = pd.read_csv('pokedex.csv')

#%%

# grouping pokemon by type
fire_types = poke.loc[poke['type_1'] == "Fire"]
water_types = poke.loc[poke['type_1'] == "Water"]
grass_types = poke.loc[poke['type_1'] == "Grass"]
electric_types = poke.loc[poke['type_1'] == "Electric"]
normal_types = poke.loc[poke['type_1'] == "Normal"]
ground_types = poke.loc[poke['type_1'] == "Ground"]
rock_types = poke.loc[poke['type_1'] == "Rock"]
steel_types = poke.loc[poke['type_1'] == "Steel"]
ice_types = poke.loc[poke['type_1'] == "Ice"]
flying_types = poke.loc[poke['type_1'] == "Flying"]
fighting_types = poke.loc[poke['type_1'] == "Fighting"]
poison_types = poke.loc[poke['type_1'] == "Poison"]
psychic_types = poke.loc[poke['type_1'] == "Psychic"]
bug_types = poke.loc[poke['type_1'] == "Bug"]
ghost_types = poke.loc[poke['type_1'] == "Ghost"]
dark_types = poke.loc[poke['type_1'] == "Dark"]
dragon_types = poke.loc[poke['type_1'] == "Dragon"]
fairy_types = poke.loc[poke['type_1'] == "Fair"]


#%%
# fire types data analytics
gen1_fire = fire_types.loc[fire_types['generation'] == 1]
gen2_fire = fire_types.loc[fire_types['generation'] == 2]
gen3_fire = fire_types.loc[fire_types['generation'] == 3]
gen4_fire = fire_types.loc[fire_types['generation'] == 4]
gen5_fire = fire_types.loc[fire_types['generation'] == 5]
gen6_fire = fire_types.loc[fire_types['generation'] == 6]
gen7_fire = fire_types.loc[fire_types['generation'] == 7]
gen8_fire = fire_types.loc[fire_types['generation'] == 8]

stats_gen1_fire = gen1_fire.describe()
stats_gen2_fire = gen2_fire.describe()
stats_gen3_fire = gen3_fire.describe()
stats_gen4_fire = gen4_fire.describe()
stats_gen5_fire = gen5_fire.describe()
stats_gen6_fire = gen6_fire.describe()
stats_gen7_fire = gen7_fire.describe()
stats_gen8_fire = gen8_fire.describe()

#%%
# central limit theorem for attack
cli_attack = poke['attack']

# replace a with any of the following line to see different distributions
# a = np.random.randn(10**6)*5 +  175;


# mean of each column

# sampleMean = np.mean(cli_attack, axis=0)

# plt.hist(sampleMean)
# plt.hist(sampleMean)

# plotting bell curve for fire types
plt.figure()

plt.title("Fire Type pokemon base stats for Generation 1")
plt.hist(cli_attack)
plt.show()


#%%
# you can also read in by the chunk size incase your data set is extremely large
#  example:
#  for df in pd.read_csv("pokemon_data.csv", chunksize=5)
#       results = df.groupby(['Type 1']).count()
#
#       new_df = pd.concat([new_df, results])

#%%
#  printing certain column elements
# print(poke[['Name', 'Type 1', '#']])

#%%
# sort by col value, here we are sorting first by type 1 in order a->z then speed highest -> lowest
# poke.sort_values(['Type 1', 'Speed'], ascending=[1, 1])

#%%
# finds location that matched; here we find all pokemon with type 1 of fire
# print(poke.loc[poke['Type 1'] == "Fire" ] )

#%%
# # creating a new col of base stat totals
# poke["Stat Total"] = poke.iloc[:, 4:10].sum(axis=1)  #poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']
# cols = list(poke.columns.values)
# poke = poke[cols[0:10] + [cols[-1]] + cols[10:12]]
# modified = poke.to_csv('modified_pokemon.csv', index=False)
# print(count_type1)

#%%
# remove a collum
# poke = poke.drop(columns=["Stat Total"])
# print(poke.head(5))

#%%
# grouping by type1 with average attack
# type1_atk = poke[['Type 1', 'Attack']]
# avg_attack_by_type1 = type1_atk.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
# avg_attack_by_type1.rename(columns={'Attack': 'Avg. Atk.'}, inplace=True)
# avg_attack_by_type1.plot(kind='bar')
# plt.show()

#%%
