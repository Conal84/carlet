/**
 * A function to autocomplete city user input
 * @function activatePlacesSearch
 */
function activatePlacesSearch() {
  const options = {
    types: ["(cities)"],
  };

  let input = document.getElementById("id_location");
  let autocomplete = new google.maps.places.Autocomplete(input, options);
}

$(".delete-link").click(function(e) {
    let csrfToken = "{{ csrf_token }}";
    let itemId = $(this).data('item');
    let name = $(this).data('name');
    let url = `/bag/remove/${itemId}/${name}`
    let data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
    .done(function() {
        location.reload();
    }) 
})
