import customtkinter as ctk

# ---------------- Window ----------------
app = ctk.CTk()
app.title("Button Example")
app.geometry("400x200")

# ---------------- Function ----------------
def change_text():
    if button.cget("text") == "Start":
        button.configure(text="Stop")
    else:
        button.configure(text="Start")

# ---------------- Button ----------------
button = ctk.CTkButton(
    app,
    text="Start",
    command=change_text,
    width=150,
    height=40
)

button.pack(pady=50)

# ---------------- Run ----------------
app.mainloop()