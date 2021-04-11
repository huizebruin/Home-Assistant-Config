# Home-Assistant-Config

Nederlandstalige pollen informatie voor je Home assistent.
https://github.com/huizebruin/Home-Assistant-Config/blob/main/ambee-nl.yaml
![ambee-hooikoort-homeassistant](https://user-images.githubusercontent.com/62996429/114306196-63559300-9adb-11eb-8627-eba67729126e.jpg)

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

