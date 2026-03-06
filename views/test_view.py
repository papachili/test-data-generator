import tkinter as tk
from tkinter import ttk
from views.base_generator import BaseView


class TestView(BaseView):
    """Test view"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.title_label['text'] = "Test View"
        self.create_additional_widgets()

    def create_additional_widgets(self):
        pass

    def reset_generator(self):
        super().reset_generator()  # Call the original implementation
        # Add your specific modifications here
        # self._additional_reset_steps()

    def on_show(self):
        """Called when this frame is shown"""
        pass
