$(document).ready(function () {
  /**
   * A click event to show the toast
   */
  $("#bag-nav").click(function () {
    $(".toast").toast("show");
  });
});
// Toast Bag - Remove item and reload on click
$(".delete-link").click(function(e) {
    var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let name = $(this).data('name');
    let url = `/bag/remove/`
    let home = `/`
    let data = {'csrfmiddlewaretoken': csrfToken, 'name': name};

    $.post(url, data)
    .done(function() {
        // If user deletes the car redirect to the home page
        if(name==="del_car"){
            window.location.replace(home);
        }else{
            // Else reload the current page
            location.reload();
        }
        
    });
})