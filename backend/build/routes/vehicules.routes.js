import express from "express";
import { getVehicules, getVehicule_marque, getVehicule_marque_modele, getVehicule_marque_modele_annee, getVehicule_marque_modele_annee_config } from "../controllers/vehicules.controller.js";
export const router = express.Router();
router.get("/", getVehicules);
//router.get("/:id", getVehicule_id);
router.get("/:marque", getVehicule_marque);
router.get("/:marque/:modele", getVehicule_marque_modele);
router.get("/:marque/:modele/:annee", getVehicule_marque_modele_annee);
router.get("/:marque/:modele/:annee/:config", getVehicule_marque_modele_annee_config);
