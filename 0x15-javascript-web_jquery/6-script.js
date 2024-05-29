$(document).ready(function () {
  // Selecting div with an id 'update_header'
  $('#update_header').click(function () {
    // Query selector header element
    $('header').text('New Header!!!');
  });
});
