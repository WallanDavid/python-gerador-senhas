import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Adicionando a importação do ttk para usar o Progressbar
import secrets
import string
import keyring

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerador de Senhas Seguras")
        self.master.geometry("400x350")

        self.label_length = tk.Label(master, text="Comprimento da Senha:")
        self.label_length.pack(pady=10)

        self.length_var = tk.StringVar()
        self.entry_length = tk.Entry(master, textvariable=self.length_var)
        self.entry_length.pack()

        self.label_password_strength = tk.Label(master, text="Força da Senha:")
        self.label_password_strength.pack()

        self.progressbar_strength = ttk.Progressbar(master, length=200, mode="determinate")
        self.progressbar_strength.pack(pady=5)

        self.button_generate = tk.Button(master, text="Gerar Senha", command=self.generate_password)
        self.button_generate.pack(pady=10)

        self.label_password = tk.Label(master, text="Senha Gerada:")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, state="readonly")
        self.entry_password.pack()

        self.button_copy = tk.Button(master, text="Copiar para a Área de Transferência", command=self.copy_to_clipboard)
        self.button_copy.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                messagebox.showerror("Erro", "O comprimento deve ser maior que zero.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(characters) for _ in range(length))

            # Avalia a força da senha
            strength = self.evaluate_password_strength(password)
            self.progressbar_strength["value"] = strength

            self.entry_password.config(state="normal")
            self.entry_password.delete(0, "end")
            self.entry_password.insert(0, password)
            self.entry_password.config(state="readonly")

        except ValueError:
            messagebox.showerror("Erro", "Digite um comprimento válido.")

    def evaluate_password_strength(self, password):
        # Implementação básica para avaliar a força da senha (pode ser melhorada)
        upper_case = any(char.isupper() for char in password)
        lower_case = any(char.islower() for char in password)
        digit = any(char.isdigit() for char in password)
        special_char = any(char in string.punctuation for char in password)

        requirements = [upper_case, lower_case, digit, special_char]
        strength = sum(requirements) / len(requirements) * 100

        return int(strength)

    def copy_to_clipboard(self):
        password = self.entry_password.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            self.master.update()
            messagebox.showinfo("Copiado", "Senha copiada para a Área de Transferência.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
