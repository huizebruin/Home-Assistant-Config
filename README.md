08/05/2021:
- update van de pollen (categorie Overige toegevoegd) en het yaml bestand hernoemd naar :ambee-pollen.yaml
- toevoeging van ambee-weer.yaml

![image](https://user-images.githubusercontent.com/65857422/117537520-c4508800-b001-11eb-9d55-828b6d358f6c.png)
![image](https://user-images.githubusercontent.com/65857422/117546799-96346d80-b02c-11eb-8dac-3d72fe27d8cb.png)






# Home-Assistant-Config

07/05/2021 : Update met meer gedetailleerde informatie over de pollen:

![image](https://user-images.githubusercontent.com/65857422/117507134-fb358800-af86-11eb-95fc-da9fbf3180f9.png)

Nederlandstalige pollen informatie voor je Home assistent.

https://github.com/huizebruin/Home-Assistant-Config/blob/main/sensors/ambee-nl.yaml deze code plaats je in je configuration.yaml ambee-hooikoort-homeassistant En deze code vul je bij het toevoegen van een nieuwe kaart ( kies je de onderste opitie) om yaml code toe te voegen afbeelding

Veel plezier ermee .

Het thema welke ik gebruik voor Home assistant /themes/Huizebruin/Huizebruin (Dark).yaml huizebruin-home assistant

En dan maak je een automation Set theme at startup afbeelding

alias: Set theme at startup trigger:

platform: homeassistant event: start action:
service: frontend.set_theme data: name: Huizebruin (Dark) mode: single
Nu zal bij elke herstart deze thema geladen worden.
