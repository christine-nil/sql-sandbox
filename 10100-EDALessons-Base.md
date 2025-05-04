# Exploratory Data Analysis Lessons

This guide walks through common data exploration tasks using SQL queries on our sample datasets.

By default the sqlite3 interactive environment won't include column names in its output. To activate display of the column names use the command `.headers on` which will make your output more readable.

## How To Study With This Guide

For each task this guide both describes a simplistic and realistic data exploration task and also provides code in Python (Pandas) that will produce the desired result. Your task, as a learner who already knows Pandas, is to write SQL queries that will accomplish the exploration task.

## MPG Dataset Explorations

### 1. Overall Vehicle Statistics
Task: Write a query to get the average weight, horsepower, and efficiency across all vehicles.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('mpg')
>>> df[['weight','horsepower','mpg']].mean().apply(lambda x: round(x, 2))

weight        2970.42
horsepower     104.47
mpg             23.51
dtype: float64
```

Your SQL solution here:
```sql
-- Write your query here
```

### 2. Statistics by Origin
Task: Write a query to compare vehicle characteristics across different manufacturing origins.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('mpg')
>>> df.groupby('origin')[['weight', 'horsepower', 'mpg']].mean().round(2)

             weight  horsepower    mpg
origin                               
europe    2423.30      80.56   27.89
japan     2221.23      79.84   30.45
usa       3361.93     119.05   20.08
```

Your SQL solution here:
```sql
-- Write your query here
```

### 3. Yearly Trends
Task: Write a query to see how vehicle characteristics have changed over time.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('mpg')
>>> df.groupby('model_year')[['weight', 'horsepower', 'mpg']].mean().round(2)

            weight  horsepower    mpg
model_year                           
70         3372.79     147.83   17.69
71         2995.43     107.04   21.25
72         3237.71     120.18   18.71
73         3419.03     130.48   17.10
74         2877.93      94.23   22.70
75         3176.80     101.07   20.27
76         3078.74     101.12   21.57
77         2997.36     105.07   23.38
78         2861.81      99.69   24.06
79         3055.34     101.21   25.09
80         2436.66      77.48   33.70
81         2522.93      81.04   30.33
82         2453.55      81.47   31.71
```

Your SQL solution here:
```sql
-- Write your query here
```

### 4. Detailed Analysis by Year and Origin
Task: Write a query to combine year and origin to see more detailed trends.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('mpg')
>>> df.groupby(['model_year', 'origin'])[['weight', 'horsepower', 'mpg']].mean().round(2)

                        weight  horsepower    mpg
model_year origin                               
70         europe    2309.20      86.20   25.20
           japan     2251.00      91.50   25.50
           usa       3716.50     166.95   15.27
71         europe    2024.00      74.00   28.75
           japan     1936.00      79.25   29.50
           usa       3401.60     119.84   18.10
...
```

Your SQL solution here:
```sql
-- Write your query here
```

## Tips Dataset Analysis

### 5. Tips as Proportion of Bill
Task: Write a query to view tips both as absolute amounts and as percentages of the total bill.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('tips')
>>> df['proportion'] = df['tip'] / df['total_bill']
>>> df[['total_bill','tip','proportion']].sample(5)

     total_bill   tip  proportion
98        21.01  3.00    0.142789
22        15.77  2.23    0.141408
138       16.00  2.00    0.125000
169       10.63  2.00    0.188147
235       10.07  1.25    0.124131
```

Your SQL solution here:
```sql
-- Write your query here
```

## Penguins Dataset Analysis

### 6. Species and Sex Distribution
Task: Write a query to create a cross-tabulation of penguin species and sex.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('penguins')
>>> pd.crosstab(df['species'], df['sex'])

sex        Female  Male
species                
Adelie         73    73
Chinstrap      34    34
Gentoo         58    61
```

Your SQL solution here:
```sql
-- Write your query here
```

### 7. Island and Sex Distribution
Task: Write a query to create a cross-tabulation of island location and sex.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('penguins')
>>> pd.crosstab(df['island'], df['sex'])

sex        Female  Male
island                 
Biscoe         80    83
Dream          61    62
Torgersen      24    23
```

Your SQL solution here:
```sql
-- Write your query here
```

### 8. Island Location, Sex, and Species
Task: Write a query to create a cross-tabulation of species, island location, and sex.

Here's how we'd do it in Python:
```python
>>> df = sns.load_dataset('penguins')
>>> pd.crosstab([df['species'], df['island']], df['sex'])

sex                  Female  Male
species   island                 
Adelie    Biscoe         22    22
          Dream          27    28
          Torgersen      24    23
Chinstrap Dream          34    34
Gentoo    Biscoe         58    61
```

Your SQL solution here:
```sql
-- Write your query here
```

## Additional Guidance for These SQL Queries

1. Enter SQLite command line:
```bash
sqlite3 sandbox.db
```

2. For better output formatting, run these commands first:
```sql
.mode column
.headers on
```

3. To exit SQLite:
```sql
.quit
```

## Understanding the Results

- The ROUND() function is used to limit decimal places for readability
- COUNT(*) shows the number of records in each group
- Percentages are calculated by (tip/total_bill * 100)
- The CASE statements in the penguin queries create pivot-table-like results
