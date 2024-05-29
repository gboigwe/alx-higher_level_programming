$(document).ready(function () {
  // The api for the movie name will be fetched
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Select the unordered list with id 'list_movies'
    const $movieList = $('#list_movies');

    // Clear any existing list items
    $movieList.empty();

    // Iterate over the movie data and create a list item for each movie
    $.each(data.results, function (index, movie) {
      const listItem = $('<li></li>').text(movie.title);
      $movieList.append(listItem);
    });
  });
});
