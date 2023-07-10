def data_colis():
    nombre_colis = int(input("Entrez le nombre de colis : "))
    colis = []

    for i in range(nombre_colis):
        longueur = float(input("Entrez la longueur du colis {} : ".format(i+1)))
        largeur = float(input("Entrez la largeur du colis {} : ".format(i+1)))
        hauteur = float(input("Entrez la hauteur du colis {} : ".format(i+1)))
        colis.append((longueur, largeur, hauteur))
    return colis
def data_vehicule()

def main():
    T = data_colis()
    print(T)

if __name__=="__main__":
    main()