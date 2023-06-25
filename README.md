# Rust AI

## Hvorfor ble dette lagd
Alle de forskjellige filene viser utviklingsprosessen min gjennom øvelseseksamen (5 timer).
Dagen etter gjorde jeg slik at de aktuelle filene ha X i navnet sitt for å lage mindre krøll. xXProgram XModel2 og XFunctions er de aktuelle filene.

## Hva er målet
Programmet er utvikling av Computer vision for å prøve å lage en "Cheat" for spillet Rust, ikke bekymre deg programmet er både for tregt og for dårlig for at det skulle blitt ett problem.
Dette er fordi programmet har: Datasett med for lite innhold til å bli ekstremt bra og  programmet behøver get request for JSON data, til den tid musen ville bevegd seg ville fienden vert langt unna.

## Hvordan fungerer programmet
Programmet bruker ett egenlagd Datasett fra Roboflow med rundt 600 bilder med annoteringer. Dette datasettet blir kalt på med Roboflow sitt api som deretter returnerer JSON, dette blir håndtert i programmet og satt i lister med X og Y koordinater slik at cv2 og PyAutoGUI libraries til å tegne bounding boxes og ett midpunkt blir funnet for å flytte musen og skyte denne personen.

## Hvordan kan du kjøre programmet

Du kan ikke kjøre programmet fordi det krever en API nøkkel til mitt workspace.


## Instrukser til meg selv
Du trenger en Roboflow API key for å kjøre denne koden, roboflow API keyen må være min siden jeg lagde AI Modellen, jeg kan ikke dele API keyen fordi det er som ett passord til mitt Workspace.

Du trenger en secret.py fil med MIN roboflow api key
Denne filen skal kun inneholde:

    key = ""

Denne filen er .gitignore´d



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
