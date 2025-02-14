import axios from "axios";
import config from "./config.json"

class APICaller{
    static api = axios.create({
        baseURL: config["api-mode"] == "prod" ? config["prod-url"] : config["dev-url"]
    })

    static async healthCheck(){
        try{
            const response = await this.api(
                `/`
            )

            return response;
        }catch(error){
            console.log(error)
            return null;
        }
    }
};


export default APICaller;
