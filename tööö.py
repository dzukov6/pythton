import tkinter as tk
from tkinter import messagebox, ttk
import csv

class ServiceManager:
    def __init__(self, filename='services.csv'):
        self.filename = filename
        self.services = self.load_services()
    
    def load_services(self):
        services = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    services.append(row)
        except FileNotFoundError:
            pass
        return services
    
    def save_services(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'description', 'price'])
            writer.writeheader()
            for service in self.services:
                writer.writerow(service)
    
    def add_service(self, name, description, price):
        self.services.append({'name': name, 'description': description, 'price': price})
        self.save_services()

    def update_service(self, index, name, description, price):
        self.services[index] = {'name': name, 'description': description, 'price': price}
        self.save_services()

    def delete_service(self, index):
        self.services.pop(index)
        self.save_services()

class InvoiceManager:
    def __init__(self, filename='invoices.csv'):
        self.filename = filename
        self.invoices = self.load_invoices()
    
    def load_invoices(self):
        invoices = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['services'] = eval(row['services'])
                    invoices.append(row)
        except FileNotFoundError:
            pass
        return invoices
    
    def save_invoices(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['client', 'services', 'total'])
            writer.writeheader()
            for invoice in self.invoices:
                writer.writerow(invoice)
    
    def add_invoice(self, client, services):
        total = sum(float(service['price']) for service in services)
        self.invoices.append({'client': client, 'services': services, 'total': total})
        self.save_invoices()

    def update_invoice(self, index, client, services):
        total = sum(float(service['price']) for service in services)
        self.invoices[index] = {'client': client, 'services': services, 'total': total}
        self.save_invoices()

    def delete_invoice(self, index):
        self.invoices.pop(index)
        self.save_invoices()

class App:
    def __init__(self, root):
        self.root = root
        self.service_manager = ServiceManager()
        self.invoice_manager = InvoiceManager()
        self.setup_ui()

    def setup_ui(self):
        self.tab_control = ttk.Notebook(self.root)
        
        self.service_tab = ttk.Frame(self.tab_control)
        self.invoice_tab = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.service_tab, text='Teenuste Haldamine')
        self.tab_control.add(self.invoice_tab, text='Arvete Haldamine')
        self.tab_control.pack(expand=1, fill="both")
        
        self.setup_service_tab()
        self.setup_invoice_tab()
    
    def setup_service_tab(self):
        self.service_list = tk.Listbox(self.service_tab, selectmode=tk.SINGLE)
        self.service_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.update_service_list()
        
        self.service_details = ttk.Frame(self.service_tab)
        self.service_details.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        tk.Label(self.service_details, text="Nimi").pack()
        self.service_name = tk.Entry(self.service_details)
        self.service_name.pack()
        
        tk.Label(self.service_details, text="Kirjeldus").pack()
        self.service_description = tk.Entry(self.service_details)
        self.service_description.pack()
        
        tk.Label(self.service_details, text="Hind").pack()
        self.service_price = tk.Entry(self.service_details)
        self.service_price.pack()
        
        self.add_service_button = tk.Button(self.service_details, text="Lisa Teenus", command=self.add_service)
        self.add_service_button.pack()
        
        self.update_service_button = tk.Button(self.service_details, text="Uuenda Teenus", command=self.update_service)
        self.update_service_button.pack()
        
        self.delete_service_button = tk.Button(self.service_details, text="Kustuta Teenus", command=self.delete_service)
        self.delete_service_button.pack()
        
        self.service_list.bind('<<ListboxSelect>>', self.load_service_details)

    def setup_invoice_tab(self):
        self.invoice_list = tk.Listbox(self.invoice_tab, selectmode=tk.SINGLE)
        self.invoice_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.update_invoice_list()
        
        self.invoice_details = ttk.Frame(self.invoice_tab)
        self.invoice_details.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        tk.Label(self.invoice_details, text="Klient").pack()
        self.invoice_client = tk.Entry(self.invoice_details)
        self.invoice_client.pack()
        
        tk.Label(self.invoice_details, text="Teenused").pack()
        self.invoice_services = tk.Listbox(self.invoice_details, selectmode=tk.MULTIPLE)
        self.invoice_services.pack()
        self.update_invoice_services_list()
        
        self.add_invoice_button = tk.Button(self.invoice_details, text="Lisa Arve", command=self.add_invoice)
        self.add_invoice_button.pack()
        
        self.update_invoice_button = tk.Button(self.invoice_details, text="Uuenda Arve", command=self.update_invoice)
        self.update_invoice_button.pack()
        
        self.delete_invoice_button = tk.Button(self.invoice_details, text="Kustuta Arve", command=self.delete_invoice)
        self.delete_invoice_button.pack()
        
        self.invoice_list.bind('<<ListboxSelect>>', self.load_invoice_details)

    def update_service_list(self):
        self.service_list.delete(0, tk.END)
        for service in self.service_manager.services:
            self.service_list.insert(tk.END, service['name'])

    def load_service_details(self, event):
        selection = self.service_list.curselection()
        if selection:
            index = selection[0]
            service = self.service_manager.services[index]
            self.service_name.delete(0, tk.END)
            self.service_name.insert(0, service['name'])
            self.service_description.delete(0, tk.END)
            self.service_description.insert(0, service['description'])
            self.service_price.delete(0, tk.END)
            self.service_price.insert(0, service['price'])

    def add_service(self):
        name = self.service_name.get()
        description = self.service_description.get()
        price = self.service_price.get()
        self.service_manager.add_service(name, description, price)
        self.update_service_list()

    def update_service(self):
        selection = self.service_list.curselection()
        if selection:
            index = selection[0]
            name = self.service_name.get()
            description = self.service_description.get()
            price = self.service_price.get()
            self.service_manager.update_service(index, name, description, price)
            self.update_service_list()

    def delete_service(self):
        selection = self.service_list.curselection()
        if selection:
            index = selection[0]
            self.service_manager.delete_service(index)
            self.update_service_list()

    def update_invoice_list(self):
        self.invoice_list.delete(0, tk.END)
        for invoice in self.invoice_manager.invoices:
            self.invoice_list.insert(tk.END, invoice['client'])

    def load_invoice_details(self, event):
        selection = self.invoice_list.curselection()
        if selection:
            index = selection[0]
            invoice = self.invoice_manager.invoices[index]
            self.invoice_client.delete(0, tk.END)
            self.invoice_client.insert(0, invoice['client'])
            self.invoice_services.selection_clear(0, tk.END)
            for service in invoice['services']:
                idx = self.get_service_index(service['name'])
                if idx is not None:
                    self.invoice_services.selection_set(idx)

    def add_invoice(self):
        client = self.invoice_client.get()
        selected_services = self.invoice_services.curselection()
        services = [self.service_manager.services[i] for i in selected_services]
        self.invoice_manager.add_invoice(client, services)
        self.update_invoice_list()

    def update_invoice(self):
        selection = self.invoice_list.curselection()
        if selection:
            index = selection[0]
            client = self.invoice_client.get()
            selected_services = self.invoice_services.curselection()
            services = [self.service_manager.services[i] for i in selected_services]
            self.invoice_manager.update_invoice(index, client, services)
            self.update_invoice_list()

    def delete_invoice(self):
        selection = self.invoice_list.curselection()
        if selection:
            index = selection[0]
            self.invoice_manager.delete_invoice(index)
            self.update_invoice_list()

    def update_invoice_services_list(self):
        self.invoice_services.delete(0, tk.END)
        for service in self.service_manager.services:
            self.invoice_services.insert(tk.END, service['name'])

    def get_service_index(self, name):
        for index, service in enumerate(self.service_manager.services):
            if service['name'] == name:
                return index
        return None

def main():
    root = tk.Tk()
    root.title("Arve Halduse Rakendus")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
