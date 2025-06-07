# Bus Tracking System

## Project Overview
This project is a real-time bus tracking system designed to allow students to view the live location of their assigned college bus via a web interface. The system integrates the Traccar client app installed on the driver's mobile device, a Python Flask middleware server, Firebase Realtime Database, and a frontend website using Leaflet.js for map visualization.

## Features
- Real-time tracking of buses on a map
- Secure student login linked to assigned buses
- Estimated Time of Arrival (ETA) and proximity alerts when bus approaches college
- Firebase Realtime Database as backend for location data storage
- Python Flask middleware to receive GPS data and update Firebase
- Responsive frontend interface with live location updates

## Technologies Used
- Traccar GPS Client (Mobile)
- Python 3 with Flask
- Firebase Realtime Database
- JavaScript, HTML, CSS
- Leaflet.js (Mapping library)

## Setup Instructions

### 1. Firebase Setup
- Create a Firebase project and enable Realtime Database.
- Download the `serviceAccountKey.json` file.
- Configure your database rules for secure read/write access.
  
### 2. Middleware Server
- Install required Python packages:
- Place the `serviceAccountKey.json` in your project directory.
- Run the Flask app (`app.py`) on port 5500:

### 3. Traccar Client Configuration
- Install the Traccar client app on the bus driver’s mobile device.
- Configure it to send location updates to your middleware server’s IP and port (e.g., `http://<server-ip>:5500`).
- Set location update frequency (e.g., every 10 seconds).

### 4. Frontend Website
- Update Firebase config with your project details.
- Serve the website files via any web server or Firebase Hosting.
- Ensure the frontend reads live bus locations from Firebase and updates the map accordingly.

## Usage
- Students log in using their credentials.
- Select their bus number to view live location on the map.
- Receive ETA and alert notifications when the bus approaches the college.

## License
This project is protected by a custom license. Unauthorized use, copying, or distribution is prohibited.

## Author
Manoj

## Contact
For questions or support, please contact: manojchinthala217@gmail.com

