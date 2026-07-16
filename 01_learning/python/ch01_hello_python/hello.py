# First Python script on x14
import sys
import pandas as pd 

print("Hello from X14!")
print(f"Python version:{sys.version}")

# Quick pandas test
data = {'name':['Alice','Bob','Charlie'], 'score':[85,92,78]}
df = pd.DataFrame(data)
print("\nPandas DataFrame test:")
print(df)