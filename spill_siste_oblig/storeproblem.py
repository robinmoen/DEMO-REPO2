from turtle import tiltangle


class Verden:
    def __init__(self, rutenett):
        self._rutenett = rutenett

    def hoyde(self):
        return len(self._rutenett)

    def bredde(self):
        return len(self._rutenett[0])

    def er_gyldig_rute(self, y, x):
        if y < self.hoyde() and x < self.bredde() \
            and y >= 0 and x >= 0:
            return True 
        return False

    def gyldige_naboer(self, y, x):
        naboer = []

        for diff_x in [-1, 0, 1]:
            for diff_y in [-1, 0, 1]:
                ny_x = x + diff_x
                ny_y = y + diff_y

                # ikke ta med egne ruter
                if ny_x == x and ny_y == y:
                    continue 

                # sjekk hjørner
                if abs(diff_x) + abs(diff_y) %2 != 0:
                    continue 

                if self.er_gyldig_rute(ny_y, ny_x):
                    naboer.append((ny_y, ny_x))

class Pathfinder:
    def __init__(self, verden, til, fra):
        self._verden = verden
        self._til = til
        self._fra = fra
        self._aktive_ruter = {fra}
        self._sjekket = set()

    def sjekk_om_finnes_sti(self):
        while len(self._aktive_ruter) > 0:
            sjekk_neste_gang = set()
            for aktiv_rute in self._aktive_ruter:
                self.sjekket.add(aktiv_rute)
                for rute_rundt in self._verden.gyldige_naboer(aktiv_rute):

        


def eksempel():
    rutenett = [
    
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

def test_opprett_verden():
    verden = Verden(rutenett)
    assert verden.hoyde() == 4
    assert verden.bredde() == 3
    assert not verden.er_gyldig_rute(1, 3)
    assert not verden.er_gyldig_rute(-1, 3)
    assert not verden.er_gyldig_rute(1, 3)
