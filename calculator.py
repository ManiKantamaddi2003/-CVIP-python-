import tkinter as tk
import time
import requests

def fetch_weather():
    city = 'vijayawada'  # Replace with your city
    url = f'http://wttr.in/{city}?format=%C+%t+%w'

    response = requests.get(url)
    data = response.text

    return data

def get_greeting():
    current_time = int(time.strftime("%H"))
    if 6 <= current_time < 12:
        return "Good morning!"
    elif 12 <= current_time < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def update_time_label():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=f'Time: {current_time}')
    weather_info = fetch_weather()
    weather_label.config(text=f'Weather: {weather_info}')
    greeting_label.config(text=get_greeting())

def button_click(number):
    if number == "=":
        calculate()
    elif number == "√":
        square_root()
    elif number == "C":
        clear()
    else:
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    num = entry.get()
    try:
        num = float(num)
        result = round((num ** 0.5), 2)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Doshna's Calculator")
window.geometry("400x500")

# Create a top frame for the calculator
top_frame = tk.Frame(window, bg="blue", height=100)
top_frame.pack(side="top", fill="x")

# Create a frame for the calculator
frame = tk.Frame(window)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "√", "C"
]

row_val, col_val = 1, 0

for text in buttons:
    if text == "C":
        tk.Button(frame, text=text, font=("Arial", 16), width=5, height=2, command=lambda t=text: button_click(t), bg="red").grid(row=row_val, column=col_val)
    else:
        tk.Button(frame, text=text, font=("Arial", 16), width=5, height=2, command=lambda t=text: button_click(t)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

greeting_label = tk.Label(top_frame, text=get_greeting(), font=("Arial", 18), fg="white", bg="blue")
greeting_label.pack()

time_label = tk.Label(top_frame, text="", font=("Arial", 14), fg="white", bg="blue")
time_label.pack(side="left")

weather_label = tk.Label(top_frame, text="", font=("Arial", 14), fg="white", bg="blue")
weather_label.pack(side="right")

update_time_label()
window.after(1000, update_time_label)  # Update time, weather info, and greeting message every second

copyright_label = tk.Label(window, text="Copyright © Doshna@2003", font=("Arial", 10))
copyright_label.pack(side="bottom")

window.mainloop()
