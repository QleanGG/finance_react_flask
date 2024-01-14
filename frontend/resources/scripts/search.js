const MY_SERVER = 'http://127.0.0.1:5000'

const resultDiv = document.getElementById('result')

const get_stock = async () => {
    const ticker = document.getElementById('ticker-input').value;
    axios.post(`${MY_SERVER}/get_stock`, {ticker: ticker})
    .then(response => {
        const data = response.data;
        console.log(data.currentPrice);
        // Check if the 'currentPrice' key exists in the response
        if(data.currentPrice) {
            // Update the HTML element with the current price
            resultDiv.innerHTML = `Current price of ${data.ticker}: ${data.currentPrice}`;
        } else if(data.error) {
            // Handle any errors
            resultDiv.innerHTML = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        // Handle any errors during the request
        resultDiv.innerHTML = `Request failed:: ${error}`;
    });
}
