import tkinter as tk
from tkinter import ttk

# =========================
# Load data from the csv file


def load_data():
    data = []
    with open("BC Census 2016 data.csv", "r", encoding="utf-8") as file: #read the file
        lines = file.readlines()

        headers = lines[0].strip().split(",")

        for line in lines[1:]:
            parts = line.strip().split(",")

            row = {}
            for i in range(len(headers)):
                if i < len(parts):
                    row[headers[i].strip()] = parts[i].strip()
                else:
                    row[headers[i].strip()] = ""

            data.append(row)

    return data


data = load_data() # Call the load_data function and store the returned dataset 

# =========================
# TASK 1: High rent areas

def task1():
    display.delete("1.0", tk.END)
    display.insert(tk.END, "High Rent Burden Areas (>50%)\n\n")

    count = 0

    for row in data:
        try:
            # Convert the rent rate to a float (from string)
            rate = float(row["shelt_rent_30plus_rate"])
            if rate > 50:
                # Display the area name and its rate
                display.insert(tk.END, f"{row['chsa']} → {rate}%\n")
                count += 1
        except:
             # If there is missing or invalid data, skip that row
            pass
    # Show the total number of areas that met the condition
    display.insert(tk.END, f"\nTotal Areas: {count}")


# =========================
# TASK 2: Region analysis

def task2():
    selected = region_var.get().strip()
    region_data = []

    for row in data:
        try:
            region_name = row["pha"].strip()
            if selected == "All" or region_name == selected:
                region_data.append(float(row["shelt_rent_30plus_rate"]))
        except:
            pass

    display.delete("1.0", tk.END)

    if region_data:
        avg = sum(region_data) / len(region_data)

        display.insert(tk.END, f"Region: {selected}\n")
        display.insert(tk.END, f"Average Rent Burden: {round(avg, 2)}%\n")
    else:
        display.insert(tk.END, f"No data found for region: {selected}\n")   

# =========================
# Draw chart

def draw_chart():
    canvas.delete("all")

    values = []
    labels = []

    for row in data:
        try:
            # DEBUG print
            print(row["chsa"], "→", row["shelt_rent_30plus_rate"])

            val = float(row["shelt_rent_30plus_rate"])

            # skip bad values
            if val <= 0:
                continue

            values.append(val)
            labels.append(row["chsa"][:12])

        except:
            continue

    if not values:
        return

    max_val = max(values)

    for i, val in enumerate(values):
        x1 = 150
        y1 = 30 + i * 30
        bar_length = (val / max_val) * 350

        # highlight high values
        color = "red" if val > 50 else "green"

        canvas.create_rectangle(x1, y1, x1 + bar_length, y1 + 20, fill=color)
        canvas.create_text(10, y1 + 10, text=labels[i], anchor="w")
        canvas.create_text(x1 + bar_length + 30, y1 + 10, text=f"{round(val,1)}%")

    canvas.configure(scrollregion=canvas.bbox("all"))


# =========================
# Summary

def show_summary():
    display.delete("1.0", tk.END)

    display.insert(tk.END, "Project Summary\n\n")
    display.insert(tk.END, "- Some areas have very high rent burden (>50%)\n")
    display.insert(tk.END, "- These areas may need more support\n")
    display.insert(tk.END, "- Rent burden varies across regions\n")
    display.insert(tk.END, "- Subsidies may not be equally distributed\n")


# =========================
# GUI window

window = tk.Tk()
window.title("BC Housing Data App")
window.geometry("700x600")
window.configure(bg="#f0f0f0")

title = tk.Label(window, text="BC Housing Data Visualization",
                 font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

frame = tk.Frame(window, bg="#f0f0f0")
frame.pack()

tk.Button(frame, text="Task 1", width=18, command=task1).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Task 2", width=18, command=task2).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Chart", width=18, command=draw_chart).grid(row=0, column=2, padx=5)
tk.Button(frame, text="Summary", width=18, command=show_summary).grid(row=0, column=3, padx=5)

# Dropdown
region_var = tk.StringVar()
region_dropdown = ttk.Combobox(window, textvariable=region_var, state="readonly")
region_dropdown["values"] = ["All", "Fraser", "Interior", "Northern", "Vancouver Coastal", "Vancouver Island"]
region_dropdown.current(0)
region_dropdown.pack(pady=10)
region_dropdown.bind("<<ComboboxSelected>>", lambda e: task2())
# I added this code because I want to change the data in task 2 right at the moment I chose the data

# Text display
display = tk.Text(window, height=10, width=70)
display.pack(pady=10)

# =========================
# Canvas 

canvas_frame = tk.Frame(window)
canvas_frame.pack(pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(canvas_frame)
scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(canvas_frame, width=600, height=250, bg="white",
                   yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

scrollbar.config(command=canvas.yview)

#mouse scroll
canvas.bind_all("<MouseWheel>",
    lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

window.mainloop()