console.log("carregado post do ethereum antes")


import { CryptoAPI } from "./module/requestCrypto.js";

console.log("carregado post do ethereum depois")

const apiUrl = new CryptoAPI("http://127.0.0.1:8000/"); // REST URL


const postEth = document.getElementById("postDataETH");

postEth.addEventListener('click', () => {

    apiUrl.postData("api/ethereum/price/", {
        path_binance: "ticker/price",
        symbol: "ETHUSDT",
    })
        .catch(error => {
            console.log(error);
        })
})