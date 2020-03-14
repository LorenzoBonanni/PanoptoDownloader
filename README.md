# PanoptoDownloader
A Python Script to download lessons from panopto
## How to Use:
### Italian: 
#### Requisiti:
1) [Python 3.x](https://www.html.it/pag/15609/installare-python/)
2) [pip](https://www.html.it/pag/346968/pip-il-package-manager-per-python/)
3) [Chrome](https://www.google.com/chrome/) 
4) [ChromeDriver](https://chromedriver.chromium.org/downloads)<br/>
   la versione win32 funziona sia su dispositivi a 32 che a 64bit
#### Avviare il Programma
1) Rinominare il Chrome driver in ```chromedriver``` e inserirlo nella cartella config
2) Aprire la riga di comando navigare fino alla cartella del progetto
3) Installare le Dipendenze con il Comando: <br /> ```pip install -r requirements.txt```
4) Inserire le credenziali GIA nel file [config.yaml](./config/config.yaml) seguendo questa struttura: <br/>
    ```yaml
    username: id123abc
    password: password1234
    ```
5) Inserire i link ai video da scaricare e il nome della materia nel file [videos.yaml](./config/videos.yaml) con la seguente struttura:<br />
    ```yaml
    Architettura degli elaboratori:
        - htttp:\\example-link1.com
        - htttp:\\example-link2.com
    subject2:
        - htttp:\\example-link1.com
        - htttp:\\example-link2.com
    ```
6) Avviare il programma con il comando: ```python main.py``` 

### English: 
#### Requirements:
1) [Python 3.x](https://realpython.com/installing-python/)
2) [pip](https://www.makeuseof.com/tag/install-pip-for-python/)
3) [Chrome](https://www.google.com/chrome/) 
4) [ChromeDriver](https://chromedriver.chromium.org/downloads)<br/>
   the win32 version works on both windows 32 and 64bit
#### Run the Program
1) Rename Chrome Driver into ```chromedriver``` and then insert it into the config folder
2) Open CommandLine and go to the project directory 
3) Install dependencies with the command: <br /> ```pip install -r requirements.txt```
4) Insert GIA credentials into the file [config.yaml](./config/config.yaml) with the following structure: <br/> 
    ```yaml 
    username: id123abc 
    password: password1234
    ```
5) Insert video links and subject name into the file [videos.yaml](./config/videos.yaml) with the following structure:<br />
    ```yaml
    Architettura degli elaboratori:
        - htttp:\\example-link1.com
        - htttp:\\example-link2.com
    subject2:
        - htttp:\\example-link1.com
        - htttp:\\example-link2.com
    ```
6) Start the program with the command: ```python main.py``` 