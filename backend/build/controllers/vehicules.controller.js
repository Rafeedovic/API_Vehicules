import * as VehiculesService from '../services/vehicules.services.js';
export const getVehicules = (req, res) => {
    const Vehicules = VehiculesService.getVehicules();
    return res.status(200).json(Vehicules);
};
export const getVehicule_id = (req, res) => {
    const { id } = req.params;
    const Vehicule = VehiculesService.getVehicule_id(id);
    return res.status(200).json(Vehicule);
};
export const getVehicule_marque = (req, res) => {
    const { marque } = req.params;
    const Vehicule = VehiculesService.getVehicule_marque(marque);
    return res.status(200).json(Vehicule);
};
export const getVehicule_marque_modele = (req, res) => {
    const { marque, modele } = req.params;
    const Vehicule = VehiculesService.getVehicule_marque_modele(marque, modele);
    return res.status(200).json(Vehicule);
};
export const getVehicule_marque_modele_annee = (req, res) => {
    const { marque, modele, annee } = req.params;
    const Vehicule = VehiculesService.getVehicule_marque_modele_annee(marque, modele, annee);
    return res.status(200).json(Vehicule);
};
export const getVehicule_marque_modele_annee_config = (req, res) => {
    const { marque, modele, annee, config } = req.params;
    const Vehicule = VehiculesService.getVehicule_marque_modele_annee_config(marque, modele, annee, config);
    return res.status(200).json(Vehicule);
};
