document.addEventListener('DOMContentLoaded', function () {
	var characterElement = document.getElementById('character');

	fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
		.then(function (response) {
			if (response.ok) {
				return response.json();
			} else {
				throw new Error('Failed to fetch character data');
			}
		})
		.then(function (data) {
			var characterName = data.name;

			characterElement.textContent = characterName;
		})
		.catch(function (error) {
			console.error('Error:', error);
		});
});
