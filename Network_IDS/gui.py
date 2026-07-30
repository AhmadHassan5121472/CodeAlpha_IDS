import customtkinter as ctk
from tkinter import ttk
import threading

from packet_capture import start_monitoring
from graphs import show_graphs

class IDSDashboard(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Network Intrusion Detection System")

        self.geometry("1200x700")

        self.resizable(False, False)

        # --------------------------
        # Title
        # --------------------------

        title = ctk.CTkLabel(
            self,
            text="NETWORK INTRUSION DETECTION SYSTEM",
            font=("Arial",30,"bold")
        )

        title.pack(pady=20)

        # --------------------------
        # Status
        # --------------------------

        self.status = ctk.CTkLabel(
            self,
            text="Status : Idle",
            font=("Arial",18)
        )

        self.status.pack()

        # --------------------------
        # Progress Bar
        # --------------------------

        self.progress = ctk.CTkProgressBar(
            self,
            width=600
        )

        self.progress.pack(pady=20)

        self.progress.set(0)

        # --------------------------
        # Buttons
        # --------------------------

        frame = ctk.CTkFrame(self)

        frame.pack(pady=20)

        start_btn = ctk.CTkButton(
            frame,
            text="Start Monitoring",
            width=170,
            command=self.start_ids
        )

        start_btn.grid(row=0,column=0,padx=15)

        graph_btn = ctk.CTkButton(
            frame,
            text="Show Graph",
            width=170,
            command=show_graphs
        )

        graph_btn.grid(row=0,column=1,padx=15)

        exit_btn = ctk.CTkButton(
            frame,
            text="Exit",
            fg_color="red",
            hover_color="#990000",
            width=170,
            command=self.destroy
        )

        exit_btn.grid(row=0,column=2,padx=15)

        # --------------------------
        # Alert Table
        # --------------------------

        self.table = ttk.Treeview(
            self,
            columns=("Time","IP","Attack"),
            show="headings",
            height=18
        )

        self.table.heading("Time",text="Time")
        self.table.heading("IP",text="Source IP")
        self.table.heading("Attack",text="Attack")

        self.table.column("Time",width=200)
        self.table.column("IP",width=350)
        self.table.column("Attack",width=500)

        self.table.pack(fill="both",expand=True,padx=20,pady=20)

    # ------------------------------------

    def add_alert(self,time,ip,attack):

        self.table.insert(
            "",
            "end",
            values=(time,ip,attack)
        )

    # ------------------------------------

    def start_ids(self):

        self.status.configure(
            text="Status : Monitoring..."
        )

        thread = threading.Thread(
            target=start_monitoring,
            args=(self,)
        )

        thread.daemon=True

        thread.start()