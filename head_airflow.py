# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
def fit_and_plot(Q_actual, Head, speed_label):
    Q_actual = np.array(Q_actual)
    Head = np.array(Head)
    model = np.poly1d(np.polyfit(Q_actual, Head, degree_of_fit))
    polyline = np.linspace(0, Q_actual[0], num_points)
    ax.scatter(Q_actual, Head)
    ax.plot(polyline, model(polyline), label=speed_label)
    print(f"Model for {speed_label}: {model}")
    return model

degree_of_fit = 2
num_points = 100

# Fan speed data
fan_speeds = [
    ([0.0134, 0.0107, 0.0081, 0.00535, 0.0027, 0], [181.92899, 204.73565, 224.43232, 235.83565, 264.86232, 264.86232], '30 rps'),
    ([0.0207, 0.01655, 0.01235, 0.0083, 0.0041, 0], [338.54322, 394.52322, 432.87989, 460.86989, 480.56655, 501.29989], '42 rps'),
    ([0.0289, 0.02305, 0.01735, 0.01155, 0.0058, 0], [540.10476, 640.66142, 711.15476, 762.98809, 794.08809, 795.12476], '54 rps')
]

fig, ax = plt.subplots()

for Q_actual, Head, speed_label in fan_speeds:
    fit_and_plot(Q_actual, Head, speed_label)
    
# Overall Plot Settings
ax.set_xlabel('Flow rate, Q [m$^3$/s]')
ax.set_ylabel('Head, H [m of air]')
ax.set_title('Head as a Function of Flow Rate')
ax.legend(loc='upper right')
ax.grid(True)
plt.show()