import tkinter as tk

__version__ = "0.3.0-beta"


class App(tk.Tk):
    """Main application class handling window and frame management"""

    def __init__(self):
        super().__init__()
        self.title("Test Data Generator")

        # Withdraw the window until fully positioned
        self.withdraw()

        # Configure core app settings, including geometry and frames
        self.configure_app()

        # Now show the window
        self.deiconify()

        # Show main menu initially
        self.show_frame('MainMenu')

    def configure_app(self):
        """Configure application settings, geometry, and initialize frames"""
        self.setup_window()
        self.setup_container()
        self.init_frames()

    def setup_window(self):
        """Set window size and position it at the center of the screen"""
        # Set initial size
        self.geometry("500x680")
        # Center the window on the screen
        self.center_window()

    def setup_container(self):
        """Configure main container grid and create frame holder"""
        self.minsize(500, 650)
        # Configure grid for main container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Create main container frame
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def center_window(self):
        """Center the window on the screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.geometry(f"{width}x{height}+{x}+{y}")

    def init_frames(self):
        """Initialize all application frames"""
        # Import here to avoid circular imports
        from gui.main_menu import MainMenu
        from gui.name_generator import NameGenerator
        from gui.phone_generator import PhoneGenerator
        from gui.email_generator import EmailGenerator

        self.frame_classes = {
            'MainMenu': MainMenu,
            'NameGenerator': NameGenerator,
            'PhoneGenerator': PhoneGenerator,
            'EmailGenerator': EmailGenerator,
        }

        self.frames = {}
        for name, frame_class in self.frame_classes.items():
            frame = frame_class(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_name):
        """Bring specified frame to front"""
        if frame_name in self.frames:
            self.frames[frame_name].tkraise()
