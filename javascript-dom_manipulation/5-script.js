document.addEventListener('DOMContentLoaded', function () {
	var updateHeaderElement = document.getElementById('update_header');
	var headerElement = document.querySelector('header');

	updateHeaderElement.addEventListener('click', function () {
		headerElement.textContent = 'New Header!!!'; // Update the text of the header
	});
});
