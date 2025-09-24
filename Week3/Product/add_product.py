import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url,key)

def add_product(name, sku, price, stock):
    payload = {"name":name, "sku":sku, "price":price, "stock":stock }
    resp = sb.table("product").insert(payload).execute()
    return resp.data

if __name__ == "__main__":
    name = input("Enter product name: ").strip()
    sku = input("Enter SKU: ").strip()
    price = float(input("Enter price: ").strip())
    stock = int(input("Enter stock: ").strip())

    created = add_product(name, sku, price, stock)
    print("Inserted:",created)