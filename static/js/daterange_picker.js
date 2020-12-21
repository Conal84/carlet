let checkinDate;
let checkoutDate;
let checkinDp;
let checkoutDp;

$(document).ready(function () {
  /*
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