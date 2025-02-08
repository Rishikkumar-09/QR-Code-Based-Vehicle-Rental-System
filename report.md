# Project Report: QR Rental System

## Introduction
The QR Rental System is a Python-based project designed to generate and verify QR codes for vehicle rentals. It utilizes Tkinter for the graphical user interface (GUI), OpenCV for scanning QR codes, and JSON for data handling. The system ensures efficient rental tracking by embedding rental rate, vehicle ID, and timestamp into the QR code.

## Objectives
- Generate QR codes containing rental details.
- Scan QR codes to extract rental details.
- Calculate rental duration and cost dynamically.
- Provide a user-friendly interface for both generating and scanning QR codes.

## Technologies Used
- Python
- Tkinter
- OpenCV
- JSON
- PIL (Pillow for image handling)
- datetime module

## Implementation
### QR Code Generator
1. The user inputs vehicle ID and rental rate.
2. The system generates a timestamp and encodes data in JSON format.
3. A QR code is created and saved as an image file.

### QR Code Scanner
1. The system continuously scans for QR codes using the webcam.
2. When a QR code is detected, it extracts rental details.
3. The rental duration is calculated from the timestamp.
4. The total rental cost is displayed to the user.

## Applications
- Vehicle rental management
- Equipment rentals
- Parking ticketing systems
- Digital asset tracking

## Future Enhancements
- Implement a database for storing rental records.
- Add mobile app integration for better accessibility.
- Enhance security with encrypted QR codes.

## Conclusion
The QR Rental System provides a robust solution for managing rental services using QR codes. By automating rental tracking and calculations, the system ensures accuracy and ease of use for both users and service providers.
