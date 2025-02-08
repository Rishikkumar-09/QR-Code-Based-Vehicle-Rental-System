import qrcode
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to generate a QR code
def generate_qr():
    try:
        # Get inputs from GUI
        vehicle_id = vehicle_id_entry.get()
        rental_rate = rental_rate_entry.get()

        # Validate inputs
        if not vehicle_id or not rental_rate:
            raise ValueError("Please fill all fields correctly.")

        # Generate timestamp for the QR
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create the QR data
        qr_data = {
            "vehicle_id": vehicle_id,
            "rental_rate": rental_rate,  # rental rate per minute
            "timestamp": timestamp
        }

        # Convert to JSON string
        qr_json = json.dumps(qr_data)

        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_json)
        qr.make(fit=True)

        # Save the QR code image
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            qr_img = qr.make_image(fill='black', back_color='white')
            qr_img.save(save_path)
            messagebox.showinfo("Success", f"QR Code generated and saved at:\n{save_path}")

    except ValueError as e:
        messagebox.showerror("Input Error", f"Error: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")

# GUI for QR Code Generation
root = tk.Tk()
root.title("Vehicle QR Code Generator")
root.geometry("400x400")

# Input fields
tk.Label(root, text="Vehicle ID:", font=("Arial", 12)).pack(pady=5)
vehicle_id_entry = tk.Entry(root, font=("Arial", 12))
vehicle_id_entry.pack(pady=5)

tk.Label(root, text="Rental Rate (per minute):", font=("Arial", 12)).pack(pady=5)
rental_rate_entry = tk.Entry(root, font=("Arial", 12))
rental_rate_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", font=("Arial", 12), command=generate_qr)
generate_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
