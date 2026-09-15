> ✅ **“What is Pandas? What are the advantages and disadvantages of Pandas in Python?”**

## What is Pandas?

**Pandas** is an open-source Python library used for **data manipulation and data analysis**.

In simple words:

> **Pandas helps us store, clean, analyze, and manipulate data easily in Python.**

For example, suppose you have student data:

| Name  | Age | Marks |
| ----- | --: | ----: |
| Rahul |  21 |    85 |
| Priya |  22 |    92 |
| Aman  |  20 |    76 |

Without Pandas, working with a large amount of such data can become difficult.

With Pandas, you can easily:

* Read data from CSV/Excel/database
* Filter rows
* Select columns
* Add or remove columns
* Handle missing values
* Sort data
* Calculate statistics
* Group data
* Clean messy data

### Basic example

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman"],
    "Marks": [85, 92, 76]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Marks
0  Rahul     85
1  Priya     92
2   Aman     76
```

Here:

* `pd` → commonly used short name for Pandas
* `DataFrame` → 2-dimensional table-like data structure
* `df` → variable containing our DataFrame

---

# Advantages of Pandas

| Advantage                  | Explanation                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------- |
| **Easy data manipulation** | You can filter, sort, update, delete and modify data easily.                           |
| **Easy data cleaning**     | Handles missing, duplicate and incorrect data.                                         |
| **Works with CSV/Excel**   | Easily reads and writes CSV, Excel and other formats.                                  |
| **Powerful analysis**      | Provides functions for mean, sum, count, minimum, maximum, etc.                        |
| **DataFrame**              | Provides a convenient table-like structure.                                            |
| **Fast**                   | Uses optimized underlying code and works efficiently with many common data operations. |
| **Integration**            | Works well with NumPy, Matplotlib, Scikit-learn and other Python libraries.            |
| **Grouping**               | `groupby()` makes it easy to analyze data category-wise.                               |
| **Large ecosystem**        | There are many tutorials, examples and community resources available.                  |

### Example of easy analysis

```python
print(df["Marks"].mean())
```

Output:

```text
84.33333333333333
```

You don't need to manually calculate the average.

---

# Disadvantages of Pandas

| Disadvantage                           | Explanation                                                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Memory consumption**                 | Large datasets can consume significant RAM.                                                                                 |
| **Not ideal for extremely large data** | Very large datasets may require distributed tools such as Spark or database systems.                                        |
| **Learning curve**                     | Basic Pandas is easy, but advanced operations can become confusing.                                                         |
| **Performance limitations**            | Some operations can be slower than specialized tools or lower-level approaches.                                             |
| **Dependency on RAM**                  | A Pandas DataFrame generally needs the data available in memory for processing.                                             |
| **Not a database**                     | Pandas is for data analysis/manipulation; it does not replace a proper database for persistent, multi-user data management. |

---

## Pandas vs Python

An important interview point:

**Pandas is NOT a programming language.**

It is a **Python library**.

Think of it like this:

```text
Python
  |
  ├── Pandas       → Data analysis
  ├── NumPy        → Numerical computing
  ├── Matplotlib   → Data visualization
  ├── Requests     → HTTP/API requests
  └── Flask/Django → Web development
```

### Interview answer

> **Pandas is an open-source Python library used for data manipulation and data analysis. It provides powerful data structures such as Series and DataFrame, which make it easy to work with structured data. It is commonly used for data cleaning, filtering, transformation, aggregation, and analysis.**








## Next: DataFrame

A **DataFrame** is a **2-dimensional tabular data structure** in Pandas.

Think of it like an **Excel table** or a **SQL table**.

```text
        Name    Age   Marks
0       Rahul   21     85
1       Priya   22     92
2       Aman    20     76
```

It has:

* **Rows** → individual records
* **Columns** → attributes/fields
* **Index** → identifies rows

### Create a DataFrame

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman"],
    "Age": [21, 22, 20],
    "Marks": [85, 92, 76]
}

df = pd.DataFrame(data)

print(df)
```

### Your first hands-on task 🧑‍💻

Create this DataFrame yourself:

```text
Name       City       Salary
Bhavna     Bhopal     30000
Rahul      Indore     35000
Priya      Betul      28000
Aman       Bhopal     32000
```

**Don't use `read_csv()` yet.** Create it using a Python dictionary and `pd.DataFrame()`.

Then print:

```python
print(df)
```



Sure. Let's move to the **next DataFrame concept: accessing columns**.

## 1. Access a single column

Suppose:

```python
import pandas as pd

data = {
    "Name": ["Bhavna", "Rahul", "Priya", "Aman"],
    "City": ["Bhopal", "Indore", "Betul", "Bhopal"],
    "Salary": [30000, 35000, 28000, 32000]
}

df = pd.DataFrame(data)
```

### Using `[]`

```python
print(df["Name"])
```

Output:

```text
0    Bhavna
1    Rahul
2    Priya
3    Aman
Name: Name, dtype: object
```

This returns a **Series**.

### Access multiple columns

```python
print(df[["Name", "Salary"]])
```

Output:

```text
     Name  Salary
0  Bhavna   30000
1   Rahul   35000
2   Priya   28000
3    Aman   32000
```

Notice the **double brackets**:

```python
df["Name"]             # one column → Series

df[["Name", "Salary"]] # multiple columns → DataFrame
```

### Important interview point

**Series = 1-dimensional**

```text
Name
Bhavna
Rahul
Priya
```

**DataFrame = 2-dimensional**

```text
Name     City      Salary
Bhavna   Bhopal    30000
Rahul    Indore    35000
```



## Next: Accessing Rows with `loc` and `iloc`

This is an important Pandas concept. There are **two main ways** to select rows:

* `loc` → select using **labels/index**
* `iloc` → select using **integer position**

We'll use this DataFrame:

```python
import pandas as pd

data = {
    "Name": ["Bhavna", "Rahul", "Priya", "Aman"],
    "City": ["Bhopal", "Indore", "Betul", "Bhopal"],
    "Salary": [30000, 35000, 28000, 32000]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
     Name    City  Salary
0  Bhavna  Bhopal   30000
1   Rahul  Indore   35000
2   Priya   Betul   28000
3    Aman  Bhopal   32000
```

### 1. `iloc` — position-based selection

`iloc` means **integer-location**.

```python
print(df.iloc[0])
```

It selects the **first row**, because position starts from `0`.

```text
Name       Bhavna
City       Bhopal
Salary     30000
```

Second row:

```python
print(df.iloc[1])
```

Third row:

```python
print(df.iloc[2])
```

### Select multiple rows

```python
print(df.iloc[0:2])
```

This selects rows at positions **0 and 1**.

```text
     Name    City  Salary
0  Bhavna  Bhopal   30000
1   Rahul  Indore   35000
```

---

## 2. `loc` — label-based selection

Our index labels are:

```text
0
1
2
3
```

So:

```python
print(df.loc[0])
```

selects the row whose **label is 0**.

Multiple rows:

```python
print(df.loc[0:2])
```

⚠️ Important difference:

```python
df.iloc[0:2]  # 0, 1
df.loc[0:2]   # 0, 1, 2
```

With `loc`, the ending label **is included**.

---

### Easy way to remember

| Method | Based on | Example      |
| ------ | -------- | ------------ |
| `loc`  | Label    | `df.loc[2]`  |
| `iloc` | Position | `df.iloc[2]` |

### Interview question

**Q: What is the difference between `loc` and `iloc`?**

**Answer:**
`loc` is used for **label-based indexing**, whereas `iloc` is used for **integer position-based indexing**.

---

### Next concept

After `loc` and `iloc`, we'll learn **how to select a specific row AND column together**, such as:

```python
df.loc[1, "Name"]
```

which gives:

```text
Rahul
```





## Next: Selecting Specific Rows and Columns

Now we'll combine what we learned about `loc` and `iloc`.

Using:

```python
import pandas as pd

data = {
    "Name": ["Bhavna", "Rahul", "Priya", "Aman"],
    "City": ["Bhopal", "Indore", "Betul", "Bhopal"],
    "Salary": [30000, 35000, 28000, 32000]
}

df = pd.DataFrame(data)
```

### 1. `loc` — row label + column name

```python
print(df.loc[1, "Name"])
```

Output:

```text
Rahul
```

Here:

```text
1       → row label
"Name"  → column name
```

### Select multiple rows and columns

```python
print(df.loc[0:2, ["Name", "Salary"]])
```

Output:

```text
     Name  Salary
0  Bhavna   30000
1   Rahul   35000
2   Priya   28000
```

---

## 2. `iloc` — row position + column position

Remember:

```text
Column position:
Name = 0
City = 1
Salary = 2
```

So:

```python
print(df.iloc[1, 0])
```

Output:

```text
Rahul
```

Because:

```text
1 → second row
0 → first column
```

### Multiple rows and columns

```python
print(df.iloc[0:3, [0, 2]])
```

Output:

```text
     Name  Salary
0  Bhavna   30000
1   Rahul   35000
2   Priya   28000
```

---

### ⭐ Very important pattern

```python
df.loc[row_label, column_name]
```

Example:

```python
df.loc[2, "Salary"]
```

→ `28000`

And:

```python
df.iloc[row_position, column_position]
```

Example:

```python
df.iloc[2, 2]
```

→ `28000`

---



## Next: Adding, Updating & Deleting Columns

This is another very common DataFrame operation.

We'll use:

```python
import pandas as pd

data = {
    "Name": ["Bhavna", "Rahul", "Priya", "Aman"],
    "City": ["Bhopal", "Indore", "Betul", "Bhopal"],
    "Salary": [30000, 35000, 28000, 32000]
}

df = pd.DataFrame(data)
```

---

### 1. Add a new column

Suppose we want to add an `Age` column:

```python
df["Age"] = [23, 25, 22, 24]

print(df)
```

Output:

```text
     Name    City  Salary  Age
0  Bhavna  Bhopal   30000   23
1   Rahul  Indore   35000   25
2   Priya   Betul   28000   22
3    Aman  Bhopal   32000   24
```

### Add a calculated column

We can also create a column using existing columns.

For example, salary after adding ₹5,000:

```python
df["New_Salary"] = df["Salary"] + 5000
```

Output:

```text
   Salary  New_Salary
0   30000       35000
1   35000       40000
2   28000       33000
3   32000       37000
```

This is one of the powerful features of Pandas: **vectorized operations**.

---

## 2. Update an existing column

Suppose we want to increase every salary by ₹2,000:

```python
df["Salary"] = df["Salary"] + 2000
```

Now:

```text
Bhavna → 32000
Rahul  → 37000
Priya  → 30000
Aman   → 34000
```

---

## 3. Update a specific value

Suppose Rahul's salary should be `40000`.

Using `loc`:

```python
df.loc[1, "Salary"] = 40000
```

Here:

```text
1       → Rahul's row
"Salary" → Salary column
```

---

## 4. Delete a column

Suppose we don't need `Age`.

```python
df.drop("Age", axis=1, inplace=True)
```

### Understand `axis`

| axis     | Meaning |
| -------- | ------- |
| `axis=0` | Rows    |
| `axis=1` | Columns |

So:

```python
df.drop("Age", axis=1)
```

means **drop the Age column**.

---

### Another way

You can also write:

```python
df = df.drop("Age", axis=1)
```

Here `inplace=True` is not required because we're assigning the modified DataFrame back to `df`.

---

## ⭐ Important interview point

`drop()` does not normally modify the original DataFrame unless you use:

```python
inplace=True
```

Example:

```python
df.drop("Age", axis=1, inplace=True)
```

---





