# Python Data Analysis Learning

> My self‑learning journey in Python for data analysis and quantitative finance.

---

## 📚 Learning Progress

- [ ] Python Basics (syntax, functions, data types)
- [ ] Pandas Fundamentals (Series, DataFrame, indexing)
- [ ] Data Cleaning & Preprocessing
- [ ] Data Visualization (Matplotlib, Seaborn)
- [ ] NumPy for Numerical Computing
- [ ] Time Series Analysis
- [ ] Quantitative Strategy Backtesting

---

## 📁 Folder Structure

python/
├── 01_pandas_basics/ # Pandas core operations
├── 02_data_cleaning/ # Missing values, duplicates, outliers
├── 03_data_viz/ # Matplotlib, Seaborn
├── 04_pandas_advanced/ # Merge, apply, pivot, time series
└── projects/ # Complete analysis projects

---

## 📖 Key Concepts Covered

### Pandas
- `Series` and `DataFrame`
- Data loading (`read_csv`, `read_excel`)
- Data inspection (`head`, `info`, `describe`)
- Filtering and sorting
- Groupby and aggregation
- Handling missing values
- Merging and joining DataFrames

### Visualization
- Line plots, bar charts, histograms
- Scatter plots
- Customizing figures (labels, titles, legends)
- Seaborn for statistical plots

### NumPy
- `ndarray` basics
- Vectorized operations
- Random number generation

---

## 🛠️ Environment

- **Python**: 3.11
- **Key Libraries**: Pandas, NumPy, Matplotlib, Seaborn
- **Tools**: VS Code + WSL 2 (Ubuntu 22.04), Jupyter Notebook

---

## 📌 Notes & Tips

- Prefer `.loc` for label‑based indexing over chained indexing.
- Use `.copy()` when modifying slices to avoid `SettingWithCopyWarning`.
- For large datasets, consider using `chunksize` in `read_csv`.
- Visualizations: always label axes and add titles for clarity.

## 🧠 Reflections

| Date | Topic | Key Takeaway |
|------|-------|--------------|
| 2026-07-16 | Pandas Groupby | `groupby` + `agg` is powerful for summary stats |
| 2026-07-17 | Data Cleaning | Always check for missing values before analysis |

---

## 🔗 Related

- Main Repository: [quant_projects](https://github.com/shaoyu-xu/quant_projects)
- Practice: [02_practice/python/](../../02_practice/python/)