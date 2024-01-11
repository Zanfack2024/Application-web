import math

class Point:
    def init(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def calculer_distance(self, autre_point):
        distance = math.sqrt((autre_point.x - self.x)**2 + (autre_point.y - self.y)**2)
        return distance

# Exemple d'utilisation
point_A = Point(1, 2)
point_B = Point(4, 6)

point_A.afficher()
point_B.afficher()

distance_AB = point_A.calculer_distance(point_B)
print(f"Distance entre les points A et B : {distance_AB}")