import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed (words per minute)
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Text to be spoken
text = "Hello, how are you today?"

# Perform text-to-speech
engine.say(text)
engine.runAndWait()
