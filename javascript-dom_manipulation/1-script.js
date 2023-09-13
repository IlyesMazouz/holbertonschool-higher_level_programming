document.addEventListener('DOMContentLoaded', function () {
	var redHeaderElement = document.getElementById('red_header');

	redHeaderElement.addEventListener('click', function () {
		var headerElement = document.querySelector('header');

		headerElement.style.color = 'red';
	});
});
