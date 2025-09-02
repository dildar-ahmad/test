# import requests
# from requests.auth import HTTPBasicAuth

# order_id = 139420
# url = f"https://www.unboxbasics.com/wp-json/wc/v3/orders/{order_id}"
# r = requests.get(url, auth=HTTPBasicAuth("ck_your", "cs_your"))
# data = r.json()

# customer = data['billing']['first_name'] + " " + data['billing']['last_name']
# status = data['status']
# total = data['total']
# order_date = data['date_created']

# # Estimated delivery date (from shipping_lines > meta_data)
# estimate = None
# for meta in data['shipping_lines'][0]['meta_data']:
#     if meta['key'] == 'shipping_estimate_msg':
#         estimate = meta['value']

# print(f"Order: {order_id}\nStatus: {status}\nCustomer: {customer}\nTotal: {total} AED\nOrder Date: {order_date}\nEstimate Date: {estimate}")
# import requests
# from requests.auth import HTTPBasicAuth

# order_id = 139420
# url = f"https://www.unboxbasics.com/wp-json/wc/v3/orders/{order_id}"
# res = requests.get(url, auth=HTTPBasicAuth(
#     "ck_ac76a5abc93b62cb0f8b8d6ac097a6f751f454cb",
#     "cs_720ce2ba17361c5be897c68e13c24d1ae443e8b2"
# ))
# data = res.json()

# # Always print to debug
# print(data)

# # Check for expected keys
# if 'billing' not in data:
#     print("Error from API:", data)
# else:
#     customer = data['billing']['first_name'] + " " + data['billing']['last_name']
#     print("Customer:", customer)
#     # (continue as before)

import requests
from requests.auth import HTTPBasicAuth

order_id = 139000
url = f"https://www.unboxbasics.com/wp-json/wc/v3/orders/{order_id}"
res = requests.get(url, auth=HTTPBasicAuth(
    "ck_ac76a5abc93b62cb0f8b8d6ac097a6f751f454cb",
    "cs_720ce2ba17361c5be897c68e13c24d1ae443e8b2"
))
data = res.json()
# print(data) 
# input("press h ") # Always print to debug

# Main order fields
customer = data['billing']['first_name'] + " " + data['billing']['last_name']
status = data['status']
total = data['total']
order_date = data['date_created']
simple_date = order_date.replace("T", " at ")
currency = data['currency']
email = data['billing']['email']

# Product info (first item)
product = data['line_items'][0]['name'] if data['line_items'] else "N/A"

# ---- ESTIMATE DATE: from shipping_lines[0].meta_data where key == 'shipping_estimate_msg'
estimate_msg = None
# shipping_lines = data.get('shipping_lines', [])
# if shipping_lines and 'meta_data' in shipping_lines[0]:
#     for meta in shipping_lines[0]['meta_data']:
#         if meta['key'] == 'shipping_estimate_msg':
#             estimate_msg = meta['value']

# # If not found, try meta_data (order-level)
# if not estimate_msg:
for meta in data['meta_data']:
        if meta['key'] == 'estimate_details':
            estimate = meta['value']
            # Get min/max date (may be same)
            estimate_msg = f"{estimate.get('min_date')} to {estimate.get('max_date')}"

# Print summary
print(f"Order ID: {order_id}")
print(f"Customer: {customer}")
print(f"Email: {email}")
print(f"Status: {status}")
print(f"Order Date and time : {simple_date }")
print(f"Product: {product}")
print(f"Total: {total} {currency}")
print(f"Estimate Date: {estimate_msg}")
