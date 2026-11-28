#   ======================  RAILS & GAUGES  ============================
#
#   PROJECT NAME : RAILS & GAUGES - A Data Journey Along the Tracks
#   DATASET      : railway_gauges.csv  (Year, Broad / Metre / Narrow Gauge, Total)
#   TOOLS USED   : Pandas (data), NumPy (maths), Matplotlib (graphs)
#   STORY: Railway tracks come in different widths called "gauges".
#          In this project we load the data, clean it, draw graphs and
#          finally answer one big question:
#          "Is the railway moving towards ONE dominant gauge?"
#   HOW TO RUN : keep this main.py and the CSV file in the same folder, then
#                python main.py
#   NOTE       : All graphs are saved automatically inside a folder called
#                "graphs"
# =====================================================================


# =====================================================================
# IMPORTS  (everything the project needs, with the reason for each)
# =====================================================================
import os                          # to create the "graphs" folder
import pandas as pd                # to load the CSV and work with tables (DataFrame)
import numpy as np                 # for maths: np.diff, np.arange, np.polyfit
import matplotlib.pyplot as plt    # to draw and save the graphs


# =====================================================================
# SCENARIO 1 : Basic Data Loading & Cleaning
# =====================================================================

"""You are given a CSV file containing railway gauge data. 
Tasks: 
1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types."""

print("\n" + "=" * 60)
print("SCENARIO 1 : Basic Data Loading & Cleaning")
print("=" * 60)
      
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
    # to_numeric converts text like "3521" into a number.
    # errors="coerce" turns anything that is not a number into NaN,
    # and the fillna(0) after it makes that NaN a 0 again.
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("\nMissing values in each column (after):")
print(df.isnull().sum())
print("\nData types after conversion:")
print(df.dtypes)
    
# =====================================================================
# SCENARIO 2 : Simple Visualization (Total track growth)
# =====================================================================
"""You want a quick understanding of total railway track growth. 
Tasks: 
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing."""

print("\n" + "=" * 60)
print("SCENARIO 2 : Total Track Growth (Line Graph)")
print("=" * 60)

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

# 4. Identify whether the trend is increasing or decreasing
# Method 1: compare the first year with the last year
first_total = df["Total"].iloc[0]                 # total in the first year
last_total = df["Total"].iloc[-1]                 # total in the last year
change = last_total - first_total
print("\nFirst year total :", first_total)
print("Last year total  :", last_total)
print("Overall change   :", change)

if change > 0:
    print("Trend: INCREASING overall (first year -> last year).")
else:
    print("Trend: DECREASING overall (first year -> last year).")
    
# =====================================================================
# SCENARIO 3 : Filtering + Bar Chart (Modern railway expansion)
# =====================================================================
"""You are asked to analyze modern railway expansion. 
Tasks: 
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years."""

print("\n" + "=" * 60)
print("SCENARIO 3 : Years after 2000 (Grouped Bar Chart)")
print("=" * 60)


#1. Filter the dataset for years after 2000.

df["first_year"] = df["Year"].str.split("-").str[0].astype(int)
df_after_2000 = df[df["first_year"] >2000].copy()
print(df_after_2000)

#2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
GAUGES = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
df_after_2000 = df_after_2000[["Year"] + GAUGES]
print(df_after_2000)
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

# 5. Identify which gauge dominates in recent years
# Add up each gauge over the recent years and pick the biggest one
recent_totals = df_after_2000[GAUGES].sum()
print("\nSum of each gauge after 2000:")
print(recent_totals)
print("Dominant gauge in recent years:", recent_totals.idxmax())

# =====================================================================
# SCENARIO 4 : Feature Engineering + Pie Chart (Contribution of each gauge)
# =====================================================================
"""You want to analyze the contribution of each gauge type. 
Tasks: 
1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most."""

print("\n" + "=" * 60)
print("SCENARIO 4 : Contribution of Each Gauge (Pie Chart)")
print("=" * 60)

#1 & 2. Calculate total sum of each gauge across all years.new structure (Series/DataFrame) for totals.
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

# 5. Interpret which gauge contributes the most
top_gauge = gauge_totals.idxmax()
top_percent = gauge_totals.max() / gauge_totals.sum() * 100
print(f"\nInterpretation: {top_gauge} contributes the most "
      f"({top_percent:.1f}% of all gauge track).")


# =====================================================================
# SCENARIO 5 : Advanced Analysis + Multiple Graphs
# =====================================================================
"""You are asked to perform a complete analysis of railway trends. 
Tasks: 
1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges 
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
Is the railway system shifting towards a single dominant gauge?"""

print("\n" + "=" * 60)
print("SCENARIO 5 : Advanced Analysis + Multiple Graphs")
print("=" * 60)


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


# ------------------------------------------------------------
# STEP 5: IDENTIFY GAUGES WITH DECLINING TRENDS
# ------------------------------------------------------------

print("\nGauge Trend Analysis:")

for column in [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge"
]:

    starting_value = df[column].iloc[0]

    ending_value = df[column].iloc[-1]

    change = ending_value - starting_value

    print("\nGauge:", column)

    print("Starting Value:", starting_value)

    print("Ending Value:", ending_value)
    print("Overall Change:", change)

    if change > 0:
        print("Trend: Increasing")

    elif change < 0:
        print("Trend: Decreasing")

    else:
        print("Trend: No Change")

# ------------------------------------------------------------
# STEP 6: FINAL CONCLUSION
# ------------------------------------------------------------

print("\n======================================")
print("FINAL PROJECT CONCLUSION")
print("======================================")

# Compare gauge percentages in first and last years
first_broad = df["% Broad Gauge"].iloc[0]

last_broad = df["% Broad Gauge"].iloc[-1]

first_metre = df["% Metre Gauge"].iloc[0]

last_metre = df["% Metre Gauge"].iloc[-1]

first_narrow = df["% Narrow Gauge"].iloc[0]

last_narrow = df["% Narrow Gauge"].iloc[-1]

print("\nBroad Gauge Percentage Change:",
      round(last_broad - first_broad, 2), "%")
print("Metre Gauge Percentage Change:",
      round(last_metre - first_metre, 2), "%")
print("Narrow Gauge Percentage Change:",
      round(last_narrow - first_narrow, 2), "%")

if last_broad > first_broad:
    print(
        "\nConclusion: The railway system shows "
        "a shift towards Broad Gauge dominance."
    )

else:
    print(
        "\nConclusion: Broad Gauge percentage "
        "has not increased over the analyzed period."
    )

print("\nAll graphs successfully saved to the 'Graphs/' folder!")

# =====================================================================
#   END OF PROJECT - RAILS & GAUGES
#   All 5 scenarios done. Check the "graphs" folder for the saved images.
# =====================================================================














