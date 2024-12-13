import tkinter as tk
from tkinter import ttk
import time
import tracemalloc
import statistics


class FibonacciPerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyseur de Performance de Fibonacci - JAOUAD Salah-Eddine")
        self.root.geometry("800x600")

        # Création des méthodes de Fibonacci
        self.methodes = {
            "Récursif": self.fibonacci_recursif,
            "Dynamique": self.fibonacci_dynamique,
            "Iteratif": self.fibonacci_iteratif
        }

        self.creer_interface()

    def fibonacci_recursif(self, n):
        if n <= 1:
            return n
        return self.fibonacci_recursif(n - 1) + self.fibonacci_recursif(n - 2)

    def fibonacci_dynamique(self, n, memo=None):
        if memo is None:
            memo = {}

        if n in memo:
            return memo[n]

        if n <= 1:
            return n

        memo[n] = (self.fibonacci_dynamique(n - 1, memo) +
                   self.fibonacci_dynamique(n - 2, memo))
        return memo[n]

    def fibonacci_iteratif(self, n):
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def mesurer_performance(self, fonction, n, nombre_executions=100):
        """
        Mesure précise des performances
        """
        temps_executions = []
        memoires_utilisees = []

        for _ in range(nombre_executions):
            debut_temps = time.perf_counter()
            tracemalloc.start()

            try:
                resultat = fonction(n)
            except RecursionError:
                return None, None, None, "Dépassement de pile"

            memoire_courante, memoire_pic = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            fin_temps = time.perf_counter()
            temps_execution = (fin_temps - debut_temps) * 1_000_000  # en microsecondes

            temps_executions.append(temps_execution)
            memoires_utilisees.append(memoire_pic)

        temps_moyen = statistics.mean(temps_executions)
        temps_ecart_type = statistics.stdev(temps_executions)
        memoire_moyenne = statistics.mean(memoires_utilisees)

        return resultat, temps_moyen, temps_ecart_type, memoire_moyenne

    def creer_interface(self):

        # Frame de saisie
        frame_saisie = ttk.Frame(self.root, padding="10")
        frame_saisie.pack(fill=tk.X)

        ttk.Label(frame_saisie, text="Entrez la valeur de n :").pack(side=tk.LEFT)

        self.entree_n = tk.Entry(frame_saisie, width=10)
        self.entree_n.pack(side=tk.LEFT, padx=10)

        ttk.Button(frame_saisie, text="Calculer", command=self.analyser_performances).pack(side=tk.LEFT)

        # Tableau des résultats
        self.tree = ttk.Treeview(self.root, columns=(
            "Methode", "Resultat", "Temps Moyen (µs)", "Écart-Type (µs)", "Mémoire (octets)"
        ), show="headings")

        # Configuration des colonnes
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def analyser_performances(self):
        # Nettoyer le tableau précédent
        for i in self.tree.get_children():
            self.tree.delete(i)

        try:
            n = int(self.entree_n.get())
        except ValueError:
            tk.messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide")
            return

        # Exécuter les analyses pour chaque méthode
        for nom_methode, methode in self.methodes.items():
            try:
                resultat, temps_moyen, temps_ecart, memoire = self.mesurer_performance(methode, n)

                # Formater les valeurs numériques
                temps_moyen_formate = f"{temps_moyen:.2f}" if temps_moyen is not None else "N/A"
                temps_ecart_formate = f"{temps_ecart:.2f}" if temps_ecart is not None else "N/A"
                memoire_formate = f"{memoire:.0f}" if memoire is not None else "N/A"

                # Insérer les résultats dans le tableau
                self.tree.insert("", "end", values=(
                    nom_methode,
                    resultat,
                    temps_moyen_formate,
                    temps_ecart_formate,
                    memoire_formate
                ))
            except Exception as e:
                # Gestion des erreurs
                self.tree.insert("", "end", values=(nom_methode, "Erreur", str(e), "", ""))


def main():
    root = tk.Tk()
    app = FibonacciPerformanceApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()