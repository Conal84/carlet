// Set up Stripe.js and Elements to use in checkout form
let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);

// Code from https://stripe.com/docs/stripe-js
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
  base: {
    color: "#32325d",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};

// Create an instance of the card Element.
let card = elements.create("card", { style: style, hidePostalCode: true });

// Add an instance of the card Element into the `card-element` <div>.
card.mount("#card-element");

// Handle real-time validation errors from the card Element.
card.on("change", function (event) {
  var displayError = document.getElementById("card-errors");
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = "";
  }
});

// Handle form submission.
var payform = document.getElementById("payment-form");

// object.onsubmit = function(){myScript};

// payform.addEventListener('submit', function(ev) {
// payform.onsubmit = function(ev) {
//     ev.preventDefault();
//     console.log("payment form submit event happens");
//     console.log(form);
//     card.update({ 'disabled': true});
//     $('#submit-button').attr('disabled', true);

//     var saveInfo = Boolean($('#id-save-info').attr('checked'));
//     // From using {% csrf_token %} in the form
//     var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
//     var postData = {
//         'csrfmiddlewaretoken': csrfToken,
//         'client_secret': clientSecret,
//         'save_info': saveInfo,
//     };
//     var url = '/checkout/cache_checkout_data/';

//     $.post(url, postData).done(function () {
//         stripe.confirmCardPayment(clientSecret, {
//             payment_method: {
//                 card: card,
//             },
//         }).then(function(result) {
//             if (result.error) {
//                 var errorDiv = document.getElementById('card-errors');
//                 var html = `
//                     <span class="icon" role="alert">
//                     <i class="fas fa-times"></i>
//                     </span>
//                     <span>${result.error.message}</span>`;
//                 $(errorDiv).html(html);
//                 // $('#payment-form').fadeToggle(100);
//                 // $('#loading-overlay').fadeToggle(100);
//                 card.update({ 'disabled': false});
//                 $('#submit-button').attr('disabled', false);
//             } else {
//                 if (result.paymentIntent.status === 'succeeded') {
//                     form.submit();
//                 }
//             }
//         });
//     }).fail(function () {
//         // just reload the page, the error will be in django messages
//         location.reload();
//     })
// };
payform.onsubmit = function(ev) {
    ev.preventDefault();
    console.log("payment form submit event happens");
    console.log(form);
}