#!/bin/bash
# exporta o pino 18 para torná-lo acessível ao usuário
echo 18 > /sys/class/gpio/export

# configura o pino 18 como saída (out) para controlar o LED
echo out > /sys/class/gpio/gpio18/direction
# loop infinito para manter o serviço rodando
while [ 1 ]
do
    # envia '1' para o arquivo 'value', ligando o LED 
    echo 1 > /sys/class/gpio/gpio18/value
    
    # aguarda 0.2 segundos
    sleep 0.2s
    
    # envia '0' para o arquivo 'value', desligando o LED (nível baixo)
    echo 0 > /sys/class/gpio/gpio18/value
    
    # aguarda 0.2 segundos
    sleep 0.2s
done # fim do bloco de repetição