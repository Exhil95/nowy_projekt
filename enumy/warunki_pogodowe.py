from enum import StrEnum

class WarunkiPogodowe(StrEnum):
    sunny = "słonecznie"
    cloudy = "pochmurnie"
    rainy = "deszczowo"
    snowy = "śnieżnie"
    windy = "wietrznie"
    partly_cloudy = "częściowe zachmurzenie"
    patchy_rain_nearby = "miejscowe opady"
    clear = "czyste niebo"
    light_rain = "łagodne opady"
    overcast = "zachmurzone niebo"
    light_freezing_rain = "lekkie marznące opady"
    moderate_or_heavy_snow_showers = "średnie lub duże opady śniegu"