# 📊 BC Housing Data Visualization App

## Description

This project is a Python GUI application that I built using `tkinter` to analyze housing affordability data from the BC Census 2016 dataset.

The goal of this program is to let users explore rent burden in different areas and regions in British Columbia in a simple and interactive way. The program shows results in text format and also visualizes the data using a bar chart.

This project demonstrates basic concepts in Python, including:

* Reading and processing data from a CSV file  
* Using functions to organize and structure the program  
* Building a graphical user interface (GUI) with Tkinter  
* Using event-driven programming (buttons and dropdown)  
* Creating a custom chart using Canvas  

---

## Code Overview

The project is organized into several functions:

* `load_data()` – reads the CSV file and stores the data into a list of dictionaries  
* `task1()` – finds areas where rent burden is greater than 50% and displays them  
* `task2()` – calculates the average rent burden based on the selected region  
* `draw_chart()` – draws a bar chart using Canvas to visualize the data  
* `show_summary()` – displays general conclusions about the data  

I used `try/except` in multiple places to handle missing or incorrect data so the program doesn’t crash.

For Task 2, I connected the dropdown menu to an event (`<<ComboboxSelected>>`) so that the result updates immediately when the user selects a region. I added this because I wanted the program to feel more interactive without needing an extra button click.

---

## 🖥️ Application Preview

### 🏠 Main Interface  
![Main UI](screenshots/main-ui.png.PNG)

---

### 📍 Task 1 – High Rent Burden  
![Task 1](screenshots/task1-high-rent.png.PNG)

---

### 🌍 Task 2 – Regional Analysis  
![Task 2](screenshots/task2-region-analysis.png.PNG)

---

### 📈 Chart Visualization  
![Chart](screenshots/chart-visualization.png.PNG)

---

## How to Run

1. Clone or download this repository  
2. Make sure the dataset file is in the same folder: