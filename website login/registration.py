import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

DB_HOST = "localhost"
DB_NAME = "citl1"
DB_USER = "root"
DB_PASSWORD = ""

conn = mysql.connector.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        employee_id VARCHAR(50) UNIQUE NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
""")
conn.commit()

def register():
    global name_entry, password_entry, employee_id_entry, phone_number_entry, email_entry

    name = name_entry.get()
    password = password_entry.get()
    employee_id = employee_id_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()

    try:
        cur.execute("""
            INSERT INTO employees (name, password, employee_id, phone_number, email)
            VALUES (%s, %s, %s, %s, %s);
        """, (name, password, employee_id, phone_number, email))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
        registration_window.destroy()  
        open_login_window()  
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Registration failed: {e}")

def login():
    global employee_id_entry, password_entry

    employee_id = employee_id_entry.get()
    password = password_entry.get()

    cur.execute("""
        SELECT * FROM employees WHERE employee_id = %s;
    """, (employee_id,))
    employee = cur.fetchone()

    if employee and employee[2] == password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

def open_registration_window():
    global registration_window, name_entry, password_entry, employee_id_entry, phone_number_entry, email_entry

    registration_window = tk.Tk()
    registration_window.title("Registration")

    style = ttk.Style()
    style.configure("TFrame")

    register_frame = ttk.Frame(registration_window)
    register_frame.pack(pady=10)

    name_label = ttk.Label(register_frame, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(register_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = ttk.Label(register_frame, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry = ttk.Entry(register_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    employee_id_label = ttk.Label(register_frame, text="Employee ID:")
    employee_id_label.grid(row=2, column=0, padx=5, pady=5)
    employee_id_entry = ttk.Entry(register_frame)
    employee_id_entry.grid(row=2, column=1, padx=5, pady=5)

    phone_number_label = ttk.Label(register_frame, text="Phone Number:")
    phone_number_label.grid(row=3, column=0, padx=5, pady=5)
    phone_number_entry = ttk.Entry(register_frame)
    phone_number_entry.grid(row=3, column=1, padx=5, pady=5)

    email_label = ttk.Label(register_frame, text="Email:")
    email_label.grid(row=4, column=0, padx=5, pady=5)
    email_entry = ttk.Entry(register_frame)
    email_entry.grid(row=4, column=1, padx=5, pady=5)

    register_button = ttk.Button(register_frame, text="Register", command=register)
    register_button.grid(row=5, columnspan=2, padx=5, pady=5)

def open_login_window():
    global login_window, employee_id_entry, password_entry

    login_window = tk.Tk()
    login_window.title("Login")

    style = ttk.Style()
    style.configure("TFrame")

    login_frame = ttk.Frame(login_window)
    login_frame.pack(pady=10)

    employee_id_label = ttk.Label(login_frame, text="Employee ID:")
    employee_id_label.grid(row=0, column=0, padx=5, pady=5)
    employee_id_entry = ttk.Entry(login_frame)
    employee_id_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = ttk.Label(login_frame, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    login_button = ttk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=5)

window = tk.Tk()
window.title("Employee Portal")

register_button = ttk.Button(window, text="Register", command=open_registration_window)
register_button.pack(pady=10)

login_button = ttk.Button(window, text="Login", command=open_login_window)
login_button.pack(pady=10)
window.mainloop()