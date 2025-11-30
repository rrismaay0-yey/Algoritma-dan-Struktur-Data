#Nurrisma
#D0425308

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe modifikasi")

# -----------------------------
# Pengaturan pemain
# -----------------------------
pemain1 = "A"
pemain2 = "B"
giliran = pemain1

# Board
board = [""] * 9
buttons = []


# -----------------------------
# Cek Pemenang
# -----------------------------
def cek_pemenang():
    pola = [
        (0,1,2), (3,4,5), (6,7,8),     # horizontal
        (0,3,6), (1,4,7), (2,5,8),     # vertikal
        (0,4,8), (2,4,6)               # diagonal
    ]
    for a,b,c in pola:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a]
    return None


# -----------------------------
# Aksi ketika tombol ditekan
# -----------------------------
def tekan(i):
    global giliran

    if board[i] != "":
        return

    board[i] = giliran

    # Warna berbeda untuk A & B
    warna = "#1e90ff" if giliran == pemain1 else "#ff1493"

    buttons[i].config(text=giliran,
                      fg=warna,
                      font=("Arial", 28, "bold"),
                      state="disabled")

    # Cek menang
    p = cek_pemenang()
    if p:
        messagebox.showinfo("Game Selesai", f"Pemenang: Pemain {p}!")
        reset()
        return

    # Cek seri
    if "" not in board:
        messagebox.showinfo("Game Selesai", "Hasil: SERI!")
        reset()
        return

    # Ganti giliran
    giliran = pemain1 if giliran == pemain2 else pemain2
    info_label.config(text=f"Giliran: {giliran}")


# -----------------------------
# Reset Game
# -----------------------------
def reset():
    global board, giliran
    board = [""] * 9
    giliran = pemain1
    for btn in buttons:
        btn.config(text="", state="normal")
    info_label.config(text="Giliran: A")


# -----------------------------
# Frame UI
# -----------------------------
frame = TK.Frame(root, bg="#ececec", padx=10, pady=10)
frame.pack()

# Label giliran
info_label = TK.Label(frame, text="Giliran: A", font=("Arial", 16, "bold"), bg="#ececec")
info_label.grid(row=0, column=0, columnspan=3, pady=10)

# Buat tombol board
for i in range(9):
    btn = TK.Button(frame, width=4, height=2, text="",
                    font=("Arial", 24, "bold"),
                    bg="#ffffff",
                    activebackground="#d9d9d9",
                    command=lambda i=i: tekan(i))
    btn.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
    buttons.append(btn)

# Tombol Reset
reset_btn = tk.Button(frame, text="Reset Game", font=("Arial", 12),
                      command=reset, bg="#ffcc00")
reset_btn.grid(row=5, column=0, columnspan=3, pady=10)


root.mainloop()
