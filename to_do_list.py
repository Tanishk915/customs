import customtkinter as ctk

app = ctk.CTk()
app.title("todo list")
app.geometry("500x200")

ctk.set_widget_scaling(1.2)
ctk.set_window_scaling(1.1)

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("light")

def button_on_click():
    if button.cget("text")== "click me":
        button.configure(
            text = "clicked",
            fg_colour = "green"
        )
    else:
        button.configure(
            text = "click me",
            fg_colour = "red"
        )

button =ctk.CTkButton(app,text="click me", fg_color= "red", command= button_on_click)
button.pack(pady=20)



app.mainloop()