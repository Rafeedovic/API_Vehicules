import express from "express";
import bodyParser from "body-parser";
import { router } from "./routes/vehicules.routes.js";
const hostname = "127.0.0.1";
const port = 5000;
const app = express();
app.use(bodyParser.json());
app.get("/", (req, res) => {
    res.send("Hello asba !");
});
app.use("/students", router);
app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
