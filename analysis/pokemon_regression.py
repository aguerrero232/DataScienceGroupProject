import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import loaddata
import helper_functions

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score as r2
from sklearn import linear_model

separator_char = ", "
separator = '---------------------------------------------------------------'
tab: str = "\t"

x_cols = loaddata.stat_cols
y_cols = loaddata.physical_attr_cols


def pokemon_regression_analysis(set_name, set_data, z_set_data, trim_data='', modified_data_tag=''):
    # ----------------------------------------------------------------------------------
    print(f'{separator + separator}\n')
    print(f'{tab * 7}- - - Pokemon Data Analysis - Pokemon Linear Regression - - -')
    print(f'{tab * 14}Group 18\n')
    print(f'{separator + separator}\n')
    print(f'{tab * 7}Relevant data about the figures will be printed to the console to\n'
          f'{tab * 6}conserve space, please refer to the console using the figure numbers provided.\n'
          f'{tab * 14}Thank you!\n')
    print(f'{separator + separator}\n')
    print(f"{tab * 2}Looking at {set_name} data! {modified_data_tag}\n")
    print(f'{separator + separator}\n')

    if len(trim_data) > 0:
        print(trim_data)

    print(helper_functions.data_set_stats(set_data, set_name + " " + modified_data_tag, loaddata.total_attr,
                                          loaddata.study_attr, loaddata.cols, loaddata.z_cols))
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    curr_fig = "1"
    print(f'{separator + separator}\n')
    print(f'{tab * 3}- - - Figure {curr_fig}: {set_name} Stat Points Distributions {modified_data_tag} - - -\n')
    plt.figure(figsize=(9, 6))
    set_data[loaddata.stat_cols].boxplot()
    plt.title(f"Figure {curr_fig}: {set_name} Stat Point Distributions {modified_data_tag}")
    plt.show()
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    curr_fig = "2"
    print(f'{separator + separator}\n')
    print(f'{tab * 3}- - - Figure {curr_fig}: {set_name} Height(m) and Weight(kg) Distributions {modified_data_tag} - - -\n')
    plt.figure(figsize=(9, 6))
    set_data[loaddata.physical_attr_cols].boxplot()
    plt.title(f"Figure {curr_fig}: {set_name} Height(m) and Weight(kg) Distributions {modified_data_tag}")
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    curr_fig = "2b"
    print(f'{separator + separator}\n')
    print(
        f'{tab * 3}- - - Figure {curr_fig}: {set_name} Height(m) and Weight(kg) Distributions (standardized) {modified_data_tag} - - -\n')
    plt.figure(figsize=(9, 6))
    z_set_data[loaddata.physical_attr_cols].boxplot()
    plt.title(f"Figure {curr_fig}: {set_name} Height(m) and Weight(kg) Distributions (standardized) {modified_data_tag}")
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    curr_fig = "3"

    if len(x_cols) < 2:
        x_values = np.array(z_set_data[x_cols]).reshape(-1, 1)
    else:
        x_values = np.array(z_set_data[x_cols])

    if len(y_cols) < 2:
        y_values = np.array(z_set_data[y_cols]).reshape(-1, 1)
    else:
        y_values = np.array(z_set_data[y_cols])

    x_train, x_test, y_train, y_test = train_test_split(x_values, y_values, test_size=0.2, random_state=0)

    lr = linear_model.LinearRegression()
    lr.fit(x_train, y_train)
    score = lr.score(x_test, y_test)
    co_ef_z_and_d = pd.DataFrame(lr.coef_)
    pred = lr.predict(x_values)
    r2_val = r2(y_values, pred)

    print(f'{separator + separator}\n')
    print(f'{tab * 3}- - - Figure {curr_fig}: Linear Regression on {set_name} Data (standardized) {modified_data_tag} '
          f'- - -\n')
    print(f'{tab * 1}Testing: {separator_char.join(x_cols)} (standardized)'
          f'{tab * 1}Against: {separator_char.join(y_cols)} (standardized)\n')
    print(f"{tab * 4}Accuracy: {round(score, 2)}")
    print(f"{tab * 4}R2: {round(r2_val, 2)}\n")
    print(f"\n{tab * 5}What is R2?:")
    print(f"{tab * 6}It is the percentage of variation in the dependent or predicted variable(s)\n"
          f"{tab * 6}({separator_char.join(y_cols)}).\n\n"
          f"{tab * 6}that can be explained by variation in the independent or explanatory variable(s)\n"
          f"{tab * 6}({separator_char.join(x_cols)}).\n")

    plt.figure(figsize=(12, 8))
    plt.imshow(co_ef_z_and_d)
    cb = plt.colorbar()
    cb.set_label('coefficient', rotation=90)
    plt.xticks(range(0, 6), x_cols, rotation=90)
    plt.yticks(range(0, 2), y_cols)
    plt.title(f"Figure {curr_fig}: Linear Reg. on {set_name} Data (standardized) {modified_data_tag}")
    plt.legend(x_cols)
    plt.show()
    print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    curr_fig = "4"
    print(f'{separator + separator}\n')
    print(f'{tab * 3}- - - Figure {curr_fig}: LR on {set_name} Attack vs Sp.Attack {modified_data_tag} - - -\n')

    X = set_data['attack'].values.reshape(-1, 1)
    Y = set_data['sp_attack']

    set_data_attack_stat_stats = set_data['attack'].describe()

    lr = linear_model.LinearRegression()
    lr.fit(X, Y)
    lr_cc = lr.coef_[0]
    lr_intercept = lr.intercept_

    pred = lr.predict(X)

    print(f'{tab * 4}alpha = {round(lr_intercept, 2)}')
    print(f'{tab * 4}beta = {round(lr_cc, 2)}\n')
    print(f'{tab * 4}Equation obtained by linear regression: sp_attack = {round(lr_cc, 2)} * attack + '
          f'{round(lr_intercept, 2)}.\n')
    test_attack = np.random.randint(round(set_data_attack_stat_stats['min']), round(set_data_attack_stat_stats['max']), 1)[0]
    pred_atk_sp_atk = round(lr.predict(pd.DataFrame([test_attack]).values.reshape(-1, 1))[0])
    print(f"{tab * 4}{'- ' * 2}Predicting Sp Attack given Attack {'- ' * 2}\n\n"
          f"{tab * 4}Given: \n"
          f"{tab * 5}Attack = {test_attack}\n\n"
          f"{tab * 4}Predicted SP.Attack --> {pred_atk_sp_atk}\n")
    print(f'{separator + separator}\n')

    plt.scatter(X, Y)
    plt.plot(X, pred, 'r-')
    plt.xlabel('Attack')
    plt.ylabel('Sp.Attack')
    plt.legend(['predicted', 'actual'])
    plt.title(f'{curr_fig}: LR Attack And Sp.Attack for {set_name} {modified_data_tag}')
    plt.show()

    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------
    curr_fig = "5"
    print(f'{separator + separator}\n')
    print(f'{tab * 3}- - - Figure {curr_fig}: LR on {set_name} Defense vs Sp.Defense {modified_data_tag} - - -\n')

    X = set_data['sp_defense'].values.reshape(-1, 1)
    Y = set_data['defense']

    set_data_sp_defense_stat_stats = set_data['defense'].describe()

    lr = linear_model.LinearRegression()
    lr.fit(X, Y)
    lr_cc = lr.coef_[0]
    lr_intercept = lr.intercept_

    pred = lr.predict(X)

    print(f'{tab * 4}alpha = {round(lr_intercept, 2)}')
    print(f'{tab * 4}beta = {round(lr_cc, 2)}\n')
    print(f'{tab * 4}Equation obtained by linear regression: defense = {round(lr_cc, 2)} * sp_defense + '
          f'{round(lr_intercept, 2)}.\n')
    test_sp_defense = np.random.randint(round(set_data_sp_defense_stat_stats['min']), round(set_data_sp_defense_stat_stats['max']), 1)[0]
    pred_sp_def_def = round(lr.predict(pd.DataFrame([test_sp_defense]).values.reshape(-1, 1))[0])
    print(f"{tab * 4}{'- ' * 2}Predicting Defense given Sp. Defense {'- ' * 2}\n\n"
          f"{tab * 4}Given: \n"
          f"{tab * 5}Sp. Defense = {test_sp_defense}\n\n"
          f"{tab * 4}Predicted Defense --> {pred_sp_def_def}\n")
    print(f'{separator + separator}\n')

    plt.scatter(X, Y)
    plt.plot(X, pred, 'r-')
    plt.xlabel('Sp.Defense')
    plt.ylabel('Defense')
    plt.legend(['predicted', 'actual'])
    plt.title(f'{curr_fig}: LR Defense And Sp.Defense for {set_name} {modified_data_tag}')
    plt.show()

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------

    curr_fig = "6"
    print(f'{separator + separator}\n')
    print(f'{tab * 3}- - - Figure {curr_fig}: LR on {set_name} Weight(kg) vs Speed {modified_data_tag} - - -\n')

    X = set_data['weight_kg'].values.reshape(-1, 1)
    Y = set_data['speed']

    set_data_weight_stats = set_data['weight_kg'].describe()

    lr = linear_model.LinearRegression()
    lr.fit(X, Y)
    lr_cc = lr.coef_[0]
    lr_intercept = lr.intercept_

    pred = lr.predict(X)

    print(f'{tab * 4}alpha = {round(lr_intercept, 2)}')
    print(f'{tab * 4}beta = {round(lr_cc, 2)}\n')
    print(f'{tab * 4}Equation obtained by linear regression: speed = {round(lr_cc, 2)} * weight + '
          f'{round(lr_intercept, 2)}.\n')
    test_weight = np.random.randint(round(set_data_weight_stats['min']), round(set_data_weight_stats['max']), 1)[0]
    pred_weight_spd = round(lr.predict(pd.DataFrame([test_weight]).values.reshape(-1, 1))[0])
    print(f"{tab * 4}{'- ' * 2}Predicting Speed given Weight(kg) {'- ' * 2}\n\n"
          f"{tab * 4}Given: \n"
          f"{tab * 5}Weight = {test_weight}(kg)\n\n"
          f"{tab * 4}Predicted Speed --> {pred_weight_spd}\n")
    print(f'{separator + separator}\n')

    plt.scatter(X, Y)
    plt.plot(X, pred, 'r-')
    plt.xlabel('Weight(kg)')
    plt.ylabel('Speed')
    plt.legend(['predicted', 'actual'])
    plt.title(f'{curr_fig}: LR Weight(kg) And Speed for {set_name} {modified_data_tag}')
    plt.show()

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------

    return

    # # ----------------------------------------------------------------------------------
    # curr_fig = "1b"
    # print(f'{separator + separator}\n')
    # print(f'{tab * 3}- - - Figure {curr_fig}: {set_name} Stat Point Data (standardized) {modified_data_tag} - - -\n')
    # plt.figure(figsize=(9, 6))
    # z_set_data[loaddata.stat_cols].boxplot()
    # plt.title(f"Figure {curr_fig}: {set_name} Stat Point Distributions (standardized) {modified_data_tag}")
    # plt.show()
    # print(f'{separator + separator}\n')
    # # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # curr_fig = "4"
    # y_cols = ['weight_kg']
    #
    # if len(x_cols) < 2:
    #     x_values = np.array(set_data[x_cols]).reshape(-1, 1)
    # else:
    #     x_values = np.array(set_data[x_cols])
    #
    # if len(y_cols) < 2:
    #     y_values = np.array(set_data[y_cols]).reshape(-1, 1)
    # else:
    #     y_values = np.array(set_data[y_cols])
    #
    # x_train, x_test, y_train, y_test = train_test_split(x_values, y_values, test_size=0.2, random_state=0)
    # lr = linear_model.LinearRegression()
    # lr.fit(x_train, y_train)
    # score = lr.score(x_test, y_test) * 100
    # co_ef_z_and_d = pd.DataFrame(lr.coef_)
    # pred = lr.predict(x_values)
    # r2_val = r2(y_values, pred) * 100
    # print(f'{separator + separator}\n')
    # print(f'{tab * 3}- - - Figure {curr_fig}: Linear Regression on {set_name} Data {modified_data_tag} - - -\n')
    # print(f'{tab * 1}Testing: {separator_char.join(x_cols)}'
    #       f'{tab * 1}Against: {separator_char.join(y_cols)}\n')
    # print(f"{tab * 4}Accuracy: {round(score)}%")
    # print(f"{tab * 4}R2: {round(r2_val)}%\n")
    # print(f"\n{tab * 5}What is R2?:")
    # print(f"{tab * 6}It is the percentage of variation in the dependent or predicted variable(s)\n"
    #       f"{tab * 6}({separator_char.join(y_cols)}).\n\n"
    #       f"{tab * 6}that can be explained by variation in the independent or explanatory variable(s)\n"
    #       f"{tab * 6}({separator_char.join(x_cols)}).\n")
    # co_ef_z_and_d.plot.bar()
    # ax = plt.gca()
    # ax.set_xticklabels(labels=y_cols, rotation=0)
    # plt.ylabel('Coefficient')
    # plt.title(f"Figure {curr_fig}: Linear Reg. on {set_name} Data")
    # plt.legend(x_cols)
    # plt.show()
    # print(f'{separator + separator}\n')
    # # ----------------------------------------------------------------------------------
    #
    # # ----------------------------------------------------------------------------------
    # curr_fig = "4b"
    #
    # if len(x_cols) < 2:
    #     x_values = np.array(z_set_data[x_cols]).reshape(-1, 1)
    # else:
    #     x_values = np.array(z_set_data[x_cols])
    #
    # if len(y_cols) < 2:
    #     y_values = np.array(z_set_data[y_cols]).reshape(-1, 1)
    # else:
    #     y_values = np.array(z_set_data[y_cols])
    #
    # x_train, x_test, y_train, y_test = train_test_split(x_values, y_values, test_size=0.2, random_state=0)
    # lr = linear_model.LinearRegression()
    # lr.fit(x_train, y_train)
    # score = lr.score(x_test, y_test) * 100
    # co_ef_z_and_d = pd.DataFrame(lr.coef_)
    # pred = lr.predict(x_values)
    # r2_val = r2(y_values, pred) * 100
    # print(f'{separator + separator}\n')
    # print(f'{tab * 3}- - - Figure {curr_fig}: Linear Regression on {set_name} Data (standardized) {modified_data_tag} '
    #       f'- - -\n')
    # print(f'{tab * 1}Testing: {separator_char.join(x_cols)} (standardized)'
    #       f'{tab * 1}Against: {separator_char.join(y_cols)} (standardized)\n')
    # print(f"{tab * 4}Accuracy: {round(score)}%")
    # print(f"{tab * 4}R2: {round(r2_val)}%\n")
    # print(f"\n{tab * 5}What is R2?:")
    # print(f"{tab * 6}It is the percentage of variation in the dependent or predicted variable(s)\n"
    #       f"{tab * 6}({separator_char.join(y_cols)}).\n\n"
    #       f"{tab * 6}that can be explained by variation in the independent or explanatory variable(s)\n"
    #       f"{tab * 6}({separator_char.join(x_cols)}).\n")
    # co_ef_z_and_d.plot.bar()
    # ax = plt.gca()
    # ax.set_xticklabels(labels=y_cols, rotation=0)
    # plt.ylabel('Coefficient')
    # plt.title(f"Figure {curr_fig}: Linear Reg. on {set_name} Data (standardized)")
    # plt.legend(x_cols)
    # plt.show()
    # print(f'{separator + separator}\n')
    # ----------------------------------------------------------------------------------

    # # ----------------------------------------------------------------------------------
    # curr_fig = "3"
    #
    # if len(x_cols) < 2:
    #     x_values = np.array(set_data[x_cols]).reshape(-1, 1)
    # else:
    #     x_values = np.array(set_data[x_cols])
    #
    # if len(y_cols) < 2:
    #     y_values = np.array(set_data[y_cols]).reshape(-1, 1)
    # else:
    #     y_values = np.array(set_data[y_cols])
    #
    # x_train, x_test, y_train, y_test = train_test_split(x_values, y_values, test_size=0.2, random_state=0)
    # lr = linear_model.LinearRegression()
    # lr.fit(x_train, y_train)
    # score = lr.score(x_test, y_test) * 100
    # co_ef_z_and_d = pd.DataFrame(lr.coef_)
    # pred = lr.predict(x_values)
    # r2_val = r2(y_values, pred) * 100
    # print(f'{separator + separator}\n')
    # print(f'{tab * 3}- - - Figure {curr_fig}: Linear Regression on {set_name} Data {modified_data_tag} - - -\n')
    # print(f'{tab * 1}Testing: {separator_char.join(x_cols)}'
    #       f'{tab * 1}Against: {separator_char.join(y_cols)}\n')
    # print(f"{tab * 4}Accuracy: {round(score)}%")
    # print(f"{tab * 4}R2: {round(r2_val)}%\n")
    # print(f"\n{tab * 5}What is R2?:")
    # print(f"{tab * 6}It is the percentage of variation in the dependent or predicted variable(s)\n"
    #       f"{tab * 6}({separator_char.join(y_cols)}).\n\n"
    #       f"{tab * 6}that can be explained by variation in the independent or explanatory variable(s)\n"
    #       f"{tab * 6}({separator_char.join(x_cols)}).\n")
    # # co_ef_z_and_d.plot.bar()
    # # ax = plt.gca()
    # # ax.set_xticklabels(labels=y_cols, rotation=0)
    # plt.figure(figsize=(16, 8))
    # plt.imshow(co_ef_z_and_d)
    # plt.colorbar()
    # plt.xticks(range(0, 6), x_cols, rotation=90)
    # plt.yticks(range(0, 2), y_cols)
    # plt.title(f"Figure {curr_fig}: Linear Reg. on {set_name} Data. {modified_data_tag}")
    # plt.legend(x_cols)
    # plt.show()
    # print(f'{separator + separator}\n')
    # # ----------------------------------------------------------------------------------
    # # ----------------------------------------------------------------------------------
    # curr_fig = "4"
    #
    # if len(x_cols) < 2:
    #     x_values = np.array(set_data[x_cols]).reshape(-1, 1)
    # else:
    #     x_values = np.array(set_data[x_cols])
    #
    # x_train, x_test, y_train, y_test = train_test_split(x_values, x_values, test_size=0.2, random_state=0)
    #
    # lr = linear_model.LinearRegression()
    # lr.fit(x_train, y_train)
    # score = lr.score(x_test, y_test) * 100
    # co_ef = pd.DataFrame(lr.coef_)
    # pred = lr.predict(x_values)
    # r2_val = r2(x_values, pred) * 100
    #
    # print(f'{separator + separator}\n')
    # print(f'{tab * 3}- - - Figure {curr_fig}: Linear Regression on {set_name} Data (standardized) {modified_data_tag} '
    #       f'- - -\n')
    # print(f'{tab * 1}Testing: {separator_char.join(x_cols)} (standardized)'
    #       f'{tab * 1}Against: {separator_char.join(y_cols)} (standardized)\n')
    # print(f"{tab * 4}Accuracy: {round(score)}%")
    # print(f"{tab * 4}R2: {round(r2_val)}%\n")
    # print(f"\n{tab * 5}What is R2?:")
    # print(f"{tab * 6}It is the percentage of variation in the dependent or predicted variable(s)\n"
    #       f"{tab * 6}({separator_char.join(y_cols)}).\n\n"
    #       f"{tab * 6}that can be explained by variation in the independent or explanatory variable(s)\n"
    #       f"{tab * 6}({separator_char.join(x_cols)}).\n")
    #
    # # Displaying dataframe as an heatmap
    # # with diverging colourmap as RdYlBu
    # plt.imshow(co_ef)
    # plt.colorbar()
    # plt.xticks(range(0, 6), x_cols)
    # plt.yticks(range(0, 6), x_cols)
    # plt.title(f"Figure {curr_fig}: Corr of stats for {set_name} {modified_data_tag}")
    # plt.legend(x_cols)
    # plt.show()
    # print(f'{separator + separator}\n')
    # # ----------------------------------------------------------------------------------
