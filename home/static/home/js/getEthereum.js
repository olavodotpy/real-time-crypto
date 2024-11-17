import { CryptoAPI } from "./module/requestCrypto.js";
import { formatPrice } from "./module/formattingPrice.js"


const requestCryptoData = new CryptoAPI("http://127.0.0.1:8000/");



document.addEventListener("DOMContentLoaded", () => {

    // message before request
    const HTMLText = document.getElementById("priceSet");
    HTMLText.innerText = "Loading..."
    
    setInterval(() => {
        requestCryptoData.getData("api/ethereum/price/")
            .then(data => {
                // Will take the price from the JSON format and display innerText price
                const HTMLText = document.getElementById("priceSet");
                HTMLText.innerText = formatPrice(data.price);
            })
            .catch(error => {
                console.log(error);
            })
        }, 3000);
});