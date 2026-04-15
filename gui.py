import tkinter as tk
from tkinter import messagebox
from turtle1 import triangle 
from rps import rockpaperscissors
from geo import calculator
from wordcount1 import main 
#import everything, 

class PortfolioApp:
    def __init__(self, root):
        self.root = root

        self.root.title("PORTFoLIO")
        self.root.geometry("600x700")

        start
        intro_frame = tk.Frame(self.root, pady=10)
        intro_frame.pack(fill="x")

        tk.Label(intro_frame, text="My Programming Portfolio", font=("Arial", 16, "bold")).pack()
        
        intro_text = (
            "T portfolio contains four projects, 2 older, 2 newr to show progression\n"
            "to use click on the projects. "
            "Tclick run on specific ones to watch it apper in terminal "
        )
        tk.Label(intro_frame, text=intro_text, wraplength=500, justify="center").pack(pady=10)

        # sisplays 
        self.details_frame = tk.LabelFrame(self.root, text="Project Details", padx=10, pady=10)
        self.details_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.desc_label = tk.Label(self.details_frame, text="Select a project to see details", wraplength=450, justify="left")
        self.desc_label.pack(anchor="w")

        self.run_button = tk.Button(self.details_frame, text="Run Project", state="disabled")

        self.run_button.pack(pady=10)

        #select the things!
        # weak projects
        tk.Label(self.root, text="Older Projects", font=("Arial", 12, "bold")).pack(pady=(10, 0))
        old_frame = tk.Frame(self.root)
        old_frame.pack()

        self.add_project_button(old_frame, "Project 1", self.show_p1, "Older")
        self.add_project_button(old_frame, "Project 2", self.show_p2, "Older")

        #way better ones
        tk.Label(self.root, text="Advanced Projects", font=("Arial", 12, "bold")).pack(pady=(20, 0))
        new_frame = tk.Frame(self.root)
        new_frame.pack()

        self.add_project_button(new_frame, "Project 3", self.show_p3, "Advaanced")
        
        self.add_project_button(new_frame, "Project 4", self.show_p4, "Advanced")

    def add_project_button(self, frame, name, command, section):
        btn = tk.Button(frame, text=name, width=15, command=command)
        btn.pack(side="left", padx=5, pady=5)

    def update_display(self, title, desc, learned, challenge, run_command):
        # gets rid if pervios part
        for widget in self.details_frame.winfo_children():
            widget.destroy()

        # Update text
        tk.Label(self.details_frame, text=title, font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(self.details_frame, text=f"\nWhat it does:\n{desc}", wraplength=500, justify="left").pack(anchor="w")
        
        tk.Label(self.details_frame, text="\nWhat I learned:").pack(anchor="w")
        for item in learned:
            tk.Label(self.details_frame, text=f"• {item}").pack(anchor="w", padx=20)
        
        tk.Label(self.details_frame, text=f"\nchallenge :\n• {challenge}", wraplength=500, justify="left").pack(anchor="w")

        # setup run part


        tk.Button(self.details_frame, text=f"Run {title}", bg="lightgray", command=run_command).pack(pady=15)

    # all the datat and project importation
    
    def show_p1(self):
        self.update_display(
            "fractal generator",
            "gens a complex tringle chape recersevly",
            ["recursive stuffs", "turtle code"],
            "TRIANGLEsplitting files",
            lambda: triangle.triangle1()
        )

    def show_p2(self):
        self.update_display(
            "rock paperscissors",
            "a simple rock paper scissors game uses in a score project",

            ["back to basics", "for, if, while etc"],
            "RPS",
            lambda: rockpaperscissors.rps()
        )

    def show_p3(self):
       
        self.update_display(
            "geo calculator",
            "calc and maker for geo shapes",
            ["importing from otehr files", "complex libraries and classes"],
            "GEO CALC",
            lambda: calculator.play()
        )

    def show_p4(self):
        self.update_display(
            "word counter",
            "Counts words ina  text imputted",
            ["files", " "],
            "code.",

            lambda: main.wordcount()
        )

# all this below starts app and makes sure runs properly
if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioApp(root)
    root.mainloop()
