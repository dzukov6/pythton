import tkinter as tk
from tkinter import messagebox
import csv

class ArveteRakendus:
    def __init__(self, root):
        self.root = root
        self.root.title("Arvete Haldamine")

        # Andmestruktuurid
        self.teenused = []
        self.arved = []

        # Lae teenused ja arved failist
        self.lae_andmed()

        # Teenuste raam
        self.teenuste_raam = tk.LabelFrame(root, text="Teenuste Haldamine")
        self.teenuste_raam.pack(padx=10, pady=10, fill="both", expand="yes")

        # Teenuste loendi loomine
        self.teenduste_loend = tk.Listbox(self.teenuste_raam, width=50)
        self.teenduste_loend.pack(side="left", fill="both", expand="yes")

        # Väljad teenuse lisamiseks
        self.nimi_sisend = tk.Entry(self.teenuste_raam)
        self.nimi_sisend.pack()
        self.hind_sisend = tk.Entry(self.teenuste_raam)
        self.hind_sisend.pack()

        # Nupud teenuste lisamiseks, muutmiseks ja kustutamiseks
        self.lisa_nupp = tk.Button(self.teenuste_raam, text="Lisa Teenus", command=self.lisa_teenus)
        self.lisa_nupp.pack(side="left", padx=5)
        self.muuda_nupp = tk.Button(self.teenuste_raam, text="Muuda Teenust", command=self.muuda_teenust)
        self.muuda_nupp.pack(side="left", padx=5)
        self.kustuta_nupp = tk.Button(self.teenuste_raam, text="Kustuta Teenus", command=self.kustuta_teenus)
        self.kustuta_nupp.pack(side="left", padx=5)

        # Arvete raam
        self.arvete_raam = tk.LabelFrame(root, text="Arvete Haldamine")
        self.arvete_raam.pack(padx=10, pady=10, fill="both", expand="yes")

        # Arvete loendi loomine
        self.arvete_loend = tk.Listbox(self.arvete_raam, width=50)
        self.arvete_loend.pack(side="left", fill="both", expand="yes")

        # Nupp arve koostamiseks
        self.koosta_arve_nupp = tk.Button(self.arvete_raam, text="Koosta Arve", command=self.koosta_arve)
        self.koosta_arve_nupp.pack()

        # Lae teenused ja arved
        self.uuenda_teenuste_loend()
        self.uuenda_arvete_loend()

    def lisa_teenus(self):
        nimi = self.nimi_sisend.get()
        hind = self.hind_sisend.get()
        if nimi and hind:
            self.teenused.append({"nimi": nimi, "hind": hind})
            self.uuenda_teenuste_loend()
            self.nimi_sisend.delete(0, tk.END)
            self.hind_sisend.delete(0, tk.END)
            self.salvesta_andmed()
        else:
            messagebox.showwarning("Hoiatus", "Palun täida kõik väljad!")

    def muuda_teenust(self):
        valitud_indeks = self.teenduste_loend.curselection()
        if valitud_indeks:
            valitud_indeks = int(valitud_indeks[0])
            nimi = self.nimi_sisend.get()
            hind = self.hind_sisend.get()
            if nimi and hind:
                self.teenused[valitud_indeks] = {"nimi": nimi, "hind": hind}
                self.uuenda_teenuste_loend()
                self.nimi_sisend.delete(0, tk.END)
                self.hind_sisend.delete(0, tk.END)
                self.salvesta_andmed()
            else:
                messagebox.showwarning("Hoiatus", "Palun täida kõik väljad!")
        else:
            messagebox.showwarning("Hoiatus", "Palun vali teenus!")

    def kustuta_teenus(self):
        valitud_indeks = self.teenduste_loend.curselection()
        if valitud_indeks:
            valitud_indeks = int(valitud_indeks[0])
            del self.teenused[valitud_indeks]
            self.uuenda_teenuste_loend()
            self.salvesta_andmed()
        else:
            messagebox.showwarning("Hoiatus", "Palun vali teenus!")

    def koosta_arve(self):
        valitud_indeksid = self.teenduste_loend.curselection()
        if valitud_indeksid:
            teenused_arvele = [self.teenused[int(i)] for i in valitud_indeksid]
            kogusumma = sum(float(teenus["hind"]) for teenus in teenused_arvele)
            self.arved.append({"teenused": teenused_arvele, "summa": kogusumma})
            self.uuenda_arvete_loend()
            self.salvesta_andmed()
        else:
            messagebox.showwarning("Hoiatus", "Palun vali vähemalt üks teenus!")

    def uuenda_teenuste_loend(self):
        self.teenduste_loend.delete(0, tk.END)
        for teenus in self.teenused:
            self.teenduste_loend.insert(tk.END, f"{teenus['nimi']} - {teenus['hind']} €")

    def uuenda_arvete_loend(self):
        self.arvete_loend.delete(0, tk.END)
        for arve in self.arved:
            teenused_str = ", ".join([teenus["nimi"] for teenus in arve["teenused"]])
            self.arvete_loend.insert(tk.END, f"Teenused: {teenused_str}, Summa: {arve['summa']} €")

    def salvesta_andmed(self):
        with open("andmed.csv", "w", newline="") as csvfile:
            fieldnames = ["nimi", "hind"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for teenus in self.teenused:
                writer.writerow(teenus)

    def lae_andmed(self):
        try:
            with open("andmed.csv", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.teenused.append(row)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ArveteRakendus(root)
    root.mainloop()
