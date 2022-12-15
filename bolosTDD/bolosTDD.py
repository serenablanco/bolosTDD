import unittest
from bolos import *


class TestBolos(unittest.TestCase):
    
    def test_puntuacion_inicial(self):
        
        b = Bolos()
        
        self.assertEqual(b.puntuacion_inicial, 0)
        
    
    def test_puntos_partida(self):

        self.bolos_rondas = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 0)
        
    def test_puntos_partida_8(self):
        
        self.bolos_rondas = [(5, 0), (0, 0), (3, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 8)
        
    def test_puntos_partida_23(self):
        
        self.bolos_rondas = [(5, 0), (9, 0), (3, 0), (0, 0), (0, 6), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 23)
        
    def puntos_partida_TDD(self, bolos_rondas):
        b = Bolos()
        self.puntos = b.puntos_partida(bolos_rondas)
        return self.puntos
    
    def test_puntos_partida_11_rondas(self):
        
        b = Bolos()
        self.bolos_rondas = [(5, 0), (9, 0), (3, 0), (0, 0), (0, 6), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoMaximoRondas):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_12_rondas(self):
        
        b = Bolos()
        self.bolos_rondas = [(5, 0), (9, 0), (3, 0), (0, 0), (0, 6), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoMaximoRondas):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_8_rondas(self):
        
        b = Bolos()
        self.bolos_rondas = [(5, 0), (9, 0), (3, 0), (0, 0), (0, 6), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoMinimoRondas):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_12_bolos_en_una_ronda(self):
        b = Bolos()
        self.bolos_rondas = [(12, 0), (0, 0), (3, 0), (0, 0), (0, 5), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoNumBolos):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_13_bolos_en_una_ronda(self):
        b = Bolos()
        self.bolos_rondas = [(7, 1), (0, 0), (3, 0), (0, 0), (0, 5), (0, 0), (4, 9), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoNumBolos):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_bolos_negativos(self):
        b = Bolos()
        self.bolos_rondas = [(-2, 1), (0, 0), (3, 0), (0, 0), (0, 5), (0, 0), (4, 1), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcBolosNegativos):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_bolos_negativos2(self):
        b = Bolos()
        self.bolos_rondas = [(2, 1), (0, 0), (3, 0), (0, -7), (0, 5), (0, 0), (4, 1), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcBolosNegativos):
            self.puntos = b.puntos_partida(self.bolos_rondas)

    def test_solo_una_bola_no_pleno(self):
        
        b = Bolos()
        self.bolos_rondas = [(7, ), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoNumBolasRonda):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_3_bolas_ronda(self):
        b = Bolos()
        self.bolos_rondas = [(2, 1, 0), (0, 0), (3, 0), (0, 7), (0, 5), (0, 0), (4, 1), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoNumBolasRonda):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_4_bolas_ronda(self):
        b = Bolos()
        self.bolos_rondas = [(2, 1, 0, 1), (0, 0), (3, 0), (0, 7), (0, 5), (0, 0), (4, 1), (0, 0), (0, 0), (0, 0)]
        
        with self.assertRaises(ExcedidoNumBolasRonda):
            self.puntos = b.puntos_partida(self.bolos_rondas)
            
    def test_puntos_partida_pleno(self):
        
        self.bolos_rondas = [(10, ), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 10)
        
    def test_puntos_partida_pleno_2(self):
        
        self.bolos_rondas = [(10, ), (5, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 20)
        
    def test_puntos_partida_pleno_3(self):
        
        self.bolos_rondas = [(10, ), (5, 2), (0, 0), (0, 5), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 30)
        
    def test_puntos_partida_pleno_4(self):
        
        self.bolos_rondas = [(3, 1), (5, 2), (0, 0), (10, ), (1, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 24)
        
    def test_puntos_partida_2_plenos(self):
        
        self.bolos_rondas = [(10, ), (10, ), (7, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 51)
        
    def test_puntos_partida_3_plenos(self):
        
        self.bolos_rondas = [(10, ), (10, ), (10, ), (1, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 67)
        
    def test_puntos_partida_4_plenos(self):
        
        self.bolos_rondas = [(10, ), (10, ), (10, ), (10, ), (1, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 97)
        
    def test_puntos_partida_4_plenos_en_medio(self):
        
        self.bolos_rondas = [(5, 0), (1, 3), (10, ), (10, ), (10, ), (10, ), (1, 2), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 106)  

    def test_puntos_partida_4_plenos_separados(self):
        
        self.bolos_rondas = [(10, ), (1, 3), (10, ), (10, ), (10, ), (1, 2), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 85)   
        
    def test_puntos_partida_semipleno(self):
        
        self.bolos_rondas = [(7, 3), (5, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 22)
        
    def test_puntos_partida_2_semiplenos(self):
        
        self.bolos_rondas = [(3, 7), (3, 7), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 23)

    def test_puntos_partida_3_semiplenos(self):
        
        self.bolos_rondas = [(3, 7), (2, 8), (5, 5), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 39)  

    def test_puntos_partida_2_semiplenos_en_medio(self):
        
        self.bolos_rondas = [(3, 1), (2, 1), (5, 5), (1, 9), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 28)
        
    def test_puntos_partida_2_semiplenos_separados(self):
        
        self.bolos_rondas = [(3, 1), (2, 8), (5, 0), (1, 9), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 34)
        
    def test_puntos_partida_1_pleno_1_semipleno_separados(self):
        
        self.bolos_rondas = [(3, 1), (10, ), (5, 1), (1, 9), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 38)
        
    def test_puntos_partida_1_pleno_1_semipleno_seguidos(self):
        
        self.bolos_rondas = [(3, 1), (1, 2), (10, ), (1, 9), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 39)

    def test_puntos_partida_2_plenos_1_semipleno_seguidos(self):
        
        self.bolos_rondas = [(3, 1), (10, ), (10, ), (1, 9), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 57)
        
    def test_puntos_partida_3_plenos_2_semiplenos_seguidos(self):
        
        self.bolos_rondas = [(10, ), (10, ), (10, ), (1, 9), (3, 7), (2, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 98)
        
    def test_puntos_partida_1_semipleno_1_pleno_seguidos(self):
        
        self.bolos_rondas = [(3, 1), (1, 2), (1, 9), (10, ), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 39)
        
    def test_puntos_partida_2_semiplenos_1_pleno_seguidos(self):
        
        self.bolos_rondas = [(3, 1), (8, 2), (1, 9), (10, ), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 47)
        
    def test_puntos_partida_3_semiplenos_2_plenos_seguidos(self):
        
        self.bolos_rondas = [(3, 7), (8, 2), (1, 9), (10, ), (10, ), (1, 2), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 86)
        
    def test_puntos_partida_2_semiplenos_2_plenos_mezclados(self):
        
        self.bolos_rondas = [(3, 1), (8, 2), (10, ), (1, 9), (10, ), (1, 2), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 80)
        
    def test_puntos_partida_3_semiplenos_3_plenos_mezclados(self):
        
        self.bolos_rondas = [(10, ), (8, 2), (10, ), (1, 9), (10, ), (3, 7), (4, 1), (0, 0), (0, 0), (0, 0)]
        self.puntos = self.puntos_partida_TDD(self.bolos_rondas)
        self.assertEqual(self.puntos, 119)
        
    

if __name__ == '__main__':
    unittest.main()