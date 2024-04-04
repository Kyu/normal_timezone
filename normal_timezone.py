import sys
import json

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


sys.tracebacklimit = 0  # Removes traceback from errors


def get_timezone_list(input_file: str) -> list[int]:
    with open(input_file, 'r') as file:
        json_data = json.load(file)

    tz_list = json_data.get("times")
    return tz_list


def get_score(timezone_list: list[int], percentile_grain=10, do_plot=False) -> (list[tuple], np.ndarray):
    percentile_list = np.arange(0, 100 + percentile_grain, percentile_grain)

    mean = stats.tmean(timezone_list)
    stdev = stats.tstd(timezone_list)

    # Calculate the PDF for each timezone
    pdf_values = stats.norm.pdf(timezone_list, mean, stdev)

    # Normalize the probabilities to get weights
    weights = pdf_values / pdf_values.sum()

    # Create a table with numbers and weights
    weight_table = list(zip(timezone_list, weights))

    return weight_table, pdf_values  # stats.scoreatpercentile(timezone_list, percentile_list)


def make_plot(tz_list: list[int], pdf_values: np.ndarray):
    plt.plot(tz_list, pdf_values, label=f'Label')
    plt.title('Title')
    plt.xlabel('Number')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.show()


tlist = get_timezone_list("times_example.json")
print(tlist)
print()

s = get_score(tlist)
print(s[0])

sorted_s = sorted(s[0], key=lambda x: x[1], reverse=True)
print(sorted_s)

make_plot(tlist, s[1])
