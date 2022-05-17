from PIL import Image
import pystray

image = Image.open("icon.png")

def maximizeMe(icon, item):
    print("Yes, OnCourse")
def closeSystem(icon: pystray.Icon, _: pystray._base.Menu):
    """Close System Tray Icon
    Args:
        icon (pystray.Icon): _description_
        _ (pystray._base.Menu): _description_
    """
    print("Exiting Parameter")
    # exit()
    icon.stop()
icon = pystray.Icon("Python Script On Tray", image, menu = pystray.Menu(
    pystray.MenuItem("Maximize", maximizeMe),
    pystray.MenuItem("Exit", closeSystem)
), title="Main Application")

def main():
    if input("[Yes/No] ").lower() == 'yes':
        icon.run()
    else:
        # icon.stop()
        exit()
icon.run()
