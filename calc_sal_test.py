import unittest
import calc_sal_code as m

class salaire_test(unittest.TestCase):

    def test_sal_archi(self):
        self.assertEqual(m.calculer_salaire("architecte", "12"), "4400")

    def test_sal_medec(self):
        self.assertEqual(m.calculer_salaire("medecin", "15"), "7000")

    def test_sal_consu(self):
        self.assertEqual(m.calculer_salaire("consultant", "6"), "3000")



if __name__ == '__name__':
    unittest.main()