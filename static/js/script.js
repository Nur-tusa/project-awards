$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url':'/ajax/awwards/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
        $('#id_design').val('');
        $('#id_usability').val('');
        $('#id_content').val('');
        $('#id_rating').val('');
  }) // End of submit event

}) // End of document ready function
