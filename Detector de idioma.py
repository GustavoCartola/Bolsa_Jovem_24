import tkinter as tk
from langdetect import detect

def detect_language():
    texto = entry.get()
    idioma_detectado = detect(texto)
    if idioma_detectado:
        result_label.config(text=f"Idioma detectado: {idioma_detectado}")
    else:
        result_label.config(text="Não foi possível detectar o idioma.")

# Configuração da janela
root = tk.Tk()
root.title("Reconhecedor de Idioma")

# Entrada de texto
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Botão para detectar idioma
detect_button = tk.Button(root, text="Detectar Idioma", command=detect_language)
detect_button.pack()

# Resultado
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
