import requests
from bs4 import BeautifulSoup

class Rate:
    def __init__(self, name, symbol, to_usd, from_usd):
        self.name = name
        self.symbol = symbol
        self.to_usd = to_usd
        self.from_usd = from_usd

    def __str__(self):
        return f"Rate(Name: {self.name}, Symbol: {self.symbol}, To USD: {self.to_usd}, From USD: {self.from_usd})"

# URL de la page contenant les taux de change
url = 'https://www.x-rates.com/table/?from=USD&amount=1'

# Effectuer une requête GET pour récupérer le contenu de la page
response = requests.get(url)
response.raise_for_status()  # Vérifie que la requête a réussi

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Localiser la table des taux de change
table = soup.find('table', {'class': 'tablesorter ratesTable'})

# Liste pour stocker les objets Taux
taux_list = []

# Parcourir les lignes du tableau et extraire les données
for row in table.find('tbody').find_all('tr'):
    cols = row.find_all('td')
    if len(cols) == 3:
        name = cols[0].text.strip()
        #symbol = name.split()[0]  # Extract a basic symbol approximation
        symbol = ""
        to_usd = cols[1].text.strip()
        from_usd = cols[2].text.strip()
        taux = Rate(name, symbol, to_usd, from_usd)
        taux_list.append(taux)

# Afficher les objets Taux
for taux in taux_list:
    print(taux)
