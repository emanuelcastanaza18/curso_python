class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords == coords2)  # False
print(coords != coords2)  # False
