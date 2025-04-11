from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip  # For copy-to-clipboard functionality

# Translation function
def translate_text(event=None):
    try:
        input_text = entry.get().strip()
        if not input_text:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Enter text to translate!")
            return
        
        source_lang = source_lang_combo.get().split()[0]  # Extract code (e.g., "en")
        target_lang = target_lang_combo.get().split()[0]  # Extract code (e.g., "ne")
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, translated if translated else "Translation failed!")
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

# Copy translated text to clipboard
def copy_to_clipboard():
    translated = result_text.get(1.0, tk.END).strip()
    if translated and translated != "Enter text to translate!":
        pyperclip.copy(translated)
        messagebox.showinfo("Success", "Translated text copied to clipboard!")

# Toggle between light and dark themes
def toggle_theme():
    if theme_var.get() == "Dark":
        root.configure(bg="#2b2b2b")
        main_frame.configure(style="Dark.TFrame")
        header_label.configure(bg="#2b2b2b", fg="white")
        instruction_label.configure(bg="#2b2b2b", fg="white")
        result_label.configure(bg="#2b2b2b", fg="white")
        style.configure("TButton", background="#555555", foreground="white")
        style.configure("TCombobox", fieldbackground="#333333", background="#555555", foreground="white")
        entry.configure(bg="#333333", fg="white", insertbackground="white")
        result_text.configure(bg="#333333", fg="white")
    else:
        root.configure(bg="#f0f0f0")
        main_frame.configure(style="Light.TFrame")
        header_label.configure(bg="#f0f0f0", fg="black")
        instruction_label.configure(bg="#f0f0f0", fg="black")
        result_label.configure(bg="#f0f0f0", fg="black")
        style.configure("TButton", background="#e0e0e0", foreground="black")
        style.configure("TCombobox", fieldbackground="white", background="#e0e0e0", foreground="black")
        entry.configure(bg="white", fg="black", insertbackground="black")
        result_text.configure(bg="white", fg="black")

# Clear input and output
def clear_text():
    entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Advanced Translator")
root.geometry("600x450")  # Slightly larger window for better layout
root.configure(bg="#f0f0f0")  # Default light theme

# Styling with ttk
style = ttk.Style()
style.configure("Light.TFrame", background="#f0f0f0")
style.configure("Dark.TFrame", background="#2b2b2b")
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TCombobox", font=("Helvetica", 10))

# Main Frame
main_frame = ttk.Frame(root, padding=20, style="Light.TFrame")
main_frame.pack(expand=True, fill="both")

# Header Label
header_label = tk.Label(main_frame, text="🌐 Advanced Translator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
header_label.pack(pady=10)

# Instruction Label
instruction_label = tk.Label(main_frame, text="Enter text to translate:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
instruction_label.pack(pady=5)

# Language Selection
lang_frame = ttk.Frame(main_frame)
lang_frame.pack(pady=5)

source_lang_combo = ttk.Combobox(lang_frame, values=["en - English", "es - Spanish", "fr - French", "de - German"], width=15, state="readonly")
source_lang_combo.set("en - English")
source_lang_combo.grid(row=0, column=0, padx=5)

target_lang_combo = ttk.Combobox(lang_frame, values=["ne - Nepali", "hi - Hindi", "es - Spanish", "fr - French", "de - German"], width=15, state="readonly")
target_lang_combo.set("ne - Nepali")
target_lang_combo.grid(row=0, column=1, padx=5)  # Fixed the syntax error here

# Input Text Entry
entry = tk.Entry(main_frame, width=50, font=("Helvetica", 11), relief="flat", borderwidth=2)
entry.pack(pady=10)
entry.bind("<KeyRelease>", translate_text)  # Real-time translation as you type

# Button Frame for Translate and Clear
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=5)

translate_button = ttk.Button(button_frame, text="Translate Now", command=translate_text)
translate_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=1, padx=5)

# Result Label and Text Box
result_label = tk.Label(main_frame, text="Translated Output:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=5)

result_text = tk.Text(main_frame, height=5, width=50, font=("Helvetica", 11), relief="flat", borderwidth=2)
result_text.pack(pady=5)

# Copy Button
copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Theme Toggle
theme_var = tk.StringVar(value="Light")
theme_check = ttk.Checkbutton(main_frame, text="Dark Mode", variable=theme_var, onvalue="Dark", offvalue="Light", command=toggle_theme)
theme_check.pack(pady=10)

# Run the GUI
root.mainloop()