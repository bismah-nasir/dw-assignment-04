# 🧁 Bakery Orders ECT & Data Analysis Project

This project is part of the **Data Warehousing and Data Mining (BSCS-635)** course assignment. It involves reading, cleaning, transforming, and analyzing a real-world bakery orders dataset using Python and pandas.

---

## 📌 Project Objectives

- Perform ECT (Extract, Clean, Transform) operations on a bakery orders dataset.
- Handle missing values and inconsistent data.
- Fill missing prices based on the mean price of the respective item category.
- Calculate and display basic statistical insights using NumPy.
- Prepare the dataset for further analysis or visualization.

---

## 📂 Dataset

- **Filename**: `BakeryOrders.csv`
- **Records**: 1000 rows of bakery order data
- **Columns** include:
  - `Order_ID`
  - `Date`
  - `Item`
  - `Quantity`
  - `Price`
  - `Total_Price`
  - `Email`
  - `Delivery_Status`

---

## 🔧 Tools & Technologies Used

- `Python 3.12.3`
- `Pandas`
- `NumPy`
- `SciPy` (for mode)
- VS Code

---

## 🧹 ETL Steps

**Extract**:  
- Loaded the dataset from a CSV file using pandas.

**Clean**:  
- Filled missing `Email` values with a default placeholder (`noemail@example.com`).  
- Filled missing `Delivery_Status` values with `"Pending"`.  
- Filled missing `Price` values based on the average price of the same `Item` category (not global average).  

**Transform**:  
- Calculated `Total_Price` by multiplying `Price × Quantity`.  
- Performed basic mathematical operations like mean, mode, min, max, etc., using NumPy.  

---

## 📊 Statistical Insights

Performed the following operations on `Total_Price` using **NumPy**:

| Metric                  | Value         |
|-------------------------|---------------|
| Highest Price           | ✔️ Calculated |
| Lowest Price            | ✔️ Calculated |
| Mean Price              | ✔️ Calculated |
| Median Price            | ✔️ Calculated |
| Mode Price              | ✔️ Calculated |
| Standard Deviation      | ✔️ Calculated |
| Total Revenue           | ✔️ Calculated |
| Count of Valid Entries  | ✔️ Calculated |

---

## 📁 Project Structure
```
dw-assignment-04/
│
├── code/
│   └── code.py               # Main Python script
│
├── data/
│   └── BakeryOrders.csv      # Dataset file
│
└── README.md                 # This documentation file
```

⚠️ **Important: Keep this structure unchanged when cloning or downloading the repository.**

---

## ✅ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/bismah-nasir/dw-assignment-04
   
2. Open the project in your preferred Python IDE.

3. Make sure required libraries are installed:
   pip install pandas numpy 

4. Run code.py to execute the data pipeline and see the results.
