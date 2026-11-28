# Day 17 Analytics Project quetion 1

"""Scenario 1: Basic Data Loading & Cleaning."""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#1. Load the dataset into a Pandas DataFrame.
df = pd.read_csv("railway_gauges.csv")

#2. Display the first 5 rows and column names.
data = df.head()
print(data)
print(df.columns.tolist())

#3. Check for missing values and replace them with 0.
print(df.isnull().sum())
df.fillna(0, inplace=True)

#4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
gauge_cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]

for col in gauge_cols:
    df[col] =pd.to_numeric(df[col],errors ="coerce").fillna(0)
    
""" Scenario 2: Simple Visualization"""

#1. Extract Year and Total columns.
yt = df[["Year","Total"]]

#2. Plot a line graph showing Total tracks over years.
plt.figure(figsize=(12, 6))
plt.plot(yt["Year"],yt["Total"],marker="o",color = "navy",linewidth =2)

#3. Add: Title and X and Y labels
plt.title("Total Railway Track Length Over Years (1964-65 to 2012-13)",fontsize=14, fontweight="bold")
plt.xlabel("Year",fontsize=12)
plt.ylabel("Total",fontsize=12)
plt.xticks(rotation =90)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("Graphs/scenario2_total_track_trend.png", dpi=300)
plt.close()

#4. Identify whether the trend is increasing or decreasing."""
"""Trend Direction: The overall trend is slightly increasing with minor mid-period fluctuations. Total track length rose from 6,876 in
1964-65 to a peak of 7,172 in 2012-13 (an overall net increase of 296 units, or ~4.3%), despite temporary dips around 1998–2001."""

#Scenario 3: Filtering + Bar Chart

#1. Filter the dataset for years after 2000.

df["first_year"] = df["Year"].str.split("-").str[0].astype(int)
df_after_2000 = df[df["first_year"] >2000].copy()
print(df_after_2000)

#2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
#3. Plot a grouped bar chart comparing all three gauges.
ax = df_after_2000.plot(
    x="Year",
    y=["Broad Gauge", "Metre Gauge", "Narrow Gauge"],
    kind="bar",
    figsize=(12, 6),
    width=0.8,
    color=["#1f77b4", "#ff7f0e", "#2ca02c"]
)


plt.title("Comparison of Railway Gauges After 2000", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Track Length", fontsize=12)

#4. Add legend and proper labels.

plt.legend(title="Gauge Type")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("Graphs/scenario3_grouped_bar_after_2000.png", dpi=300)
plt.close()

#5. Identify which gauge dominates in recent years.
"""
Dominant Gauge: Broad Gauge overwhelmingly dominates in recent years, growing steadily from 5,338 in 2001-02 to 6,577 in 2012-13,
while Metre Gauge and Narrow Gauge shrunk significantly."""

#Scenario 4: Feature Engineering + Pie Chart

#1. Calculate total sum of each gauge across all years.
gauge_totals = df[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum()
print(gauge_totals)

#2. Create a new structure (Series/DataFrame) for totals.
"""3. Plot a pie chart showing percentage contribution.
4. Add percentage labels (autopct).
"""

plt.figure(figsize=(8, 8))
plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#1f77b4", "#ff7f0e", "#2ca02c"],
    explode=(0.05, 0, 0)
)
plt.title("Cumulative Share of Railway Gauges (1964–2013)", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("Graphs/scenario4_gauge_contribution_pie.png", dpi=300)
plt.close()

#5. Interpret which gauge contributes the most.
"""Cumulative Totals:
	• Broad Gauge: 224,066 (65.0%)
	• Metre Gauge: 101,798 (29.5%)
	• Narrow Gauge: 18,953 (5.5%)
Interpretation: Broad Gauge contributes the most, accounting for nearly two-thirds of cumulative track length across the entire 49-year timeframe."""

#Scenario 5: Advanced Analysis + Multiple Graphs

#1. Create new columns: % Broad Gauge % Metre Gauge % Narrow Gauge
df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100

#2. Use NumPy (np.diff) to calculate yearly growth of Total tracks.

yearly_growth = np.diff(df["Total"])
# Prepend 0 for the first year since there is no prior year to compare against
df["Yearly_Growth"] = np.insert(yearly_growth, 0, 0)

# Identify top 3 years with highest growth
top_growth = df.sort_values(by="Yearly_Growth", ascending=False)[["Year", "Total", "Yearly_Growth"]].head(3)
print("\n--- Top 3 Years with Highest Track Growth ---")
print(top_growth)

# 3a. Line graph for all gauges
plt.figure(figsize=(12, 6))
plt.plot(df["Year"], df["Broad Gauge"], label="Broad Gauge", marker="o", linewidth=2)
plt.plot(df["Year"], df["Metre Gauge"], label="Metre Gauge", marker="s", linewidth=2)
plt.plot(df["Year"], df["Narrow Gauge"], label="Narrow Gauge", marker="^", linewidth=2)
plt.title("Trend of All Railway Gauges (1964-65 to 2012-13)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Track Length", fontsize=12)
plt.legend()
plt.xticks(rotation=90)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("Graphs/scenario5_all_gauges_line.png", dpi=300)
plt.close()


# 3b. Stacked bar chart showing composition
ax = df.plot(
    x="Year",
    y=["Broad Gauge", "Metre Gauge", "Narrow Gauge"],
    kind="bar",
    stacked=True,
    figsize=(14, 7),
    width=0.8,
    color=["#1f77b4", "#ff7f0e", "#2ca02c"]
)
plt.title("Composition of Railway Gauges Over Time (Stacked)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Track Length", fontsize=12)
plt.legend(title="Gauge Type")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Graphs/scenario5_stacked_composition.png", dpi=300)
plt.close()

print("\nAll graphs successfully saved to the 'graphs/' folder!")

# Growth Highlights & Final Conclusion

"""• Years with Highest Total Growth (via np.diff):
	1. 2003-04: +125 (jumped from 6,906 to 7,031)
	2. 2007-08: +116 (jumped from 6,909 to 7,025)
	3. 1965-66: +110 (jumped from 6,876 to 6,986)
• Decline in Gauges: Both Metre Gauge (dropped by 86.9%, from 2,891 in 1964-65 to 379 in 2012-13) and Narrow Gauge (dropped by 53.4%, from 464 to 216) show steep,
consistent declines."""

#• Final Conclusion:
""""Yes, the railway system is decisively shifting towards a single dominant gauge. While total track length stayed relatively
stable (~6,850–7,170), Broad Gauge's share rose from 51.2% in 1964-65 to 91.7% in 2012-13, demonstrating active gauge conversion (Project Unigauge) rather than
just new track laying."""















