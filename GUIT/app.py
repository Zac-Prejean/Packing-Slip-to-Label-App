import tkinter as tk  
import requests  
import base64  
from config import create_tkinter_interface  
  
def read_barcode_from_scanner():  
    scanned_data = input("Please scan the barcode: ")  
    return scanned_data.strip()  

# Your API Key should be encrypted
API_KEY_BASE64 = 'your_api_key'
API_SECRET_BASE64 = 'your_api_secret'
  
API_KEY = base64.b64decode(API_KEY_BASE64).decode("utf-8")  
API_SECRET = base64.b64decode(API_SECRET_BASE64).decode("utf-8")  
BASE_URL = 'https://ssapi.shipstation.com'  
  
def get_encoded_credentials(api_key, api_secret):  
    combined_credentials = f"{api_key}:{api_secret}"  
    encoded_credentials = base64.b64encode(combined_credentials.encode("utf-8")).decode("utf-8")  
    return encoded_credentials  
  
def get_headers():  
    encoded_credentials = get_encoded_credentials(API_KEY, API_SECRET)  
    headers = {'Content-Type': 'application/json', 'Authorization': f'Basic {encoded_credentials}'}  
    return headers  
  
def print_packing_slip(order_id, shipment_id):  
    headers = get_headers()  
    url = f'{BASE_URL}/orders/{order_id}/documents/packingslip/generate'  
  
    response = requests.post(url, headers=headers)  
  
    if response.status_code == 200:  
        with open('packing_slip.pdf', 'wb') as file:  
            file.write(response.content)  
        print("Packing slip has been saved as 'packing_slip.pdf'")  
    else:  
        print("Error generating packing slip:", response.text)      

def get_shipment_id(order_id):  
    headers = get_headers()  
    url = f'{BASE_URL}/shipments?order_id={order_id}'  
  
    response = requests.get(url, headers=headers)  
  
    if response.status_code == 200:  
        shipments = response.json()['shipments']  
        if shipments:  
            return shipments[0]['shipmentId']  # Update this line  
        else:  
            print(f"No shipments found for Order ID: {order_id}")  
            return None  
    else:  
        print("Error fetching shipments:", response.text)  
        return None  

def process_scanned_barcode(event):  
    order_id = barcode_entry.get().strip()  
    shipment_id = get_shipment_id(order_id)  
  
    if shipment_id:  
        print_packing_slip(order_id, shipment_id)  
        result_text.set(f"Packing slip generated for Order ID: {order_id}, Shipment ID: {shipment_id}")  
        history_listbox.insert(tk.END, f"Order ID: {order_id}, Shipment ID: {shipment_id}")  # Add the order_id and shipment_id to the history listbox  
    else:  
        result_text.set(f"Error: Could not fetch shipment details for Order ID: {order_id}")  
  
    barcode_entry.delete(0, 'end')  

if __name__ == '__main__':  
    root, barcode_entry, result_text, history_listbox = create_tkinter_interface()  
  
    barcode_entry.bind('<Return>', process_scanned_barcode)  
  
    root.mainloop()  
