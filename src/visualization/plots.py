import matplotlib.pyplot as plt

def plot_importance(names, importance, title):
    plt.figure()
    plt.bar(names, importance)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
