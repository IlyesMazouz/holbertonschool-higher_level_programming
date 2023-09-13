document.addEventListener('DOMContentLoaded', function () {
	var listMoviesElement = document.getElementById('list_movies');

	fetch('https://swapi-api.hbtn.io/api/films/?format=json')
		.then(function (response) {
			if (response.ok) {
				return response.json();
			} else {
				throw new Error('Failed to fetch movie data');
			}
		})
		.then(function (data) {
			var movies = data.results;

			movies.forEach(function (movie) {
				var listItem = document.createElement('li');
				listItem.textContent = movie.title;
				listMoviesElement.appendChild(listItem);
			});
		})
		.catch(function (error) {
			console.error('Error:', error);
		});
});
