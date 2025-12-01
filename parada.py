#!/usr/bin/python3
import os

# definição do pino
gpio_pin = "18"
gpio_path = f"/sys/class/gpio/gpio{gpio_pin}"

# verifica se o pino está ativo.
if os.path.exists(gpio_path):
    # Garante que o LED termine desligado (segurança)
    with open(f"{gpio_path}/value", "w") as f:
        f.write("0")
    
    # realiza o 'unexport' para liberar o recurso no sistema
    with open("/sys/class/gpio/unexport", "w") as f:
        f.write(gpio_pin)