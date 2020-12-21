/**
 * A function to autocomplete city user input
 * @function activatePlacesSearch
 */
function activatePlacesSearch() {
  const options = {
    types: ["(cities)"],
    componentRestrictions: { country: "gb" },
  };

  let input = document.getElementById("search-location");
  let autocomplete = new google.maps.places.Autocomplete(input, options);
}