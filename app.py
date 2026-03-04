import tkinter as tk


class App(tk.Tk):
    """Main application class handling window and frame management"""

    def __init__(self):
        super().__init__()
        self.title("Test Data Generator")
        self.geometry("800x600")
        self.configure_app()

        # Dictionary to hold frame classes
        self.frame_classes = {}
        self.frames = {}

        # Initialize frames
        self.init_frames()

        # Show main menu initially
        self.show_frame('MainMenu')

    def configure_app(self):
        """Configure application settings"""
        # Make window resizable
        self.minsize(400, 300)

        # Configure grid for main container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create main container
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def init_frames(self):
        """Initialize all application frames"""
        # Import here to avoid circular imports
        from views.main_menu import MainMenu
        from views.phone_generator import PhoneGenerator
        from views.name_generator import NameGenerator

        # Store frame classes
        self.frame_classes = {
            'MainMenu': MainMenu,
            'PhoneGenerator': PhoneGenerator,
            'NameGenerator': NameGenerator
        }

        # Create frames
        for name, frame_class in self.frame_classes.items():
            frame = frame_class(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_name):
        """Show frame by name"""
        if frame_name in self.frames:
            frame = self.frames[frame_name]
            if frame.winfo_exists():  # Check if the frame exists
                frame.tkraise()
