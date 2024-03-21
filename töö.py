import tkinter as tk
from tkinter import messagebox

class ArveldusRakendus:
    def __init__(self, root):
        # Algatame rakenduse
        self.root = root
        self.root.title("Teenusepõhine Arveldussüsteem")  # Määrame põhiakna pealkirja
        self.teenused = {}  # Sõnastik teenuste salvestamiseks
        self.arved = {}     # Sõnastik arvete salvestamiseks
        
        # Loome nupud teenuste lisamiseks ja arve koostamiseks
        self.lisa_teenus_nupp = tk.Button(self.root, text="Lisa Teenus", command=self.lisa_teenus)
        self.lisa_teenus_nupp.pack()
        
        self.koosta_arve_nupp = tk.Button(self.root, text="Koosta Arve", command=self.koosta_arve)
        self.koosta_arve_nupp.pack()

        # Laeme olemasolevad andmed
        self.loe_andmed()
        
    def lisa_teenus(self):
        # Meetod teenuse lisamiseks
        lisa_aken = tk.Toplevel(self.root)  # Loome uue akna teenuse lisamiseks
        lisa_aken.title("Lisa Teenus")      # Määrame akna pealkirja
        
        # Sildid ja tekstiväljad teenuse kirjelduse ja hinna sisestamiseks
        tk.Label(lisa_aken, text="Teenuse Kirjeldus:").pack()
        kirjeldus_sisend = tk.Entry(lisa_aken)
        kirjeldus_sisend.pack()
        
        tk.Label(lisa_aken, text="Teenuse Hind:").pack()
        hind_sisend = tk.Entry(lisa_aken)
        hind_sisend.pack()
        
        # Nupp teenuse salvestamiseks
        tk.Button(lisa_aken, text="Lisa", command=lambda: self.salvesta_teenus(kirjeldus_sisend.get(), hind_sisend.get())).pack()
        
    def salvesta_teenus(self, kirjeldus, hind):
        # Meetod teenuse salvestamiseks
        if kirjeldus and hind:  # Kontrollime, kas nii kirjeldus kui ka hind on sisestatud
            teenus_id = max(self.teenused.keys(), default=0) + 1  # Genereerime unikaalse ID teenusele
            self.teenused[teenus_id] = {"kirjeldus": kirjeldus, "hind": hind}  # Salvestame teenuse sõnastikku
            self.salvesta_andmed()  # Uuendame andmefaili
            messagebox.showinfo("Teenus Lisatud", "Teenus on edukalt lisatud!")  # Näitame teavitust edukast salvestamisest
        else:
            messagebox.showerror("Viga", "Palun täitke kõik väljad!")  # Näitame veateadet, kui mõni väli on täitmata
    
    def koosta_arve(self):
        # Meetod arve koostamiseks
        valitud_teenused = []
        for teenus_id, teenus in self.teenused.items():
            valitud_teenused.append(f"{teenus_id}: {teenus['kirjeldus']} - {teenus['hind']} EUR")
        
        koosta_arve_aken = tk.Toplevel(self.root)  # Loome uue akna arve koostamiseks
        koosta_arve_aken.title("Koosta Arve")     # Määrame akna pealkirja
        
        # Listbox valitud teenuste valimiseks
        tk.Label(koosta_arve_aken, text="Vali Teenused:").pack()
        teenuste_valik = tk.Listbox(koosta_arve_aken, selectmode=tk.MULTIPLE)
        for teenus in valitud_teenused:
            teenuste_valik.insert(tk.END, teenus)
        teenuste_valik.pack()
        
        # Nupp arve koostamiseks
        tk.Button(koosta_arve_aken, text="Koosta", command=lambda: self.salvesta_arve(teenuste_valik.curselection())).pack()
    
    def salvesta_arve(self, valitud_teenused):
        # Meetod arve salvestamiseks
        if valitud_teenused:  # Kontrollime, kas vähemalt üks teenus on valitud
            teenused_arvele = []
            summa = 0
            for index in valitud_teenused:
                teenus_id = int(index) + 1
                teenus = self.teenused[teenus_id]
                summa += float(teenus["hind"])
                teenused_arvele.append(teenus)
            self.arved[max(self.arved.keys(), default=0) + 1] = {"teenused": teenused_arvele, "summa": summa}  # Salvestame arve
            messagebox.showinfo("Arve Koostatud", f"Arve summa: {summa} EUR")  # Näitame kogusummat
        else:
            messagebox.showerror("Viga", "Valige vähemalt üks teenus!")  # Näitame veateadet, kui ühtegi teenust ei ole valitud
    
    def salvesta_andmed(self):
        # Meetod andmete salvestamiseks faili
        with open("andmed.txt", "w") as f:
            for teenus_id, teenus in self.teenused.items():
                f.write("{},{},{}\n".format(teenus_id, teenus['kirjeldus'], teenus['hind']))
            
    def loe_andmed(self):
        # Meetod andmete lugemiseks failist
        try:
            with open("andmed.txt", "r") as f:
                for line in f:
                    teenus_id, kirjeldus, hind = line.strip().split(",")
                    self.teenused[int(teenus_id)] = {"kirjeldus": kirjeldus, "hind": hind}
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()                    # Loome põhiakna
    rakendus = ArveldusRakendus(root)  # Loome rakenduse eksemplari
    root.mainloop()                   # Alustame Tkinteri sündmustsükli tööd
