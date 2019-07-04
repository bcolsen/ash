# ASH: Average Shifted Histograms for Python

![ASH Example](https://github.com/bcolsen/ash/blob/master/example.png)

## Requirements
- matplotlib >= 2.0.0
- numpy >= 1.7.0
- scipy
- pandas

It works well with the Spyder IDE in the [Anaconda](https://www.anaconda.com/) python distibution

## Usage
```python
# Import matplotlib and ash
import matplotlib.pyplot as plt
from ash import ash

# Set up the figure
fig = plt.figure()
ax = plt.subplot()

# Make an ash object with 1D distibution 'data'
ash_obj = ash(data)

#plot ASH as a line
ax.plot(ash_obj.ash_mesh,ash_obj_a.ash_den)

#plot the solid ASH
ash_obj.plot_ash_infill(ax)

# Make a Rugplot (the barcode like data representation)
ash_obj_a.plot_rug(ax)
```
See [ash_usage_example.py](https://github.com/bcolsen/ash/blob/master/ash_usage_example.py) for code to make the image above.

## Citations
If you enjoyed using this tool
#### Substance over Subjectivity: Moving beyond the Histogram
Sam L. Anderson, Erik J. Luber, Brian C. Olsen, and Jillian M. Buriak
Chemistry of Materials 2016 28 (17), 5973-5975
DOI: [10.1021/acs.chemmater.6b03430](https://doi.org/10.1021/acs.chemmater.6b03430)

