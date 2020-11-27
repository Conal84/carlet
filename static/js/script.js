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

/**
 * A function to act as a back button
 */
function goBack() {
    window.history.back()
}
