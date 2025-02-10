import cv2
import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
from PIL import Image, ImageTk


# Function to show a popup with a message
def show_popup(message):
    """Display a popup window with the given message."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("QR Code Validation Result", message)


# Function to load and update QR data from a JSON file
def load_qr_data(file_path):
    """Load QR code data from a file or return default if not found."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return None


def save_qr_data(file_path, data):
    """Save updated QR code data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Function to calculate the total rental amount
def calculate_total_amount(rental_rate, start_time):
    """Calculate the total rental amount based on the rental rate and time."""
    current_time = datetime.now()
    rental_duration = current_time - start_time
    rental_minutes = rental_duration.total_seconds() / 60  # Convert to minutes
    total_amount = rental_minutes * float(rental_rate)  # Rental rate is per minute
    return total_amount, rental_minutes


# Function to update the label with the webcam frame
def update_frame():
    """Update the webcam feed frame in the Tkinter GUI."""
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image from webcam.")
        return

    # QR Code detection
    data, bbox, _ = detector.detectAndDecode(frame)
    if data:
        try:
            # Parse the QR code data (assuming it's a JSON string)
            qr_data = json.loads(data)

            # Extract vehicle details from QR
            vehicle_id = qr_data.get("vehicle_id", "Unknown")
            rental_rate = qr_data.get("rental_rate", "0")
            timestamp_str = qr_data.get("timestamp", None)

            if timestamp_str:
                start_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

                # Calculate the total amount
                total_amount, rental_minutes = calculate_total_amount(rental_rate, start_time)

                # Show total amount in the GUI
                total_amount_label.config(text=f"Total Amount: ₹{total_amount:.2f}")
                rental_duration_label.config(text=f"Duration: {rental_minutes:.2f} minutes")

                # Display QR code validation result
                show_popup(
                    f"QR Code Scanned!\nVehicle ID: {vehicle_id}\nTotal Duration: {rental_minutes:.2f} minutes\nTotal Amount: ₹{total_amount:.2f}")

        except json.JSONDecodeError:
            print("Error: Unable to decode QR code data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Convert the frame to a format Tkinter can use
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_image = Image.fromarray(frame_rgb)
    frame_tk = ImageTk.PhotoImage(frame_image)

    # Update the Tkinter label with the webcam frame
    label.config(image=frame_tk)
    label.image = frame_tk

    # Call update_frame again to continue the webcam feed
    root.after(10, update_frame)


# Function to start webcam and Tkinter GUI
def start_webcam_gui():
    """Initialize the webcam feed in a Tkinter window."""
    global root, label, cap, detector, total_amount_label, rental_duration_label

    # Set up the webcam
    cap = cv2.VideoCapture(0)  # 0 is the default camera ID
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Set up the QR code detector
    detector = cv2.QRCodeDetector()

    # Create a Tkinter window
    root = tk.Tk()
    root.title("QR Code Scanner")

    # Create a Label widget to display the webcam feed
    label = tk.Label(root)
    label.pack()

    # Create labels to display the total amount and rental duration
    total_amount_label = tk.Label(root, text="Total Amount: ₹0.00", font=("Arial", 14))
    total_amount_label.pack(pady=10)

    rental_duration_label = tk.Label(root, text="Duration: 0 minutes", font=("Arial", 14))
    rental_duration_label.pack(pady=10)

    # Start updating the webcam feed in the Tkinter window
    update_frame()

    # Start the Tkinter event loop
    root.mainloop()


# Call the function to start the webcam feed with QR code scanning and validation
start_webcam_gui()
