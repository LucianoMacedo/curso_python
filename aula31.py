RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# Definindo os valores da velocidade e local do carro
velocidade = 70  # exemplo: carro está a 70 km/h
local_carro = 100  # exemplo: carro passou exatamente pelo radar

# Verificações
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')
