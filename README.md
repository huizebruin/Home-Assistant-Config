[![GitHub stars](https://img.shields.io/github/stars/huizebruin/Home-Assistant-Config.svg?style=plasticr)](https://github.com/huizebruin/Home-Assistant-Config/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/huizebruin/Home-Assistant-Config.svg?style=plasticr)](https://github.com/huizebruin/Home-Assistant-Config/commits/main)
[![HA Version](https://img.shields.io/badge/Running%20Home%20Assistant-2021.6.4%20-darkblue)](https://github.com/home-assistant/home-assistant/releases/latest)
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)
![GitHub Forks][forks-shield]
![Discord](https://img.shields.io/discord/723629686093119650)

Volg mij op mijn reis om een leuke Home Assistant te maken mis geen update door  GitHub :star2: te drukken.
# Home-Assistant-Config
Gebruik de code uit deze repo voor je eigen Home Assistant-omgeving, houd er rekening mee dat je niet altijd alles regel voor regel kunt kopiëren. 
Als je vragen hebt, stel ze dan gerust via e-mail of socials! 

https://discord.gg/AskpfnY

12/06/2021:
 - sensor Ambee weer een update gegeven
22/05/2021:
 - map schakelaars toegevoegd in config en hoofd map
 
14/05/2021:
  - update ambee pollen naar v01.08 in de sensor map
  - automations geplaatst
  - readme update gedaan
  - utility_meter map bijgewerkt
  
08/05/2021:
- update van de pollen (categorie Overige toegevoegd) en het yaml bestand hernoemd naar :ambee-pollen.yaml
- toevoeging van ambee-weer.yaml

![image](https://user-images.githubusercontent.com/65857422/117537520-c4508800-b001-11eb-9d55-828b6d358f6c.png)
![image](https://user-images.githubusercontent.com/65857422/117546799-96346d80-b02c-11eb-8dac-3d72fe27d8cb.png)

07/05/2021 : Update met meer gedetailleerde informatie over de pollen:

![image](https://user-images.githubusercontent.com/65857422/117507134-fb358800-af86-11eb-95fc-da9fbf3180f9.png)


Nederlandstalige pollen informatie voor je Home assistent.

https://github.com/huizebruin/Home-Assistant-Config/blob/main/sensors/ambee-nl.yaml  deze code plaats je in je configuration.yaml
![ambee-hooikoort-homeassistant](https://user-images.githubusercontent.com/62996429/114306196-63559300-9adb-11eb-8627-eba67729126e.jpg)
En deze code vul je bij het toevoegen van een nieuwe kaart ( kies je de onderste opitie) om yaml code toe te voegen
![afbeelding](https://user-images.githubusercontent.com/62996429/114317312-c2c99800-9b07-11eb-8cd4-81bfc91f1788.png)

Veel plezier ermee .




*************************************************************
Het thema welke ik gebruik voor Home assistant
/themes/Huizebruin/Huizebruin (Dark).yaml
![huizebruin-home assistant](https://user-images.githubusercontent.com/62996429/114280723-ef63ae00-9a3a-11eb-9b42-49173f5d1e15.jpg)

En dan maak je een automation 
Set theme at startup
![afbeelding](https://user-images.githubusercontent.com/62996429/114281085-9d238c80-9a3c-11eb-8c01-1eec0106d6f6.png)

alias: Set theme at startup
trigger:
  - platform: homeassistant
    event: start
action:
  - service: frontend.set_theme
    data:
      name: Huizebruin (Dark)
mode: single

Nu zal bij elke herstart deze thema geladen worden.




*************************************************************
Liked some of my work? Buy me a coffee (or more likely a beer)

<a href="https://www.buymeacoffee.com/huizebruin" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

[license-shield]: https://img.shields.io/github/license/huizebruin/home-assistant-config.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2021.svg
[forks-shield]: https://img.shields.io/github/forks/huizebruin/home-assistant-config.svg?style=social&label=Forks
