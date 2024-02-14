from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys

class CharacterSelectionWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Sélectionnez un personnage")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #2c3e50; color: white;")

        layout = QVBoxLayout()

        # Création des boutons pour sélectionner le personnage
        self.character_buttons = []
        for i in range(1, 4):  # Changez le nombre de personnages si nécessaire
            button = QPushButton(f"Personnage {i}")
            button.setStyleSheet("background-color: #34495e; color: white; border-radius: 5px;")
            button.clicked.connect(lambda _, character=i: self.openCharacterStats(character))
            self.character_buttons.append(button)
            layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        central_widget.setStyleSheet("background-color: #2c3e50; color: white;")
        self.setCentralWidget(central_widget)

    def openCharacterStats(self, character):
        self.character_stats_window = CharacterStatsWindow(character)
        self.character_stats_window.show()
        self.close()


class CharacterStatsWindow(QMainWindow):
    def __init__(self, character, parent=None):
        super().__init__(parent)

        self.setWindowTitle(f"Stats en radar de Personnage {character}")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #2c3e50; color: #2c3e50;")

        self.initUI(character)

    def initUI(self, character):
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #2c3e50; color: #2c3e50;")
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        # Création du tableau pour afficher les statistiques
        self.stats_table = QTableWidget()
        self.stats_table.setColumnCount(3)
        self.stats_table.setHorizontalHeaderLabels(["Statistique", "Valeur", "Description"])
        self.stats_table.setStyleSheet("background-color: #2c3e50; color: #2c3e50; gridline-color: #2c3e50;")

        # Définir la couleur de fond des titres de colonne et de ligne
        self.stats_table.horizontalHeader().setStyleSheet("background-color: #34495e; color: #2c3e50;")
        self.stats_table.verticalHeader().setStyleSheet("background-color: #34495e; color: #2c3e50;")

        # Création du graphique en radar pour afficher les statistiques
        self.radar_canvas = RadarCanvas()

        # Ajout des widgets au layout
        layout.addWidget(self.stats_table)
        layout.addWidget(self.radar_canvas)

        # Mise à jour des statistiques et du graphique radar
        self.updateStats(character)

    def updateStats(self, character):
        # Exemple de données de statistiques pour les personnages (à remplacer par vos données réelles)
        stats_data = [
            ("Force", 80, "Capacité de porter des objets lourds"),
            ("Agilité", 65, "Capacité à se déplacer rapidement"),
            ("Intelligence", 90, "Capacité à comprendre et apprendre"),
            ("Endurance", 75, "Capacité à résister à la fatigue"),
            ("Charisme", 85, "Capacité à influencer les autres")
        ]

        # Met à jour le tableau avec les statistiques du personnage sélectionné
        self.stats_table.setRowCount(len(stats_data))
        for i, (stat, value, description) in enumerate(stats_data):
            self.stats_table.setItem(i, 0, QTableWidgetItem(stat))
            self.stats_table.setItem(i, 1, QTableWidgetItem(str(value)))
            self.stats_table.setItem(i, 2, QTableWidgetItem(description))
            for j in range(3):  # Changer la couleur du texte dans chaque cellule du tableau
                self.stats_table.item(i, j).setForeground(Qt.white)

        # Met à jour le graphique en radar avec les statistiques du personnage sélectionné
        self.radar_canvas.plot(character, stats_data)


class RadarCanvas(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
        super().__init__(self.fig)
        self.ax.set_ylim(0, 100)  # Réglage de la limite de l'axe y
        self.ax.set_yticks(np.arange(0, 101, 20))  # Réglage des marques de l'axe y

    def plot(self, character, stats_data):
        stats = [value for _, value, _ in stats_data]  # Récupération des valeurs des statistiques
        labels = [stat for stat, _, _ in stats_data]  # Récupération des noms des statistiques

        # Création des angles pour les différentes statistiques
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

        # Fermer le polygone
        stats = np.concatenate((stats, [stats[0]]))
        angles += angles[:1]

        # Tracer le radar
        self.ax.clear()
        self.ax.plot(angles, stats, 'o-', linewidth=2, color='#ff5733')  # Couleur orange
        self.ax.fill(angles, stats, alpha=0.25, color='#ffab66')  # Remplissage orange clair
        self.ax.set_yticklabels([])  # Supprimer les étiquettes de l'axe y
        self.ax.set_xticks(angles[:-1])
        self.ax.set_xticklabels(labels, color='white')  # Couleur blanche pour les étiquettes
        self.ax.set_title(f"Stats en radar de Personnage {character}", size=14, color='white')  # Couleur blanche pour le titre
        self.ax.set_facecolor('#2c3e50')  # Fond gris foncé pour le graphique
        self.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CharacterSelectionWindow()
    window.show()
    sys.exit(app.exec_())
