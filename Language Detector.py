import tkinter as tk
from langdetect import detect

def detect_language():
    texto = entry.get()  # get the text from the entry widget
    detected_language = detect(texto)  # detect the language of the text
    if detected_language:
        result_label.config(text=f"Idioma detectado: {detected_language}")  # display detected language
    else:
        result_label.config(text="Não foi possível detectar o idioma.")  # display error message if detection fails

# Window configuration
root = tk.Tk()
root.title("Reconhecedor de Idioma")  # set the window title

# Text entry
entry = tk.Entry(root, width=30)  # create an entry widget for text input
entry.pack(pady=10)

# Button to detect language
detect_button = tk.Button(root, text="Detectar Idioma", command=detect_language)  # create a button to trigger language detection
detect_button.pack()

# Result label
result_label = tk.Label(root, text="")  # create a label to display the result
result_label.pack(pady=10)

root.mainloop()  # start the main event loop
