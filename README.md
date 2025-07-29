# Aluno: Wilton Lacerda Silva Júnior
## Matrícula: TIC370100193
# Video explicativo: https://youtu.be/qcWQLMQwbAE
# Datalogger
O objetivo do projeto é utilizar do MPU e do adaptador e cartão SD para salvar dados, passar para o computador e plotar gráficos sobre esses dados.
## Funcionalidades

- **LED RGB**
  - O LED central da placa RGB serve como um aviso, mostrando o que está acontecendo no momento na placa.
- **Sensores**
	- O sensor MPU servirá para captar as informações do giroscópio e acelerômetro, para serem salvas e analisadas.
- **Cartão SD**
   - O cartão SD salvará os dados do sensor MPU para serem analisados futuramente no computador e plotar seu gráfico.

# Requisitos
## Hardware:

- Raspberry Pi Pico W.
- 1 LED vermelho no pino 13.
- 1 LED azul no pino 12.
- 1 LED verde no pino 11.
- 1 adaptador de cartão SD.
- 1 sensor MPU no I2C da placa.

## Software:

- Ambiente de desenvolvimento VS Code com extensão Pico SDK.
- Python.
- Envio do arquivo salvo no cartão SD.

# Instruções de uso
## Configure o ambiente:
- Certifique-se de que o Pico SDK está instalado e configurado no VS Code.
- Compile o código utilizando a extensão do Pico SDK.
- Certifique-se que o python e suas bibliotecas (pandas, numpy, matplotlib) estão instaladas e devidamente configuradas.

## Teste:
- Utilize a placa BitDogLab para o teste. Caso não tenha, conecte os hardwares informados acima nos pinos correspondentes.
- Utilize os periféricos nas portas corretas.

# Explicação do projeto:
## Contém:
- O projeto terá uma forma de comunicar com o usuário o estado atual do programa: o LED RGB.
- O projeto capturará dados do giroscópio e acelerômetro e salvará no cartão SD.
- Também utilizará esse dados captados e salvos para plotar dois gráficos com o código python.

## Funcionalidades:
- O programa captara os valores do giroscópio e a aceleração pelo sensor.
- O programa emitira aviso pelo led RGB de acordo com o que está acontecendo na placa no momento.
- O programa salvará dos dados em um cartão SD.
- O programa plotará um gráfico de acordo com os dados salvos.
