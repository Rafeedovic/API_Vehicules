import { vehicules } from "../mocks/vehicules.mocks.js";
export const getVehicules = () => {
    return vehicules;
};
export const getVehicule_id = (id:string) => {
    const vehicule = vehicules.find((vehicule) => vehicule.index.toString() === id);
    return vehicule;
};

export const getVehicule_marque = (marque:string) => {
    const vehicule = vehicules.filter((vehicule) => vehicule.Marque.toString()=== marque);
    return vehicule;
};

export const getVehicule_marque_modele = (marque:string,modele : string) => {
    const vehicule = vehicules.filter((vehicule) => vehicule.Marque.toString()=== marque && vehicule.Modèle.toString()=== modele);
    return vehicule;
};

export const getVehicule_marque_modele_annee = (marque:string,modele : string,annee:string) => {
    const vehicule = vehicules.filter((vehicule) => vehicule.Marque.toString()=== marque && vehicule.Modèle.toString()=== modele && vehicule.Année.toString()=== annee);
    return vehicule;
};

export const getVehicule_marque_modele_annee_config = (marque:string,modele : string,annee:string,config:string) => {
    const vehicule = vehicules.filter((vehicule) => vehicule.Marque.toString()=== marque && vehicule.Modèle.toString()=== modele && vehicule.Année.toString()=== annee && vehicule.Config.toString()=== config);
    return vehicule;
};
