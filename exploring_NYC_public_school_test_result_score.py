# Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a maximum score of 800 points. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.
# 
# Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend. 
# 
# You have been provided with a dataset called schools.csv, which is previewed below.
# 
# You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.

# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...
# Which NYC schools have the best math results?
average_math_80percent_condition = schools["average_math"] >= 640
best_math_schools = schools[average_math_80percent_condition][["school_name", "average_math"]].sort_values("average_math", ascending=False)
print(best_math_schools)

# What are the top 10 performing schools based on the combined SAT scores?
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False).head(10)
print(top_10_schools)

# Which single borough has the largest standard deviation in the combined SAT score?
# largest_std_dev = schools.groupby("borough")["total_SAT"].agg(["median"])
# schools[schools["borough"] == schools["borough"].max()]
# [["borough", "num_schools", "average_SAT"]]
borough_statistics = schools.groupby("borough")["total_SAT"].agg(num_schools="count", average_SAT="mean", std_SAT="std")
largest_std_dev = (borough_statistics.sort_values("std_SAT", ascending=False).head(1).reset_index().round({"average_SAT":2, "std_SAT":2}))
print(largest_std_dev)
