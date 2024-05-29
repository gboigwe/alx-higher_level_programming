$(document).ready(function () {
  // Fetching API data from:
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Selected div with the id 'hello'
    const $helloDiv = $('#hello');

    // Updated the div content with value of 'hello' from the response
    $helloDiv.text(data.hello);
  });
});
