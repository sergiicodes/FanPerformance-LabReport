# FanPerformance-LabReport

## Thermal-Fluids Laboratory: ME 4251-502

---

## Abstract

The experiment aims to evaluate the performance of a fan by measuring various parameters like head, airflow, and power in Watts. The fan's performance was observed at different speeds, measured in hertz (Hz) and revolutions per minute (RPM). The study observed an increase in airflow with the increase in fan speed, which influenced other parameters such as heat and power.

---

## Objective

To understand the relationship between fan speed, airflow, and other performance metrics. The experiment also aims to validate the efficiency laws stated by the IEC (International Electrotechnical Commission) and NEMA (National Electrical Manufacturers Association).

---

## Methods

### Equipment Utilized
- Variable Power Supply
- LabVIEW system
- U-tube Manometers

### Procedure
The fan is powered at different frequencies, and various metrics like temperature, pressure, and brake horsepower are recorded.

---

## Results & Discussion

### Energy Content and Flow Rate

- **Head**: Head, or the measure of the energy content of the fluid in meters of air, is negatively correlated to flow rate in cubic meters per second. This observation aligns with the principles of fluid dynamics, where an increase in flow rate often leads to a decrease in pressure head due to Bernoulli's equation. The negative correlation suggests that as the fan speed increases, the ability of the fan to lift or "push" the air decreases.

![Figure_1](https://github.com/sergiicodes/FanPerformance-LabReport/assets/79073281/d41d6a62-4889-428f-af14-4c56975d701f)


### Energy and Flow Rate

- **Brake Horsepower**: Brake horsepower, a measurement of energy in watts, is positively linked to flow rate in cubic meters per second. This is consistent with the law of conservation of energy, as more energy is required to move a greater volume of air.

![Figure_2](https://github.com/sergiicodes/FanPerformance-LabReport/assets/79073281/77c62eb1-99c5-44c1-9017-42c4a6b9f490)


### Efficiency Metrics

- **Efficiency**: Efficiency has a positive quadratic relationship with flow rate in cubic meters per second. This suggests that there is an optimal flow rate at which the fan operates most efficiently, beyond which the efficiency starts to decline.

![Figure_3](https://github.com/sergiicodes/FanPerformance-LabReport/assets/79073281/ea5286d1-b37e-4817-9036-d50a4aef7787)


### Coefficients and Their Relationships

- **Head Coefficient**: The head coefficient has an inverse non-linear relationship with the capacity coefficient. This could be indicative of the fan's performance boundaries and is crucial for selecting the right fan for specific applications.

![Figure_4](https://github.com/sergiicodes/FanPerformance-LabReport/assets/79073281/8fcd3325-96ce-41bc-b0ca-372d424d50b9)


- **Power Coefficient**: The power coefficient has a directly positive and linear correlation to the capacity coefficient. This relationship is useful for scaling the fan's performance for different applications.

![Figure_5](https://github.com/sergiicodes/FanPerformance-LabReport/assets/79073281/d9518756-eb52-4d0e-bc95-487e4b86505d)


- **Efficiency**: Efficiency also has a quadratic relationship with the capacity coefficient, reinforcing the idea that there is an optimal operating point for the fan. 

![Figure_6](https://github.com/sergiicodes/FanPerformance-LabReport/assets/79073281/5f5b170f-5af8-4584-80de-02e3d38732f7)


---

## Conclusion

This experiment highlighted the principles governing scaling laws for pumps and fans—known as affinity laws. With increasing fan speeds, metrics such as brake horsepower and efficiency exhibit more pronounced variations. Efficiency, in particular, exhibited a quadratic relationship with airflow and has a global maximum. As fan speed increases—intuitively—so does the power required, and the rate of change in watts for Standard Cubic Feet per Minute (SCFM) also increases. The relationship between efficiency and airflow indicates there is a point of diminishing returns: where the efficiency starts decreasing after reaching its peak. 
This report also provides lines of best fit, allowing for the replication of the experiment under different conditions*.
*Note:* This report was completed and submitted in the summer of 2020; however, in the fall of 2023, I took the liberty of adding in additional confidence regions to several plots which can be replicated via the Python files but are not reflected in the report that is available in this repo. 


## Dependencies or Technologies Used

This project relies on Python scripts to generate various figures. Below are the libraries and technologies used:

- **Python**: The programming language used for all data processing and visualization tasks.
- **NumPy**: Used for numerical operations and data manipulation.
- **Matplotlib**: Used for plotting and visualizing the data.


### Example Script Structure

Each figure is generated from a separate Python script with a structure similar to the following:

```python
# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt

# Function to plot fan speed
def plot_fan_speed(ax, C_of_Q, C_of_P, label, color, marker):
    ...
# Fan speed data and plotting logic
...
# For the complete scripts, please refer to the scripts/ directory in the repository.
