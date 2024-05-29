$(document).ready(function () {
  // Select the div with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Select the header element using jQuery
    const $header = $('header');

    // Check if the header has the 'red' class
    if ($header.hasClass('red')) {
      // Remove the 'red' class and add the 'green' class
      $header.removeClass('red').addClass('green');
    } else {
      // Remove the 'green' class and add the 'red' class
      $header.removeClass('green').addClass('red');
    }
  });
});
