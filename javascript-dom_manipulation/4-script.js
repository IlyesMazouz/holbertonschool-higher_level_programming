document.addEventListener('DOMContentLoaded', function () {
	var addItemElement = document.getElementById('add_item');
	var myListElement = document.querySelector('.my_list');

	addItemElement.addEventListener('click', function () {
		var newListItem = document.createElement('li');
		newListItem.textContent = 'Item';
		myListElement.appendChild(newListItem);
	});
});
