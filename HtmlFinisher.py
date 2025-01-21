import keyboard
import re
import time
'''
Install these for it to work:
    pip install keyboard
    pip install pyperclip
'''


def handle_key_event(e):
    global buffer
    if e.event_type == 'down':
        if e.name == 'backspace' and buffer:
            buffer = buffer[:-1]  # Handle backspace correctly
        elif len(e.name) == 1:
            buffer += e.name  # Add other key presses to our buffer

        if e.name == '>':
            # Temporarily release Shift to avoid interference
            if keyboard.is_pressed('shift'):
                keyboard.release('shift')
            time.sleep(0.05)  # Wait to ensure all keys are released

            text = ''.join(buffer)
            match = re.search(r"<(\w+)[^>]*>$", text)
            if match:
                tag_name = match.group(1)
                closing_tag = f"</{tag_name}>"
                keyboard.write(closing_tag)  # Write the closing tag

                # Ensure cursor placement is inside the closing tag
                # This is handled by counting and moving the cursor back inside the tag
                time.sleep(0.08)  # Additional slight delay to stabilize input
                for _ in range(len(tag_name) + 3):
                    keyboard.press_and_release('left')


            buffer = ""  # Clear the buffer after processing


buffer = ""  # Initialize the buffer to capture keystrokes


def main():
    print("Listening for HTML tags. Type away and end tags with '>'.")
    keyboard.hook(handle_key_event)
    keyboard.wait()


if __name__ == "__main__":
    main()
