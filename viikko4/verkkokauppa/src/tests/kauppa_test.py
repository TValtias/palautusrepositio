import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            return 10

        def varasto_hae_tuote(tuote_id):
            tuotteet = {
                1: Tuote(1, "maito", 5),
                2: Tuote(2, "leipä", 3),
                3: Tuote(3, "juusto", 7),
            }
            return tuotteet[tuote_id]

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.pankki_mock = pankki_mock
        self.varasto_mock = varasto_mock
        self.viitegeneraattori_mock = viitegeneraattori_mock
        self.kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        self.asiakas = "pekka"
        self.tilinumero = "12345"

    def test_aloita_asiointi_nollaa_edelliset_ostokset(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, 42, self.tilinumero, "33333-44455", 0
        )

    def test_jokainen_maksu_pyytaa_uuden_viitenumeron(self):
        self.viitegeneraattori_mock.uusi.side_effect = [101, 202]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list[0][0][1], 101
        )
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list[1][0][1], 202
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, 42, self.tilinumero, "33333-44455", 5
        )

    def test_ostos_voidaan_poistaa_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.varasto_mock.palauta_varastoon.assert_called_once_with(
            Tuote(1, "maito", 5)
        )
        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, 42, self.tilinumero, "33333-44455", 3
        )

    def test_kahden_eri_tuotteen_ostos_maksaa_yhteishinnan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, 42, self.tilinumero, "33333-44455", 8
        )

    def test_kahden_saman_tuotteen_ostos_maksaa_yhteishinnan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, 42, self.tilinumero, "33333-44455", 14
        )

    def test_loppuunmyytya_tuotetta_ei_lasketa_mukaan_maksuun(self):
        self.varasto_mock.saldo.side_effect = lambda tuote_id: 0 if tuote_id == 2 else 10

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.asiakas, self.tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, 42, self.tilinumero, "33333-44455", 5
        )
