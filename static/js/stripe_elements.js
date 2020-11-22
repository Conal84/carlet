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
var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
  ev.preventDefault();
  card.update({ disabled: true });
  $("#submit-button").attr("disabled", true);
  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
      },
    })
    .then(function (result) {
      var displayError = document.getElementById("card-errors");
      // Show error to your customer (e.g., insufficient funds)
      if (result.error) {
        displayError.textContent = result.error.message;
        card.update({ disabled: false });
        $("#submit-button").attr("disabled", false);
      } else {
            if (result.paymentIntent.status === "succeeded") {
                form.submit();
            }
      }
    });
});
