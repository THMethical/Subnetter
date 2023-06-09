import tkinter as tk
import ipaddress

class SubnetCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Subnetter")

        # IP Address Label and Entry
        self.ip_label = tk.Label(master, text="IP Address:")
        self.ip_label.grid(row=0, column=0, padx=5, pady=5)
        self.ip_entry = tk.Entry(master)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        # Number of Subnets Label and Drop-down
        self.subnet_label = tk.Label(master, text="Number of Subnets:")
        self.subnet_label.grid(row=1, column=0, padx=5, pady=5)
        self.subnet_choices = [2**i for i in range(1, 9)]
        self.subnet_var = tk.StringVar(master)
        self.subnet_var.set(self.subnet_choices[0])
        self.subnet_dropdown = tk.OptionMenu(master, self.subnet_var, *self.subnet_choices)
        self.subnet_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Subnet Mask Label and Drop-down
        self.mask_label = tk.Label(master, text="Subnet Mask:")
        self.mask_label.grid(row=2, column=0, padx=5, pady=5)
        self.mask_choices = ['255.255.255.0', '255.255.0.0', '255.0.0.0']
        self.mask_var = tk.StringVar(master)
        self.mask_var.set(self.mask_choices[0])
        self.mask_dropdown = tk.OptionMenu(master, self.mask_var, *self.mask_choices)
        self.mask_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Calculate Button
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Subnets Listbox
        self.subnet_listbox = tk.Listbox(master, width=40)
        self.subnet_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Example Label
        self.example_label = tk.Label(master, text="Example: Enter '192.168.1.0/24' for IP Address, select '4' for Number of Subnets")
        self.example_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def calculate(self):
        ip_addr = self.ip_entry.get()
        num_subnets = int(self.subnet_var.get())
        selected_netmask = self.mask_var.get()

        subnets = list(ipaddress.ip_network(ip_addr).subnets(prefixlen_diff=num_subnets))
        subnets_with_netmask = [(str(subnet), selected_netmask) for subnet in subnets]

        self.subnet_listbox.delete(0, tk.END)

        for subnet, netmask in subnets_with_netmask:
            self.subnet_listbox.insert(tk.END, f"{subnet}/{netmask}")

root = tk.Tk()
subnet_calculator = SubnetCalculator(root)
root.mainloop()
