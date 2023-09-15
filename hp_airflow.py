# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
def fit_and_plot(Q_actual, Bhp, speed_label):
    model = np.poly1d(np.polyfit(Q_actual, Bhp, degree_of_fit))
    polyline = np.linspace(0, Q_actual[0], num_points)
    plt.scatter(Q_actual, Bhp)
    plt.plot(polyline, model(polyline), label=speed_label)
    print(f"Model for {speed_label}: {model}")
    return model

degree_of_fit = 1
num_points = 100

# Fan speed data
fan_speeds = [
    ([0.0134, 0.0107, 0.0081, 0.00535, 0.0027, 0], [330, 290, 240, 190, 140, 110], '30 rps'),
    ([0.0207, 0.01655, 0.01235, 0.0083, 0.0041, 0], [880, 740, 620, 500, 340, 250], '42 rps'),
    ([0.0289, 0.02305, 0.01735, 0.01155, 0.0058, 0], [1660, 1370, 1180, 960, 680, 470], '54 rps')
]
fig, ax = plt.subplots()

for Q_actual, Bhp, speed_label in fan_speeds:
    fit_and_plot(Q_actual, Bhp, speed_label)
    
# Overall Plot Settings
ax.set_xlabel('Flow rate, Q [m$^3$/s]')
ax.set_ylabel('Brake Horsepower, Bhp [W]')
ax.set_title('Power as a Function of Flow Rate')
ax.legend(loc='upper left')
ax.grid(True)
plt.show()