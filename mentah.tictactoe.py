#Nurrisma
#D0425308

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

# --- Pengaturan simbol pemain ---
pemain1 = "A"
pemain2 = "B"
giliran = pemain1

# --- Board kosong ---
board = ["", "", "",
         "", "", "",
         "", "", ""]

buttons = []

# --- Fungsi cek pemenang ---
def cek_pemenang():
    pola = [
        (0,1,2), (3,4,5), (6,7,8),   # Horizontal
        (0,3,6), (1,4,7), (2,5,8),   # Vertikal
        (0,4,8), (2,4,6)             # Diagonal
    ]

    for a,b,c in pola:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a]
    return None

# --- Fungsi tombol ditekan ---
def tekan(i):
    global giliran

    if board[i] != "":
        return

    board[i] = giliran
    buttons[i].config(text=giliran, font=("Arial", 24), disabledforeground="black")
    buttons[i]["state"] = "disabled"

    p = cek_pemenang()
    if p:
        messagebox.showinfo("Selesai", f"Pemenang: {p}")
        reset()
        return

    if "" not in board:
        messagebox.showinfo("Seri", "Permainan Seri!")
        reset()
        return

    giliran = pemain1 if giliran == pemain2 else pemain2

# --- Reset ---
def reset():
    global board, giliran
    board = [""] * 9
    giliran = pemain1
    for btn in buttons:
        btn.config(text="", state="normal")

# --- Membuat tombol ---
for i in range(9):
    btn = tk.Button(root, text="", width=5, height=2, font=("Arial", 20),
                    command=lambda i=i: tekan(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
