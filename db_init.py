import pandas as pd
import sqlite3

def load_data_to_sqlite(db_path="ecommerce.db"):
    conn = sqlite3.connect(db_path)

    # Load files
    ad_sales = pd.read_excel("C:/Users/darsh/Desktop/Ammu/Ammu VIT assignments/Anarix/data/ad_sales.xlsx")
    total_sales = pd.read_excel("C:/Users/darsh/Desktop/Ammu/Ammu VIT assignments/Anarix/data/total_sales.xlsx")
    eligibility = pd.read_excel("C:/Users/darsh/Desktop/Ammu/Ammu VIT assignments/Anarix/data/eligibility.xlsx")

    # Write to SQLite
    ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
    total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)
    eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)

    conn.close()
    print("All data loaded to SQLite successfully.")

if __name__ == "__main__":
    load_data_to_sqlite()
