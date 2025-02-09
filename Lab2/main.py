import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def f(x1, x2):
    return np.cos(x1) / (1 + np.e ** (-2 * x2))

def generate_csv(size):
    file_name = "input.csv"

    x1 = np.linspace(-5, 5, size)
    x2 = np.linspace(-5, 5, size)
    y = f(x1, x2)

    pd.DataFrame({"y": y, "x1": x1, "x2": x2}).to_csv(file_name, index=False)

    return file_name

def parse_csv(file_name):
    data = pd.read_csv(file_name)
    return data

def paint_graphs(data):

    pairs = [
        ("x1", "x2", lambda x, fixed: f(x, fixed)),
        ("x2", "x1", lambda x, fixed: f(fixed, x))
    ]

    for var, fixed_var, curr_f in pairs:
        fixed_value = data[fixed_var].iloc[randint(0, len(data))]
        x = data[var]
        y = curr_f(x, fixed_value)

        plt.figure(figsize=(10, 5))
        plt.plot(x, y)
        plt.xlabel(var)
        plt.ylabel("y")
        plt.title(f"y({var}) and {fixed_var} = const ({fixed_value})")
        plt.grid()

        plt.show()

def print_stats(data):
    for var in ["x1", "x2", "y"]:
        print(var, f"min = {data[var].min()}\nmax = {data[var].max()}\naverage = {data[var].mean()}", sep="\n")
        print()

def generate_result_csv(data):
    result = data[(data["x1"] < data["x1"].mean()) | (data["x2"] < data["x2"].mean())]
    result.to_csv("result.csv", index=False)

def paint_3d_graphs(data):
    x1, x2 = np.meshgrid(data['x1'], data['x2'])
    y = f(x1, x2)
    
    ax = plt.axes(projection='3d')
    ax.plot_surface(x1, x2, y, cmap='viridis')

    plt.show()

def main():
    file_name = generate_csv(400)
    data = parse_csv(file_name)

    print_stats(data)
    paint_graphs(data)
    paint_3d_graphs(data)

    generate_result_csv(data)
main()
