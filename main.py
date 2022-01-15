from pyowm.owm import OWM
import time

owm = OWM('YOUR API KEY') # api key
registerCitys = owm.city_id_registry() # registre des villes
weather_mgr = owm.weather_manager() # meteo

# questions sur la ville et le pays
villesOuLOnSouhaiteLaMeteo = input("Vous voulez la météo de quelle ville ? ")
paysOuSeTrouveLaVille = ""

if villesOuLOnSouhaiteLaMeteo == "alencon":
    villesOuLOnSouhaiteLaMeteo = "alençon"

while paysOuSeTrouveLaVille != "france" or "allemagne" or "grande bretagne":
    paysOuSeTrouveLaVille = input("Dans quel pays se trouve la ville ? ")
    if paysOuSeTrouveLaVille == "france":
        paysOuSeTrouveLaVille = "FR"
        break
    elif paysOuSeTrouveLaVille == "allemagne":
        paysOuSeTrouveLaVille = "DE"
        break
    elif paysOuSeTrouveLaVille == "grande bretagne":
        paysOuSeTrouveLaVille = "GB"
        break
    else:
        print("Veuillez indiquer une valeure correcte.")
        print("Voici les valeures correcte : france, allemagne, grande bretagne")


observation = weather_mgr.weather_at_place(f'{villesOuLOnSouhaiteLaMeteo}') # definit l'emplacement
weather = observation.weather # defenit l'emplacement qu'on veut la météo

# température
temperaure = weather.temperature('celsius')
# get temp normal
temperaureNormal = temperaure.get('temp')
# ciel
sky = weather.detailed_status
# vent
wind = weather.wind()

# conclusion
print("The temperature is", temperaureNormal,"°C. There is a", sky, ". The wind speed is", wind['speed'], "Km/h.")
time.sleep(1)

# estimations
print("Estimates :")

estimateForTomorrow = weather_mgr.weather_at_place(f'{villesOuLOnSouhaiteLaMeteo}, {paysOuSeTrouveLaVille}', 'daily').forecast
