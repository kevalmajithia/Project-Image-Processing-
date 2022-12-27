const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '28d0dc950bmsh4cae4044c38d67fp1106bajsn3322eac56a86',
		'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
	}
};

fetch('https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=Seattle', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));