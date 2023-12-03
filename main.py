import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import threading
import time
from datetime import datetime, timedelta

class RansomwareSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("WannaSim - Your Files Are Encrypted")
        self.master.geometry("870x500")
        self.master.configure(bg="#000000")

        # Simulated victim information
        self.victim_id = "V123456"
        self.wallet_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        self.ransom_amount = "$500 worth of Ethereum"

        # Set the deadline date
        self.deadline_date = datetime.now() + timedelta(days=1)  # 24 hours from now

        # Left Column
        left_frame = tk.Frame(self.master, bg="#000000")
        left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        # Load the image
        self.image = tk.PhotoImage(file='./image.png')  # Replace with the actual path and name of your image file
        self.image_label = tk.Label(left_frame, image=self.image, bg="#000000")
        self.image_label.pack(pady=10)

        # Countdown timer variables
        self.timer_seconds = 86400  # 24 hours
        self.timer_label = tk.Label(left_frame, text=f"Your files will \nbe lost on: \n{self.deadline_date.strftime('%Y-%m-%d %H:%M:%S')}\n\nTime left: \n{self.format_time(self.timer_seconds)}", font=("Courier", 18), bg="#000000", fg="#ff0000")
        self.timer_label.pack(pady=10)

        # Live Chat Support Button
        self.live_chat_button = tk.Button(left_frame, text="Live Chat Support", command=self.open_live_chat, font=("Courier", 12), bg="#ff0000", fg="#000000", height=3)
        self.live_chat_button.pack(pady=10)

        # Right Column
        right_frame = tk.Frame(self.master, bg="#000000")
        right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        # Ransomware title
        self.title_label = tk.Label(right_frame, text="Ooops, your files have been encrypted!", font=("Courier", 18, "bold"), bg="#000000", fg="#ff0000")
        self.title_label.pack(pady=10)

        # Scrollable Textbox for Ransomware Information
        self.ransomware_info_text = (
            "WannaSim Ransomware Information:\n\n"
            "ATTENTION: Your computer has been infected with WannaSim, a highly sophisticated ransomware.\n\n"
            "What happened to your files?\n\n"
            "All your personal files, including documents, photos, videos, and databases, have been encrypted with a "
            "strong cryptographic algorithm. This means you will not be able to access them without the decryption key.\n\n"
            "What does this mean for you?\n\n"
            "To restore your files and regain access to your system, you must pay a ransom of $500 in Ethereum. "
            "Failure to comply with this demand within the specified time will result in permanent loss of your files.\n\n"
            "How to pay the ransom?\n\n"
            "1. Purchase $500 worth of Ethereum (ETH).\n"
            "2. Send the Ethereum to the following wallet address:\n"
            f"   Ethereum Address: {self.wallet_address}\n"
            "3. After the payment is confirmed, you will receive the decryption key to unlock your files.\n\n"
            "IMPORTANT NOTES:\n\n"
            "- Do not attempt to decrypt the files without the provided key, as it may result in permanent data loss.\n"
            "- Any attempt to involve law enforcement or third parties will lead to the destruction of the decryption key.\n"
            "- The ransom amount is subject to increase if payment is not made within the specified timeframe.\n\n"
            "This is a time-sensitive matter, and you have 24 hours to make the payment. Time is of the essence."
        )

        self.ransomware_info_box = scrolledtext.ScrolledText(right_frame, width=80, height=20, wrap=tk.WORD, font=("Courier", 12), bg="#000000", fg="#ff0000")
        self.ransomware_info_box.insert(tk.END, self.ransomware_info_text)
        self.ransomware_info_box.config(state="disabled")
        self.ransomware_info_box.pack(pady=10)

        # Instruction to send $500 to the Ethereum address
        self.send_instruction_label = tk.Label(right_frame, text="Send $500 to the following Ethereum address:", font=("Courier", 20), bg="#000000", fg="#ff0000", bd=5, relief=tk.GROOVE)
        self.send_instruction_label.pack(pady=5)

        # Ethereum Wallet Address and Copy Button
        wallet_frame = tk.Frame(right_frame, bg="#000000")
        wallet_frame.pack()

        self.wallet_label = tk.Label(wallet_frame, text=f"{self.wallet_address}", font=("Courier", 16), bg="#000000", fg="#ff0000")
        self.wallet_label.pack(side="left", padx=10)

        self.copy_button = tk.Button(wallet_frame, text="Copy", command=self.copy_address, font=("Courier", 16), bg="#ff0000", fg="#000000")
        self.copy_button.pack(side="left", padx=10)

        # Check Payment and Decrypt Buttons
        buttons_frame = tk.Frame(right_frame, bg="#000000")
        buttons_frame.pack(pady=10)

        self.check_payment_button = tk.Button(buttons_frame, text="Check Payment", command=self.check_payment, font=("Courier", 16), bg="#ff0000", fg="#000000")
        self.check_payment_button.pack(side="left", padx=10)

        self.decrypt_button = tk.Button(buttons_frame, text="Decrypt", command=self.decrypt_files, font=("Courier", 16), bg="#ff0000", fg="#000000")
        self.decrypt_button.pack(side="left", padx=10)

        # Start countdown thread
        self.countdown_thread = threading.Thread(target=self.update_timer)
        self.countdown_thread.start()

    def update_timer(self):
        while self.timer_seconds > 0:
            time.sleep(1)
            self.timer_seconds -= 1
            time_left = self.format_time(self.timer_seconds)
            self.timer_label.config(text=f"Your files will \nbe lost on: \n{self.deadline_date.strftime('%Y-%m-%d %H:%M:%S')}\n\nTime left: \n{time_left}")

        # Display a message when the timer reaches 0
        messagebox.showinfo("Time's Up!", "The payment deadline has passed. Your files will remain encrypted.")

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def open_live_chat(self):
        messagebox.showinfo("Live Chat Support", "Connecting to live chat support...")

    def copy_address(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.wallet_address)
        self.master.update()

    def check_payment(self):
        messagebox.showinfo("Payment Status", "Payment status: Pending")

    def decrypt_files(self):
        messagebox.showinfo("Decryption", "Decryption process initiated. Please wait for further instructions.")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap('icon.ico')  # Replace 'icon.ico' with the path to your icon file
    root.configure(bg="#000000")
    ransomware_simulator = RansomwareSimulator(root)
    root.mainloop()
