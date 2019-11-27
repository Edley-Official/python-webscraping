# # # # # # # # # # # # # # # # # # # # # # # # # #
# Vorwort
# Für dieses Programm benötigst du Selenium. Dies installierst du durch Eingabe in das Terminal:
# pip install selenium
# Damit das Programm nutzbar ist, sollte Google Chrome auf deinem PC installiert sein
# Zusätzlich benötigst du einen Chromedriver. Gehe dazu auf einen der folgenden Links und lade dir den für deinen Computer geeigneten Chromedriver herunter 
# https://chromedriver.chromium.org/
# https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.105/
# 
# Solltest du Google Chrome bereits verwenden, prüfe bitte die Kompatibilität und Update entweder Google Chrome, oder suche nach einem passenden Chromedriver für dein Betriebssystem.
#
# Sobald du den Chromedriver heruntergeladen hast, füge ihn einfach in den Ordner tools->assets
# Bitte entpacke die ZIP Datei vorher! Das ganze Funktioniert nicht, sofern der Browser noch in der ZIP ist.
#
# Das Programm wurde in Python 3 geschrieben und getestet. 
# # # # # # # # # # # # # # # # # # # # # # # # # #

from tools import settings

# Chrome-Browser starten // 
driver = settings.get_driver(headless=False)

# # # # # # # # # # #
# Hier Code einfügen





# Code Ende
# # # # # # # # # # #

driver.quit()