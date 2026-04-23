#📊 BC Housing Data Visualization App

##📌 Description

This project is a Python Tkinter GUI application that analyzes housing affordability data from the BC Census 2016 dataset.

It allows users to explore rent burden across different areas and regions in British Columbia through interactive analysis and visualization tools.

The project demonstrates:

* GUI development with Tkinter
* CSV file processing (manual parsing, no pandas)
* Data filtering and analysis
* Event-driven programming
* Custom data visualization using Canvas


##🖥️ Application Preview

##🏠 Main Interface


##📍 Task 1 – High Rent Burden Areas (>50%)

##🌍 Task 2 – Regional Analysis (Dropdown + Auto Update)



##📈 Chart Visualization (Color-coded + Scrollable)



##🚀 Features

#✅ Task 1 – High Rent Burden Detection

* Identifies areas where rent burden exceeds 50%
* Displays CHSA names and percentages
* Counts total high-risk areas

⸻

#🌍 Task 2 – Regional Analysis

* Dropdown selection for:
    * Fraser
    * Interior
    * Northern
    * Vancouver Coastal
    * Vancouver Island
* Calculates average rent burden
* Automatically updates when selection changes

⸻

📈 Interactive Chart

* Bar chart built using Tkinter Canvas
* Features:
    * 🔴 Red bars → High rent burden (>50%)
    * 🟢 Green bars → Normal levels
    * Scroll support for large datasets
    * Dynamic scaling

⸻

📝 Summary Insights

* Highlights key findings about:
    * Housing affordability
    * Regional differences
    * Need for subsidies

⸻

🧠 How It Works

📂 Data Loading

* Reads CSV manually using file handling
* Converts rows into dictionaries
* Handles missing/invalid data safely

⸻

⚙️ Data Processing

* Extracts:
    * shelt_rent_30plus_rate (rent burden)
    * pha (region)
    * chsa (area name)
* Filters based on conditions (e.g., >50%)

⸻

🎨 Visualization Logic

* Uses Tkinter Canvas to draw bars
* Scales values relative to maximum
* Adds:
    * Labels (CHSA names)
    * Percentages
    * Color indicators

⸻

▶️ How to Run

1. Make sure Python is installed
2. Place dataset file in the same folder:

BC Census 2016 data.csv

3. Run the program:

python your_file_name.py

4. Use the interface:

* Task 1 → High rent areas
* Task 2 → Regional averages
* Chart → Visual data
* Summary → Insights

⸻

📂 Project Structure

project-folder/
│
├── BC Census 2016 data.csv
├── your_file_name.py
├── README.md
└── screenshots/

⸻

🛠️ Technologies Used

* Python 🐍
* Tkinter (GUI framework)
* CSV file handling
* Canvas (custom chart rendering)

⸻

💡 Key Insights

* Several areas exceed 50% rent burden, indicating affordability issues
* Rent burden varies significantly across regions
* Some regions may require better housing support and subsidies

⸻

🧑‍💻 Author

Barsin Saki

⸻

📜 License

This project is for educational purposes.

⸻

🔥 If You Want Next Level (Optional Upgrade)

I can upgrade this even further with:

* 🎥 ￼ GIF demo (looks insane on GitHub)
* 🎨 ￼ Custom badges (Python, Tkinter, Status)
* 🌐 ￼ Hosted demo style preview
* 🧠 ￼ “Why I built this” section (for resume)

Just say:
👉 “upgrade to final boss README” 😈