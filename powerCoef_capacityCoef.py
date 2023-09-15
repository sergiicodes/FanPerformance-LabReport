# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
def plot_fan_speed(ax, C_of_Q, C_of_P, label, color, marker):
    ax.scatter(C_of_Q, C_of_P, color=color, marker=marker, label=label)

# Fan speed data
fan_speeds = [
    (30, [0.003509778, 0.002802584, 0.002121582, 0.001401292, 0.000707194, 0],
    [8.928635473, 7.846376628, 6.493553071, 5.140729515, 3.787905958, 2.976211824]),
    (42, [0.003872729, 0.003096312, 0.002310541, 0.001552833, 0.000767062, 0],
    [12.14780336, 10.21519828, 8.558679643, 6.902161003, 4.693469482, 3.451080501]),
    (54, [0.00420533, 0.003354078, 0.002524653, 0.001680677, 0.000843976, 0],
    [13.86226607, 11.44054489, 9.85389998, 8.016732187, 5.678518632, 3.924858466])
]

# Combine data into 1D vectors
CofQ = np.concatenate([C_of_Q for _, C_of_Q, _ in fan_speeds])
CofP = np.concatenate([C_of_P for _, _, C_of_P in fan_speeds])

# Overall plot settings
fig, ax = plt.subplots()
ax.set_xlabel('$C_{Q}$')
ax.set_ylabel('$C_{P}$')
ax.set_title('Power Coefficient ($C_{P}$) as a function of the Capacity Coefficient ($C_{Q}$)')
ax.grid(True)

# Plot each fan speed
for speed, C_of_Q, C_of_P in fan_speeds:
    color = "green" if speed == 30 else ("red" if speed == 42 else "blue")
    marker = "s" if speed == 30 else ("d" if speed == 42 else "o")
    label = f"{speed} rps"
    plot_fan_speed(ax, C_of_Q, C_of_P, label, color, marker)

# Fit a first degree polynomial to the data
model = np.poly1d(np.polyfit(CofQ, CofP, 1))

# Calculate the standard error of the estimate
residuals = CofP - model(CofQ)
mse = np.mean(residuals**2)
se = np.sqrt(mse)

# Set the confidence level (e.g., 95%)
confidence_level = 0.95

# Calculate the critical value for the confidence interval
from scipy.stats import t
n = len(CofQ)
t_critical = t.ppf((1 + confidence_level) / 2, n - 2)

# Calculate the margin of error
margin_of_error = t_critical * se

polyline = np.linspace(0, max(CofQ), num=100)

# Calculate the upper and lower bounds of the confidence interval
upper_bound = model(polyline) + margin_of_error
lower_bound = model(polyline) - margin_of_error

# Plot the curve fit with the shaded confidence region
ax.fill_between(polyline, lower_bound, upper_bound, color='gray', alpha=0.5, label=f'{int(confidence_level*100)}% Confidence Interval')

# Plot the curve fit
ax.plot(polyline, model(polyline), label="Curve Fit")
ax.legend(loc='upper left')
plt.show()
