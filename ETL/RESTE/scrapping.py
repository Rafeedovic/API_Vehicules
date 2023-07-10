from bs4 import BeautifulSoup



soup = BeautifulSoup(html_code, "html.parser")

# Extraction des éléments

longueur = soup.find("span", class_="longueur").text.strip()
largeur = soup.find("span", class_="largeur").text.strip()
hauteur = soup.find("span", class_="hauteur").text.strip()
empattement = soup.find("span", class_="txt", text="2,53 m").text.strip()
coffre = soup.find("li", class_="caract02").find("span", class_="txt").text.strip()
portes = soup.find("li", class_="caract03").find("span", class_="txt").text.strip()
places = soup.find("li", class_="caract01").find("span", class_="txt").text.strip()
poids = soup.find("li", class_="caract05").find("span", class_="txt").text.strip()

# Affichage des résultats

print("Longueur:", longueur)
print("Largeur:", largeur)
print("Hauteur:", hauteur)
print("Empattement:", empattement)
print("Volume de coffre mini/maxi:", coffre)
print("Nombre de portes:", portes)
print("Nombre de places assises:", places)
print("Poids à vide:", poids)