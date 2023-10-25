# Fitness Watch Data Analysis

This repository contains code for analyzing fitness watch data using Python. The data is stored in a CSV file named "Apple-Fitness-Data.csv." The code in the file "Fitness Watch Data Analysis.py" uses various data analysis and visualization techniques to explore and understand the fitness data. 

## Prerequisites

Before running the code, you will need the following Python libraries:

- Pandas
- Plotly

You can install these libraries using pip:

```bash
pip install pandas plotly
```

## Getting Started

### Clone the Repository

To get started, you can clone this repository using the following command:

```bash
git clone https://github.com/kayteekay1412/Fitness-Watch-Data-Analysis.git
```

### Running the Code

1. Make sure you have Python and the required libraries installed.
2. Open the "Fitness Watch Data Analysis.py" file.
3. Set the working directory to the location of the CSV file, "Apple-Fitness-Data.csv."
4. Run the code in your Python environment.

## Code Overview

### Measured Per Unit Time

This section of the code allows you to select a metric (Step Count, Distance, Energy Burned, or Walking Speed) and visualize how it changes over time using a line chart.

### Average Steps Per Day

This section calculates and visualizes the average step count per day using a bar chart.

### Calculate Walking Efficiency

Here, the code calculates walking efficiency and displays it over time using a line chart.

### Create Time Intervals

This part of the code creates time intervals (Morning, Afternoon, Evening) based on the time of the day.

### Variations in Step Count and Walking Speed by Time Interval

Visualizes variations in Step Count and Walking Speed by time interval using a scatter plot.

### Treemaps for Daily Averages

Generates treemaps to visualize daily averages for various metrics, including Step Count, Distance, Energy Burned, Flights Climbed, Walking Double Support Percentage, and Walking Speed.

### Treemaps for Daily Averages (Excluding Step Count)

Similar to the previous treemaps, but this time excluding the Step Count metric.

## Data File

The fitness data is stored in the "Apple-Fitness-Data.csv" file. Ensure that this file is present in the same directory as the code file.
