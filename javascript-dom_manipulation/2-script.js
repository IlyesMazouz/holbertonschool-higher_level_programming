document.addEventListener('DOMContentLoaded', function () {
	var redHeaderElement = document.getElementById('red_header');
	var headerElement = document.querySelector('header');

	redHeaderElement.addEventListener('click', function () {
		headerElement.classList.add('red');
	});
});
