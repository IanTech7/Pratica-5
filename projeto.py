#!/usr/bin/python3
# shebang: Indica o interpretador Python 3

import time
import os

# Definição do pino GPIO a ser usado (pino 18)
gpio_pin = "18"
gpio_path = f"/sys/class/gpio/gpio{gpio_pin}"

# função para configurar a GPIO (caso não esteja exportada).
def setup_gpio():
    if not os.path.exists(gpio_path):
        # Exporta o pino se ele ainda não existir
        with open("/sys/class/gpio/export", "w") as f:
            f.write(gpio_pin)
    
    # Aguarda o sistema criar os arquivos
    time.sleep(0.1)
    
    # Configura como saída (out)
    with open(f"{gpio_path}/direction", "w") as f:
        f.write("out")

# Executa configuração
setup_gpio()

# loop principal do serviço
while True:
    # Liga o LED (escreve '1')
    with open(f"{gpio_path}/value", "w") as f:
        f.write("1")
    time.sleep(0.5)
    
    # Desliga o LED (escreve '0')
    with open(f"{gpio_path}/value", "w") as f:
        f.write("0")
    time.sleep(0.5)