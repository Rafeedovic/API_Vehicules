import { vehicules } from '../mocks/vehicules.mocks.js';
import * as VehiculesService from '../services/vehicules.services.js';

export const getVehicules = (req:any, res:any) => {
    const Vehicules = VehiculesService.getVehicules();
    return res.status(200).json(Vehicules);
};

export const getVehicule_id = (req:any, res:any) => {
    const { id } = req.params;
    const Vehicule = VehiculesService.getVehicule_id(id);
    return res.status(200).json(Vehicule);
};

export const getVehicule_marque = (req:any, res:any) => {
    const { marque} = req.params;
    const Vehicule = VehiculesService.getVehicule_marque(marque);
    return res.status(200).json(Vehicule);
};

export const getVehicule_marque_modele = (req:any, res:any) => {
    const { marque,modele} = req.params;
    const Vehicule = VehiculesService.getVehicule_marque_modele(marque,modele);
    return res.status(200).json(Vehicule);
};

export const getVehicule_marque_modele_annee = (req:any, res:any) => {
    const { marque,modele,annee} = req.params;
    const Vehicule = VehiculesService.getVehicule_marque_modele_annee(marque,modele,annee);
    return res.status(200).json(Vehicule);
};

export const getVehicule_marque_modele_annee_config = (req:any, res:any) => {
    const { marque,modele,annee,config} = req.params;
    const Vehicule = VehiculesService.getVehicule_marque_modele_annee_config(marque,modele,annee,config);
    return res.status(200).json(Vehicule);
};