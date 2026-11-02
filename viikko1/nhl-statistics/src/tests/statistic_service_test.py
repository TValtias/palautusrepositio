import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_loytaa_pelaajan(self):
        pelaaja = self.stats.search("Lemieux")

        self.assertEqual(pelaaja.name, "Lemieux")

    def test_loytaa_maalien_maaran(self):
        pelaajan_maalit = self.stats.search("Kurri")

        self.assertEqual(pelaajan_maalit.goals, 37)

    def test_pelaajaa_ei_ole(self):
        pelaaja = self.stats.search("Hihi")

        self.assertIsNone(pelaaja)

    def test_loytaa_tiimin_maaran(self):
        pelaajat = self.stats.team("EDM")

        self.assertEqual(len(pelaajat), 3)

    def test_joukkuetta_ei_ole(self):
        pelaajat = self.stats.team("Kaalitjyrää")

        self.assertEqual(len(pelaajat), 0)

    def test_loytaa_parhaat_pelaajat(self):
        tulos = self.stats.top(3)

        self.assertEqual(tulos[0].name, "Gretzky")
        self.assertEqual(tulos[1].name, "Lemieux")
        self.assertEqual(tulos[2].name, "Yzerman")