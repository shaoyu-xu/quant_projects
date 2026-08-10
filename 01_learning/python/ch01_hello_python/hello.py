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

# TODO: 完成数据处理函数
# FIXME: 这里有空值需要处理
# BUG: 计算结果有偏差
# NOTE: 该函数时间复杂度为 O(n²)
# OPTIMIZE: 可以改用向量化操作
# HACK: 临时绕过了权限校验
# WARNING: 该接口已废弃，请勿使用