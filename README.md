# schimmelwaechter
Die Anwendung gibt auf einem Display Klimadaten aus, welche zum Teil errechnet werden.
Hardwarebasis ist ein Raspberry Pico mit einem OLED Display ssd1306, einem Sensor BME280, sowie einem Sensor DS18B20.
Der Sensor BME280 ist für das Erfassen der Raumklimadaten verantwortlich. Daraus wird die tatsächlich in der Raumluft vorhandenen Wassermenge (genauer er vorhandene Dampfdruck) errechnet. Der Sensor DS18B20 wird an der Schimmelstelle angebracht und erfasst die Temperatur.
Das Display gibt die erfassten und errechneten Klimadaten aus. Berechnet wird vor allem auch die relative Luftfeuchtigkeit an der zu untersuchenden Stelle, welche im direkten Zusammenhang mit einem potenziellen Schimmelwachstum steht.

Schimmel.zip -> Datei für den Platinenhersteller
Pico_Schimmel.fzz -> Fritzing Datei um das Platinenlayout anzusehen
