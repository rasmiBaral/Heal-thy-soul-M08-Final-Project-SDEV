"""
M08 Final Project
Rashmi Baral

This is a Python program that helps users calculate their recommended daily intake (RDI) and also shows them healthy recipes. The program uses the tkinter and PIL libraries for the GUI
"""
import tkinter as tk
from PIL import ImageTk, Image
# creating message box widget, which act as a window displaying information
from tkinter import messagebox 
# shows the message box
messagebox.showinfo("Welcome!", "You are about to calculate your Reccomended Daily Intake(RDI).")
# Class RDICalculator consisting labels,entry box and radio buttons
class RDICalculator:
    # Defines a class named RDICalculator which takes in a master parameter in its constructor.
    def __init__(self, master):
        self.master = master
        master.title("RDI Calculator")
        # loads the image and resize it to 200x200 pixels
        self.image = Image.open("image1.gif").resize((200, 200), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        # creats label with the image
        tk.Label(master,text="Image Description-Count on the app to provide a accurate result", image=self.photo).grid(row=15, column=0, columnspan=2, padx=10, pady=10, sticky="E")
        # Creates label called weight and also a entry box for user input
        tk.Label(master, text="Weight (kg):",bg="lightblue", fg="blue").grid(row=0, column=0)
        self.weight_entry = tk.Entry(master)
        self.weight_entry.grid(row=0, column=1)
      
        #Create label called height and also a entry box for user input
        tk.Label(master, text="Height (cm):",bg="lightblue", fg="blue").grid(row=1, column=0)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=1, column=1)
      
        # Create label called age and also a entry box for user input
        tk.Label(master, text="Age:",bg="lightblue", fg="blue").grid(row=2, column=0)
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=2, column=1)

        # Create label called gender and two radio buttons for the user to select their gender. 
        tk.Label(master, text="Gender:",  bg="lightblue", fg="blue").grid(row=3, column=0)
        self.gender_var = tk.StringVar(value="male")
        tk.Radiobutton(master, text="Male", variable=self.gender_var, value="male",bg="lightblue", fg="blue").grid(row=3, column=1)
        tk.Radiobutton(master, text="Female", variable=self.gender_var, value="female",bg="lightblue", fg="blue").grid(row=3, column=2)
      
        # Create label called Activity level and three radio buttons for the user to select their activity level. 
        tk.Label(master, text="Activity level:",bg="lightblue", fg="blue").grid(row=4, column=0)
        self.activity_var = tk.StringVar(value="sedentary")
        tk.Radiobutton(master, text="Sedentary", variable=self.activity_var, value="sedentary",bg="lightblue", fg="blue").grid(row=4, column=1)
        tk.Radiobutton(master, text="Moderate", variable=self.activity_var, value="moderate",bg="lightblue", fg="blue").grid(row=4, column=2)
        tk.Radiobutton(master, text="Active", variable=self.activity_var, value="active",bg="lightblue", fg="blue").grid(row=4, column=3)

        # Create button to calculate RDI
        tk.Button(master, text="Calculate RDI", 
        command=self.calculate_rdi,bg="green", fg="white").grid(row=5, column=1)

        # Create label to display result
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=6, column=1) 
      
# Defines a method called calculate_rdi that takes in self as a parameter
    def calculate_rdi(self):
        # Get user input from entry boxes
        weight_input = self.weight_entry.get()
        height_input = self.height_entry.get()
        age_input = self.age_entry.get()
        # Validate input for weight
        try:
          weight = float(weight_input)
          if weight <= 0:
             raise ValueError("Weight must be a positive number.")
        except ValueError:
          messagebox.showerror("Invalid input", "Please enter a valid weight.")
          return
        # Validate input for height
        try:
          height = float(height_input)
          if height <= 0:
             raise ValueError("Height must be a positive number.")
        except ValueError:
          messagebox.showerror("Invalid input", "Please enter a valid height.")
          return
        # Validate input for age
        try:
          age = int(age_input)
          if age <= 0:
             raise ValueError("Age must be a positive number.")
        except ValueError:
          messagebox.showerror("Invalid input", "Please enter a valid age.")
          return
        # Get selected gender and activity levels from clicked radio button
        gender = self.gender_var.get()
        activity_level = self.activity_var.get()

        # Calculates RDI
        if gender == "male":
            rdi = 88.4 + (13.4 * weight) + (4.8 * height) - (5.68 * age)
        else:
            rdi = 447.6 + (9.25 * weight) + (3.10 * height) - (4.33 * age)
        if activity_level == "sedentary":
            rdi *= 1.2
        elif activity_level == "moderate":
            rdi *= 1.55
        elif activity_level == "active":
            rdi *= 1.9

        # Update result label
        self.result_label.config(text=f"Your recommended daily intake is {rdi:.0f} calories.")
      
# class Recipe for showing few healthy recipes:
class Recipe:
    def __init__(self, master):
        self.master = master
        # loads the image and resize it to 40x40 pixels
        self.photo = ImageTk.PhotoImage(Image.open("image2.gif").resize((40, 40)))
        # creates label with the image
        self.label = tk.Label(self.master,text="Logo of the app",image=self.photo)
        self.label.grid(row=0, column=5,sticky="e", padx=10, pady=10)
        self.button = tk.Button(self.master, text="Click me for Healthy Recipes", command=self.show_recipe, bg="green", fg="white")
        self.button.grid(row=7, column=1)

    def show_recipe(self):
      # Prints the recipe
        print("1. Chia Pudding for Breakfast-INGREDIENTS & NUTRITION VALUE: Info- 1.5 tbsp chia seeds- 70cal,1/2 cup low fat milk or plant based milk- 51.2cal,Stevia to taste(can also use honey or sweetener of choice),1/4cup sweet or plain low fat curd curd (optional) - 33.7cal,1/4 cup Apple- 22cal,Pomegranate optional-Total calories 194")
        print( "2. Steamed Salad for Dinner-INGREDIENTS & NUTRITION VALUE-100g chana sprouts- 165cal,3 tbsp green peas- 25cal,3 tbsp sweet corn 23cal,50g carrot- 24cal,50g beetroot- 21.5cal,1/2 cup cucumber- 7.8cal,1 tomato- 18.2cal,1/4 cup lettuce optional- 1.9cal,100g fresh paneer- 265cal (can also add tofu),1 tsp olive oil- 40.5cal,fresh coriander leaves,Mint leaves,roasted cumin powder,lemon juice,salt to taste, Total calories - 592cal")
        print( "3. Toast for snack-INGREDIENTS & NUTRITION VALUE (makes 2pc),30g boiled chickpeas- 49.2cal,40g whole wheat bread- 108cal,1 tbsp tomato- 2.2cal,1 tbsp onion- 4cal,1 tbsp cucumber- 1.2cal,1 tsp pizza/pasta sauce- 2.8cal,(Can use any sauce of choice),Total calories - 167g")


# class ExitButton for closing the window:
class ExitButton:
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(self.master, text="Exit", bg="maroon", fg="white", command=self.exit)
        self.button.grid(row=8, column=1)
    def exit(self):
        self.master.destroy()
      
# Create and run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="light blue")
    RDICalculator =  RDICalculator(root)
    Recipes = Recipe(root)
    Close = ExitButton(root)
    root.mainloop()
