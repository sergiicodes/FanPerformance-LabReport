# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
def fit_and_plot(Q_actual, efficiency, speed_label):
    model = np.poly1d(np.polyfit(Q_actual, efficiency, degree_of_fit))
    polyline = np.linspace(0, Q_actual[0], num_points)
    plt.scatter(Q_actual, efficiency)
    plt.plot(polyline, model(polyline), label=speed_label)
    print(f"Model for {speed_label}: {model}")
    return model

degree_of_fit = 2
num_points = 100

# Fan speed data
fan_speeds = [
    ([0.0134, 0.0107, 0.0081, 0.00535, 0.0027, 0], [0.088649034, 0.090648476, 0.09089509, 0.079687626, 0.061296708, 0], '30 rps'),
    ([0.0207, 0.01655, 0.01235, 0.0083, 0.0041, 0], [0.095561518, 0.105881502, 0.103472257, 0.091805281, 0.069540807, 0], '42 rps'),
    ([0.0289, 0.02305, 0.01735, 0.01155, 0.0058, 0], [0.112836343, 0.129348139, 0.125476628, 0.110156406, 0.081277252, 0], '54 rps')
]

fig, ax = plt.subplots()

for Q_actual, efficiency, speed_label in fan_speeds:
    fit_and_plot(Q_actual, efficiency, speed_label)
    
# Overall Plot Settings
ax.set_xlabel('Flow rate, Q [m$^3$/s]')
ax.set_ylabel('Efficiency, η')
ax.set_title('Efficiency as a Function of Flow Rate')
ax.legend(loc='upper left')
ax.grid(True)
plt.show()