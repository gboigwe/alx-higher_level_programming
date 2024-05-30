$(document).ready(function () {
  function translateHello () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    })
      .fail(function () {
        $('#hello').text('Error: Invalid language code');
      });
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      translateHello();
    }
  });
});
