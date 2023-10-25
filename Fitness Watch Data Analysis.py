# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:39:36 2023

@author: ktk
"""
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
import plotly.express as px
data = pd.read_csv("Apple-Fitness-Data.csv")

#Measured Per Unit Time
k = int(input("Enter"))
if k==1:
    a="Step Count"
elif k==2:
    a="Distance"
elif k==3:
    a="Energy Burned"
elif k==4:
    a="Walking Speed"
fig1 = px.line(data, x="Time",y=a,title=f"{a} over Time")
fig1.show()

#Average Steps Per Day
average_step_count_per_day = data.groupby("Date")["Step Count"].mean().reset_index()
fig5 = px.bar(average_step_count_per_day, x="Date",y="Step Count",title="Average Step Count per Day")
fig5.update_xaxes(type="category")
fig5.show()

# Calculate Walking Efficiency
data["Walking Efficiency"] = data["Distance"] / data["Step Count"]
fig6 = px.line(data, x="Time", y="Walking Efficiency",title="Walking Efficiency Over Time")
fig6.show()

# Create Time Intervals
time_intervals = pd.cut(pd.to_datetime(data["Time"]).dt.hour,
                        bins=[0, 12, 18, 24],
                        labels=["Morning", "Afternoon", "Evening"], 
                        right=False)

data["Time Interval"] = time_intervals

# Variations in Step Count and Walking Speed by Time Interval
fig7 = px.scatter(data, x="Step Count",
                  y="Walking Speed",
                  color="Time Interval",
                  title="Step Count and Walking Speed Variations by Time Interval",
                  trendline='ols')
fig7.show()
# Reshape data for treemap
daily_avg_metrics = data.groupby("Date").mean().reset_index()

daily_avg_metrics_melted = daily_avg_metrics.melt(id_vars=["Date"], 
                                                  value_vars=["Step Count", "Distance", 
                                                              "Energy Burned", "Flights Climbed", 
                                                              "Walking Double Support Percentage", 
                                                              "Walking Speed"])

# Treemap of Daily Averages for Different Metrics Over Several Weeks
fig = px.treemap(daily_avg_metrics_melted,
                 path=["variable"],
                 values="value",
                 color="variable",
                 hover_data=["value"],
                 title="Daily Averages for Different Metrics")
fig.show()
# Select metrics excluding Step Count
metrics_to_visualize = ["Distance", "Energy Burned", "Flights Climbed", 
                        "Walking Double Support Percentage", "Walking Speed"]

# Reshape data for treemap
daily_avg_metrics_melted = daily_avg_metrics.melt(id_vars=["Date"], value_vars=metrics_to_visualize)

fig = px.treemap(daily_avg_metrics_melted,
                 path=["variable"],
                 values="value",
                 color="variable",
                 hover_data=["value"],
                 title="Daily Averages for Different Metrics (Excluding Step Count)")
fig.show()