console.log("carregado requestcrypto")


/**
 * class implementing the structure of an 
 * async fetch for requests made to REST
 */
export class CryptoAPI {
    /**
     * internally defines and saves the default REST URL
     * @param {string} baseURL - URL REST
     */
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    async getData(endpoint) {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, {
                credentials: 'include',
            });
            if (!response.ok) {
                // throwing exceptions
                throw new Error(`Error: ${response.statusText}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error in search data:', error);
            // returns null if something goes wrong with the request
            return null;
        }
    }


    async postData(endpoint, payload) {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json", // defines the POST content type
                },
                credentials: 'include', // credentials for sending cookies and sessions
                body: JSON.stringify(payload),
            });
            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error in request data:', error);
            return null;
        }
    }
}