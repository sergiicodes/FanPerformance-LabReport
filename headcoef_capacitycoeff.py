# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
def plot_fan_speed(ax, C_of_Q, C_of_H, label, color, marker):
    ax.scatter(C_of_Q, C_of_H, color=color, marker=marker, label=label)
# Fan speed data
fan_speeds = [
    (30, [0.003509778, 0.002802584, 0.002121582, 0.00140129, 0.000707194, 0],
    [7.837768449, 8.820313207, 9.668874589, 10.16014697, 11.41065848, 11.41065848]),
    (42, [0.003872729, 0.003096312, 0.002310541, 0.001552833, 0.000767062, 0],
    [7.441295952, 8.671755529, 9.514848201, 10.13007799, 10.56301747, 11.01874324]),
    (54, [0.00420533, 0.003354078, 0.002524653, 0.001680677, 0.000843976, 0],
    [7.18163818, 8.518715081, 9.456047342, 10.14526224, 10.55879118, 10.57257548])
]

# Combine data into 1D vectors
CofQ = np.concatenate([C_of_Q for _, C_of_Q, _ in fan_speeds])
CofH = np.concatenate([C_of_H for _, _, C_of_H in fan_speeds])

# Overall plot settings
fig, ax = plt.subplots()
ax.set_xlabel('$C_{Q}$')
ax.set_ylabel('$C_{H}$')
ax.set_title('Head Coefficient ($C_{H}$) as a function of the Capacity Coefficient ($C_{Q}$)')
ax.grid(True)

# Plot each fan speed
for speed, C_of_Q, C_of_H in fan_speeds:
    color = "green" if speed == 30 else ("red" if speed == 42 else "blue")
    marker = "s" if speed == 30 else ("d" if speed == 42 else "o")
    label = f"{speed} rps"
    plot_fan_speed(ax, C_of_Q, C_of_H, label, color, marker)

# Fit a second degree polynomial to the data
model = np.poly1d(np.polyfit(CofQ, CofH, 2))

# Plot the curve fit
polyline = np.linspace(0, max(CofQ))
ax.plot(polyline, model(polyline), label="Curve Fit")
ax.legend(loc='upper right')
plt.show()