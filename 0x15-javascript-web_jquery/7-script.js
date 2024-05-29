$(document).ready(function () {
  // The api character name will be fetched
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Selecting div character id
    const $characterDiv = $('#character');

    // Updated the div character name content
    $characterDiv.text(data.name);
  });
});
