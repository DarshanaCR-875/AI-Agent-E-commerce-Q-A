import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def plot_top_products(metric="CPC", top_n=5):
    conn = sqlite3.connect("ecommerce.db")
    df = pd.read_sql(f"SELECT * FROM ad_sales ORDER BY {metric} DESC LIMIT {top_n}", conn)
    conn.close()

    plt.figure(figsize=(10, 5))
    plt.bar(df["Product Name"], df[metric], color="skyblue")
    plt.title(f"Top {top_n} Products by {metric}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"top_{top_n}_{metric}.png")
