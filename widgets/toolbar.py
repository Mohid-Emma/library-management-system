# toolbar.py
import customtkinter as     ctk
from   config        import theme

class ToolBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color= theme.transparent)

        self.on_search = None
        self.on_sort   = None

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

        self.grid_columnconfigure(0, weight=1)

        # Search
        self.search_entry = ctk.CTkEntry(
            master                 = self, 
            height                 = 40,
            corner_radius          = 9,
            border_width           = 1,
            placeholder_text       = "Search books...",
            border_color           = theme.border,
            text_color             = theme.text,
            placeholder_text_color = theme.text_muted,
            fg_color               = theme.background,
            font                   = ("Segoe UI", 13))
        self.search_entry.grid(row=0, column=0, padx=(0,10), sticky="ew")

        self.search_entry.bind("<KeyRelease>", self.on_search_changed)

        # Sort
        sorted_option = [
            "Title (A-Z)",
            "Title (Z-A)",
            "Author",
            "Year (Newest)",
            "Year (Oldest)",
            "Pages (Smallest)",
            "Pages (Largest)",
            "Available",
            "Borrowed"]
        
        self.sort_menu = ctk.CTkOptionMenu(
            master               = self, 
            values               = sorted_option, 
            command              = self.on_sort_changed,
            height               = 40,
            width                = 170,
            corner_radius        = 9,
            font                 = ("Segoe UI", 12),
            fg_color             = theme.surface_light,
            button_color         = theme.accent,
            button_hover_color   = theme.accent_hover,
            text_color           = theme.text, 
            dropdown_fg_color    = theme.surface_light,
            dropdown_hover_color = theme.surface_light,
            dropdown_text_color  = theme.text)
        
        self.sort_menu.set("Sort by")
        self.sort_menu.grid(row=0, column=1, padx=(0,0))

# =============================================================
# Search for Book
# =============================================================

    def on_search_changed(self, _):
        if self.on_search is None:
            return
        query = self.search_entry.get().strip().lower()
        self.on_search(query)

# =============================================================
# Book Sort
# =============================================================

    def on_sort_changed(self, choice):
        if self.on_sort is None:
            return
        self.on_sort(choice)

# =============================================================
# Search Clear
# =============================================================

    def clear_search(self):
        self.search_entry.delete(0, "End")
        if self.on_search:
            self.on_search("")