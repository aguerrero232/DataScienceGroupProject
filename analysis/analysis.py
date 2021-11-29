import pokemon_regression, pokemon_stat_analysis
import loaddata

separator_char = ", "
separator = '---------------------------------------------------------------'
tab: str = "\t"


def do_regression_analysis(option):
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
    elif option == "20":
        set_name = "Pokemon"
        set_data = loaddata.pokemon_trimmed_heights
        z_set_data = loaddata.z_pokemon_trimmed_height
        modified_data_tag = '(trimmed Height(m))'
    elif option == "21":
        set_name = "Pokemon"
        set_data = loaddata.pokemon_trimmed_weights
        z_set_data = loaddata.z_pokemon_trimmed_weight
        modified_data_tag = '(trimmed Weight(kg))'
    elif option == "22":
        set_name = "Pokemon"
        set_data = loaddata.pokemon_trimmed_height_and_weight
        z_set_data = loaddata.z_pokemon_trimmed_height_and_weight
        modified_data_tag = '(trimmed Height(m) & Weight(kg))'
    else:
        return

    pokemon_regression.pokemon_regression_analysis(set_name, set_data, z_set_data, modified_data_tag)
    return


def do_stat_analysis(option):
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
        stat_values = loaddata.height
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
    ret_str = f"\n{tab*4}1: Stat Analysis\n" + \
              f"{tab*4}2: Are Pokemon Heights Normal or Log distributed?\n" + \
              f"{tab*4}3: Random Pokemon Correlations\n" + \
              f"{tab*4}4: Testing Normal Distribution against Actual Values\n" + \
              f"{tab*4}5: Are Dragon Types Taller Than Non Dragon Types\n" + \
              f"{tab*4}6: Pokemon Regression Analysis\n" + \
              f"{tab*4}0: Exit"
    print(ret_str)


def print_options_regression_analysis():
    ret_str = f"\n{tab*4}1: Grass Types {tab*3}2: Fire Types\n" + \
              f"{tab*4}3: Water Types {tab*3}4: Electric Types\n" + \
              f"{tab*4}5: Psychic Types {tab*2}6: Ice Types\n" + \
              f"{tab*4}7: Dragon Types {tab*2}8: Dark Types\n" + \
              f"{tab*4}9: Fairy Types {tab*3}10: Normal Types\n" + \
              f"{tab*4}11: Fighting Types {tab*2}12: Flying Types\n" + \
              f"{tab*4}13: Poison Types {tab*2}14: Ground Types\n" + \
              f"{tab*4}15: Rock Types {tab*3}16: Bug Types\n" + \
              f"{tab*4}17: Ghost Types {tab*2}18: Steel Types\n" + \
              f"{tab*4}19: All Pokemon {tab*2}20: Pokemon (trimmed Height(m))\n" + \
              f"{tab*4}21: Pokemon (trimmed Weight(kg))\n" + \
              f"{tab*4}22: Pokemon (trimmed Height(m) & Weight(kg))\n" + \
              f"{tab*4}0: EXIT\n"

    print(ret_str)


def print_options_stat_analysis():
    ret_str = f"\n{tab * 6}1: Stat Totals\n" + \
              f"{tab * 4}2: HP{tab * 5}3: Speed\n" + \
              f"{tab * 4}4: Attack{tab * 4}5: Defense\n" + \
              f"{tab * 4}6: Special Attack{tab * 2}7: Special Defense\n" + \
              f"{tab * 4}8: Height(m){tab * 3}9: Weight(kg)\n" + \
              f"{tab * 4}0: EXIT\n"
    print(ret_str)


if __name__ == "__main__":

    while 1:
        print_options_home()
        val_home = input(f"\n{tab*2}Enter Desired Option: ")
        print(val_home)
        if val_home == "1":
            print_options_stat_analysis()
            val_stat_an = input(f"\n{tab * 2}Enter Desired Stat: ")
            if val_stat_an == "0":
                print("Exit")
                break
            else:
                do_stat_analysis(val_stat_an)
            continue

        elif val_home == "2":
            print(f"{tab*4} Are Pokemon Heights Normal or Log distributed?")
            continue

        elif val_home == "3":
            print(f"{tab*4} Random Pokemon Correlations")
            continue

        elif val_home == "4":
            print(f"{tab*4}Testing Normal Distribution against Actual Values")
            continue

        elif val_home == "5":
            print(f"{tab*4}Are Dragon Types Taller Than Non Dragon Types")
            continue

        elif val_home == "6":
            print_options_regression_analysis()
            val_reg_an = input(f"\n{tab*2}Enter Desired Set: ")
            if val_reg_an == "0":
                print("Exit")
                break
            else:
                do_regression_analysis(val_reg_an)
            continue
        else:
            print("Exit")
            break
