document.addEventListener('DOMContentLoaded', function () {
	var toggleHeaderElement = document.getElementById('toggle_header');
	var headerElement = document.querySelector('header');

	toggleHeaderElement.addEventListener('click', function () {
		if (headerElement.classList.contains('red')) {
			headerElement.classList.remove('red');
			headerElement.classList.add('green');
		} else if (headerElement.classList.contains('green')) {
			headerElement.classList.remove('green');
			headerElement.classList.add('red');
		}
	});
});
