import tkinter as tk
from tkinter import messagebox

class ArveldusRakendus:
    def __init__(self, root):
        self.root = root
        self.root.title("Teenusepõhine Arveldussüsteem")
        self.teenused = {}
        self.arved = {}
        
        self.lisa_teenus_nupp = tk.Button(self.root, text="Lisa Teenus", command=self.lisa_teenus)
        self.lisa_teenus_nupp.pack()
        
        self.koosta_arve_nupp = tk.Button(self.root, text="Koosta Arve", command=self.koosta_arve)
        self.koosta_arve_nupp.pack()

        self.loe_andmed()
        
    def lisa_teenus(self):
        lisa_aken = tk.Toplevel(self.root)
        lisa_aken.title("Lisa Teenus")
        
        tk.Label(lisa_aken, text="Teenuse Kirjeldus:").pack()
        kirjeldus_sisend = tk.Entry(lisa_aken)
        kirjeldus_sisend.pack()
        
        tk.Label(lisa_aken, text="Teenuse Hind:").pack()
        hind_sisend = tk.Entry(lisa_aken)
        hind_sisend.pack()
        
        tk.Button(lisa_aken, text="Lisa", command=lambda: self.salvesta_teenus(kirjeldus_sisend.get(), hind_sisend.get())).pack()
        
    def salvesta_teenus(self, kirjeldus, hind):
        if kirjeldus and hind:
            teenus_id = max(self.teenused.keys(), default=0) + 1
            self.teenused[teenus_id] = {"kirjeldus": kirjeldus, "hind": hind}
            self.salvesta_andmed()
            messagebox.showinfo("Teenus Lisatud", "Teenus on edukalt lisatud!")
        else:
            messagebox.showerror("Viga", "Palun täitke kõik väljad!")
    
    def koosta_arve(self):
        valitud_teenused = []
        for teenus_id, teenus in self.teenused.items():
            valitud_teenused.append(f"{teenus_id}: {teenus['kirjeldus']} - {teenus['hind']} EUR")
        
        koosta_arve_aken = tk.Toplevel(self.root)
        koosta_arve_aken.title("Koosta Arve")
        
        tk.Label(koosta_arve_aken, text="Vali Teenused:").pack()
        teenuste_valik = tk.Listbox(koosta_arve_aken, selectmode=tk.MULTIPLE)
        for teenus in valitud_teenused:
            teenuste_valik.insert(tk.END, teenus)
        teenuste_valik.pack()
        
        tk.Button(koosta_arve_aken, text="Koosta", command=lambda: self.salvesta_arve(teenuste_valik.curselection())).pack()
    
    def salvesta_arve(self, valitud_teenused):
        if valitud_teenused:
            teenused_arvele = []
            summa = 0
            for index in valitud_teenused:
                teenus_id = int(index) + 1
                teenus = self.teenused[teenus_id]
                summa += float(teenus["hind"])
                teenused_arvele.append(teenus)
            self.arved[max(self.arved.keys(), default=0) + 1] = {"teenused": teenused_arvele, "summa": summa}
            messagebox.showinfo("Arve Koostatud", f"Arve summa: {summa} EUR")
        else:
            messagebox.showerror("Viga", "Valige vähemalt üks teenus!")
    
    def salvesta_andmed(self):
        with open("andmed.txt", "w") as f:
            for teenus_id, teenus in self.teenused.items():
                f.write("{},{},{}\n".format(teenus_id, teenus['kirjeldus'], teenus['hind']))
            
    def loe_andmed(self):
        try:
            with open("andmed.txt", "r") as f:
                for line in f:
                    teenus_id, kirjeldus, hind = line.strip().split(",")
                    self.teenused[int(teenus_id)] = {"kirjeldus": kirjeldus, "hind": hind}
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    rakendus = ArveldusRakendus(root)
    root.mainloop()
