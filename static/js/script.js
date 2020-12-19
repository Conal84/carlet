let checkinDate;
let checkoutDate;
let checkinDp;
let checkoutDp;

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

$(document).ready(function () {
  /**
   * A click event to how the toast
   */
  $("#bag-nav").click(function () {
    $(".toast").toast("show");
  });

  /**
   * Create check in datepicker at html element
   */
  let checkinDiv = $('#search-from').datepicker({
      weekStart: 1,
      startDate: "today",
      format: 'yyyy-mm-dd',
      clearBtn: true,
      autoclose: true,
      todayHighlight: true,
      orientation: "bottom",
      beforeShowDay: function (date) {
          if (checkoutDate !== undefined) {
              if (date > checkoutDate) {
                  return false;
              }
          }
          return true;
      }
  });

  checkinDp = checkinDiv.data('datepicker');
  checkinDp.update(new Date());

  checkinDiv.on('changeDate', (event) => {
      checkinDate = event.date;
      checkoutDp.update();
      checkinDp.update();
  });

  /**
   * Create check out datepicker at html element
   */
  let checkoutDiv = $('#search-to').datepicker({
      weekStart: 1,
      startDate: "today",
      format: 'yyyy-mm-dd',
      clearBtn: true,
      autoclose: true,
      todayHighlight: true,
      orientation: "bottom",
      beforeShowDay: function (date) {
          if (checkinDate !== undefined) {
              if (date < checkinDate) {
                  return false;
              }
          }
          return true;
      }
  });
  checkoutDp = checkoutDiv.data('datepicker');
  checkoutDiv.on('changeDate', (event) => {
      checkoutDate = event.date;
      checkinDp.update();
      checkoutDp.update();
  });
});
