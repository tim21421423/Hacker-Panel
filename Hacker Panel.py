import tkinter as tk
from tkinter import ttk, scrolledtext, Menu
import threading
import time
import sys
import random
import string

class HackerPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hacker Panel v0.1")
        self.root.geometry("900x700")
        self.root.configure(bg='black')
        
        # Create hacker style menu
        self.create_menu()
        
        # Style setup
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='black', borderwidth=0)
        style.configure('TNotebook.Tab', background='darkgreen', foreground='lime', 
                       padding=[10, 5], font=('Courier', 10, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', '#003300')], 
                 foreground=[('selected', '#00ff00')])
        
        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # DDoS Attack tab
        self.ddos_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.ddos_frame, text='DDoS Attack')
        
        # Roblox Hack tab
        self.roblox_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.roblox_frame, text='Roblox Hack')
        
        # VPN Dox / Leak tab
        self.vpn_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.vpn_frame, text='VPN Dox / Leak')
        
        # Message tab
        self.message_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.message_frame, text='Message')
        
        # IP Leak tab
        self.ip_leak_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.ip_leak_frame, text='IP Leak')
        
        # Console tab
        self.console_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.console_frame, text='Console')
        
        # Admin Panel tab
        self.admin_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.admin_frame, text='Admin Panel')
        
        # Gmail Leak tab
        self.gmail_frame = tk.Frame(self.notebook, bg='black')
        self.notebook.add(self.gmail_frame, text='Gmail Leak')
        
        # Initialize all tabs
        self.init_ddos_tab()
        self.init_roblox_tab()
        self.init_vpn_tab()
        self.init_message_tab()
        self.init_ip_leak_tab()
        self.init_console_tab()
        self.init_admin_tab()
        self.init_gmail_tab()
        
        # Close button
        close_btn = tk.Button(root, text="X", command=self.close_program, 
                            bg='red', fg='white', font=('Courier', 12, 'bold'),
                            bd=2, relief='raised', width=3, height=1)
        close_btn.place(relx=0.97, rely=0.02, anchor='ne')
        
        # Status bar
        self.status_bar = tk.Label(root, text="[Hacker Panel v0.1] System Ready | Connection: Secure | Status: Online | Admin: Disabled", 
                                  bg='black', fg='lime', font=('Courier', 8),
                                  bd=1, relief='sunken', anchor='w')
        self.status_bar.pack(side='bottom', fill='x')
        
        self.ddos_active = False
        self.roblox_active = False
        self.vpn_active = False
        self.stolerobux_active = False
        self.admin_logged_in = False
        
    def create_menu(self):
        # Create menu bar
        menubar = Menu(self.root, bg='black', fg='lime', 
                      activebackground='darkgreen', activeforeground='lime')
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = Menu(menubar, tearoff=0, bg='black', fg='lime',
                        activebackground='darkgreen', activeforeground='lime')
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear All Consoles", command=self.clear_all_consoles)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.close_program)
        
        # Tools menu
        tools_menu = Menu(menubar, tearoff=0, bg='black', fg='lime',
                         activebackground='darkgreen', activeforeground='lime')
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Network Scanner", command=self.fake_network_scan)
        tools_menu.add_command(label="Port Scanner", command=self.fake_port_scan)
        tools_menu.add_command(label="Password Cracker", command=self.fake_password_cracker)
        
        # Admin menu
        admin_menu = Menu(menubar, tearoff=0, bg='black', fg='lime',
                         activebackground='darkgreen', activeforeground='lime')
        menubar.add_cascade(label="Admin", menu=admin_menu)
        admin_menu.add_command(label="Login as Admin", command=self.admin_login_prompt)
        admin_menu.add_command(label="Logout", command=self.admin_logout)
        
        # Help menu
        help_menu = Menu(menubar, tearoff=0, bg='black', fg='lime',
                        activebackground='darkgreen', activeforeground='lime')
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Commands", command=self.show_commands)
        help_menu.add_command(label="About", command=self.show_about)
        
    def init_ddos_tab(self):
        # Console for DDoS
        self.ddos_console = scrolledtext.ScrolledText(self.ddos_frame, bg='black', fg='lime',
                                                     font=('Courier', 10), height=15,
                                                     wrap=tk.WORD, bd=2, relief='sunken')
        self.ddos_console.pack(pady=10, padx=10, fill='both', expand=True)
        self.ddos_console.insert(tk.END, "[Hacker Panel v0.1]: Ready for DDoS Attack\n")
        self.ddos_console.config(state='disabled')
        
        # Frame for button and textbox
        control_frame = tk.Frame(self.ddos_frame, bg='black')
        control_frame.pack(pady=10)
        
        # Textbox for URL input
        self.url_textbox = tk.Entry(control_frame, bg='darkgreen', fg='lime',
                                   font=('Courier', 10), width=40,
                                   insertbackground='lime', bd=2, relief='sunken')
        self.url_textbox.pack(side='left', padx=5)
        self.url_textbox.insert(0, "Enter target URL...")
        self.url_textbox.bind('<FocusIn>', self.clear_placeholder)
        
        # Start DDoS button
        self.ddos_btn = tk.Button(control_frame, text="Start DDoS Attack", 
                                 command=self.start_ddos,
                                 bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                 bd=2, relief='raised', padx=10, pady=5)
        self.ddos_btn.pack(side='left', padx=5)
        
    def clear_placeholder(self, event):
        if self.url_textbox.get() == "Enter target URL...":
            self.url_textbox.delete(0, tk.END)
            
    def init_roblox_tab(self):
        # Console for Roblox
        self.roblox_console = scrolledtext.ScrolledText(self.roblox_frame, bg='black', fg='lime',
                                                       font=('Courier', 10), height=15,
                                                       wrap=tk.WORD, bd=2, relief='sunken')
        self.roblox_console.pack(pady=10, padx=10, fill='both', expand=True)
        self.roblox_console.insert(tk.END, "[Hacker Panel v0.1]: Ready for Roblox Hack\n")
        self.roblox_console.config(state='disabled')
        
        # Frame for first step
        self.roblox_frame1 = tk.Frame(self.roblox_frame, bg='black')
        self.roblox_frame1.pack(pady=5)
        
        self.username_textbox = tk.Entry(self.roblox_frame1, bg='darkgreen', fg='lime',
                                        font=('Courier', 10), width=40,
                                        insertbackground='lime', bd=2, relief='sunken')
        self.username_textbox.pack(side='left', padx=5)
        self.username_textbox.insert(0, "Enter Roblox username...")
        self.username_textbox.bind('<FocusIn>', self.clear_username_placeholder)
        
        self.roblox_btn = tk.Button(self.roblox_frame1, text="Start Hack", 
                                   command=self.start_roblox_hack,
                                   bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                   bd=2, relief='raised', padx=10, pady=5)
        self.roblox_btn.pack(side='left', padx=5)
        
        # Frame for second step (initially hidden)
        self.roblox_frame2 = tk.Frame(self.roblox_frame, bg='black')
        
        self.password_textbox = tk.Entry(self.roblox_frame2, bg='darkgreen', fg='lime',
                                        font=('Courier', 10), width=40,
                                        insertbackground='lime', bd=2, relief='sunken', show='*')
        self.password_textbox.pack(side='left', padx=5)
        self.password_textbox.insert(0, "Enter new password...")
        self.password_textbox.bind('<FocusIn>', self.clear_password_placeholder)
        
        self.password_btn = tk.Button(self.roblox_frame2, text="Change Password", 
                                     command=self.change_password,
                                     bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                     bd=2, relief='raised', padx=10, pady=5)
        self.password_btn.pack(side='left', padx=5)
        
    def init_vpn_tab(self):
        # Console for VPN Dox
        self.vpn_console = scrolledtext.ScrolledText(self.vpn_frame, bg='black', fg='lime',
                                                     font=('Courier', 10), height=15,
                                                     wrap=tk.WORD, bd=2, relief='sunken')
        self.vpn_console.pack(pady=10, padx=10, fill='both', expand=True)
        self.vpn_console.insert(tk.END, "[Hacker Panel v0.1]: VPN Dox / Leak Ready\n")
        self.vpn_console.config(state='disabled')
        
        # Frame for button
        control_frame = tk.Frame(self.vpn_frame, bg='black')
        control_frame.pack(pady=10)
        
        # Dox VPN button
        self.vpn_btn = tk.Button(control_frame, text="Dox VPN", 
                                command=self.start_vpn_dox,
                                bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                bd=2, relief='raised', padx=20, pady=10)
        self.vpn_btn.pack()
        
    def init_message_tab(self):
        # Console for Message
        self.message_console = scrolledtext.ScrolledText(self.message_frame, bg='black', fg='lime',
                                                        font=('Courier', 10), height=10,
                                                        wrap=tk.WORD, bd=2, relief='sunken')
        self.message_console.pack(pady=10, padx=10, fill='both', expand=True)
        self.message_console.insert(tk.END, "[Hacker Panel v0.1]: Message System Ready\n")
        self.message_console.config(state='disabled')
        
        # Frame for IP input
        ip_frame = tk.Frame(self.message_frame, bg='black')
        ip_frame.pack(pady=5)
        
        tk.Label(ip_frame, text="Target IP:", bg='black', fg='lime', 
                font=('Courier', 10)).pack(side='left', padx=5)
        
        self.ip_textbox = tk.Entry(ip_frame, bg='darkgreen', fg='lime',
                                  font=('Courier', 10), width=30,
                                  insertbackground='lime', bd=2, relief='sunken')
        self.ip_textbox.pack(side='left', padx=5)
        self.ip_textbox.insert(0, "Enter IP address...")
        self.ip_textbox.bind('<FocusIn>', self.clear_ip_placeholder)
        
        self.ip_btn = tk.Button(ip_frame, text="Set IP", 
                               command=self.set_ip,
                               bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                               bd=2, relief='raised', padx=10, pady=2)
        self.ip_btn.pack(side='left', padx=5)
        
        # Frame for message input (initially hidden)
        self.message_frame2 = tk.Frame(self.message_frame, bg='black')
        
        tk.Label(self.message_frame2, text="Message:", bg='black', fg='lime',
                font=('Courier', 10)).pack(side='left', padx=5)
        
        self.message_textbox = tk.Entry(self.message_frame2, bg='darkgreen', fg='lime',
                                       font=('Courier', 10), width=40,
                                       insertbackground='lime', bd=2, relief='sunken')
        self.message_textbox.pack(side='left', padx=5)
        self.message_textbox.insert(0, "Enter your message...")
        self.message_textbox.bind('<FocusIn>', self.clear_message_placeholder)
        
        self.send_btn = tk.Button(self.message_frame2, text="Send Message", 
                                 command=self.send_message,
                                 bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                 bd=2, relief='raised', padx=10, pady=2)
        self.send_btn.pack(side='left', padx=5)
        
    def init_ip_leak_tab(self):
        # Console for IP Leak
        self.ip_leak_console = scrolledtext.ScrolledText(self.ip_leak_frame, bg='black', fg='lime',
                                                        font=('Courier', 10), height=15,
                                                        wrap=tk.WORD, bd=2, relief='sunken')
        self.ip_leak_console.pack(pady=10, padx=10, fill='both', expand=True)
        self.ip_leak_console.insert(tk.END, "[Hacker Panel v0.1]: IP Leak System Ready\n")
        self.ip_leak_console.config(state='disabled')
        
        # Frame for button
        control_frame = tk.Frame(self.ip_leak_frame, bg='black')
        control_frame.pack(pady=10)
        
        # Give IP button
        self.ip_leak_btn = tk.Button(control_frame, text="Give IP", 
                                    command=self.generate_random_ip,
                                    bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                    bd=2, relief='raised', padx=20, pady=10)
        self.ip_leak_btn.pack()
        
    def init_console_tab(self):
        # Console for commands
        self.console = scrolledtext.ScrolledText(self.console_frame, bg='black', fg='lime',
                                                font=('Courier', 10), height=15,
                                                wrap=tk.WORD, bd=2, relief='sunken')
        self.console.pack(pady=10, padx=10, fill='both', expand=True)
        self.console.insert(tk.END, "[Hacker Panel v0.1]: Console Ready\n")
        self.console.insert(tk.END, "Available commands: help, CookieGive, RobloxInfoCookie <cookie>, stolerobux <username>, givemerobux, robloxplayers, offinternet, stealallrobux\n")
        self.console.config(state='disabled')
        
        # Frame for command input
        cmd_frame = tk.Frame(self.console_frame, bg='black')
        cmd_frame.pack(pady=10)
        
        tk.Label(cmd_frame, text=">", bg='black', fg='lime', 
                font=('Courier', 12, 'bold')).pack(side='left', padx=5)
        
        self.cmd_textbox = tk.Entry(cmd_frame, bg='darkgreen', fg='lime',
                                   font=('Courier', 11), width=60,
                                   insertbackground='lime', bd=2, relief='sunken')
        self.cmd_textbox.pack(side='left', padx=5)
        self.cmd_textbox.bind('<Return>', self.execute_command)
        
        self.cmd_btn = tk.Button(cmd_frame, text="Execute", 
                                command=self.execute_command,
                                bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                bd=2, relief='raised', padx=10, pady=2)
        self.cmd_btn.pack(side='left', padx=5)
        
        # Frame for stolerobux input (initially hidden)
        self.stolerobux_frame = tk.Frame(self.console_frame, bg='black')
        
        tk.Label(self.stolerobux_frame, text="Username to give robux:", bg='black', fg='lime',
                font=('Courier', 10)).pack(side='left', padx=5)
        
        self.stolerobux_textbox = tk.Entry(self.stolerobux_frame, bg='darkgreen', fg='lime',
                                          font=('Courier', 10), width=30,
                                          insertbackground='lime', bd=2, relief='sunken')
        self.stolerobux_textbox.pack(side='left', padx=5)
        
        self.stolerobux_btn = tk.Button(self.stolerobux_frame, text="Give Robux", 
                                       command=self.give_robux,
                                       bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                       bd=2, relief='raised', padx=10, pady=2)
        self.stolerobux_btn.pack(side='left', padx=5)
    
    def init_admin_tab(self):
        # Console for Admin Panel
        self.admin_console = scrolledtext.ScrolledText(self.admin_frame, bg='black', fg='lime',
                                                      font=('Courier', 10), height=12,
                                                      wrap=tk.WORD, bd=2, relief='sunken')
        self.admin_console.pack(pady=10, padx=10, fill='both', expand=True)
        self.admin_console.insert(tk.END, "[Hacker Panel v0.1]: Admin Panel Ready\n")
        self.admin_console.insert(tk.END, "[Hacker Panel v0.1]: Please login to use admin functions\n")
        self.admin_console.config(state='disabled')
        
        # Login Frame
        self.admin_login_frame = tk.Frame(self.admin_frame, bg='black')
        self.admin_login_frame.pack(pady=10)
        
        tk.Label(self.admin_login_frame, text="Admin Username:", bg='black', fg='lime',
                font=('Courier', 10)).pack(side='left', padx=5)
        
        self.admin_username = tk.Entry(self.admin_login_frame, bg='darkgreen', fg='lime',
                                      font=('Courier', 10), width=20,
                                      insertbackground='lime', bd=2, relief='sunken')
        self.admin_username.pack(side='left', padx=5)
        self.admin_username.insert(0, "admin")
        
        tk.Label(self.admin_login_frame, text="Password:", bg='black', fg='lime',
                font=('Courier', 10)).pack(side='left', padx=5)
        
        self.admin_password = tk.Entry(self.admin_login_frame, bg='darkgreen', fg='lime',
                                      font=('Courier', 10), width=20,
                                      insertbackground='lime', bd=2, relief='sunken', show='*')
        self.admin_password.pack(side='left', padx=5)
        self.admin_password.insert(0, "password")
        
        self.admin_login_btn = tk.Button(self.admin_login_frame, text="Continue", 
                                        command=self.admin_login,
                                        bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                        bd=2, relief='raised', padx=10, pady=2)
        self.admin_login_btn.pack(side='left', padx=5)
        
        # Admin Control Frame (initially hidden)
        self.admin_control_frame = tk.Frame(self.admin_frame, bg='black')
        
        tk.Label(self.admin_control_frame, text="Player to ban:", bg='black', fg='lime',
                font=('Courier', 10)).pack(side='left', padx=5)
        
        self.admin_ban_textbox = tk.Entry(self.admin_control_frame, bg='darkgreen', fg='lime',
                                         font=('Courier', 10), width=30,
                                         insertbackground='lime', bd=2, relief='sunken')
        self.admin_ban_textbox.pack(side='left', padx=5)
        self.admin_ban_textbox.insert(0, "Enter username...")
        self.admin_ban_textbox.bind('<FocusIn>', self.clear_admin_placeholder)
        
        self.admin_ban_btn = tk.Button(self.admin_control_frame, text="Ban Player", 
                                      command=self.ban_player,
                                      bg='darkred', fg='white', font=('Courier', 10, 'bold'),
                                      bd=2, relief='raised', padx=15, pady=5)
        self.admin_ban_btn.pack(side='left', padx=10)
        
        self.admin_unban_btn = tk.Button(self.admin_control_frame, text="Unban Player", 
                                        command=self.unban_player,
                                        bg='darkgreen', fg='lime', font=('Courier', 10, 'bold'),
                                        bd=2, relief='raised', padx=15, pady=5)
        self.admin_unban_btn.pack(side='left', padx=5)
        
    def init_gmail_tab(self):
        # Console for Gmail Leak
        self.gmail_console = scrolledtext.ScrolledText(self.gmail_frame, bg='black', fg='lime',
                                                      font=('Courier', 10), height=15,
                                                      wrap=tk.WORD, bd=2, relief='sunken')
        self.gmail_console.pack(pady=10, padx=10, fill='both', expand=True)
        self.gmail_console.insert(tk.END, "[Hacker Panel v0.1]: Gmail Leak System Ready\n")
        self.gmail_console.config(state='disabled')
        
        # Frame for button
        control_frame = tk.Frame(self.gmail_frame, bg='black')
        control_frame.pack(pady=10)
        
        # Leak button
        self.gmail_btn = tk.Button(control_frame, text="LEAK GMAILS", 
                                  command=self.generate_gmails,
                                  bg='darkgreen', fg='lime', font=('Courier', 12, 'bold'),
                                  bd=3, relief='raised', padx=30, pady=15)
        self.gmail_btn.pack()
        
        # Info label
        info_label = tk.Label(self.gmail_frame, text="[ Generating real-looking Gmail addresses ]", 
                            bg='black', fg='darkgreen', font=('Courier', 8))
        info_label.pack(pady=5)
        
    def generate_gmails(self):
        # Start generation in separate thread
        thread = threading.Thread(target=self.gmail_generation_process)
        thread.daemon = True
        thread.start()
        
    def gmail_generation_process(self):
        # Disable button temporarily
        self.gmail_btn.config(state='disabled', bg='gray', text="LEAKING...")
        
        # Generate 15 fake Gmail addresses
        for _ in range(15):
            gmail = self.generate_realistic_gmail()
            self.update_console(self.gmail_console, f"[Hacker Panel v0.1]: {gmail}")
            time.sleep(0.3)  # Small delay between generations
        
        # Re-enable button
        self.gmail_btn.config(state='normal', bg='darkgreen', text="LEAK GMAILS")
        self.update_console(self.gmail_console, "[Hacker Panel v0.1]: Gmail leak complete! 15 addresses found.")
        
    def generate_realistic_gmail(self):
        # First names
        first_names = ["John", "Jane", "Mike", "Sarah", "David", "Emma", "Chris", "Lisa", "James", "Mary",
                      "Robert", "Patricia", "Michael", "Jennifer", "William", "Linda", "Richard", "Elizabeth",
                      "Joseph", "Susan", "Thomas", "Jessica", "Charles", "Karen", "Daniel", "Nancy", "Matthew",
                      "Betty", "Anthony", "Helen", "Donald", "Sandra", "Mark", "Donna", "Paul", "Carol",
                      "Steven", "Ruth", "Andrew", "Sharon", "Kenneth", "Michelle", "Joshua", "Laura",
                      "Kevin", "Sarah", "Brian", "Kimberly", "George", "Deborah"]
        
        # Last names
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
                     "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
                     "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
                     "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
                     "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
                     "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter"]
        
        # Common words for usernames
        words = ["Gamer", "Pro", "Master", "Player", "King", "Queen", "Star", "Cool", "Epic", "Legend",
                "Shadow", "Hunter", "Warrior", "Knight", "Ninja", "Dragon", "Phoenix", "Wolf", "Tiger",
                "Eagle", "Thunder", "Lightning", "Storm", "Blaze", "Frost", "Fire", "Ice", "Dark", "Light"]
        
        # Decide generation method
        method = random.randint(1, 4)
        
        if method == 1:
            # FirstName.LastName + numbers
            first = random.choice(first_names)
            last = random.choice(last_names)
            numbers = random.randint(10, 9999)
            return f"{first.lower()}.{last.lower()}{numbers}@gmail.com"
            
        elif method == 2:
            # FirstName + word + numbers
            first = random.choice(first_names)
            word = random.choice(words)
            numbers = random.randint(1, 999)
            return f"{first.lower()}{word.lower()}{numbers}@gmail.com"
            
        elif method == 3:
            # Word + LastName + numbers
            word = random.choice(words)
            last = random.choice(last_names)
            numbers = random.randint(10, 999)
            return f"{word.lower()}{last.lower()}{numbers}@gmail.com"
            
        else:
            # First initial + LastName + numbers
            first = random.choice(first_names)
            last = random.choice(last_names)
            numbers = random.randint(100, 9999)
            return f"{first[0].lower()}{last.lower()}{numbers}@gmail.com"
    
    def admin_login_prompt(self):
        # Switch to admin tab and show login
        self.notebook.select(self.admin_frame)
        self.update_console(self.admin_console, "[Hacker Panel v0.1]: Please login to continue")
        
    def admin_logout(self):
        if self.admin_logged_in:
            self.admin_logged_in = False
            self.admin_control_frame.pack_forget()
            self.admin_login_frame.pack(pady=10)
            self.status_bar.config(text="[Hacker Panel v0.1] System Ready | Connection: Secure | Status: Online | Admin: Disabled")
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Admin logged out")
        
    def admin_login(self):
        username = self.admin_username.get()
        password = self.admin_password.get()
        
        # Simple fake authentication
        if username and password:
            self.admin_logged_in = True
            self.admin_login_frame.pack_forget()
            self.admin_control_frame.pack(pady=10)
            self.status_bar.config(text="[Hacker Panel v0.1] System Ready | Connection: Secure | Status: Online | Admin: Enabled")
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Admin login successful!")
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Welcome to Admin Panel")
        else:
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Login failed! Invalid credentials")
            
    def clear_admin_placeholder(self, event):
        if self.admin_ban_textbox.get() == "Enter username...":
            self.admin_ban_textbox.delete(0, tk.END)
    
    def ban_player(self):
        if not self.admin_logged_in:
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Please login first!")
            return
            
        player = self.admin_ban_textbox.get()
        if player == "Enter username..." or not player:
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Please enter a username!")
            return
            
        self.update_console(self.admin_console, f"[Hacker Panel v0.1]: Player {player} Has been banned!")
        self.admin_ban_textbox.delete(0, tk.END)
        self.admin_ban_textbox.insert(0, "Enter username...")
        
    def unban_player(self):
        if not self.admin_logged_in:
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Please login first!")
            return
            
        player = self.admin_ban_textbox.get()
        if player == "Enter username..." or not player:
            self.update_console(self.admin_console, "[Hacker Panel v0.1]: Please enter a username!")
            return
            
        self.update_console(self.admin_console, f"[Hacker Panel v0.1]: Player {player} Has been unbanned!")
        self.admin_ban_textbox.delete(0, tk.END)
        self.admin_ban_textbox.insert(0, "Enter username...")
        
    def generate_cookie(self):
        cookies = []
        base = "_|WARNING:-DO-NOT-SHARE-THIS.--This-very-long-string-is-your-security-key--|_"
        
        for _ in range(12):
            random_chars = ''.join(random.choices('0123456789abcdef', k=38))
            cookies.append(base + random_chars)
        
        return cookies
    
    def generate_roblox_username(self):
        adjectives = ["Cool", "Epic", "Pro", "Mega", "Ultra", "Super", "Hyper", "Dark", "Shadow", "Light", "Night", "Fire", "Ice", "Thunder", "Dragon", "Phoenix", "Wolf", "Tiger", "Eagle", "Masked"]
        names = ["Player", "Gamer", "Master", "Hunter", "Warrior", "Knight", "Lord", "King", "Queen", "Ninja", "Samurai", "Assassin", "Legend", "Hero", "Champion", "Wizard", "Sorcerer", "Archer", "Ranger"]
        numbers = random.randint(100, 9999)
        
        return f"{random.choice(adjectives)}{random.choice(names)}{numbers}"
    
    def generate_password(self):
        length = random.randint(10, 16)
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(characters) for _ in range(length))
    
    def clear_username_placeholder(self, event):
        if self.username_textbox.get() == "Enter Roblox username...":
            self.username_textbox.delete(0, tk.END)
            
    def clear_password_placeholder(self, event):
        if self.password_textbox.get() == "Enter new password...":
            self.password_textbox.delete(0, tk.END)
    
    def clear_ip_placeholder(self, event):
        if self.ip_textbox.get() == "Enter IP address...":
            self.ip_textbox.delete(0, tk.END)
    
    def clear_message_placeholder(self, event):
        if self.message_textbox.get() == "Enter your message...":
            self.message_textbox.delete(0, tk.END)
    
    def clear_all_consoles(self):
        consoles = [self.ddos_console, self.roblox_console, self.vpn_console,
                   self.message_console, self.ip_leak_console, self.console,
                   self.admin_console, self.gmail_console]
        
        for console in consoles:
            console.config(state='normal')
            console.delete(1.0, tk.END)
            console.config(state='disabled')
    
    def fake_network_scan(self):
        self.update_console(self.console, "[Hacker Panel v0.1]: Scanning network...")
        time.sleep(2)
        self.update_console(self.console, "[Hacker Panel v0.1]: Found 5 devices on network")
        
    def fake_port_scan(self):
        self.update_console(self.console, "[Hacker Panel v0.1]: Scanning ports...")
        time.sleep(2)
        self.update_console(self.console, "[Hacker Panel v0.1]: Open ports: 80, 443, 22, 3389")
        
    def fake_password_cracker(self):
        self.update_console(self.console, "[Hacker Panel v0.1]: Cracking password...")
        time.sleep(3)
        self.update_console(self.console, "[Hacker Panel v0.1]: Password found: hunter2")
        
    def show_commands(self):
        self.update_console(self.console, "[Hacker Panel v0.1]: Available commands:")
        self.update_console(self.console, "  help - Show this help message")
        self.update_console(self.console, "  CookieGive - Generate fake Roblox cookies")
        self.update_console(self.console, "  RobloxInfoCookie <cookie> - Get info from cookie")
        self.update_console(self.console, "  stolerobux <username> - Steal robux from user")
        self.update_console(self.console, "  givemerobux - Give yourself infinite robux")
        self.update_console(self.console, "  robloxplayers - Show active Roblox players")
        self.update_console(self.console, "  offinternet - Turn off internet for everyone")
        self.update_console(self.console, "  stealallrobux - Steal all robux from all players")
        
    def show_about(self):
        self.update_console(self.console, "[Hacker Panel v0.1]: Hacker Panel v0.1")
        self.update_console(self.console, "[Hacker Panel v0.1]: Created by c00lVoid_8")
            
    def close_program(self):
        self.root.quit()
        self.root.destroy()
        sys.exit()
        
    def start_ddos(self):
        if self.ddos_active:
            return
            
        url = self.url_textbox.get()
        if url == "Enter target URL..." or not url:
            self.update_console(self.ddos_console, "[Hacker Panel v0.1]: Please enter a URL first!")
            return
            
        # Hide textbox
        self.url_textbox.pack_forget()
        self.ddos_btn.config(state='disabled')
        
        self.ddos_active = True
        self.update_console(self.ddos_console, f"[Hacker Panel v0.1]: Starting DDoS Attack on {url}...")
        
        # Start process in separate thread
        thread = threading.Thread(target=self.ddos_process)
        thread.daemon = True
        thread.start()
        
    def ddos_process(self):
        # Wait 5 seconds
        time.sleep(5)
        
        # Spam Response Code 500
        start_time = time.time()
        while self.ddos_active and (time.time() - start_time) < 10:
            self.update_console(self.ddos_console, "[Hacker Panel v0.1]: Response Code 500")
            time.sleep(0.1)
            
        # Stop spamming
        self.ddos_active = False
        self.update_console(self.ddos_console, "[Hacker Panel v0.1]: Stopped.")
        
        # Restore textbox
        self.root.after(0, self.restore_ddos_controls)
        
    def restore_ddos_controls(self):
        self.url_textbox.pack(side='left', padx=5)
        self.url_textbox.delete(0, tk.END)
        self.url_textbox.insert(0, "Enter target URL...")
        self.ddos_btn.config(state='normal')
        
    def start_roblox_hack(self):
        if self.roblox_active:
            return
            
        username = self.username_textbox.get()
        if username == "Enter Roblox username..." or not username:
            self.update_console(self.roblox_console, "[Hacker Panel v0.1]: Please enter a username first!")
            return
            
        # Hide first textbox
        self.username_textbox.pack_forget()
        self.roblox_btn.pack_forget()
        self.roblox_frame1.pack_forget()
        
        self.roblox_active = True
        self.update_console(self.roblox_console, f"[Hacker Panel v0.1]: Starting Hacking Account for {username}...")
        
        # Start process in separate thread
        thread = threading.Thread(target=self.roblox_process)
        thread.daemon = True
        thread.start()
        
    def roblox_process(self):
        # Wait 3 seconds
        time.sleep(3)
        
        # Spam Hacking...
        for i in range(70):  # approximately 7 seconds with time.sleep(0.1)
            if not self.roblox_active:
                break
            self.update_console(self.roblox_console, "[Hacker Panel v0.1]: Hacking...")
            time.sleep(0.1)
            
        # Spam Changing Cookie Files
        for i in range(70):  # approximately 7 seconds
            if not self.roblox_active:
                break
            self.update_console(self.roblox_console, "[Hacker Panel v0.1]: Changing Cookie Files Of user...")
            time.sleep(0.1)
            
        # Show second textbox
        if self.roblox_active:
            self.root.after(0, self.show_password_input)
            
    def show_password_input(self):
        self.roblox_frame2.pack(pady=5)
        
    def change_password(self):
        password = self.password_textbox.get()
        if password == "Enter new password..." or not password:
            self.update_console(self.roblox_console, "[Hacker Panel v0.1]: Please enter a password!")
            return
            
        # Hide second textbox
        self.password_textbox.pack_forget()
        self.password_btn.pack_forget()
        self.roblox_frame2.pack_forget()
        
        self.update_console(self.roblox_console, f"[Hacker Panel v0.1]: Changing Password user by cookie...")
        
        # Start final step
        thread = threading.Thread(target=self.final_roblox_step)
        thread.daemon = True
        thread.start()
        
    def final_roblox_step(self):
        time.sleep(6)
        self.update_console(self.roblox_console, "[Hacker Panel v0.1]: Hacking Ended you can log in on the user by new password.")
        
        # Reset state
        self.roblox_active = False
        
        # Restore initial elements
        self.root.after(0, self.restore_roblox_controls)
        
    def restore_roblox_controls(self):
        self.roblox_frame1.pack(pady=5)
        self.username_textbox.pack(side='left', padx=5)
        self.username_textbox.delete(0, tk.END)
        self.username_textbox.insert(0, "Enter Roblox username...")
        self.roblox_btn.pack(side='left', padx=5)
    
    def start_vpn_dox(self):
        if self.vpn_active:
            return
            
        self.vpn_active = True
        
        # Change button appearance
        self.vpn_btn.config(text="Collecting data...", state='disabled', bg='gray')
        
        # Start VPN dox process
        thread = threading.Thread(target=self.vpn_dox_process)
        thread.daemon = True
        thread.start()
        
    def vpn_dox_process(self):
        # Simulate data collection
        time.sleep(1)
        self.update_console(self.vpn_console, "[Hacker Panel v0.1]: Username Target: Pensil")
        time.sleep(1)
        self.update_console(self.vpn_console, "[Hacker Panel v0.1]: Password: Youtube Password: ImPakeALove9481")
        time.sleep(1)
        self.update_console(self.vpn_console, "[Hacker Panel v0.1]: New User Target Found!")
        time.sleep(1)
        self.update_console(self.vpn_console, "[Hacker Panel v0.1]: Username Target: Jake")
        time.sleep(1)
        self.update_console(self.vpn_console, "[Hacker Panel v0.1]: Password: Discord Password: JakeLoveAAAAA4235")
        
        # Keep button disabled (gray) as requested
        # No need to re-enable it
        
    def set_ip(self):
        ip = self.ip_textbox.get()
        if ip == "Enter IP address..." or not ip:
            self.update_console(self.message_console, "[Hacker Panel v0.1]: Please enter an IP address!")
            return
            
        self.target_ip = ip
        self.update_console(self.message_console, f"[Hacker Panel v0.1]: IP {ip} set. Enter a text message")
        
        # Hide IP input frame and show message input frame
        self.ip_textbox.master.pack_forget()
        self.message_frame2.pack(pady=5)
        
    def send_message(self):
        message = self.message_textbox.get()
        if message == "Enter your message..." or not message:
            self.update_console(self.message_console, "[Hacker Panel v0.1]: Please enter a message!")
            return
            
        self.update_console(self.message_console, f"[Hacker Panel v0.1]: Sending message to {self.target_ip}: {message}")
        time.sleep(1)
        self.update_console(self.message_console, "[Hacker Panel v0.1]: Sent.")
        
        # Reset message tab
        self.message_frame2.pack_forget()
        self.ip_textbox.master.pack(pady=5)
        self.ip_textbox.delete(0, tk.END)
        self.ip_textbox.insert(0, "Enter IP address...")
        self.message_textbox.delete(0, tk.END)
        self.message_textbox.insert(0, "Enter your message...")
        
    def generate_random_ip(self):
        # Generate random IP addresses
        for _ in range(5):  # Generate 5 random IPs
            ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            self.update_console(self.ip_leak_console, f"[Hacker Panel v0.1]: Leaked IP: {ip}")
            time.sleep(0.5)  # Small delay between IPs
    
    def execute_command(self, event=None):
        command = self.cmd_textbox.get().strip()
        
        if not command:
            return
            
        self.update_console(self.console, f"> {command}")
        self.cmd_textbox.delete(0, tk.END)
        
        parts = command.split()
        cmd = parts[0].lower()
        
        if cmd == "help":
            self.show_commands()
            
        elif cmd == "cookiegive":
            cookies = self.generate_cookie()
            for cookie in cookies:
                self.update_console(self.console, cookie)
                time.sleep(0.1)
                
        elif cmd == "robloxinfocookie" and len(parts) >= 2:
            cookie = parts[1]
            username = self.generate_roblox_username()
            password = self.generate_password()
            robux = random.randint(1, 2000)
            
            self.update_console(self.console, f"[Hacker Panel v0.1]: Username user: {username}")
            self.update_console(self.console, f"[Hacker Panel v0.1]: Password: {password}")
            self.update_console(self.console, f"[Hacker Panel v0.1]: Robux: {robux}")
            
        elif cmd == "stolerobux" and len(parts) >= 2:
            target_user = parts[1]
            self.update_console(self.console, f"[Hacker Panel v0.1]: Enter name to continue.")
            
            # Store target user for later
            self.stolerobux_target = target_user
            
            # Hide command input and show stolerobux input
            self.cmd_textbox.master.pack_forget()
            self.stolerobux_frame.pack(pady=10)
            
        elif cmd == "givemerobux":
            self.update_console(self.console, "[Hacker Panel v0.1]: Giving a infinity robux...")
            
            # Start robux giving process
            thread = threading.Thread(target=self.give_me_robux_process)
            thread.daemon = True
            thread.start()
            
        elif cmd == "robloxplayers":
            self.update_console(self.console, "[Hacker Panel v0.1]: Looking for All players...")
            
            # Start player count process
            thread = threading.Thread(target=self.roblox_players_process)
            thread.daemon = True
            thread.start()
            
        elif cmd == "offinternet":
            self.update_console(self.console, "[Hacker Panel v0.1]: Offing internet for all...")
            
            # Start internet off process
            thread = threading.Thread(target=self.off_internet_process)
            thread.daemon = True
            thread.start()
            
        elif cmd == "stealallrobux":
            self.update_console(self.console, "[Hacker Panel v0.1]: Robux are gived for you! You have 100,000,000 robux!")
            
        else:
            self.update_console(self.console, f"[Hacker Panel v0.1]: Unknown command: {cmd}")
            self.update_console(self.console, "[Hacker Panel v0.1]: Type 'help' for available commands")
    
    def give_me_robux_process(self):
        time.sleep(4)
        self.update_console(self.console, "[Hacker Panel v0.1]: Robux are gived.")
    
    def roblox_players_process(self):
        time.sleep(2)
        self.update_console(self.console, "[Hacker Panel v0.1]: 174,184,491 Active Players on roblox!")
    
    def off_internet_process(self):
        time.sleep(2)
        self.update_console(self.console, "[Hacker Panel v0.1]: For all internet was offed! No for you")
    
    def give_robux(self):
        username = self.stolerobux_textbox.get()
        
        if not username:
            self.update_console(self.console, "[Hacker Panel v0.1]: Please enter a username!")
            return
            
        self.update_console(self.console, f"[Hacker Panel v0.1]: Giving Robux to {username}...")
        
        # Hide stolerobux input and show command input again
        self.stolerobux_frame.pack_forget()
        self.cmd_textbox.master.pack(pady=10)
        
        # Start robux giving process
        thread = threading.Thread(target=self.robux_give_process)
        thread.daemon = True
        thread.start()
        
    def robux_give_process(self):
        time.sleep(4)
        self.update_console(self.console, "[Hacker Panel v0.1]: Robux are gived.")
        
    def update_console(self, console, message):
        def _update():
            console.config(state='normal')
            console.insert(tk.END, message + "\n")
            console.see(tk.END)
            console.config(state='disabled')
        self.root.after(0, _update)

if __name__ == "__main__":
    root = tk.Tk()
    app = HackerPanel(root)
    root.protocol("WM_DELETE_WINDOW", app.close_program)
    root.mainloop()