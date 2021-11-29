import loaddata
import pokemon_regression
import pokemon_stat_analysis
import pokemon_test_are_dragons_taller
import pokemon_normal_dist_and_actual_vals

separator_char = ", "
separator = '---------------------------------------------------------------'
tab: str = "\t"


def do_normal_dist_against_actual_values(options):
    data_set, type_set, stat_set = options[0], options[1], options[2]
    if data_set == "1":  # all pokemon
        set_name = "Pokemon"
        modifier = ''
        # grass pokemon
        if type_set == "1":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.grass_types['total_points']
                stat_stats = loaddata.grass_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.grass_types['hp']
                stat_stats = loaddata.grass_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.grass_types['speed']
                stat_stats = loaddata.grass_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.grass_types['attack']
                stat_stats = loaddata.grass_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.grass_types['defense']
                stat_stats = loaddata.grass_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.grass_types['sp_attack']
                stat_stats = loaddata.grass_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.grass_types['sp_defense']
                stat_stats = loaddata.grass_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.grass_types['height_m']
                stat_stats = loaddata.grass_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.grass_types['weight_kg']
                stat_stats = loaddata.grass_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # fire pokemon
        elif type_set == "2":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.fire_types['total_points']
                stat_stats = loaddata.fire_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.fire_types['hp']
                stat_stats = loaddata.fire_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.fire_types['speed']
                stat_stats = loaddata.fire_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.fire_types['attack']
                stat_stats = loaddata.fire_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.fire_types['defense']
                stat_stats = loaddata.fire_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.fire_types['sp_attack']
                stat_stats = loaddata.fire_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.fire_types['sp_defense']
                stat_stats = loaddata.fire_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.fire_types['height_m']
                stat_stats = loaddata.fire_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.fire_types['weight_kg']
                stat_stats = loaddata.fire_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # water pokemon
        elif type_set == "3":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.water_types['total_points']
                stat_stats = loaddata.water_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.water_types['hp']
                stat_stats = loaddata.water_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.water_types['speed']
                stat_stats = loaddata.water_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.water_types['attack']
                stat_stats = loaddata.water_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.water_types['defense']
                stat_stats = loaddata.water_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.water_types['sp_attack']
                stat_stats = loaddata.water_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.water_types['sp_defense']
                stat_stats = loaddata.water_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.water_types['height_m']
                stat_stats = loaddata.water_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.water_types['weight_kg']
                stat_stats = loaddata.water_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # electric pokemon
        elif type_set == "4":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.electric_types['total_points']
                stat_stats = loaddata.electric_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.electric_types['hp']
                stat_stats = loaddata.electric_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.electric_types['speed']
                stat_stats = loaddata.electric_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.electric_types['attack']
                stat_stats = loaddata.electric_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.electric_types['defense']
                stat_stats = loaddata.electric_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.electric_types['sp_attack']
                stat_stats = loaddata.electric_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.electric_types['sp_defense']
                stat_stats = loaddata.electric_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.electric_types['height_m']
                stat_stats = loaddata.electric_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.electric_types['weight_kg']
                stat_stats = loaddata.electric_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # psychic pokemon
        elif type_set == "5":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.psychic_types['total_points']
                stat_stats = loaddata.psychic_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.psychic_types['hp']
                stat_stats = loaddata.psychic_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.psychic_types['speed']
                stat_stats = loaddata.psychic_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.psychic_types['attack']
                stat_stats = loaddata.psychic_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.psychic_types['defense']
                stat_stats = loaddata.psychic_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.psychic_types['sp_attack']
                stat_stats = loaddata.psychic_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.psychic_types['sp_defense']
                stat_stats = loaddata.psychic_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.psychic_types['height_m']
                stat_stats = loaddata.psychic_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.psychic_types['weight_kg']
                stat_stats = loaddata.psychic_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # ice pokemon
        elif type_set == "6":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.ice_types['total_points']
                stat_stats = loaddata.ice_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.ice_types['hp']
                stat_stats = loaddata.ice_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.ice_types['speed']
                stat_stats = loaddata.ice_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.ice_types['attack']
                stat_stats = loaddata.ice_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.ice_types['defense']
                stat_stats = loaddata.ice_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.ice_types['sp_attack']
                stat_stats = loaddata.ice_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.ice_types['sp_defense']
                stat_stats = loaddata.ice_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.ice_types['height_m']
                stat_stats = loaddata.ice_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.ice_types['weight_kg']
                stat_stats = loaddata.ice_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # dragon pokemon
        elif type_set == "7":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.dragon_types['total_points']
                stat_stats = loaddata.dragon_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.dragon_types['hp']
                stat_stats = loaddata.dragon_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.dragon_types['speed']
                stat_stats = loaddata.dragon_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.dragon_types['attack']
                stat_stats = loaddata.dragon_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.dragon_types['defense']
                stat_stats = loaddata.dragon_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.dragon_types['sp_attack']
                stat_stats = loaddata.dragon_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.dragon_types['sp_defense']
                stat_stats = loaddata.dragon_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.dragon_types['height_m']
                stat_stats = loaddata.dragon_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.dragon_types['weight_kg']
                stat_stats = loaddata.dragon_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # dark pokemon
        elif type_set == "8":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.dark_types['total_points']
                stat_stats = loaddata.dark_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.dark_types['hp']
                stat_stats = loaddata.dark_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.dark_types['speed']
                stat_stats = loaddata.dark_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.dark_types['attack']
                stat_stats = loaddata.dark_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.dark_types['defense']
                stat_stats = loaddata.dark_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.dark_types['sp_attack']
                stat_stats = loaddata.dark_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.dark_types['sp_defense']
                stat_stats = loaddata.dark_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.dark_types['height_m']
                stat_stats = loaddata.dark_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.dark_types['weight_kg']
                stat_stats = loaddata.dark_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # fairy pokemon
        elif type_set == "9":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.fairy_types['total_points']
                stat_stats = loaddata.fairy_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.fairy_types['hp']
                stat_stats = loaddata.fairy_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.fairy_types['speed']
                stat_stats = loaddata.fairy_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.fairy_types['attack']
                stat_stats = loaddata.fairy_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.fairy_types['defense']
                stat_stats = loaddata.fairy_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.fairy_types['sp_attack']
                stat_stats = loaddata.fairy_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.fairy_types['sp_defense']
                stat_stats = loaddata.fairy_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.fairy_types['height_m']
                stat_stats = loaddata.fairy_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.fairy_types['weight_kg']
                stat_stats = loaddata.fairy_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # normal pokemon
        elif type_set == "10":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.normal_types['total_points']
                stat_stats = loaddata.normal_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.normal_types['hp']
                stat_stats = loaddata.normal_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.normal_types['speed']
                stat_stats = loaddata.normal_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.normal_types['attack']
                stat_stats = loaddata.normal_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.normal_types['defense']
                stat_stats = loaddata.normal_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.normal_types['sp_attack']
                stat_stats = loaddata.normal_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.normal_types['sp_defense']
                stat_stats = loaddata.normal_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.normal_types['height_m']
                stat_stats = loaddata.normal_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.normal_types['weight_kg']
                stat_stats = loaddata.normal_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # fighting pokemon
        elif type_set == "11":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.fighting_types['total_points']
                stat_stats = loaddata.fighting_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.fighting_types['hp']
                stat_stats = loaddata.fighting_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.fighting_types['speed']
                stat_stats = loaddata.fighting_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.fighting_types['attack']
                stat_stats = loaddata.fighting_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.fighting_types['defense']
                stat_stats = loaddata.fighting_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.fighting_types['sp_attack']
                stat_stats = loaddata.fighting_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.fighting_types['sp_defense']
                stat_stats = loaddata.fighting_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.fighting_types['height_m']
                stat_stats = loaddata.fighting_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.fighting_types['weight_kg']
                stat_stats = loaddata.fighting_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # flying pokemon
        elif type_set == "12":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.flying_types['total_points']
                stat_stats = loaddata.flying_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.flying_types['hp']
                stat_stats = loaddata.flying_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.flying_types['speed']
                stat_stats = loaddata.flying_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.flying_types['attack']
                stat_stats = loaddata.flying_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.flying_types['defense']
                stat_stats = loaddata.flying_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.flying_types['sp_attack']
                stat_stats = loaddata.flying_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.flying_types['sp_defense']
                stat_stats = loaddata.flying_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.flying_types['height_m']
                stat_stats = loaddata.flying_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.flying_types['weight_kg']
                stat_stats = loaddata.flying_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # poison pokemon
        elif type_set == "13":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.poison_types['total_points']
                stat_stats = loaddata.poison_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.poison_types['hp']
                stat_stats = loaddata.poison_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.poison_types['speed']
                stat_stats = loaddata.poison_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.poison_types['attack']
                stat_stats = loaddata.poison_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.poison_types['defense']
                stat_stats = loaddata.poison_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.poison_types['sp_attack']
                stat_stats = loaddata.poison_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.poison_types['sp_defense']
                stat_stats = loaddata.poison_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.poison_types['height_m']
                stat_stats = loaddata.poison_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.poison_types['weight_kg']
                stat_stats = loaddata.poison_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # ground pokemon
        elif type_set == "14":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.ground_types['total_points']
                stat_stats = loaddata.ground_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.ground_types['hp']
                stat_stats = loaddata.ground_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.ground_types['speed']
                stat_stats = loaddata.ground_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.ground_types['attack']
                stat_stats = loaddata.ground_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.ground_types['defense']
                stat_stats = loaddata.ground_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.ground_types['sp_attack']
                stat_stats = loaddata.ground_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.ground_types['sp_defense']
                stat_stats = loaddata.ground_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.ground_types['height_m']
                stat_stats = loaddata.ground_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.ground_types['weight_kg']
                stat_stats = loaddata.ground_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # rock pokemon
        elif type_set == "15":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.rock_types['total_points']
                stat_stats = loaddata.rock_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.rock_types['hp']
                stat_stats = loaddata.rock_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.rock_types['speed']
                stat_stats = loaddata.rock_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.rock_types['attack']
                stat_stats = loaddata.rock_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.rock_types['defense']
                stat_stats = loaddata.rock_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.rock_types['sp_attack']
                stat_stats = loaddata.rock_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.rock_types['sp_defense']
                stat_stats = loaddata.rock_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.rock_types['height_m']
                stat_stats = loaddata.rock_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.rock_types['weight_kg']
                stat_stats = loaddata.rock_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # bug pokemon
        elif type_set == "16":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.bug_types['total_points']
                stat_stats = loaddata.bug_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.bug_types['hp']
                stat_stats = loaddata.bug_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.bug_types['speed']
                stat_stats = loaddata.bug_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.bug_types['attack']
                stat_stats = loaddata.bug_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.bug_types['defense']
                stat_stats = loaddata.bug_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.bug_types['sp_attack']
                stat_stats = loaddata.bug_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.bug_types['sp_defense']
                stat_stats = loaddata.bug_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.bug_types['height_m']
                stat_stats = loaddata.bug_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.bug_types['weight_kg']
                stat_stats = loaddata.bug_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # ghost pokemon
        elif type_set == "17":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.ghost_types['total_points']
                stat_stats = loaddata.ghost_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.ghost_types['hp']
                stat_stats = loaddata.ghost_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.ghost_types['speed']
                stat_stats = loaddata.ghost_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.ghost_types['attack']
                stat_stats = loaddata.ghost_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.ghost_types['defense']
                stat_stats = loaddata.ghost_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.ghost_types['sp_attack']
                stat_stats = loaddata.ghost_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.ghost_types['sp_defense']
                stat_stats = loaddata.ghost_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.ghost_types['height_m']
                stat_stats = loaddata.ghost_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.ghost_types['weight_kg']
                stat_stats = loaddata.ghost_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # steel pokemon
        elif type_set == "18":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.steel_types['total_points']
                stat_stats = loaddata.steel_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.steel_types['hp']
                stat_stats = loaddata.steel_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.steel_types['speed']
                stat_stats = loaddata.steel_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.steel_types['attack']
                stat_stats = loaddata.steel_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.steel_types['defense']
                stat_stats = loaddata.steel_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.steel_types['sp_attack']
                stat_stats = loaddata.steel_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.steel_types['sp_defense']
                stat_stats = loaddata.steel_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.steel_types['height_m']
                stat_stats = loaddata.steel_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.steel_types['weight_kg']
                stat_stats = loaddata.steel_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # all pokemon
        elif type_set == "19":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.total_points
                stat_stats = loaddata.total_points_stats
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.hp
                stat_stats = loaddata.hp_stats
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.speed
                stat_stats = loaddata.speed_stats
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.attack
                stat_stats = loaddata.attack_stats
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.defense
                stat_stats = loaddata.defense_stats
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.sp_attack
                stat_stats = loaddata.sp_attack_stats
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.sp_defense
                stat_stats = loaddata.sp_defense_stats
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.heights
                stat_stats = loaddata.height_stats
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.weight
                stat_stats = loaddata.weight_stats
                unit = '(kg)'
            else:
                return
        else:
            return
    elif data_set == "2":  # trimmed pokemon
        set_name = "Pokemon"
        modifier = '(trimmed)'
        # grass pokemon
        if type_set == "1":

            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_grass_types['total_points']
                stat_stats = loaddata.trimmed_grass_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_grass_types['hp']
                stat_stats = loaddata.trimmed_grass_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_grass_types['speed']
                stat_stats = loaddata.trimmed_grass_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_grass_types['attack']
                stat_stats = loaddata.trimmed_grass_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_grass_types['defense']
                stat_stats = loaddata.trimmed_grass_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_grass_types['sp_attack']
                stat_stats = loaddata.trimmed_grass_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_grass_types['sp_defense']
                stat_stats = loaddata.trimmed_grass_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_grass_types['height_m']
                stat_stats = loaddata.trimmed_grass_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_grass_types['weight_kg']
                stat_stats = loaddata.trimmed_grass_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # fire pokemon
        elif type_set == "2":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_fire_types['total_points']
                stat_stats = loaddata.trimmed_fire_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fire_types['hp']
                stat_stats = loaddata.trimmed_fire_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fire_types['speed']
                stat_stats = loaddata.trimmed_fire_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fire_types['attack']
                stat_stats = loaddata.trimmed_fire_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fire_types['defense']
                stat_stats = loaddata.trimmed_fire_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fire_types['sp_attack']
                stat_stats = loaddata.trimmed_fire_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fire_types['sp_defense']
                stat_stats = loaddata.trimmed_fire_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_fire_types['height_m']
                stat_stats = loaddata.trimmed_fire_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_fire_types['weight_kg']
                stat_stats = loaddata.trimmed_fire_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # water pokemon
        elif type_set == "3":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_water_types['total_points']
                stat_stats = loaddata.trimmed_water_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_water_types['hp']
                stat_stats = loaddata.trimmed_water_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_water_types['speed']
                stat_stats = loaddata.trimmed_water_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_water_types['attack']
                stat_stats = loaddata.trimmed_water_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_water_types['defense']
                stat_stats = loaddata.trimmed_water_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_water_types['sp_attack']
                stat_stats = loaddata.trimmed_water_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_water_types['sp_defense']
                stat_stats = loaddata.trimmed_water_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_water_types['height_m']
                stat_stats = loaddata.trimmed_water_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_water_types['weight_kg']
                stat_stats = loaddata.trimmed_water_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # electric pokemon
        elif type_set == "4":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_electric_types['total_points']
                stat_stats = loaddata.trimmed_electric_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_electric_types['hp']
                stat_stats = loaddata.trimmed_electric_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_electric_types['speed']
                stat_stats = loaddata.trimmed_electric_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_electric_types['attack']
                stat_stats = loaddata.trimmed_electric_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_electric_types['defense']
                stat_stats = loaddata.trimmed_electric_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_electric_types['sp_attack']
                stat_stats = loaddata.trimmed_electric_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_electric_types['sp_defense']
                stat_stats = loaddata.trimmed_electric_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_electric_types['height_m']
                stat_stats = loaddata.trimmed_electric_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_electric_types['weight_kg']
                stat_stats = loaddata.trimmed_electric_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # psychic pokemon
        elif type_set == "5":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_psychic_types['total_points']
                stat_stats = loaddata.trimmed_psychic_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_psychic_types['hp']
                stat_stats = loaddata.trimmed_psychic_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_psychic_types['speed']
                stat_stats = loaddata.trimmed_psychic_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_psychic_types['attack']
                stat_stats = loaddata.trimmed_psychic_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_psychic_types['defense']
                stat_stats = loaddata.trimmed_psychic_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_psychic_types['sp_attack']
                stat_stats = loaddata.trimmed_psychic_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_psychic_types['sp_defense']
                stat_stats = loaddata.trimmed_psychic_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_psychic_types['height_m']
                stat_stats = loaddata.trimmed_psychic_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_psychic_types['weight_kg']
                stat_stats = loaddata.trimmed_psychic_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # ice pokemon
        elif type_set == "6":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_ice_types['total_points']
                stat_stats = loaddata.trimmed_ice_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ice_types['hp']
                stat_stats = loaddata.trimmed_ice_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ice_types['speed']
                stat_stats = loaddata.trimmed_ice_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ice_types['attack']
                stat_stats = loaddata.trimmed_ice_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ice_types['defense']
                stat_stats = loaddata.trimmed_ice_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ice_types['sp_attack']
                stat_stats = loaddata.trimmed_ice_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ice_types['sp_defense']
                stat_stats = loaddata.trimmed_ice_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_ice_types['height_m']
                stat_stats = loaddata.trimmed_ice_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_ice_types['weight_kg']
                stat_stats = loaddata.trimmed_ice_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # dragon pokemon
        elif type_set == "7":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_dragon_types['total_points']
                stat_stats = loaddata.trimmed_dragon_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dragon_types['hp']
                stat_stats = loaddata.trimmed_dragon_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dragon_types['speed']
                stat_stats = loaddata.trimmed_dragon_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dragon_types['attack']
                stat_stats = loaddata.trimmed_dragon_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dragon_types['defense']
                stat_stats = loaddata.trimmed_dragon_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dragon_types['sp_attack']
                stat_stats = loaddata.trimmed_dragon_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dragon_types['sp_defense']
                stat_stats = loaddata.trimmed_dragon_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_dragon_types['height_m']
                stat_stats = loaddata.trimmed_dragon_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_dragon_types['weight_kg']
                stat_stats = loaddata.trimmed_dragon_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # dark pokemon
        elif type_set == "8":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_dark_types['total_points']
                stat_stats = loaddata.trimmed_dark_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dark_types['hp']
                stat_stats = loaddata.trimmed_dark_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dark_types['speed']
                stat_stats = loaddata.trimmed_dark_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dark_types['attack']
                stat_stats = loaddata.trimmed_dark_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dark_types['defense']
                stat_stats = loaddata.trimmed_dark_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dark_types['sp_attack']
                stat_stats = loaddata.trimmed_dark_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_dark_types['sp_defense']
                stat_stats = loaddata.trimmed_dark_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_dark_types['height_m']
                stat_stats = loaddata.trimmed_dark_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_dark_types['weight_kg']
                stat_stats = loaddata.trimmed_dark_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # fairy pokemon
        elif type_set == "9":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_fairy_types['total_points']
                stat_stats = loaddata.trimmed_fairy_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fairy_types['hp']
                stat_stats = loaddata.trimmed_fairy_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fairy_types['speed']
                stat_stats = loaddata.trimmed_fairy_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fairy_types['attack']
                stat_stats = loaddata.trimmed_fairy_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fairy_types['defense']
                stat_stats = loaddata.trimmed_fairy_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fairy_types['sp_attack']
                stat_stats = loaddata.trimmed_fairy_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fairy_types['sp_defense']
                stat_stats = loaddata.trimmed_fairy_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_fairy_types['height_m']
                stat_stats = loaddata.trimmed_fairy_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_fairy_types['weight_kg']
                stat_stats = loaddata.trimmed_fairy_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # normal pokemon
        elif type_set == "10":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_normal_types['total_points']
                stat_stats = loaddata.trimmed_normal_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_normal_types['hp']
                stat_stats = loaddata.trimmed_normal_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_normal_types['speed']
                stat_stats = loaddata.trimmed_normal_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_normal_types['attack']
                stat_stats = loaddata.trimmed_normal_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_normal_types['defense']
                stat_stats = loaddata.trimmed_normal_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_normal_types['sp_attack']
                stat_stats = loaddata.trimmed_normal_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_normal_types['sp_defense']
                stat_stats = loaddata.trimmed_normal_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_normal_types['height_m']
                stat_stats = loaddata.trimmed_normal_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_normal_types['weight_kg']
                stat_stats = loaddata.trimmed_normal_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # fighting pokemon
        elif type_set == "11":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_fighting_types['total_points']
                stat_stats = loaddata.trimmed_fighting_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fighting_types['hp']
                stat_stats = loaddata.trimmed_fighting_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fighting_types['speed']
                stat_stats = loaddata.trimmed_fighting_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fighting_types['attack']
                stat_stats = loaddata.trimmed_fighting_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fighting_types['defense']
                stat_stats = loaddata.trimmed_fighting_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fighting_types['sp_attack']
                stat_stats = loaddata.trimmed_fighting_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_fighting_types['sp_defense']
                stat_stats = loaddata.trimmed_fighting_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_fighting_types['height_m']
                stat_stats = loaddata.trimmed_fighting_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_fighting_types['weight_kg']
                stat_stats = loaddata.trimmed_fighting_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # flying pokemon
        elif type_set == "12":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_flying_types['total_points']
                stat_stats = loaddata.trimmed_flying_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_flying_types['hp']
                stat_stats = loaddata.trimmed_flying_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_flying_types['speed']
                stat_stats = loaddata.trimmed_flying_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_flying_types['attack']
                stat_stats = loaddata.trimmed_flying_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_flying_types['defense']
                stat_stats = loaddata.trimmed_flying_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_flying_types['sp_attack']
                stat_stats = loaddata.trimmed_flying_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_flying_types['sp_defense']
                stat_stats = loaddata.trimmed_flying_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_flying_types['height_m']
                stat_stats = loaddata.trimmed_flying_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_flying_types['weight_kg']
                stat_stats = loaddata.trimmed_flying_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # poison pokemon
        elif type_set == "13":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_poison_types['total_points']
                stat_stats = loaddata.trimmed_poison_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_poison_types['hp']
                stat_stats = loaddata.trimmed_poison_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_poison_types['speed']
                stat_stats = loaddata.trimmed_poison_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_poison_types['attack']
                stat_stats = loaddata.trimmed_poison_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_poison_types['defense']
                stat_stats = loaddata.trimmed_poison_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_poison_types['sp_attack']
                stat_stats = loaddata.trimmed_poison_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_poison_types['sp_defense']
                stat_stats = loaddata.trimmed_poison_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_poison_types['height_m']
                stat_stats = loaddata.trimmed_poison_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_poison_types['weight_kg']
                stat_stats = loaddata.trimmed_poison_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # ground pokemon
        elif type_set == "14":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_ground_types['total_points']
                stat_stats = loaddata.trimmed_ground_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ground_types['hp']
                stat_stats = loaddata.trimmed_ground_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ground_types['speed']
                stat_stats = loaddata.trimmed_ground_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ground_types['attack']
                stat_stats = loaddata.trimmed_ground_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ground_types['defense']
                stat_stats = loaddata.trimmed_ground_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ground_types['sp_attack']
                stat_stats = loaddata.trimmed_ground_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ground_types['sp_defense']
                stat_stats = loaddata.trimmed_ground_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_ground_types['height_m']
                stat_stats = loaddata.trimmed_ground_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_ground_types['weight_kg']
                stat_stats = loaddata.trimmed_ground_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # rock pokemon
        elif type_set == "15":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_rock_types['total_points']
                stat_stats = loaddata.trimmed_rock_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_rock_types['hp']
                stat_stats = loaddata.trimmed_rock_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_rock_types['speed']
                stat_stats = loaddata.trimmed_rock_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_rock_types['attack']
                stat_stats = loaddata.trimmed_rock_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_rock_types['defense']
                stat_stats = loaddata.trimmed_rock_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_rock_types['sp_attack']
                stat_stats = loaddata.trimmed_rock_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_rock_types['sp_defense']
                stat_stats = loaddata.trimmed_rock_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_rock_types['height_m']
                stat_stats = loaddata.trimmed_rock_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_rock_types['weight_kg']
                stat_stats = loaddata.trimmed_rock_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # bug pokemon
        elif type_set == "16":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_bug_types['total_points']
                stat_stats = loaddata.trimmed_bug_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_bug_types['hp']
                stat_stats = loaddata.trimmed_bug_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_bug_types['speed']
                stat_stats = loaddata.trimmed_bug_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_bug_types['attack']
                stat_stats = loaddata.trimmed_bug_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_bug_types['defense']
                stat_stats = loaddata.trimmed_bug_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_bug_types['sp_attack']
                stat_stats = loaddata.trimmed_bug_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_bug_types['sp_defense']
                stat_stats = loaddata.trimmed_bug_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_bug_types['height_m']
                stat_stats = loaddata.trimmed_bug_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_bug_types['weight_kg']
                stat_stats = loaddata.trimmed_bug_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # ghost pokemon
        elif type_set == "17":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_ghost_types['total_points']
                stat_stats = loaddata.trimmed_ghost_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ghost_types['hp']
                stat_stats = loaddata.trimmed_ghost_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ghost_types['speed']
                stat_stats = loaddata.trimmed_ghost_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ghost_types['attack']
                stat_stats = loaddata.trimmed_ghost_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ghost_types['defense']
                stat_stats = loaddata.trimmed_ghost_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ghost_types['sp_attack']
                stat_stats = loaddata.trimmed_ghost_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_ghost_types['sp_defense']
                stat_stats = loaddata.trimmed_ghost_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_ghost_types['height_m']
                stat_stats = loaddata.trimmed_ghost_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_ghost_types['weight_kg']
                stat_stats = loaddata.trimmed_ghost_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # steel pokemon
        elif type_set == "18":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_steel_types['total_points']
                stat_stats = loaddata.trimmed_steel_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_steel_types['hp']
                stat_stats = loaddata.trimmed_steel_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_steel_types['speed']
                stat_stats = loaddata.trimmed_steel_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_steel_types['attack']
                stat_stats = loaddata.trimmed_steel_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_steel_types['defense']
                stat_stats = loaddata.trimmed_steel_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_steel_types['sp_attack']
                stat_stats = loaddata.trimmed_steel_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_steel_types['sp_defense']
                stat_stats = loaddata.trimmed_steel_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_steel_types['height_m']
                stat_stats = loaddata.trimmed_steel_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_steel_types['weight_kg']
                stat_stats = loaddata.trimmed_steel_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
        # all pokemon (trimmed h & w)
        elif type_set == "19":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.trimmed_total_points
                stat_stats = loaddata.trimmed_total_points_stats
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_hp
                stat_stats = loaddata.trimmed_hp_stats
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_speed
                stat_stats = loaddata.trimmed_speed_stats
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_attack
                stat_stats = loaddata.trimmed_attack_stats
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_defense
                stat_stats = loaddata.trimmed_defense_stats
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_sp_attack
                stat_stats = loaddata.trimmed_sp_attack_stats
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.trimmed_sp_defense
                stat_stats = loaddata.trimmed_sp_defense_stats
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.trimmed_height
                stat_stats = loaddata.trimmed_height_stats
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.trimmed_weight
                stat_stats = loaddata.trimmed_weight_stats
                unit = '(kg)'
            else:
                return
        else:
            return
    elif data_set == "3":  # non legendary pokemon
        set_name = "Non Legendary Pokemon"
        modifier = '(non legendary)'
        if type_set == "1":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_grass_types['total_points']
                stat_stats = loaddata.non_legendary_grass_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_grass_types['hp']
                stat_stats = loaddata.non_legendary_grass_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_grass_types['speed']
                stat_stats = loaddata.non_legendary_grass_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_grass_types['attack']
                stat_stats = loaddata.non_legendary_grass_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_grass_types['defense']
                stat_stats = loaddata.non_legendary_grass_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_grass_types['sp_attack']
                stat_stats = loaddata.non_legendary_grass_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_grass_types['sp_defense']
                stat_stats = loaddata.non_legendary_grass_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_grass_types['height_m']
                stat_stats = loaddata.non_legendary_grass_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_grass_types['weight_kg']
                stat_stats = loaddata.non_legendary_grass_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # fire pokemon
        elif type_set == "2":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_fire_types['total_points']
                stat_stats = loaddata.non_legendary_fire_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fire_types['hp']
                stat_stats = loaddata.non_legendary_fire_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fire_types['speed']
                stat_stats = loaddata.non_legendary_fire_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fire_types['attack']
                stat_stats = loaddata.non_legendary_fire_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fire_types['defense']
                stat_stats = loaddata.non_legendary_fire_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fire_types['sp_attack']
                stat_stats = loaddata.non_legendary_fire_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fire_types['sp_defense']
                stat_stats = loaddata.non_legendary_fire_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_fire_types['height_m']
                stat_stats = loaddata.non_legendary_fire_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_fire_types['weight_kg']
                stat_stats = loaddata.non_legendary_fire_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # water pokemon
        elif type_set == "3":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_water_types['total_points']
                stat_stats = loaddata.non_legendary_water_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_water_types['hp']
                stat_stats = loaddata.non_legendary_water_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_water_types['speed']
                stat_stats = loaddata.non_legendary_water_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_water_types['attack']
                stat_stats = loaddata.non_legendary_water_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_water_types['defense']
                stat_stats = loaddata.non_legendary_water_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_water_types['sp_attack']
                stat_stats = loaddata.non_legendary_water_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_water_types['sp_defense']
                stat_stats = loaddata.non_legendary_water_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_water_types['height_m']
                stat_stats = loaddata.non_legendary_water_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_water_types['weight_kg']
                stat_stats = loaddata.non_legendary_water_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # electric pokemon
        elif type_set == "4":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_electric_types['total_points']
                stat_stats = loaddata.non_legendary_electric_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_electric_types['hp']
                stat_stats = loaddata.non_legendary_electric_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_electric_types['speed']
                stat_stats = loaddata.non_legendary_electric_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_electric_types['attack']
                stat_stats = loaddata.non_legendary_electric_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_electric_types['defense']
                stat_stats = loaddata.non_legendary_electric_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_electric_types['sp_attack']
                stat_stats = loaddata.non_legendary_electric_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_electric_types['sp_defense']
                stat_stats = loaddata.non_legendary_electric_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_electric_types['height_m']
                stat_stats = loaddata.non_legendary_electric_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_electric_types['weight_kg']
                stat_stats = loaddata.non_legendary_electric_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # psychic pokemon
        elif type_set == "5":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_psychic_types['total_points']
                stat_stats = loaddata.non_legendary_psychic_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_psychic_types['hp']
                stat_stats = loaddata.non_legendary_psychic_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_psychic_types['speed']
                stat_stats = loaddata.non_legendary_psychic_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_psychic_types['attack']
                stat_stats = loaddata.non_legendary_psychic_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_psychic_types['defense']
                stat_stats = loaddata.non_legendary_psychic_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_psychic_types['sp_attack']
                stat_stats = loaddata.non_legendary_psychic_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_psychic_types['sp_defense']
                stat_stats = loaddata.non_legendary_psychic_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_psychic_types['height_m']
                stat_stats = loaddata.non_legendary_psychic_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_psychic_types['weight_kg']
                stat_stats = loaddata.non_legendary_psychic_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # ice pokemon
        elif type_set == "6":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_ice_types['total_points']
                stat_stats = loaddata.non_legendary_ice_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ice_types['hp']
                stat_stats = loaddata.non_legendary_ice_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ice_types['speed']
                stat_stats = loaddata.non_legendary_ice_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ice_types['attack']
                stat_stats = loaddata.non_legendary_ice_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ice_types['defense']
                stat_stats = loaddata.non_legendary_ice_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ice_types['sp_attack']
                stat_stats = loaddata.non_legendary_ice_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ice_types['sp_defense']
                stat_stats = loaddata.non_legendary_ice_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_ice_types['height_m']
                stat_stats = loaddata.non_legendary_ice_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_ice_types['weight_kg']
                stat_stats = loaddata.non_legendary_ice_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # dragon pokemon
        elif type_set == "7":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_dragon_types['total_points']
                stat_stats = loaddata.non_legendary_dragon_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dragon_types['hp']
                stat_stats = loaddata.non_legendary_dragon_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dragon_types['speed']
                stat_stats = loaddata.non_legendary_dragon_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dragon_types['attack']
                stat_stats = loaddata.non_legendary_dragon_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dragon_types['defense']
                stat_stats = loaddata.non_legendary_dragon_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dragon_types['sp_attack']
                stat_stats = loaddata.non_legendary_dragon_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dragon_types['sp_defense']
                stat_stats = loaddata.non_legendary_dragon_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_dragon_types['height_m']
                stat_stats = loaddata.non_legendary_dragon_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_dragon_types['weight_kg']
                stat_stats = loaddata.non_legendary_dragon_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # dark pokemon
        elif type_set == "8":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_dark_types['total_points']
                stat_stats = loaddata.non_legendary_dark_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dark_types['hp']
                stat_stats = loaddata.non_legendary_dark_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dark_types['speed']
                stat_stats = loaddata.non_legendary_dark_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dark_types['attack']
                stat_stats = loaddata.non_legendary_dark_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dark_types['defense']
                stat_stats = loaddata.non_legendary_dark_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dark_types['sp_attack']
                stat_stats = loaddata.non_legendary_dark_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_dark_types['sp_defense']
                stat_stats = loaddata.non_legendary_dark_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_dark_types['height_m']
                stat_stats = loaddata.non_legendary_dark_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_dark_types['weight_kg']
                stat_stats = loaddata.non_legendary_dark_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # fairy pokemon
        elif type_set == "9":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_fairy_types['total_points']
                stat_stats = loaddata.non_legendary_fairy_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fairy_types['hp']
                stat_stats = loaddata.non_legendary_fairy_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fairy_types['speed']
                stat_stats = loaddata.non_legendary_fairy_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fairy_types['attack']
                stat_stats = loaddata.non_legendary_fairy_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fairy_types['defense']
                stat_stats = loaddata.non_legendary_fairy_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fairy_types['sp_attack']
                stat_stats = loaddata.non_legendary_fairy_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fairy_types['sp_defense']
                stat_stats = loaddata.non_legendary_fairy_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_fairy_types['height_m']
                stat_stats = loaddata.non_legendary_fairy_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_fairy_types['weight_kg']
                stat_stats = loaddata.non_legendary_fairy_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # normal pokemon
        elif type_set == "10":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_normal_types['total_points']
                stat_stats = loaddata.non_legendary_normal_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_normal_types['hp']
                stat_stats = loaddata.non_legendary_normal_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_normal_types['speed']
                stat_stats = loaddata.non_legendary_normal_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_normal_types['attack']
                stat_stats = loaddata.non_legendary_normal_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_normal_types['defense']
                stat_stats = loaddata.non_legendary_normal_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_normal_types['sp_attack']
                stat_stats = loaddata.non_legendary_normal_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_normal_types['sp_defense']
                stat_stats = loaddata.non_legendary_normal_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_normal_types['height_m']
                stat_stats = loaddata.non_legendary_normal_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_normal_types['weight_kg']
                stat_stats = loaddata.non_legendary_normal_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # fighting pokemon
        elif type_set == "11":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_fighting_types['total_points']
                stat_stats = loaddata.non_legendary_fighting_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fighting_types['hp']
                stat_stats = loaddata.non_legendary_fighting_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fighting_types['speed']
                stat_stats = loaddata.non_legendary_fighting_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fighting_types['attack']
                stat_stats = loaddata.non_legendary_fighting_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fighting_types['defense']
                stat_stats = loaddata.non_legendary_fighting_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fighting_types['sp_attack']
                stat_stats = loaddata.non_legendary_fighting_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_fighting_types['sp_defense']
                stat_stats = loaddata.non_legendary_fighting_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_fighting_types['height_m']
                stat_stats = loaddata.non_legendary_fighting_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_fighting_types['weight_kg']
                stat_stats = loaddata.non_legendary_fighting_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # flying pokemon
        elif type_set == "12":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_flying_types['total_points']
                stat_stats = loaddata.non_legendary_flying_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_flying_types['hp']
                stat_stats = loaddata.non_legendary_flying_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_flying_types['speed']
                stat_stats = loaddata.non_legendary_flying_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_flying_types['attack']
                stat_stats = loaddata.non_legendary_flying_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_flying_types['defense']
                stat_stats = loaddata.non_legendary_flying_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_flying_types['sp_attack']
                stat_stats = loaddata.non_legendary_flying_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_flying_types['sp_defense']
                stat_stats = loaddata.non_legendary_flying_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_flying_types['height_m']
                stat_stats = loaddata.non_legendary_flying_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_flying_types['weight_kg']
                stat_stats = loaddata.non_legendary_flying_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # poison pokemon
        elif type_set == "13":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_poison_types['total_points']
                stat_stats = loaddata.non_legendary_poison_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_poison_types['hp']
                stat_stats = loaddata.non_legendary_poison_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_poison_types['speed']
                stat_stats = loaddata.non_legendary_poison_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_poison_types['attack']
                stat_stats = loaddata.non_legendary_poison_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_poison_types['defense']
                stat_stats = loaddata.non_legendary_poison_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_poison_types['sp_attack']
                stat_stats = loaddata.non_legendary_poison_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_poison_types['sp_defense']
                stat_stats = loaddata.non_legendary_poison_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_poison_types['height_m']
                stat_stats = loaddata.non_legendary_poison_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_poison_types['weight_kg']
                stat_stats = loaddata.non_legendary_poison_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # ground pokemon
        elif type_set == "14":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_ground_types['total_points']
                stat_stats = loaddata.non_legendary_ground_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ground_types['hp']
                stat_stats = loaddata.non_legendary_ground_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ground_types['speed']
                stat_stats = loaddata.non_legendary_ground_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ground_types['attack']
                stat_stats = loaddata.non_legendary_ground_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ground_types['defense']
                stat_stats = loaddata.non_legendary_ground_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ground_types['sp_attack']
                stat_stats = loaddata.non_legendary_ground_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ground_types['sp_defense']
                stat_stats = loaddata.non_legendary_ground_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_ground_types['height_m']
                stat_stats = loaddata.non_legendary_ground_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_ground_types['weight_kg']
                stat_stats = loaddata.non_legendary_ground_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # rock pokemon
        elif type_set == "15":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_rock_types['total_points']
                stat_stats = loaddata.non_legendary_rock_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_rock_types['hp']
                stat_stats = loaddata.non_legendary_rock_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_rock_types['speed']
                stat_stats = loaddata.non_legendary_rock_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_rock_types['attack']
                stat_stats = loaddata.non_legendary_rock_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_rock_types['defense']
                stat_stats = loaddata.non_legendary_rock_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_rock_types['sp_attack']
                stat_stats = loaddata.non_legendary_rock_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_rock_types['sp_defense']
                stat_stats = loaddata.non_legendary_rock_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_rock_types['height_m']
                stat_stats = loaddata.non_legendary_rock_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_rock_types['weight_kg']
                stat_stats = loaddata.non_legendary_rock_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # bug pokemon
        elif type_set == "16":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_bug_types['total_points']
                stat_stats = loaddata.non_legendary_bug_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_bug_types['hp']
                stat_stats = loaddata.non_legendary_bug_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_bug_types['speed']
                stat_stats = loaddata.non_legendary_bug_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_bug_types['attack']
                stat_stats = loaddata.non_legendary_bug_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_bug_types['defense']
                stat_stats = loaddata.non_legendary_bug_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_bug_types['sp_attack']
                stat_stats = loaddata.non_legendary_bug_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_bug_types['sp_defense']
                stat_stats = loaddata.non_legendary_bug_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_bug_types['height_m']
                stat_stats = loaddata.non_legendary_bug_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_bug_types['weight_kg']
                stat_stats = loaddata.non_legendary_bug_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # ghost pokemon
        elif type_set == "17":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_ghost_types['total_points']
                stat_stats = loaddata.non_legendary_ghost_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ghost_types['hp']
                stat_stats = loaddata.non_legendary_ghost_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ghost_types['speed']
                stat_stats = loaddata.non_legendary_ghost_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ghost_types['attack']
                stat_stats = loaddata.non_legendary_ghost_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ghost_types['defense']
                stat_stats = loaddata.non_legendary_ghost_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ghost_types['sp_attack']
                stat_stats = loaddata.non_legendary_ghost_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_ghost_types['sp_defense']
                stat_stats = loaddata.non_legendary_ghost_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_ghost_types['height_m']
                stat_stats = loaddata.non_legendary_ghost_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_ghost_types['weight_kg']
                stat_stats = loaddata.non_legendary_ghost_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # steel pokemon
        elif type_set == "18":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_steel_types['total_points']
                stat_stats = loaddata.non_legendary_steel_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_steel_types['hp']
                stat_stats = loaddata.non_legendary_steel_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_steel_types['speed']
                stat_stats = loaddata.non_legendary_steel_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_steel_types['attack']
                stat_stats = loaddata.non_legendary_steel_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_steel_types['defense']
                stat_stats = loaddata.non_legendary_steel_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_steel_types['sp_attack']
                stat_stats = loaddata.non_legendary_steel_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_steel_types['sp_defense']
                stat_stats = loaddata.non_legendary_steel_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_steel_types['height_m']
                stat_stats = loaddata.non_legendary_steel_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_steel_types['weight_kg']
                stat_stats = loaddata.non_legendary_steel_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # all pokemon (trimmed h & w)
        elif type_set == "19":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.non_legendary_total_points
                stat_stats = loaddata.non_legendary_total_points_stats
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_hp
                stat_stats = loaddata.non_legendary_hp_stats
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_speed
                stat_stats = loaddata.non_legendary_speed_stats
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_attack
                stat_stats = loaddata.non_legendary_attack_stats
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_defense
                stat_stats = loaddata.non_legendary_defense_stats
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_sp_attack
                stat_stats = loaddata.non_legendary_sp_attack_stats
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.non_legendary_sp_defense
                stat_stats = loaddata.non_legendary_sp_defense_stats
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.non_legendary_height
                stat_stats = loaddata.non_legendary_height_stats
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.non_legendary_weight
                stat_stats = loaddata.non_legendary_weight_stats
                unit = '(kg)'
            else:
                return
        else:
            return
    elif data_set == "4":  # legendary pokemon
        set_name = "Legendary Pokemon"
        modifier = '(legendary)'
        if type_set == "1":

            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_grass_types['total_points']
                stat_stats = loaddata.legendary_grass_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_grass_types['hp']
                stat_stats = loaddata.legendary_grass_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_grass_types['speed']
                stat_stats = loaddata.legendary_grass_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_grass_types['attack']
                stat_stats = loaddata.legendary_grass_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_grass_types['defense']
                stat_stats = loaddata.legendary_grass_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_grass_types['sp_attack']
                stat_stats = loaddata.legendary_grass_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_grass_types['sp_defense']
                stat_stats = loaddata.legendary_grass_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_grass_types['height_m']
                stat_stats = loaddata.legendary_grass_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_grass_types['weight_kg']
                stat_stats = loaddata.legendary_grass_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # fire pokemon
        elif type_set == "2":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_fire_types['total_points']
                stat_stats = loaddata.legendary_fire_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fire_types['hp']
                stat_stats = loaddata.legendary_fire_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fire_types['speed']
                stat_stats = loaddata.legendary_fire_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fire_types['attack']
                stat_stats = loaddata.legendary_fire_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fire_types['defense']
                stat_stats = loaddata.legendary_fire_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fire_types['sp_attack']
                stat_stats = loaddata.legendary_fire_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fire_types['sp_defense']
                stat_stats = loaddata.legendary_fire_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_fire_types['height_m']
                stat_stats = loaddata.legendary_fire_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_fire_types['weight_kg']
                stat_stats = loaddata.legendary_fire_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # water pokemon
        elif type_set == "3":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_water_types['total_points']
                stat_stats = loaddata.legendary_water_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_water_types['hp']
                stat_stats = loaddata.legendary_water_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_water_types['speed']
                stat_stats = loaddata.legendary_water_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_water_types['attack']
                stat_stats = loaddata.legendary_water_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_water_types['defense']
                stat_stats = loaddata.legendary_water_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_water_types['sp_attack']
                stat_stats = loaddata.legendary_water_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_water_types['sp_defense']
                stat_stats = loaddata.legendary_water_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_water_types['height_m']
                stat_stats = loaddata.legendary_water_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_water_types['weight_kg']
                stat_stats = loaddata.legendary_water_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # electric pokemon
        elif type_set == "4":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_electric_types['total_points']
                stat_stats = loaddata.legendary_electric_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_electric_types['hp']
                stat_stats = loaddata.legendary_electric_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_electric_types['speed']
                stat_stats = loaddata.legendary_electric_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_electric_types['attack']
                stat_stats = loaddata.legendary_electric_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_electric_types['defense']
                stat_stats = loaddata.legendary_electric_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_electric_types['sp_attack']
                stat_stats = loaddata.legendary_electric_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_electric_types['sp_defense']
                stat_stats = loaddata.legendary_electric_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_electric_types['height_m']
                stat_stats = loaddata.legendary_electric_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_electric_types['weight_kg']
                stat_stats = loaddata.legendary_electric_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # psychic pokemon
        elif type_set == "5":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_psychic_types['total_points']
                stat_stats = loaddata.legendary_psychic_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_psychic_types['hp']
                stat_stats = loaddata.legendary_psychic_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_psychic_types['speed']
                stat_stats = loaddata.legendary_psychic_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_psychic_types['attack']
                stat_stats = loaddata.legendary_psychic_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_psychic_types['defense']
                stat_stats = loaddata.legendary_psychic_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_psychic_types['sp_attack']
                stat_stats = loaddata.legendary_psychic_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_psychic_types['sp_defense']
                stat_stats = loaddata.legendary_psychic_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_psychic_types['height_m']
                stat_stats = loaddata.legendary_psychic_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_psychic_types['weight_kg']
                stat_stats = loaddata.legendary_psychic_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # ice pokemon
        elif type_set == "6":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_ice_types['total_points']
                stat_stats = loaddata.legendary_ice_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ice_types['hp']
                stat_stats = loaddata.legendary_ice_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ice_types['speed']
                stat_stats = loaddata.legendary_ice_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ice_types['attack']
                stat_stats = loaddata.legendary_ice_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ice_types['defense']
                stat_stats = loaddata.legendary_ice_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ice_types['sp_attack']
                stat_stats = loaddata.legendary_ice_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ice_types['sp_defense']
                stat_stats = loaddata.legendary_ice_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_ice_types['height_m']
                stat_stats = loaddata.legendary_ice_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_ice_types['weight_kg']
                stat_stats = loaddata.legendary_ice_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # dragon pokemon
        elif type_set == "7":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_dragon_types['total_points']
                stat_stats = loaddata.legendary_dragon_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dragon_types['hp']
                stat_stats = loaddata.legendary_dragon_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dragon_types['speed']
                stat_stats = loaddata.legendary_dragon_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dragon_types['attack']
                stat_stats = loaddata.legendary_dragon_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dragon_types['defense']
                stat_stats = loaddata.legendary_dragon_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dragon_types['sp_attack']
                stat_stats = loaddata.legendary_dragon_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dragon_types['sp_defense']
                stat_stats = loaddata.legendary_dragon_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_dragon_types['height_m']
                stat_stats = loaddata.legendary_dragon_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_dragon_types['weight_kg']
                stat_stats = loaddata.legendary_dragon_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # dark pokemon
        elif type_set == "8":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_dark_types['total_points']
                stat_stats = loaddata.legendary_dark_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dark_types['hp']
                stat_stats = loaddata.legendary_dark_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dark_types['speed']
                stat_stats = loaddata.legendary_dark_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dark_types['attack']
                stat_stats = loaddata.legendary_dark_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dark_types['defense']
                stat_stats = loaddata.legendary_dark_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dark_types['sp_attack']
                stat_stats = loaddata.legendary_dark_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_dark_types['sp_defense']
                stat_stats = loaddata.legendary_dark_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_dark_types['height_m']
                stat_stats = loaddata.legendary_dark_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_dark_types['weight_kg']
                stat_stats = loaddata.legendary_dark_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # fairy pokemon
        elif type_set == "9":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_fairy_types['total_points']
                stat_stats = loaddata.legendary_fairy_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fairy_types['hp']
                stat_stats = loaddata.legendary_fairy_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fairy_types['speed']
                stat_stats = loaddata.legendary_fairy_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fairy_types['attack']
                stat_stats = loaddata.legendary_fairy_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fairy_types['defense']
                stat_stats = loaddata.legendary_fairy_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fairy_types['sp_attack']
                stat_stats = loaddata.legendary_fairy_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fairy_types['sp_defense']
                stat_stats = loaddata.legendary_fairy_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_fairy_types['height_m']
                stat_stats = loaddata.legendary_fairy_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_fairy_types['weight_kg']
                stat_stats = loaddata.legendary_fairy_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # normal pokemon
        elif type_set == "10":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_normal_types['total_points']
                stat_stats = loaddata.legendary_normal_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_normal_types['hp']
                stat_stats = loaddata.legendary_normal_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_normal_types['speed']
                stat_stats = loaddata.legendary_normal_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_normal_types['attack']
                stat_stats = loaddata.legendary_normal_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_normal_types['defense']
                stat_stats = loaddata.legendary_normal_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_normal_types['sp_attack']
                stat_stats = loaddata.legendary_normal_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_normal_types['sp_defense']
                stat_stats = loaddata.legendary_normal_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_normal_types['height_m']
                stat_stats = loaddata.legendary_normal_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_normal_types['weight_kg']
                stat_stats = loaddata.legendary_normal_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # fighting pokemon
        elif type_set == "11":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_fighting_types['total_points']
                stat_stats = loaddata.legendary_fighting_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fighting_types['hp']
                stat_stats = loaddata.legendary_fighting_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fighting_types['speed']
                stat_stats = loaddata.legendary_fighting_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fighting_types['attack']
                stat_stats = loaddata.legendary_fighting_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fighting_types['defense']
                stat_stats = loaddata.legendary_fighting_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fighting_types['sp_attack']
                stat_stats = loaddata.legendary_fighting_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_fighting_types['sp_defense']
                stat_stats = loaddata.legendary_fighting_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_fighting_types['height_m']
                stat_stats = loaddata.legendary_fighting_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_fighting_types['weight_kg']
                stat_stats = loaddata.legendary_fighting_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # flying pokemon
        elif type_set == "12":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_flying_types['total_points']
                stat_stats = loaddata.legendary_flying_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_flying_types['hp']
                stat_stats = loaddata.legendary_flying_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_flying_types['speed']
                stat_stats = loaddata.legendary_flying_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_flying_types['attack']
                stat_stats = loaddata.legendary_flying_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_flying_types['defense']
                stat_stats = loaddata.legendary_flying_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_flying_types['sp_attack']
                stat_stats = loaddata.legendary_flying_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_flying_types['sp_defense']
                stat_stats = loaddata.legendary_flying_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_flying_types['height_m']
                stat_stats = loaddata.legendary_flying_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_flying_types['weight_kg']
                stat_stats = loaddata.legendary_flying_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # poison pokemon
        elif type_set == "13":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_poison_types['total_points']
                stat_stats = loaddata.legendary_poison_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_poison_types['hp']
                stat_stats = loaddata.legendary_poison_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_poison_types['speed']
                stat_stats = loaddata.legendary_poison_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_poison_types['attack']
                stat_stats = loaddata.legendary_poison_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_poison_types['defense']
                stat_stats = loaddata.legendary_poison_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_poison_types['sp_attack']
                stat_stats = loaddata.legendary_poison_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_poison_types['sp_defense']
                stat_stats = loaddata.legendary_poison_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_poison_types['height_m']
                stat_stats = loaddata.legendary_poison_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_poison_types['weight_kg']
                stat_stats = loaddata.legendary_poison_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # ground pokemon
        elif type_set == "14":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_ground_types['total_points']
                stat_stats = loaddata.legendary_ground_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ground_types['hp']
                stat_stats = loaddata.legendary_ground_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ground_types['speed']
                stat_stats = loaddata.legendary_ground_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ground_types['attack']
                stat_stats = loaddata.legendary_ground_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ground_types['defense']
                stat_stats = loaddata.legendary_ground_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ground_types['sp_attack']
                stat_stats = loaddata.legendary_ground_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ground_types['sp_defense']
                stat_stats = loaddata.legendary_ground_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_ground_types['height_m']
                stat_stats = loaddata.legendary_ground_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_ground_types['weight_kg']
                stat_stats = loaddata.legendary_ground_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # rock pokemon
        elif type_set == "15":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_rock_types['total_points']
                stat_stats = loaddata.legendary_rock_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_rock_types['hp']
                stat_stats = loaddata.legendary_rock_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_rock_types['speed']
                stat_stats = loaddata.legendary_rock_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_rock_types['attack']
                stat_stats = loaddata.legendary_rock_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_rock_types['defense']
                stat_stats = loaddata.legendary_rock_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_rock_types['sp_attack']
                stat_stats = loaddata.legendary_rock_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_rock_types['sp_defense']
                stat_stats = loaddata.legendary_rock_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_rock_types['height_m']
                stat_stats = loaddata.legendary_rock_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_rock_types['weight_kg']
                stat_stats = loaddata.legendary_rock_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # bug pokemon
        elif type_set == "16":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_bug_types['total_points']
                stat_stats = loaddata.legendary_bug_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_bug_types['hp']
                stat_stats = loaddata.legendary_bug_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_bug_types['speed']
                stat_stats = loaddata.legendary_bug_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_bug_types['attack']
                stat_stats = loaddata.legendary_bug_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_bug_types['defense']
                stat_stats = loaddata.legendary_bug_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_bug_types['sp_attack']
                stat_stats = loaddata.legendary_bug_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_bug_types['sp_defense']
                stat_stats = loaddata.legendary_bug_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_bug_types['height_m']
                stat_stats = loaddata.legendary_bug_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_bug_types['weight_kg']
                stat_stats = loaddata.legendary_bug_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # ghost pokemon
        elif type_set == "17":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_ghost_types['total_points']
                stat_stats = loaddata.legendary_ghost_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ghost_types['hp']
                stat_stats = loaddata.legendary_ghost_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ghost_types['speed']
                stat_stats = loaddata.legendary_ghost_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ghost_types['attack']
                stat_stats = loaddata.legendary_ghost_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ghost_types['defense']
                stat_stats = loaddata.legendary_ghost_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ghost_types['sp_attack']
                stat_stats = loaddata.legendary_ghost_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_ghost_types['sp_defense']
                stat_stats = loaddata.legendary_ghost_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_ghost_types['height_m']
                stat_stats = loaddata.legendary_ghost_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_ghost_types['weight_kg']
                stat_stats = loaddata.legendary_ghost_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # steel pokemon
        elif type_set == "18":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_steel_types['total_points']
                stat_stats = loaddata.legendary_steel_types['total_points'].describe()
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_steel_types['hp']
                stat_stats = loaddata.legendary_steel_types['hp'].describe()
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_steel_types['speed']
                stat_stats = loaddata.legendary_steel_types['speed'].describe()
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_steel_types['attack']
                stat_stats = loaddata.legendary_steel_types['attack'].describe()
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_steel_types['defense']
                stat_stats = loaddata.legendary_steel_types['defense'].describe()
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_steel_types['sp_attack']
                stat_stats = loaddata.legendary_steel_types['sp_attack'].describe()
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_steel_types['sp_defense']
                stat_stats = loaddata.legendary_steel_types['sp_defense'].describe()
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_steel_types['height_m']
                stat_stats = loaddata.legendary_steel_types['height_m'].describe()
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_steel_types['weight_kg']
                stat_stats = loaddata.legendary_steel_types['weight_kg'].describe()
                unit = '(kg)'
            else:
                return
            # all pokemon (trimmed h & w)
        elif type_set == "19":
            if stat_set == "1":  # stat totals
                stat_name = "Stat Total"
                test_bounds = (100, 600)
                stat_values = loaddata.legendary_total_points
                stat_stats = loaddata.legendary_total_points_stats
                unit = ''
            elif stat_set == "2":  # hp
                stat_name = "HP"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_hp
                stat_stats = loaddata.legendary_hp_stats
                unit = ''
            elif stat_set == "3":  # speed
                stat_name = "Speed"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_speed
                stat_stats = loaddata.legendary_speed_stats
                unit = ''
            elif stat_set == "4":  # attack
                stat_name = "Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_attack
                stat_stats = loaddata.legendary_attack_stats
                unit = ''
            elif stat_set == "5":  # defense
                stat_name = "Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_defense
                stat_stats = loaddata.legendary_defense_stats
                unit = ''
            elif stat_set == "6":  # sp.attack
                stat_name = "Special Attack"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_sp_attack
                stat_stats = loaddata.legendary_sp_attack_stats
                unit = ''
            elif stat_set == "7":  # sp.defense
                stat_name = "Special Defense"
                test_bounds = (20, 256)
                stat_values = loaddata.legendary_sp_defense
                stat_stats = loaddata.legendary_sp_defense_stats
                unit = ''
            elif stat_set == "8":  # height
                stat_name = "Height(m)"
                test_bounds = (0, 20)
                stat_values = loaddata.legendary_height
                stat_stats = loaddata.legendary_height_stats
                unit = '(m)'
            elif stat_set == "9":  # weight
                stat_name = "Weight(kg)"
                test_bounds = (1, 800)
                stat_values = loaddata.legendary_weight
                stat_stats = loaddata.legendary_weight_stats
                unit = '(kg)'
            else:
                return
        else:
            return
    else:
        return

    # grass pokemon
    if type_set == "1":
        set_type = "Grass Type "
    # fire pokemon
    elif type_set == "2":
        set_type = "Fire Type "
    # water pokemon
    elif type_set == "3":
        set_type = "Water Type "
    # electric pokemon
    elif type_set == "4":
        set_type = "Electric Type "
    # psychic pokemon
    elif type_set == "5":
        set_type = "Psychic Type "
    # ice pokemon
    elif type_set == "6":
        set_type = "Ice Type "
    # dragon pokemon
    elif type_set == "7":
        set_type = "Dragon Type "
    # dark pokemon
    elif type_set == "8":
        set_type = "Dark Type "
    # fairy pokemon
    elif type_set == "9":
        set_type = "Fairy Type "
    # normal pokemon
    elif type_set == "10":
        set_type = "Normal Type "
    # fighting pokemon
    elif type_set == "11":
        set_type = "Fighting Type "
    # flying pokemon
    elif type_set == "12":
        set_type = "Flying Type "
    # poison pokemon
    elif type_set == "13":
        set_type = "Poison Type "
    # ground pokemon
    elif type_set == "14":
        set_type = "Ground Type "
    # rock pokemon
    elif type_set == "15":
        set_type = "Rock Type "
    # bug pokemon
    elif type_set == "16":
        set_type = "Bug Type "
    # ghost pokemon
    elif type_set == "17":
        set_type = "Ghost Type "
    # steel pokemon
    elif type_set == "18":
        set_type = "Steel Type "
    # all pokemon
    else:
        set_type = ''

    pokemon_normal_dist_and_actual_vals.run_normal_dist_vs_actual(stat_values, stat_stats, test_bounds, set_name,
                                                                  stat_name, unit, modifier, set_type)
    return


def do_regression_analysis_non_legendary(option):
    if option == "1":
        set_name = "Grass Type"
        set_data = loaddata.non_legendary_grass_types
        z_set_data = loaddata.z_non_legendary_grass
    elif option == "2":
        set_name = "Fire Type"
        set_data = loaddata.non_legendary_fire_types
        z_set_data = loaddata.z_non_legendary_fire
    elif option == "3":
        set_name = "Water Type"
        set_data = loaddata.non_legendary_water_types
        z_set_data = loaddata.z_non_legendary_water
    elif option == "4":
        set_name = "Electric Type"
        set_data = loaddata.non_legendary_electric_types
        z_set_data = loaddata.z_non_legendary_electric
    elif option == "5":
        set_name = "Psychic Type"
        set_data = loaddata.non_legendary_psychic_types
        z_set_data = loaddata.z_non_legendary_psychic
    elif option == "6":
        set_name = "Ice Type"
        set_data = loaddata.non_legendary_ice_types
        z_set_data = loaddata.z_non_legendary_ice
    elif option == "7":
        set_name = "Dragon Type"
        set_data = loaddata.non_legendary_dragon_types
        z_set_data = loaddata.z_non_legendary_dragon
    elif option == "8":
        set_name = "Dark Type"
        set_data = loaddata.non_legendary_dark_types
        z_set_data = loaddata.z_non_legendary_dark
    elif option == "9":
        set_name = "Fairy Type"
        set_data = loaddata.non_legendary_fairy_types
        z_set_data = loaddata.z_non_legendary_fairy
    elif option == "10":
        set_name = "Normal Type"
        set_data = loaddata.non_legendary_normal_types
        z_set_data = loaddata.z_non_legendary_normal
    elif option == "11":
        set_name = "Fighting Type"
        set_data = loaddata.non_legendary_fighting_types
        z_set_data = loaddata.z_non_legendary_fighting
    elif option == "12":
        set_name = "Flying Type"
        set_data = loaddata.non_legendary_flying_types
        z_set_data = loaddata.z_non_legendary_flying
    elif option == "13":
        set_name = "Poison Type"
        set_data = loaddata.non_legendary_poison_types
        z_set_data = loaddata.z_non_legendary_poison
    elif option == "14":
        set_name = "Ground Type"
        set_data = loaddata.non_legendary_ground_types
        z_set_data = loaddata.z_non_legendary_ground
    elif option == "15":
        set_name = "Rock Type"
        set_data = loaddata.non_legendary_rock_types
        z_set_data = loaddata.z_non_legendary_rock
    elif option == "16":
        set_name = "Bug Type"
        set_data = loaddata.non_legendary_bug_types
        z_set_data = loaddata.z_non_legendary_bug
    elif option == "17":
        set_name = "Ghost Type"
        set_data = loaddata.non_legendary_ghost_types
        z_set_data = loaddata.z_non_legendary_ghost
    elif option == "18":
        set_name = "Steel Type"
        set_data = loaddata.non_legendary_steel_types
        z_set_data = loaddata.z_non_legendary_steel
    elif option == "19":
        set_name = "Pokemon"
        set_data = loaddata.non_legendary_pokemon
        z_set_data = loaddata.z_pokemon_non_legendary
    else:
        return

    pokemon_regression.pokemon_regression_analysis(set_name, set_data, z_set_data, modified_data_tag='(non legendary)')
    return


def do_regression_analysis_legendary(option):
    if option == "1":
        set_name = "Grass Type"
        set_data = loaddata.legendary_grass_types
        z_set_data = loaddata.z_legendary_grass
    elif option == "2":
        set_name = "Fire Type"
        set_data = loaddata.legendary_fire_types
        z_set_data = loaddata.z_legendary_fire
    elif option == "3":
        set_name = "Water Type"
        set_data = loaddata.legendary_water_types
        z_set_data = loaddata.z_legendary_water
    elif option == "4":
        set_name = "Electric Type"
        set_data = loaddata.legendary_electric_types
        z_set_data = loaddata.z_legendary_electric
    elif option == "5":
        set_name = "Psychic Type"
        set_data = loaddata.legendary_psychic_types
        z_set_data = loaddata.z_legendary_psychic
    elif option == "6":
        set_name = "Ice Type"
        set_data = loaddata.legendary_ice_types
        z_set_data = loaddata.z_legendary_ice
    elif option == "7":
        set_name = "Dragon Type"
        set_data = loaddata.legendary_dragon_types
        z_set_data = loaddata.z_legendary_dragon
    elif option == "8":
        set_name = "Dark Type"
        set_data = loaddata.legendary_dark_types
        z_set_data = loaddata.z_legendary_dark
    elif option == "9":
        set_name = "Fairy Type"
        set_data = loaddata.legendary_fairy_types
        z_set_data = loaddata.z_legendary_fairy
    elif option == "10":
        set_name = "Normal Type"
        set_data = loaddata.legendary_normal_types
        z_set_data = loaddata.z_legendary_normal
    elif option == "11":
        set_name = "Fighting Type"
        set_data = loaddata.legendary_fighting_types
        z_set_data = loaddata.z_legendary_fighting
    elif option == "12":
        set_name = "Flying Type"
        set_data = loaddata.legendary_flying_types
        z_set_data = loaddata.z_legendary_flying
    elif option == "13":
        set_name = "Poison Type"
        set_data = loaddata.legendary_poison_types
        z_set_data = loaddata.z_legendary_poison
    elif option == "14":
        set_name = "Ground Type"
        set_data = loaddata.legendary_ground_types
        z_set_data = loaddata.z_legendary_ground
    elif option == "15":
        set_name = "Rock Type"
        set_data = loaddata.legendary_rock_types
        z_set_data = loaddata.z_legendary_rock
    elif option == "16":
        set_name = "Bug Type"
        set_data = loaddata.legendary_bug_types
        z_set_data = loaddata.z_legendary_bug
    elif option == "17":
        set_name = "Ghost Type"
        set_data = loaddata.legendary_ghost_types
        z_set_data = loaddata.z_legendary_ghost
    elif option == "18":
        set_name = "Steel Type"
        set_data = loaddata.legendary_steel_types
        z_set_data = loaddata.z_legendary_steel
    elif option == "19":
        set_name = "Pokemon"
        set_data = loaddata.legendary_pokemon
        z_set_data = loaddata.z_pokemon_legendary
    else:
        return

    pokemon_regression.pokemon_regression_analysis(set_name, set_data, z_set_data, modified_data_tag='(legendary)')
    return


def do_regression_analysis_trimmed(option):
    modified_data_tag = '(trimmed Height(m) & Weight(kg))'

    if option == "1":
        set_name = "Grass Type"
        set_data = loaddata.trimmed_grass_types
        z_set_data = loaddata.z_trimmed_grass
        trim_data = loaddata.grass_trim_data
    elif option == "2":
        set_name = "Fire Type"
        set_data = loaddata.trimmed_fire_types
        z_set_data = loaddata.z_trimmed_fire
        trim_data = loaddata.fire_trim_data
    elif option == "3":
        set_name = "Water Type"
        set_data = loaddata.trimmed_water_types
        z_set_data = loaddata.z_trimmed_water
        trim_data = loaddata.water_trim_data
    elif option == "4":
        set_name = "Electric Type"
        set_data = loaddata.trimmed_electric_types
        z_set_data = loaddata.z_trimmed_electric
        trim_data = loaddata.electric_trim_data
    elif option == "5":
        set_name = "Psychic Type"
        set_data = loaddata.trimmed_psychic_types
        z_set_data = loaddata.z_trimmed_psychic
        trim_data = loaddata.psychic_trim_data
    elif option == "6":
        set_name = "Ice Type"
        set_data = loaddata.trimmed_ice_types
        z_set_data = loaddata.z_trimmed_ice
        trim_data = loaddata.ice_trim_data
    elif option == "7":
        set_name = "Dragon Type"
        set_data = loaddata.trimmed_dragon_types
        z_set_data = loaddata.z_trimmed_dragon
        trim_data = loaddata.dragon_trim_data
    elif option == "8":
        set_name = "Dark Type"
        set_data = loaddata.trimmed_dark_types
        z_set_data = loaddata.z_trimmed_dark
        trim_data = loaddata.dark_trim_data
    elif option == "9":
        set_name = "Fairy Type"
        set_data = loaddata.trimmed_fairy_types
        z_set_data = loaddata.z_trimmed_fairy
        trim_data = loaddata.fairy_trim_data
    elif option == "10":
        set_name = "Normal Type"
        set_data = loaddata.trimmed_normal_types
        z_set_data = loaddata.z_trimmed_normal
        trim_data = loaddata.normal_trim_data
    elif option == "11":
        set_name = "Fighting Type"
        set_data = loaddata.trimmed_fighting_types
        z_set_data = loaddata.z_trimmed_fighting
        trim_data = loaddata.fighting_trim_data
    elif option == "12":
        set_name = "Flying Type"
        set_data = loaddata.trimmed_flying_types
        z_set_data = loaddata.z_trimmed_flying
        trim_data = loaddata.flying_trim_data
    elif option == "13":
        set_name = "Poison Type"
        set_data = loaddata.trimmed_poison_types
        z_set_data = loaddata.z_trimmed_poison
        trim_data = loaddata.poison_trim_data
    elif option == "14":
        set_name = "Ground Type"
        set_data = loaddata.trimmed_ground_types
        z_set_data = loaddata.z_trimmed_ground
        trim_data = loaddata.ground_trim_data
    elif option == "15":
        set_name = "Rock Type"
        set_data = loaddata.trimmed_rock_types
        z_set_data = loaddata.z_trimmed_rock
        trim_data = loaddata.rock_trim_data
    elif option == "16":
        set_name = "Bug Type"
        set_data = loaddata.trimmed_bug_types
        z_set_data = loaddata.z_trimmed_bug
        trim_data = loaddata.bug_trim_data
    elif option == "17":
        set_name = "Ghost Type"
        set_data = loaddata.trimmed_ghost_types
        z_set_data = loaddata.z_trimmed_ghost
        trim_data = loaddata.ghost_trim_data
    elif option == "18":
        set_name = "Steel Type"
        set_data = loaddata.trimmed_steel_types
        z_set_data = loaddata.z_trimmed_steel
        trim_data = loaddata.steel_trim_data
    elif option == "19":
        set_name = "Pokemon"
        set_data = loaddata.pkm_trim_hw
        z_set_data = loaddata.z_trimmed_pokemon
        trim_data = loaddata.trim_data
    elif option == "20":
        set_name = "Pokemon"
        set_data = loaddata.pokemon_trimmed_heights
        z_set_data = loaddata.z_pokemon_t_h
        trim_data = loaddata.trim_data_h
        modified_data_tag = '(trimmed Height(m))'
    elif option == "21":
        set_name = "Pokemon"
        set_data = loaddata.pokemon_trimmed_weights
        z_set_data = loaddata.z_pokemon_t_w
        trim_data = loaddata.trim_data_w
        modified_data_tag = '(trimmed Weight(kg))'
    else:
        return

    pokemon_regression.pokemon_regression_analysis(set_name, set_data, z_set_data, trim_data, modified_data_tag)
    return


def do_regression_analysis_full(option):
    modified_data_tag = ''
    if option == "1":
        set_name = "Grass Type"
        set_data = loaddata.grass_types
        z_set_data = loaddata.z_grass
    elif option == "2":
        set_name = "Fire Type"
        set_data = loaddata.fire_types
        z_set_data = loaddata.z_fire
    elif option == "3":
        set_name = "Water Type"
        set_data = loaddata.water_types
        z_set_data = loaddata.z_water
    elif option == "4":
        set_name = "Electric Type"
        set_data = loaddata.electric_types
        z_set_data = loaddata.z_electric
    elif option == "5":
        set_name = "Psychic Type"
        set_data = loaddata.psychic_types
        z_set_data = loaddata.z_psychic
    elif option == "6":
        set_name = "Ice Type"
        set_data = loaddata.ice_types
        z_set_data = loaddata.z_ice
    elif option == "7":
        set_name = "Dragon Type"
        set_data = loaddata.dragon_types
        z_set_data = loaddata.z_dragon
    elif option == "8":
        set_name = "Dark Type"
        set_data = loaddata.dark_types
        z_set_data = loaddata.z_dark
    elif option == "9":
        set_name = "Fairy Type"
        set_data = loaddata.fairy_types
        z_set_data = loaddata.z_fairy
    elif option == "10":
        set_name = "Normal Type"
        set_data = loaddata.normal_types
        z_set_data = loaddata.z_normal
    elif option == "11":
        set_name = "Fighting Type"
        set_data = loaddata.fighting_types
        z_set_data = loaddata.z_fighting
    elif option == "12":
        set_name = "Flying Type"
        set_data = loaddata.flying_types
        z_set_data = loaddata.z_flying
    elif option == "13":
        set_name = "Poison Type"
        set_data = loaddata.poison_types
        z_set_data = loaddata.z_poison
    elif option == "14":
        set_name = "Ground Type"
        set_data = loaddata.ground_types
        z_set_data = loaddata.z_ground
    elif option == "15":
        set_name = "Rock Type"
        set_data = loaddata.rock_types
        z_set_data = loaddata.z_rock
    elif option == "16":
        set_name = "Bug Type"
        set_data = loaddata.bug_types
        z_set_data = loaddata.z_bug
    elif option == "17":
        set_name = "Ghost Type"
        set_data = loaddata.ghost_types
        z_set_data = loaddata.z_ghost
    elif option == "18":
        set_name = "Steel Type"
        set_data = loaddata.steel_types
        z_set_data = loaddata.z_steel
    elif option == "19":
        set_name = "Pokemon"
        set_data = loaddata.all_pokemon
        z_set_data = loaddata.z_pokemon
    else:
        return

    pokemon_regression.pokemon_regression_analysis(set_name, set_data, z_set_data, modified_data_tag)
    return


def do_stat_analysis_non_legendary(option):
    if option == "2":
        stat_name = "HP"
        stat_values = loaddata.non_legendary_hp
        stat_value_stats = loaddata.non_legendary_hp_stats
        z_stat_values = loaddata.z_non_legendary_hp
        z_stat_value_stats = loaddata.z_non_legendary_hp_stats
    elif option == "3":
        stat_name = "Speed"
        stat_values = loaddata.non_legendary_speed
        stat_value_stats = loaddata.non_legendary_speed_stats
        z_stat_values = loaddata.z_non_legendary_speed
        z_stat_value_stats = loaddata.z_non_legendary_speed_stats
    elif option == "4":
        stat_name = "Attack"
        stat_values = loaddata.non_legendary_attack
        stat_value_stats = loaddata.non_legendary_attack_stats
        z_stat_values = loaddata.z_non_legendary_attack
        z_stat_value_stats = loaddata.z_non_legendary_attack_stats
    elif option == "5":
        stat_name = "Defense"
        stat_values = loaddata.non_legendary_defense
        stat_value_stats = loaddata.non_legendary_defense_stats
        z_stat_values = loaddata.z_non_legendary_defense
        z_stat_value_stats = loaddata.z_non_legendary_defense_stats
    elif option == "6":
        stat_name = "Special Attack"
        stat_values = loaddata.non_legendary_sp_attack
        stat_value_stats = loaddata.non_legendary_sp_attack_stats
        z_stat_values = loaddata.z_non_legendary_sp_attack
        z_stat_value_stats = loaddata.z_non_legendary_sp_attack_stats
    elif option == "7":
        stat_name = "Special Defense"
        stat_values = loaddata.non_legendary_sp_defense
        stat_value_stats = loaddata.non_legendary_sp_defense_stats
        z_stat_values = loaddata.z_non_legendary_sp_defense
        z_stat_value_stats = loaddata.z_non_legendary_sp_defense_stats
    elif option == "1":
        stat_name = "Stat Totals"
        stat_values = loaddata.non_legendary_total_points
        stat_value_stats = loaddata.non_legendary_total_points_stats
        z_stat_values = loaddata.z_non_legendary_total_points
        z_stat_value_stats = loaddata.z_non_legendary_total_points_stats
    elif option == "8":
        stat_name = "Height(m)"
        stat_values = loaddata.non_legendary_height
        stat_value_stats = loaddata.non_legendary_height_stats
        z_stat_values = loaddata.z_non_legendary_height
        z_stat_value_stats = loaddata.z_non_legendary_height_stats
    elif option == "9":
        stat_name = "Weight(kg)"
        stat_values = loaddata.non_legendary_weight
        stat_value_stats = loaddata.non_legendary_weight_stats
        z_stat_values = loaddata.z_non_legendary_weight
        z_stat_value_stats = loaddata.z_non_legendary_weight_stats
    else:
        return

    pokemon_stat_analysis.stat_analysis(stat_name, stat_values, z_stat_values, stat_value_stats, z_stat_value_stats,
                                        modifier='(non_legendary)')
    return


def do_stat_analysis_legendary(option):
    if option == "2":
        stat_name = "HP"
        stat_values = loaddata.legendary_hp
        stat_value_stats = loaddata.legendary_hp_stats
        z_stat_values = loaddata.z_legendary_hp
        z_stat_value_stats = loaddata.z_legendary_hp_stats
    elif option == "3":
        stat_name = "Speed"
        stat_values = loaddata.legendary_speed
        stat_value_stats = loaddata.legendary_speed_stats
        z_stat_values = loaddata.z_legendary_speed
        z_stat_value_stats = loaddata.z_legendary_speed_stats
    elif option == "4":
        stat_name = "Attack"
        stat_values = loaddata.legendary_attack
        stat_value_stats = loaddata.legendary_attack_stats
        z_stat_values = loaddata.z_legendary_attack
        z_stat_value_stats = loaddata.z_legendary_attack_stats
    elif option == "5":
        stat_name = "Defense"
        stat_values = loaddata.legendary_defense
        stat_value_stats = loaddata.legendary_defense_stats
        z_stat_values = loaddata.z_legendary_defense
        z_stat_value_stats = loaddata.z_legendary_defense_stats
    elif option == "6":
        stat_name = "Special Attack"
        stat_values = loaddata.legendary_sp_attack
        stat_value_stats = loaddata.legendary_sp_attack_stats
        z_stat_values = loaddata.z_legendary_sp_attack
        z_stat_value_stats = loaddata.z_legendary_sp_attack_stats
    elif option == "7":
        stat_name = "Special Defense"
        stat_values = loaddata.legendary_sp_defense
        stat_value_stats = loaddata.legendary_sp_defense_stats
        z_stat_values = loaddata.z_legendary_sp_defense
        z_stat_value_stats = loaddata.z_legendary_sp_defense_stats
    elif option == "1":
        stat_name = "Stat Totals"
        stat_values = loaddata.legendary_total_points
        stat_value_stats = loaddata.legendary_total_points_stats
        z_stat_values = loaddata.z_legendary_total_points
        z_stat_value_stats = loaddata.z_legendary_total_points_stats
    elif option == "8":
        stat_name = "Height(m)"
        stat_values = loaddata.legendary_height
        stat_value_stats = loaddata.legendary_height_stats
        z_stat_values = loaddata.z_legendary_height
        z_stat_value_stats = loaddata.z_legendary_height_stats
    elif option == "9":
        stat_name = "Weight(kg)"
        stat_values = loaddata.legendary_weight
        stat_value_stats = loaddata.legendary_weight_stats
        z_stat_values = loaddata.z_legendary_weight
        z_stat_value_stats = loaddata.z_legendary_weight_stats
    else:
        return

    pokemon_stat_analysis.stat_analysis(stat_name, stat_values, z_stat_values, stat_value_stats, z_stat_value_stats,
                                        modifier='(legendary)')
    return


def do_stat_analysis_trimmed(option):
    if option == "2":
        stat_name = "HP"
        stat_values = loaddata.trimmed_hp
        stat_value_stats = loaddata.trimmed_hp_stats
        z_stat_values = loaddata.z_trimmed_hp
        z_stat_value_stats = loaddata.z_trimmed_hp_stats
    elif option == "3":
        stat_name = "Speed"
        stat_values = loaddata.trimmed_speed
        stat_value_stats = loaddata.trimmed_speed_stats
        z_stat_values = loaddata.z_trimmed_speed
        z_stat_value_stats = loaddata.z_trimmed_speed_stats
    elif option == "4":
        stat_name = "Attack"
        stat_values = loaddata.trimmed_attack
        stat_value_stats = loaddata.trimmed_attack_stats
        z_stat_values = loaddata.z_trimmed_attack
        z_stat_value_stats = loaddata.z_trimmed_attack_stats
    elif option == "5":
        stat_name = "Defense"
        stat_values = loaddata.trimmed_defense
        stat_value_stats = loaddata.trimmed_defense_stats
        z_stat_values = loaddata.z_trimmed_defense
        z_stat_value_stats = loaddata.z_trimmed_defense_stats
    elif option == "6":
        stat_name = "Special Attack"
        stat_values = loaddata.trimmed_sp_attack
        stat_value_stats = loaddata.trimmed_sp_attack_stats
        z_stat_values = loaddata.z_trimmed_sp_attack
        z_stat_value_stats = loaddata.z_trimmed_sp_attack_stats
    elif option == "7":
        stat_name = "Special Defense"
        stat_values = loaddata.trimmed_sp_defense
        stat_value_stats = loaddata.trimmed_sp_defense_stats
        z_stat_values = loaddata.z_trimmed_sp_defense
        z_stat_value_stats = loaddata.z_trimmed_sp_defense_stats
    elif option == "1":
        stat_name = "Stat Totals"
        stat_values = loaddata.trimmed_total_points
        stat_value_stats = loaddata.trimmed_total_points_stats
        z_stat_values = loaddata.z_trimmed_total_points
        z_stat_value_stats = loaddata.z_trimmed_total_points_stats
    elif option == "8":
        stat_name = "Height(m)"
        stat_values = loaddata.trimmed_height
        stat_value_stats = loaddata.trimmed_height_stats
        z_stat_values = loaddata.z_trimmed_height
        z_stat_value_stats = loaddata.z_trimmed_height_stats
    elif option == "9":
        stat_name = "Weight(kg)"
        stat_values = loaddata.trimmed_weight
        stat_value_stats = loaddata.trimmed_weight_stats
        z_stat_values = loaddata.z_trimmed_weight
        z_stat_value_stats = loaddata.z_trimmed_weight_stats
    else:
        return

    pokemon_stat_analysis.stat_analysis(stat_name, stat_values, z_stat_values, stat_value_stats, z_stat_value_stats,
                                        modifier='(trimmed)')
    return


def do_stat_analysis_full(option):
    if option == "2":
        stat_name = "HP"
        stat_values = loaddata.hp
        stat_value_stats = loaddata.hp_stats
        z_stat_values = loaddata.z_hp
        z_stat_value_stats = loaddata.z_hp_stats
    elif option == "3":
        stat_name = "Speed"
        stat_values = loaddata.speed
        stat_value_stats = loaddata.speed_stats
        z_stat_values = loaddata.z_speed
        z_stat_value_stats = loaddata.z_speed_stats
    elif option == "4":
        stat_name = "Attack"
        stat_values = loaddata.attack
        stat_value_stats = loaddata.attack_stats
        z_stat_values = loaddata.z_attack
        z_stat_value_stats = loaddata.z_attack_stats
    elif option == "5":
        stat_name = "Defense"
        stat_values = loaddata.defense
        stat_value_stats = loaddata.defense_stats
        z_stat_values = loaddata.z_defense
        z_stat_value_stats = loaddata.z_defense_stats
    elif option == "6":
        stat_name = "Special Attack"
        stat_values = loaddata.sp_attack
        stat_value_stats = loaddata.sp_attack_stats
        z_stat_values = loaddata.z_sp_attack
        z_stat_value_stats = loaddata.z_sp_attack_stats
    elif option == "7":
        stat_name = "Special Defense"
        stat_values = loaddata.sp_defense
        stat_value_stats = loaddata.sp_defense_stats
        z_stat_values = loaddata.z_sp_defense
        z_stat_value_stats = loaddata.z_sp_defense_stats
    elif option == "1":
        stat_name = "Stat Totals"
        stat_values = loaddata.total_points
        stat_value_stats = loaddata.total_points_stats
        z_stat_values = loaddata.z_total_points
        z_stat_value_stats = loaddata.z_total_points_stats
    elif option == "8":
        stat_name = "Height(m)"
        stat_values = loaddata.heights
        stat_value_stats = loaddata.height_stats
        z_stat_values = loaddata.z_height
        z_stat_value_stats = loaddata.z_height_stats
    elif option == "9":
        stat_name = "Weight(kg)"
        stat_values = loaddata.weight
        stat_value_stats = loaddata.weight_stats
        z_stat_values = loaddata.z_weight
        z_stat_value_stats = loaddata.z_weight_stats
    else:
        return

    pokemon_stat_analysis.stat_analysis(stat_name, stat_values, z_stat_values, stat_value_stats, z_stat_value_stats)
    return


def print_options_home():
    ret_str = f"\n{tab * 4}1: Stat Analysis\n" + \
              f"{tab * 4}2: Are Pokemon Heights Normal or Log distributed?\n" + \
              f"{tab * 4}3: Random Pokemon Correlations\n" + \
              f"{tab * 4}4: Testing Normal Distribution against Actual Values\n" + \
              f"{tab * 4}5: Are Dragon Types Taller Than Non Dragon Types?\n" + \
              f"{tab * 4}6: Pokemon Regression Analysis\n" + \
              f"{tab * 5}0: Exit"
    print(ret_str)


def print_options_sets():
    ret_str = f"\n{tab * 4}- - - Select Your Specific Pokemon Data Set - - -\n" + \
              f"\n{tab * 4}1: Full Data\n" \
              f" {tab * 4}2: Trimmed Data\n" + \
              f"{tab * 4}3: Non Legendary Pokemon\n" + \
              f"{tab * 4}4: Legendary Pokemon\n" + \
              f"{tab * 5}0: EXIT\n"
    print(ret_str)


def print_options_types(modifier=''):
    ret_str = f""
    if len(modifier) > 0:
        ret_str += f"\n{tab * 4}- - - {modifier} - - -\n"

    ret_str += f"\n{tab * 4}1: Grass Types {tab * 3}2: Fire Types\n" + \
               f"{tab * 4}3: Water Types {tab * 3}4: Electric Types\n" + \
               f"{tab * 4}5: Psychic Types {tab * 2}6: Ice Types\n" + \
               f"{tab * 4}7: Dragon Types {tab * 2}8: Dark Types\n" + \
               f"{tab * 4}9: Fairy Types {tab * 3}10: Normal Types\n" + \
               f"{tab * 4}11: Fighting Types {tab * 2}12: Flying Types\n" + \
               f"{tab * 4}13: Poison Types {tab * 2}14: Ground Types\n" + \
               f"{tab * 4}15: Rock Types {tab * 3}16: Bug Types\n" + \
               f"{tab * 4}17: Ghost Types {tab * 2}18: Steel Types\n"

    if modifier == "Trimmed":
        ret_str += f"{tab * 4}19: Pokemon (trimmed Height(m) & Weight(kg))\n"
    else:
        ret_str += f"{tab * 4}19: Entire Set\n"

    ret_str += f"{tab * 5}0: EXIT\n"
    print(ret_str)


def print_options_stats(modifier=''):
    ret_str = f""
    if len(modifier) > 0:
        ret_str += f"\n{tab * 4}- - - {modifier} - - -\n"

    ret_str += f"\n{tab * 6}1: Stat Totals\n" + \
               f"{tab * 4}2: HP{tab * 5}3: Speed\n" + \
               f"{tab * 4}4: Attack{tab * 4}5: Defense\n" + \
               f"{tab * 4}6: Special Attack{tab * 2}7: Special Defense\n" + \
               f"{tab * 4}8: Height(m){tab * 3}9: Weight(kg)\n" + \
               f"{tab * 5}0: EXIT\n"

    print(ret_str)


if __name__ == "__main__":

    while 1:
        print_options_home()
        val_home = input(f"\n{tab * 2}Enter Desired Option: ")
        print(val_home)
        if val_home == "1":

            print_options_sets()
            val_opt_set = input(f"\n{tab * 2}Enter Option: ")

            if val_opt_set == "1":
                # print options stat analysis full
                print_options_stats()
                val_opt_stat = input(f"\n{tab * 2}Enter Option: ")
                if val_opt_stat == "0":
                    break
                else:
                    do_stat_analysis_full(val_opt_stat)

            elif val_opt_set == "2":
                # print options stat analysis trimmed
                print_options_types("Trimmed")
                val_opt_stat = input(f"\n{tab * 2}Enter Option: ")
                if val_opt_stat == "0":
                    break
                else:
                    do_stat_analysis_full(val_opt_stat)

            elif val_opt_set == "3":
                # print options stat analysis non legendary
                print_options_types("Non Legendary Pokemon")
                val_opt_stat = input(f"\n{tab * 2}Enter Option: ")
                if val_opt_stat == "0":
                    break
                else:
                    do_stat_analysis_non_legendary(val_opt_stat)

            elif val_opt_set == "4":
                # print options stat analysis legendary
                print_options_types("Legendary Pokemon")
                val_opt_stat = input(f"\n{tab * 2}Enter Option: ")
                if val_opt_stat == "0":
                    break
                else:
                    do_stat_analysis_legendary(val_opt_stat)

            else:
                break
            continue
        elif val_home == "2":
            print(f"{tab * 4} Are Pokemon Heights Normal or Log distributed?")
            continue
        elif val_home == "3":
            print(f"{tab * 4} Random Pokemon Correlations")
            continue
        elif val_home == "4":
            # print(f"{tab * 4}Testing Normal Distribution against Actual Values")
            print_options_sets()
            val_opt_set = input(f"\n{tab * 2}Enter Option: ")
            if val_opt_set == "0":
                break
            else:
                # print options stat analysis full
                print_options_types()
                val_opt_type = input(f"\n{tab * 2}Enter Option: ")
                if val_opt_type == "0":
                    break
                else:
                    print_options_stats()
                    val_opt_stat = input(f"\n{tab * 2}Enter Option: ")
                    if val_opt_stat == "0":
                        break
                    else:
                        do_normal_dist_against_actual_values([val_opt_set, val_opt_type, val_opt_stat])

            continue
        elif val_home == "5":
            pokemon_test_are_dragons_taller.are_dragons_taller()
            continue
        elif val_home == "6":
            print_options_sets()
            val_opt_set = input(f"\n{tab * 2}Enter Option: ")

            if val_opt_set == "1":

                print_options_types()
                val_opt_type = input(f"\n{tab * 2}Enter Option: ")

                if val_opt_type == "0":
                    break
                else:
                    do_regression_analysis_full(val_opt_type)

            elif val_opt_set == "2":

                print_options_types("Trimmed")
                val_opt_type = input(f"\n{tab * 2}Enter Option: ")

                if val_opt_type == "0":
                    break
                else:
                    do_regression_analysis_trimmed(val_opt_type)

            elif val_opt_set == "3":

                print_options_types("Non Legendary Pokemon")
                val_opt_type = input(f"\n{tab * 2}Enter Option: ")

                if val_opt_type == "0":
                    break
                else:
                    do_regression_analysis_non_legendary(val_opt_type)

            elif val_opt_set == "4":

                print_options_types("Legendary Pokemon")
                val_opt_type = input(f"\n{tab * 2}Enter Option: ")

                if val_opt_type == "0":
                    break
                else:
                    do_regression_analysis_legendary(val_opt_type)

            else:
                break

            continue
        else:
            print("Exit")
            break
