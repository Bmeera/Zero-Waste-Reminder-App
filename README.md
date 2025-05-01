🥦 Zero-Waste Pantry Reminder App

A simple and practical command-line application to help users track food expiration dates and reduce household food waste. Users can add pantry items, view them, delete used items, and check which items are expiring soon — all through the terminal.

## 💡 Problem It Solves

Millions of pounds of food are wasted each year due to poor tracking and forgotten expiration dates. This app promotes sustainable habits by reminding users to use or donate food before it goes bad.

## 🚀 Features

• 📥 Add pantry items with an expiration date
• 📋 View all items
• ⏳ Automatically shows which items are expiring soon
• 🗑️ Delete items when used
• 💾 Stores all items in a local data.json file for persistence

## 🛠️ Technologies

• Language: Python 3
• Libraries: Standard Python libraries only (no external dependencies)

## 📂 File Structure

zero-waste-reminder/
├── app.py # Main application logic
├── utils.py # Helper functions (load/save data, date calculations)
├── data.json # Local data storage
├── requirements.txt # (Empty – uses no external libraries)
└── README.md # Project documentation

## 🔧 How to Run

1. Clone the repo:
   git clone https://github.com/Bmeera/Zero-Waste-Reminder-App.git
   cd Zero-Waste-Reminder-App
2. Run the app:
   python app.py
3. Follow the on-screen prompts to add or check items.

## ⏰ Bonus Tip – Daily Notifications

To stay on top of your pantry, you can schedule this app to run daily using:

- Windows Task Scheduler
- macOS/Linux cron job

This way, you get automatic reminders of food expiring soon without having to open the app manually.

## 🙋🏽‍♀️ What I Learned

- How to build a small CLI utility with file-based persistence
- Working with dates and user input
- Structuring clean, readable Python code across multiple files
- Simulating real-time alerts for a better user experience
- Using simple tools to make a real-world impact

## 🌍 Inspiration

Built with sustainability in mind — a small step toward reducing food waste and building better habits.

## 📜 License: MIT

This project is licensed under the MIT License. That means:

- You can freely use, copy, modify, merge, publish, and distribute the software.
- It comes with no warranty — it is provided 'as is'.
- Just include the original license notice in any copies or substantial portions of the software.
