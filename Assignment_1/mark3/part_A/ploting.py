import matplotlib.pyplot as plt


def plot_results(results, title, text_lengths, adjust_dimensions=False):
    plt.figure(figsize=(14, 8))

    if adjust_dimensions:
        plt.xlabel('Text Length (thousands of characters)')
        plt.ylabel('Running Time (microseconds)')
        for name, times in results.items():
            results[name] = [t*10**6 for t in times]
    else:
        text_lengths = [length / 10_000 for length in text_lengths]
        plt.xlabel('Text Length (10 000 characters)')
        plt.ylabel('Running Time (seconds)')

    plt.title(title)
    plt.grid(True)

    for name, times in results.items():
        plt.plot(text_lengths, times, label=name)

    plt.legend()
    plt.gca().set_facecolor('black')
    plt.show()


