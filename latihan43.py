
celcius_to_fahrenheit = lambda c: (9/5) * c + 32
celcius_to_reamur = lambda c: 0.8 * c


celsius_1 = 100
output_fahrenheit_1 = celcius_to_fahrenheit(celsius_1)
celsius_2 = 80
output_reamur_2 = celcius_to_reamur(celsius_2)
celsius_3 = 0
output_fahrenheit_3 = celcius_to_fahrenheit(celsius_3)


print(f"C = {celsius_1}.  F = {output_fahrenheit_1}.")
print(f"C = {celsius_2}.  F = {output_reamur_2}.")
print(f"C = {celsius_3}.  F = {output_fahrenheit_3}.")