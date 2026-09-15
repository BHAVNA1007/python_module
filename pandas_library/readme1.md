## Next: Reading CSV Files with Pandas

This is **very important in real-world data analysis**, because datasets are often stored as CSV files.

### 1. What is a CSV?

**CSV = Comma-Separated Values**

Example `student.csv`:

```text
Name,Age,Marks
Rahul,21,85
Priya,22,92
Aman,20,76
Bhavna,23,88
```

---

## 2. Read CSV using Pandas

```python
import pandas as pd

df = pd.read_csv("student.csv")

print(df)
```

Output:

```text
    Name  Age  Marks
0  Rahul   21     85
1  Priya   22     92
2   Aman   20     76
3  Bhavna  23     88
```

### Important

Earlier you wrote:

```python
df = pd.read_csv(student.csv)
```

❌ This is wrong because Python thinks `student` is a variable.

Correct:

```python
df = pd.read_csv("student.csv")
```

The filename must be inside **quotes**.

---

## 3. If the file is in another folder

You can provide the complete path:

```python
df = pd.read_csv(
    r"D:\InfoBeans\Python\python_Ajay_sir\python_modules\student.csv"
)
```

The `r` before the string makes it a **raw string**, which is useful for Windows paths.

You can also use:

```python
df = pd.read_csv(
    "D:/InfoBeans/Python/python_Ajay_sir/python_modules/student.csv"
)
```

---

## 4. Check the first few rows

```python
print(df.head())
```

By default, `head()` shows the first **5 rows**.

You can specify the number:

```python
print(df.head(3))
```

→ first 3 rows.

---

## 5. Check the last few rows

```python
print(df.tail())
```

Or:

```python
print(df.tail(2))
```

→ last 2 rows.

---

## 6. Get basic information

```python
print(df.info())
```

This tells you things such as:

* number of rows
* columns
* data types
* non-null values
* memory usage

---

## 7. Get statistical information

```python
print(df.describe())
```

For numerical columns, you'll get things like:

```text
count
mean
std
min
25%
50%
75%
max
```

---

### ⭐ Important commands to remember

| Command         | Purpose               |
| --------------- | --------------------- |
| `pd.read_csv()` | Read CSV              |
| `df.head()`     | First 5 rows          |
| `df.tail()`     | Last 5 rows           |
| `df.info()`     | DataFrame information |
| `df.describe()` | Statistical summary   |

### Interview question

**Q: How do you read a CSV file in Pandas?**

**Answer:**

```python
df = pd.read_csv("student.csv")
```

`read_csv()` reads the CSV file and returns a **DataFrame**.



## Next: Understanding DataFrame Properties

Now we'll learn how to quickly **inspect the structure of your DataFrame**.

Use:

```python
import pandas as pd

df = pd.read_csv("student.csv")
```

---

### 1. `shape`

`shape` tells you:

> **(number of rows, number of columns)**

```python
print(df.shape)
```

Example output:

```text
(4, 3)
```

Meaning:

* `4` → 4 rows
* `3` → 3 columns

⚠️ `shape` is a **property**, so don't write:

```python
df.shape()
```

---

### 2. `columns`

Shows all column names.

```python
print(df.columns)
```

Example:

```text
Index(['Name', 'Age', 'Marks'], dtype='object')
```

If you want them as a normal list:

```python
print(df.columns.tolist())
```

Output:

```text
['Name', 'Age', 'Marks']
```

---

### 3. `index`

Shows the row labels.

```python
print(df.index)
```

Example:

```text
RangeIndex(start=0, stop=4, step=1)
```

This means the index is:

```text
0, 1, 2, 3
```

---

### 4. `dtypes`

Shows the data type of every column.

```python
print(df.dtypes)
```

Example:

```text
Name     object
Age       int64
Marks     int64
dtype: object
```

So:

| Column | Type     |
| ------ | -------- |
| Name   | `object` |
| Age    | `int64`  |
| Marks  | `int64`  |

---

### 5. `size`

`size` gives the **total number of values/cells**.

```python
print(df.size)
```

If there are 4 rows and 3 columns:

```text
12
```

Because:

```text
4 × 3 = 12
```

---

## ⭐ Important difference

| Property     | Gives you        |
| ------------ | ---------------- |
| `df.shape`   | Rows and columns |
| `df.columns` | Column names     |
| `df.index`   | Row labels       |
| `df.dtypes`  | Data types       |
| `df.size`    | Total cells      |

### Quick interview question

**Q: What is the difference between `shape` and `size`?**

**Answer:**

`shape` returns the number of **rows and columns**, while `size` returns the **total number of elements**.

Example:

```python
df.shape
# (4, 3)

df.size
# 12
```

because `4 × 3 = 12`.

**Next → handling missing values (`NaN`, `isnull()`, `dropna()`, `fillna()`).**
