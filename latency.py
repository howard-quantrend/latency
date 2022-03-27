import requests
import numpy as np
from scipy import stats
# import matplotlib.pyplot as plt
import time

def get_latency():
    result = requests.get("https://api.binance.com/api/v3/ping")
    return result.elapsed.microseconds / 1000


def main():
    all_latency = []
    for _ in range(100):
        all_latency.append(get_latency())
        time.sleep(0.1)

    all_latency = np.array(all_latency)
    print(f"mean: {all_latency.mean()}")
    print(f"median: {np.median(all_latency)}")
    print(f"kurt: {stats.kurtosis(all_latency)}")
    # plt.hist(all_latency)
    # plt.show()

main()