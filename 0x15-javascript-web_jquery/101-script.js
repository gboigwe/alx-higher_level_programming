$(document).ready(function () {
  // Added list of an item
  $('#add_item').click(function () {
    const newListItem = $('<li>Item</li>');
    $('.my_list').append(newListItem);
  });

  // Removing a last item in a list
  $('#remove_item').click(function () {
    $('.my_list li:last-child').remove();
  });

  // Clear out entire list
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
