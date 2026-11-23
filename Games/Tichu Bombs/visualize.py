import matplotlib.pyplot as plt
plt.rc("figure", autolayout=True)
plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlesize=14, titlepad=10)


def label_bars_center(bars, decimals=2, color="white", fontsize=12):
    """
    Write each bar's height as a percentage, centered inside the bar.
    """
    plt.gca().bar_label(
        bars,
        fmt=f"%.{decimals}f%%",
        label_type="center",
        color=color,
        fontsize=fontsize,
        fontweight="bold",
    )

xticks = ["Baseline", "Conservative", "Balanced", "Bomb-oriented"]
x = list(range(len(xticks)))
y = [5.0861, 20.7582, 14.4762, 20.1131]
plt.figure(figsize=(12, 7))
bars = plt.bar(x, y)
label_bars_center(bars)
plt.title("Bomb probabilities per strategy")
plt.xlabel("Strategies")
plt.ylabel("Probability [%]")
plt.xticks(x, xticks)
plt.show()