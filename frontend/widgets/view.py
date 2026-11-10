# view.py

import customtkinter as ctk
from config import theme
from typing import Any


class View(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame, b_card: Card, toolbar_op: dict[str, Any], card_op: dict[str, Any]):
        super().__init__(
            master        = master, 
            corner_radius = 15, 
            border_width  = 1, 
            border_color  = theme.border, 
            fg_color      = theme.panel)

        self.tool_bar = ToolBar(self, toolbar_op)
        self.book_list = List(self, b_card, card_op)

        self.create_layout()
        self.create_title()
        self.create_content()

# =============================================================
# Create View GUI/UI Compounds
# =============================================================

    def create_layout(self) -> None:
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_title(self) -> None:

        title_frame = ctk.CTkFrame(
            master   = self, 
            fg_color = theme.transparent)

        title_frame.grid(row=0, column=0, padx=15, pady=(15,5), sticky="ew")

        ctk.CTkLabel(
            master     = title_frame,
            text       = "Books",
            font       = ("Segoe UI", 20, "bold"),
            text_color = theme.text 
        ).pack(anchor="w")

        ctk.CTkLabel(
            master     = title_frame,
            text       = "Browse and manage your collection",
            font       = ("Segoe UI", 11),
            text_color = theme.text_muted
        ).pack(anchor="w")

    def create_content(self) -> None:

        # ToolBar
        self.tool_bar.grid(row=1, column=0, padx=15, pady=10, sticky="ew")

        # BookList
        self.book_list.grid(row=2, column=0, padx=15, pady=(0,15), sticky="news")

    def display_books(self, books: list[dict[str, any]]) -> None:
        self.book_list.display_books(books)


class ToolBar(ctk.CTkFrame):
    def __init__(self, master, operation) -> None:
        super().__init__(master, fg_color= theme.transparent)

        self.operation = operation
        self.create_widgets()

# =============================================================
# Create ToolBar GUI/UI Compounds
# =============================================================

    def create_widgets(self) -> None:

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
            fg_color             = theme.panel_light,
            button_color         = theme.action,
            button_hover_color   = theme.action_hover,
            text_color           = theme.text, 
            dropdown_fg_color    = theme.panel_light,
            dropdown_hover_color = theme.panel_light,
            dropdown_text_color  = theme.text)
        
        self.sort_menu.set("Sort by")
        self.sort_menu.grid(row=0, column=1, padx=(0,0))

# =============================================================
# Book Sort
# =============================================================

    def on_sort_changed(self, choice : str) -> None:
        self.operation["sort"](choice)

# =============================================================
# Book Search
# =============================================================

    def on_search_changed(self, _) -> None:
        query = self.search_entry.get().strip().lower()
        self.operation["search"](query)

    def clear_search(self) -> None:
        self.search_entry.delete(0, "End")
        self.operation["search"]("")


class List(ctk.CTkScrollableFrame):
    def __init__(self, master, b_card, card_op) -> None:
            super().__init__(master, corner_radius= 10,fg_color= theme.background, scrollbar_button_color= theme.panel_light, scrollbar_button_hover_color= theme.border)

            self.b_card = b_card
            self.card_op = card_op
            
            self.create_layout()

# =============================================================
# Create List GUI/UI Compounds
# =============================================================

    def create_layout(self) -> None: 
        self.grid_columnconfigure(0, weight=1)

# =============================================================
# Book Display
# =============================================================

    def display_books(self, books: list[dict[str, Any]]) -> None:

        self.clear()

        if not books:
            self.show_empty_message()
            return
        for book in books:
            self.b_card(
                master    = self,
                book      = book,
                operation = self.card_op
        ).grid(row=self.winfo_children().__len__(), column=0, padx=10, pady=8, sticky="ew")

# =============================================================
# Destroy of Book Display
# =============================================================

    def clear(self) -> None:
        for widget in self.winfo_children():
            widget.destroy()

# =============================================================
# Display When Library is Empty
# =============================================================

    def show_empty_message(self) -> None:
        empty_frame = ctk.CTkFrame(
            master   = self, 
            fg_color = theme.transparent)
        empty_frame.grid(row=0, column=0, padx=20, pady=60, sticky="news")

        ctk.CTkLabel( 
            master = empty_frame, 
            text   = "📚", 
            font   = ("Segoe UI Emoji", 40)
            ).pack( pady=(0, 10))

        ctk.CTkLabel(
            master     = empty_frame, 
            text       = "No books available.",
            font       = ("Segoe UI", 20, "bold"),
            text_color = theme.text
            ).pack(pady=5)

        ctk.CTkLabel(
            master     = empty_frame, 
            text       = "Try adding a book or changing your search.",
            font       = ("Segoe UI", 11),
            text_color = theme.text_muted
            ).pack(pady=5) 