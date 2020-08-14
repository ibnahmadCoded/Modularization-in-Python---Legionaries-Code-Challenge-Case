from romans import int_to_roman

count = 0
for number in range(2661):
    rom_val = int_to_roman(number)
    count += rom_val.count("X")


print(count)
