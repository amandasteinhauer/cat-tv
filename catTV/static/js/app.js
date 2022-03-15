window.onbeforeunload = () => {
    for(const form of document.getElementsByTagName('form')) {
      form.reset();
    }
  }

$("#videoCategoryOptions a").click(function() {
  option = $(this).data('value');
  $("#dropdownText").text(option);
});