import tkinter as tk
from tkinter import ttk, messagebox
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import timeit


class FibonacciComparator:
    def __init__(self, master):
        self.master = master
        master.title("Comparateur de Fibonacci")
        master.geometry("900x700")
        master.configure(bg='#f0f0f0')

        # Styles
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))

        # Frame principale
        self.main_frame = ttk.Frame(master, padding="20 10 20 10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Configuration des widgets
        self.create_widgets()

    def fibonacci_recursif(self, n):
        if n <= 1:
            return n
        return self.fibonacci_recursif(n - 1) + self.fibonacci_recursif(n - 2)

    def fibonacci_dynamique(self, n):
        memo = [0] * (n + 1)
        memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

    def fibonacci_iteratif(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def create_widgets(self):
        # Titre
        ttk.Label(self.main_frame, text="Comparateur de Fibonacci - JAOUAD Salah-Eddine",
                  font=('Arial', 16, 'bold')).pack(pady=10)

        # Frame pour les inputs
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(fill=tk.X, pady=10)

        # Label et entrée pour n
        ttk.Label(input_frame, text="Numéro du terme de Fibonacci (n) :").pack(side=tk.LEFT, padx=5)
        self.n_entry = ttk.Entry(input_frame, width=10)
        self.n_entry.pack(side=tk.LEFT, padx=5)
        self.n_entry.insert(0, "30")

        # Label et entrée pour le nombre d'exécutions
        ttk.Label(input_frame, text="Nombre d'exécutions :").pack(side=tk.LEFT, padx=5)
        self.exec_entry = ttk.Entry(input_frame, width=10)
        self.exec_entry.pack(side=tk.LEFT, padx=5)
        self.exec_entry.insert(0, "1000")

        # Bouton de calcul
        ttk.Button(input_frame, text="Calculer", command=self.calculer).pack(side=tk.LEFT, padx=5)

        # Frame des résultats
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Création de la figure matplotlib
        self.figure, self.ax = plt.subplots(figsize=(9, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.result_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

    def calculer(self):
        try:
            n = int(self.n_entry.get())
            executions = int(self.exec_entry.get())

            # Préparation des méthodes et résultats
            methodes = [
                ("Récursif", lambda: self.fibonacci_recursif(n), n <= 30),
                ("Dynamique", lambda: self.fibonacci_dynamique(n), True),
                ("Itératif", lambda: self.fibonacci_iteratif(n), True)
            ]

            resultats = []
            temps_resultats = []

            # Calcul des performances
            for nom, methode, est_applicable in methodes:
                if est_applicable:
                    try:
                        # Utilisation de timeit pour des mesures précises
                        temps = timeit.timeit(methode, number=executions)
                        resultat = methode()
                        resultats.append((nom, resultat, temps / executions))
                        temps_resultats.append(temps / executions)
                    except RecursionError:
                        resultats.append((nom, "Dépassement", 0))
                        temps_resultats.append(0)
                else:
                    resultats.append((nom, "Non applicable", 0))
                    temps_resultats.append(0)

            # Effacer le graphique précédent
            self.ax.clear()

            # Créer un graphique à barres avec une échelle logarithmique
            methodes_noms = [r[0] for r in resultats]
            bars = self.ax.bar(methodes_noms, temps_resultats)
            self.ax.set_ylabel('Temps moyen par exécution (secondes)')
            self.ax.set_title(f'Comparaison des performances (n = {n}, {executions} exécutions)')
            self.ax.set_yscale('log')  # Échelle logarithmique pour mieux voir les différences

            # Coloration des barres
            couleurs = ['red', 'green', 'blue']
            for bar, couleur in zip(bars, couleurs):
                bar.set_color(couleur)

            # Ajouter des étiquettes de valeur sur les barres
            for i, v in enumerate(temps_resultats):
                if v > 0:
                    self.ax.text(i, v, f'{v:.6f}', ha='center', va='bottom')

            # Rafraîchir le canvas
            self.canvas.draw()

            # Afficher les résultats textuels
            self.afficher_resultats(resultats)

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

    def afficher_resultats(self, resultats):
        # Détruire les anciens widgets de résultats s'ils existent
        for widget in self.result_frame.winfo_children():
            if widget != self.canvas_widget:
                widget.destroy()

        # Créer un tableau de résultats
        columns = ('Méthode', 'Résultat', 'Temps moyen (s)')
        tree = ttk.Treeview(self.result_frame, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')

        for resultat in resultats:
            tree.insert('', 'end', values=resultat)

        tree.pack(fill=tk.X, padx=10, pady=10)


def main():
    root = tk.Tk()
    app = FibonacciComparator(root)
    root.mainloop()


if __name__ == "__main__":
    main()