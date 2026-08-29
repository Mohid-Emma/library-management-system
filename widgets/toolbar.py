# toolbar.py
import customtkinter as ctk
from   config        import theme

class ToolBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color= theme.surface_light)

        self.create_widgets()

    # =============================================================
    # Assignation Function to Variable
    # =============================================================

    def set_callbacks(self, on_search, on_sort):
        self.on_search = on_search
        self.on_sort   = on_sort

    # =============================================================
    # Widget Creation
    # =============================================================

    def create_widgets(self):

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search books...", font=("Helvetica", 15), corner_radius=10)
        self.search_entry.pack(padx=10, pady=20, expand="True", fill="both", side="left")

        self.search_entry.bind("<KeyRelease>", self.on_search_changed)

        sorted_option = ["Title (A-Z)","Title (Z-A)","Author","Year (Newest)","Year (Oldest)","Pages (Smallest)","Pages (Largest)","Available","Borrowed"]
        self.sort_menu = ctk.CTkOptionMenu(self, values=sorted_option, command=self.on_sort_changed)
        self.sort_menu.pack(padx=5, pady=5, side="left")

    # =============================================================
    # Search for Book
    # =============================================================

    def on_search_changed(self, _):
        query = self.search_entry.get().strip().lower()
        self.on_search(query)

    # =============================================================
    # Book Sort
    # =============================================================

    def on_sort_changed(self, choice):
        self.on_sort(choice)