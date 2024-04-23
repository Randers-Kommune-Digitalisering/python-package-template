# Python package template projekt
Template til nye Python package projekter.
Projekt indeholder en simpel python package
* To simple funktioner
* unit test af af funktionerne

# Brug af python-package-template
1. Klik på "use this template" og vælg "create a new repository"
2. Udfyld skærmbillede med information om den nye package
3. Åbn dit nye git projekt

# Nyt Python package projekt
Nedenstående relaterer sig til et nyt Python app projekt der er baseret på denne template.

## Udvikling i et Codespace:
1. Gå til det nyoprettede repository i github.
2. Klik på den grønne <>Code knap og vælg "create codespace on \<branch>"
3. Kør ```. ./setup-dev-linux.sh ```, scriptet sætter et virtual environment op og installerer pakkerne i projekt filen

## Udvikling lokalt:
1. Gå til det nyoprettede repository i github.
2. Klik på den grønne <>Code knap og kopier url'et, clone det med git: ```git clone <url>```
3. Kør ```. ./setup-dev-linux.sh ``` (Linix) eller ```setup-dev-windows.cmd``` (Windows), scriptet sætter et virtual environment op og installerer pakkerne i projekt filen

## Almindelige commands
* Unit tests: ```pytest```
* Unit tests med coverage ```pytest --cov=src```
* Lint: ```flake8 src tests --show-source```

## Brug package efterfølgende
### Installer i nyt projekt
* ```pip install git+https://github.com/Randers-Kommune-Digitalisering/<package name>@<branch>```
* ```pip install git+https://github.com/Randers-Kommune-Digitalisering/<package name>@<tag>```
### Tilføj til requirements.txt
* ```<package name> @ git+https://github.com/Randers-Kommune-Digitalisering/<package name>@<branch>```
* ```<package name> @ git+https://github.com/Randers-Kommune-Digitalisering/<package name>@<tag>```