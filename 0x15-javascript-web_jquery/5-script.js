$(document).ready(function () {
  // Selecting div with id 'add_item'
  $('#add_item').click(function () {
    // Creating an element for list item
    const newListItem = $('<li>Item</li>');

    // Append the new list item to the list with class 'my_list'
    $('.my_list').append(newListItem);
  });
});
