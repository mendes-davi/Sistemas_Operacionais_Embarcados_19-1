1. Com relação às conexões GPIO do modelo de Raspberry Pi que você usará no projeto, responda:

(a) Quais pinos podem ser utilizados como entradas e saídas digitais comuns?

> pinos 03, 05, 07, 08, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 39, 40

(b) Quais pinos possuem resistores de pull-up e pull-down?

> Todos os pinos de GPIO possuem resistores de pull-up programáveis.

(c) Quais formas de comunicação serial são suportados pelos pinos GPIO?

> Comunicação via UART, via SPI e via I2C

2. Apresente outras 3 bibliotecas de acesso I/O em C para o Raspberry Pi.

> Via biblioteca [Wiringpi](http://wiringpi.com/), via [pigpio](http://abyz.me.uk/rpi/pigpio/index.html) e via [bcm2835](http://www.airspayce.com/mikem/bcm2835/).