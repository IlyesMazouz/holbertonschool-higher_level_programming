$(document).ready(function() {
	$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
	  data.results.forEach(function(movie) {
		var listItem = $('<li></li>').text(movie.title);
		
		$('#list_movies').append(listItem);
	  });
	});
  });
  