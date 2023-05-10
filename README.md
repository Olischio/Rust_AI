# Rust AI

Du trenger en Roboflow API key for å kjøre denne koden, roboflow API keyen må være min siden jeg lagde AI Modellen, jeg kan ikke dele API keyen fordi det er som ett passord til mitt Workspace.

Du trenger en secret.py fil med MIN roboflow api key
Denne filen skal kun inneholde:

    key = ""

Denne filen er .gitignore´d

Dette Github Repositoriet viser Utviklingsprosessen for å lage en AI for Rust



## Install packages

```bash
# Først lag ett nytt virtual environment og så:
## Install dependencies from requirements.txt
# Du må stå i mappen hvor requirements.txt ligger
pip install -r requirements.txt

```
 
## Create requirements.txt from a virtual environment
 
Dersom du legger til nye dependencies så kan du trenge å regenerere requirements.txt

```bash
# Du må stå i mappen hvor requirements.txt skal ligge når du kjører denne
pip freeze > requirements.txt
```