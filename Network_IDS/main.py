import customtkinter as ctk
from gui import IDSDashboard

# -------------------------
# Application Theme
# -------------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# -------------------------
# Main Window
# -------------------------

app = IDSDashboard()

app.mainloop()