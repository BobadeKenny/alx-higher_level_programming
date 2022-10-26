$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const code = $('INPUT#language_code').val();

    $.get('https://fourtonfish.com/hellosalut/?lang=' + code, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
