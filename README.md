Easiway Realtime Bus Tracking System

This project tracks college buses in real-time using:
- Traccar Client (GPS sender on driver’s phone)
- Python Flask middleware to forward GPS data to Firebase
- Firebase Realtime Database
- Website hosted with Firebase Hosting / GitHub Pages
- Leaflet.js map showing the student’s bus live

Features

- Live bus tracking on the map
- Secure student login linked to bus ID
- Firebase-powered real-time updates
- Lightweight frontend for mobile users

Usage

1. Flask middleware runs on port 5500 and receives GPS data from Traccar Client.
2. Flask pushes GPS data to Firebase under buses/<id>/location.
3. Website listens to that Firebase node and updates marker using Leaflet.

Deployment

- Frontend can be deployed using Firebase Hosting or GitHub Pages.
- Firebase API key is protected using HTTP referrer restrictions.

Security

- .gitignore excludes serviceAccountKey.json
- Firebase Realtime Database Rules should restrict write access properly.

© 2025 Manoj
