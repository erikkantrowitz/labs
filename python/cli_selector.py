#!/usr/bin/env python3
"""
This is a Python script that creates a command-line interface (CLI) menu
allowing the user to navigate through options using the keyboard arrow keys.
The user can select one of three options, and upon selection, the script
will print the selected option to the console.

This script uses the 'curses' library, which is a standard Python library
for creating text-based user interfaces in the terminal. It provides
functions to control the terminal screen, handle keyboard input, and
display text in various ways.

The script is designed to be educational, with verbose comments explaining
every part of the code in detail.
"""

# Import the curses library. This library allows us to create text-based
# user interfaces in the terminal. It gives us control over the screen,
# keyboard input, and text display. We import it as 'curses' to use it
# throughout the script.
import curses

# Define a function called 'main' that takes a 'stdscr' parameter. This
# parameter is the standard screen object provided by curses. When we
# call curses.wrapper(main), it will initialize the curses environment
# and pass the screen object to our main function. This is the standard
# way to structure a curses application.
def main(stdscr):
    """
    The main function that contains all the logic for our CLI menu.
    
    Parameters:
    stdscr (curses.window): The standard screen object provided by curses.
                           This represents the entire terminal window.
    """
    
    # Clear the screen. This removes any existing text from the terminal
    # and gives us a clean slate to work with. It's good practice to do
    # this at the beginning of a curses application.
    stdscr.clear()
    
    # Turn off cursor visibility. In a menu interface, we don't want to
    # see the blinking cursor, as it can be distracting. Setting it to 0
    # makes the cursor invisible.
    curses.curs_set(0)
    
    # Enable keypad mode. This allows us to receive special key codes
    # for keys like the arrow keys, function keys, etc. Without this,
    # arrow keys would send multiple characters instead of a single code.
    stdscr.keypad(True)
    
    # Define the list of options that the user can choose from. This is
    # a Python list containing three strings. Each string represents one
    # option in our menu.
    options = ["Option 1", "Option 2", "Option 3"]
    
    # Initialize the current selection index. This variable keeps track
    # of which option is currently highlighted/selected. We start with 0,
    # which corresponds to the first option in our list.
    current_selection = 0
    
    # Enter the main loop. This loop will continue running until the user
    # makes a selection. Inside the loop, we display the menu, wait for
    # user input, and update the selection based on the input.
    while True:
        # Clear the screen again. We do this at the beginning of each
        # iteration to redraw the entire menu. This ensures that any
        # previous display is completely erased before we draw the new one.
        stdscr.clear()
        
        # Get the height and width of the terminal window. This information
        # is useful for centering our menu or ensuring it fits on screen.
        # stdscr.getmaxyx() returns a tuple (height, width).
        height, width = stdscr.getmaxyx()
        
        # Calculate the starting row for our menu. We want to center the
        # menu vertically on the screen. We divide the height by 2 and
        # subtract half the number of options to center it.
        start_row = height // 2 - len(options) // 2
        
        # Loop through each option in our options list. We use enumerate
        # to get both the index (i) and the option text for each item.
        for i, option in enumerate(options):
            # Calculate the row where this option should be displayed.
            # We add the index to the start_row to space out the options.
            row = start_row + i
            
            # Check if this is the currently selected option. If the index
            # (i) matches our current_selection, then this option should
            # be highlighted.
            if i == current_selection:
                # For the selected option, we use reverse video (highlighted).
                # curses.A_REVERSE is an attribute that reverses the colors,
                # making the text appear highlighted. We add this to the
                # default attributes (0).
                stdscr.addstr(row, 0, f"> {option}", curses.A_REVERSE)
            else:
                # For non-selected options, we display them normally without
                # any special attributes.
                stdscr.addstr(row, 0, f"  {option}")
        
        # Refresh the screen. This is crucial in curses - after making
        # changes to the screen with addstr(), we must call refresh()
        # to actually display those changes to the user.
        stdscr.refresh()
        
        # Wait for user input. getch() blocks until the user presses a key,
        # then returns the key code. This is how we detect arrow key presses
        # and other inputs.
        key = stdscr.getch()
        
        # Check what key was pressed. We use constants from the curses
        # module to identify special keys like arrows.
        if key == curses.KEY_UP:
            # The up arrow was pressed. We want to move the selection up.
            # We subtract 1 from current_selection, but we also use modulo
            # to wrap around to the bottom if we're at the top.
            current_selection = (current_selection - 1) % len(options)
        elif key == curses.KEY_DOWN:
            # The down arrow was pressed. We move the selection down,
            # wrapping around to the top if we're at the bottom.
            current_selection = (current_selection + 1) % len(options)
        elif key == ord('\n') or key == curses.KEY_ENTER:
            # Enter key was pressed. This means the user has made their
            # selection. We break out of the loop to end the menu.
            break
        # If any other key is pressed, we ignore it and continue the loop.
    
    # After the loop ends (user pressed Enter), we clean up the curses
    # environment. This restores the terminal to its normal state.
    curses.endwin()
    
    # Now that curses is finished, we can print to the standard output.
    # We print the selected option. We use the current_selection index
    # to get the corresponding option from our options list.
    print(f"You selected: {options[current_selection]}")

# This is the entry point of the script. When the script is run directly
# (not imported as a module), this code executes.
if __name__ == "__main__":
    # Call curses.wrapper() with our main function. This function handles
    # the initialization and cleanup of the curses environment. It sets
    # up the terminal properly and ensures that even if our program crashes,
    # the terminal is restored to a usable state.
    curses.wrapper(main)