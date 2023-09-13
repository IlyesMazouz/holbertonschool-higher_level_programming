document.addEventListener('DOMContentLoaded', function () {
	var helloElement = document.getElementById('hello');

	fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
		.then(function (response) {
			if (response.ok) {
				return response.json();
			} else {
				throw new Error('Failed to fetch translation');
			}
		})
		.then(function (data) {
			var translatedHello = data.hello;

			helloElement.textContent = translatedHello;
		})
		.catch(function (error) {
			console.error('Error:', error);
		});
});
