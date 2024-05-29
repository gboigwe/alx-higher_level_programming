$(document).ready(function () {
  // Selecting the div with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Query selector header element
    const $header = $('header');

    // Checking if header has a class 'red'
    if ($header.hasClass('red')) {
      // Removing class 'red' and adding 'green'
      $header.removeClass('red').addClass('green');
    } else {
      // Removing class 'green' and adding 'red'
      $header.removeClass('green').addClass('red');
    }
  });
});
