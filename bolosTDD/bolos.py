class ExcedidoMaximoRondas(Exception):
    pass

class ExcedidoMinimoRondas(Exception):
    pass

class ExcedidoNumBolos(Exception):
    pass

class ExcBolosNegativos(Exception):
    pass

class ExcedidoNumBolasRonda(Exception):
    pass


class Bolos:
    
    puntuacion_inicial = 0
    
    def puntos_partida(self, bolos):
        
        spare = False
        num_strikes = 0
        
        if len(bolos) > 10:
            raise ExcedidoMaximoRondas
        
        elif len(bolos) < 10:
            raise ExcedidoMinimoRondas
        
        else:
            for ronda in bolos:
                
                if len(ronda) == 1 and ronda[0] == 10:
                    num_strikes = num_strikes + 1
                    if spare == True:
                        self.puntuacion_inicial = self.puntuacion_inicial + ronda[0]
                        spare = False
                elif len(ronda) != 2:
                    raise ExcedidoNumBolasRonda
                elif ronda[0] + ronda[1] > 10:
                    raise ExcedidoNumBolos
                elif ronda[0] < 0 or ronda[1] < 0:
                    raise ExcBolosNegativos
                elif num_strikes == 1:
                    self.puntuacion_inicial = self.puntuacion_inicial + 10 + 2*(ronda[0] + ronda[1])
                    num_strikes = 0
                    if spare == True:
                        pass
                    if ronda[0] + ronda[1] == 10:
                        spare=True
                elif num_strikes > 1:
                    if ronda[0] + ronda[1] == 10:
                        spare=True
                    self.puntuacion_inicial = self.puntuacion_inicial + (num_strikes - 1)*3*10 + 3*ronda[0] + 2*ronda[1]
                    num_strikes = 0
                else:
                    self.puntuacion_inicial = self.puntuacion_inicial + ronda[0] + ronda[1]
                    if spare == True:
                        self.puntuacion_inicial = self.puntuacion_inicial + ronda[0]
                        spare = False
                    if ronda[0] + ronda[1] == 10:
                        spare=True
                 
            return self.puntuacion_inicial
