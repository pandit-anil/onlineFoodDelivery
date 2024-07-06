$(document).ready(function() {
    $('.user_link').on('click', function(event) {
      event.preventDefault();
      $('.dropdown-content').toggle();
    });
  
    $(document).on('click', function(event) {
      if (!$(event.target).closest('.user-menu').length) {
        $('.dropdown-content').hide();
      }
    });
  });
  