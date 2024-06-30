import tkinter as tk
from tkinter import messagebox
import time

class VirtualPlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Plant")
        
        self.root.configure(bg='yellow')
        
        self.last_watered = time.time()
        self.wilting_threshold = 5 
        
        self.plant_label = tk.Label(root, text="Your plant looks happy!", font=("Helvetica", 16), bg='yellow')
        self.plant_label.pack(pady=20)
        
        self.water_button = tk.Button(root, text="Water Plant", command=self.water_plant, font=("Helvetica", 14))
        self.water_button.pack(pady=20)
        
        self.check_wilt()
        
    def water_plant(self):
        self.last_watered = time.time()
        self.plant_label.config(text="Your plant looks happy!", bg='yellow')
        
    def check_wilt(self):
        current_time = time.time()
        if current_time - self.last_watered > self.wilting_threshold:
            self.plant_label.config(text="Your plant is wilting!", bg='brown')
            messagebox.showwarning("Warning", "Your plant needs attention!")
        self.root.after(1000, self.check_wilt)

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualPlantApp(root)
    root.mainloop()
