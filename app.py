from tkinter import *
import random
import time


def start_typing_speed_test():
    texts = [
        "Learning to type is a hard challenge. This is some random typing that you can use to practice. Ok, thank you for typing this!",
        "Hello my name is dev singh and i am 99 years old.",
        "Words per minute (WPM) is a measure of typing speed, commonly used in recruitment.",
        "For the purposes of WPM measurement a word is standardized to five characters or keystrokes.",
        "The benefits of a standardized measurement of input speed are that it enables comparison across language and hardware boundaries."
    ]

    # Choose a random text
    text = random.choice(texts)
    text_label.config(text="Text to type: " + text)

    # Start the timer
    start_time = time.time()

    # Clear the user input field
    user_input.delete(0, END)

    # Enable the user input field
    user_input.config(state="normal")

    # Set the focus to the user input field
    user_input.focus()

    def calculate_typing_speed(event=None):
        # Disable the user input field
        user_input.config(state="disabled")

        # Get the user input
        user_text = user_input.get()

        # Calculate the correct count
        correct_count = sum(1 for u, c in zip(user_text.split(), text.split()) if u == c)

        # Calculate the total number of words
        total_words = len(text.split())

        # Calculate the time taken
        end_time = time.time()
        time_taken = end_time - start_time

        # Calculate the accuracy and typing speed
        accuracy = (correct_count / total_words) * 100
        typing_speed_wpm = (total_words / time_taken) * 60

        # Display the results
        result_label.config(text=f"Accuracy: {accuracy:.2f}% | Typing Speed: {typing_speed_wpm:.2f} WPM")

    # Bind the Enter key to calculate the typing speed
    window.bind("<Return>", calculate_typing_speed)


# Create the main window
window = Tk()
window.title("Typing Speed Test")

# Create the canvas
canvas = Canvas(window, width=300, height=300)
canvas.pack()

# Load the image
img = PhotoImage(file="test.png")
canvas.create_image(150, 150, image=img)

# Create the label for the welcome message
cursive_font = ("Comic Sans MS", 24, "bold")
label_color = "blue"
welcome_label = Label(window, text='Welcome', font=cursive_font, fg=label_color)
welcome_label.pack()

# Create the "Start" button
start_button = Button(window, text="Start", highlightbackground=label_color, width=50, command=start_typing_speed_test)
start_button.pack()

# Create the label for displaying the text to type
text_label = Label(window, text="Text to type: ", font=("Arial", 10, 'bold'))
text_label.pack()

# Create the user input field
user_input = Entry(window, font=("Arial", 16))
user_input.pack()

# Create the label for displaying the typing speed result
result_label = Label(window, text="", font=("Arial", 16))
result_label.pack()

window.mainloop()
