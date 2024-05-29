$(document).ready(function () {
  // Select the div with id 'add_item'
  $('#add_item').click(function () {
    // Create a new list item element
    const newListItem = $('<li>Item</li>');

    // Append the new list item to the list with class 'my_list'
    $('.my_list').append(newListItem);
  });
});
