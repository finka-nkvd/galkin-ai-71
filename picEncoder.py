import customtkinter as ctk
from tkinter import ttk, filedialog, messagebox
from PIL import Image

def encode_image(img, secret_message):
    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):
                if index < len(secret_message):
                    binary_char = format(ord(secret_message[index]), '08b')
                    pixel[n] = pixel[n] & ~1 | int(binary_char[7 - (index % 8)])
                    index += 1
                    img.putpixel((col, row), tuple(pixel))
            if index >= len(secret_message):
                return img
    return img

def decode_image(img):
    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for n in range(3):
                binary_message += str(pixel[n] & 1)
                if len(binary_message) % 8 == 0:
                    char = chr(int(binary_message[-8:], 2))
                    if char == '\0':
                        return binary_message
    return binary_message

def save_image(img):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Успех", "Изображение успешно сохранено!")

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        return Image.open(file_path)
    return None

def encode_button_click():
    img = load_image()
    if img:
        secret_message = entry.get() + '\0'
        encoded_image = encode_image(img, secret_message)
        save_image(encoded_image)

def decode_button_click():
    img = load_image()
    if img:
        binary_message = decode_image(img)
        message = ""
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i + 8]
            if byte:
                char = chr(int(byte, 2))
                if char == '\0':
                    break
                message += char
        messagebox.showinfo("Расшифрованное сообщение", message)

root = ctk.CTk()
root.title("Скрыть сообщение в изображении")
root.geometry("400x180")
root.resizable(False, False)

entry_frame = ctk.CTkFrame(root)
entry_frame.pack(pady=10)

entry_label = ctk.CTkLabel(entry_frame, text="Введите секретное сообщение:")
entry_label.pack(side="top", pady=5)

entry = ctk.CTkEntry(entry_frame, width=100)
entry.pack(side="top", pady=5)

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=20)

encode_button = ctk.CTkButton(button_frame, text="Зашифровать", command=encode_button_click)
encode_button.grid(row=0, column=0, padx=10)

decode_button = ctk.CTkButton(button_frame, text="Расшифровать", command=decode_button_click)
decode_button.grid(row=0, column=1, padx=10)

root.mainloop()
