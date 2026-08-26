# statusbar.py
import customtkinter as ctk

class StatusBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.status_label = ctk.CTkLabel(self, text="🟢 Ready", anchor="w")
        self.status_label.pack(fill="x", padx=10)

    # =============================================================
    # Display Currrent Action
    # =============================================================

    def set_status(self, message):
        self.status_label.configure(text= message)
