// Set up Stripe.js and Elements to use in checkout form
let stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
let client_secret = $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let style = {
  base: {
    color: "#32325d",
  },
  invalid: {
      color: '#dc3545',
      iconColor: '#dc3545'
  }
};

let card = elements.create("card", { style: style });
card.mount("#card-element");
