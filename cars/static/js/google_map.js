// Initialize the map and geocoder
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: { lat: 51.509865, lng: -0.118092 },
  });
  const geocoder = new google.maps.Geocoder();

// Geocode the address and create the marker
    let address = document.getElementById('address').value;
    geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == 'OK') {
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location,
            animation: google.maps.Animation.DROP
        });
        } else {
        alert('Geocode was not successful for the following reason: ' + status);
        }
    });

}