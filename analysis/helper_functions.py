import numpy as np
import matplotlib.pyplot as plt
tab: str = "\t"


def plot_hist(data, title='histogram', x_label='bin center', y_label='frequency', c='blue', tc='red',
              is_z_score=False, bins=20):
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    mean_plt = np.mean(data)
    std_plt = np.std(data)

    if is_z_score:
        plt.title(title)

        # plot histogram and return counts containing frequency and bin center data
        plt.hist(data, bins, color=c)
    else:
        plt.title(title)
        # plot histogram and return counts containing frequency and bin center data
        counts = plt.hist(data, bins, color=c)
        # text to be displayed on fig
        str_m = f'mean: {round(mean_plt, 3)}, std: {round(std_plt, 3)}'
        # location of text aligned with second bin center and half max frequency
        plt.annotate(str_m, [counts[1][1], np.max(counts[0]) / 2], color=tc)


def plot_norm_prob(data, y_label='Data', title='Normal Probability Plot'):
    a = np.random.randn(len(data))
    plt.scatter(np.sort(a), np.sort(data))
    plt.xlabel('Standard Normal')
    plt.ylabel(y_label)
    plt.title(title)


def plot_cdf(data, title="CDF", x_label='x', y_label='prob(value $\leq$ x)'):
    x_cdf = np.sort(data)
    size = len(data)
    y_cdf = (1 + np.arange(size)) / size
    plt.plot(x_cdf, y_cdf)
    plt.xlabel(x_label)
    plt.ylabel(y_label)  # between $$ is latex math mode
    plt.title(title)
    return x_cdf, y_cdf


def my_hist_data(data, bins=20):
    counts = plt.hist(data, bins)
    plt.close()
    bin_center_hist = (counts[1][1:] + counts[1][:-1]) / 2
    freq = counts[0] / len(data)
    return bin_center_hist, freq


def z_score(data):
    m = np.mean(data)
    s = np.std(data)

    return (data - m) / s


def corr_compute(x, y, x_label='x', y_label='y', modified=""):
    # corr x / y
    # compute pearson correlation coefficient
    pcc = x.corr(y, method='pearson')
    # compute spearman correlation coefficient
    scc = x.corr(y, method='spearman')
    # compute kendal correlation coefficient
    kcc = x.corr(y, method='kendall')

    corr_data = f"{tab * 4}Corelation between {x_label} and {y_label} {modified}\n" + \
                f"{tab * 5}Pearson CC = {round(pcc, 2)}\n" + \
                f"{tab * 5}Spearman CC = {round(scc, 2)}\n" + \
                f"{tab * 5}Kendall CC = {round(kcc, 2)}\n"
    return corr_data


def basic_stats_string(x_stats, x_label='x'):
    # output string
    stats_string = f"{tab * 4}{x_label} Statistics:\n" \
                   f"{tab * 5}Standard Deviation: {round(x_stats.loc['std'], 2)}\n" + \
                   f"{tab * 5}Mean: {round(x_stats.loc['mean'], 2)}\n" + \
                   f"{tab * 5}Min: {round(x_stats.loc['min'], 2)}\n" + \
                   f"{tab * 5}Max: {round(x_stats.loc['max'], 2)}\n"
    return stats_string
