
PrintLayoutLab

This script is a Python program that reads order numbers from a USB scanner, requests shipping labels from ShipStation, and prints them using a label printer.


1. Imports required libraries: usb.core for USB scanner, requests for ShipStation API calls.

2. Configures the USB scanner by specifying its vendor ID and product ID.

3. Sets up the ShipStation API credentials (api_key and api_secret) and API endpoint.

4. Configures the printer by specifying its IP address.

5. Defines a function request_shipping_label to request a shipping label from ShipStation by sending an API call with the order number.

8. The main loop listens for scanner input. If a scanner is found, it reads the order number, requests a shipping label from ShipStation, and prints it on the Zebra printer. If the scanner is not found, it prints an error message

