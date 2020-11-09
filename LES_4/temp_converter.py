# Convert C to F
def celsius_to_fahr(temp_celsius):
    return 9/5 * temp_celsius + 32


# Convert K to C
def kelvins_to_celsius(temp_kelvins):
    return temp_kelvins - 273.15


# Convert K to F
def kelvins_to_fahr(temp_kelvins):
    temp_celsius = kelvins_to_celsius(temp_kelvins)
    temp_fahr = celsius_to_fahr(temp_celsius)
    return temp_fahr


print("Температура замерзания воды в градусах Фаренгейта равна:", celsius_to_fahr(0))



