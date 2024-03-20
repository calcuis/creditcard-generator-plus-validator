### random creditcard generator

#### Luhn algorithm
Base: `Luhn algorithm` is in widely used today; it is not intended to be a cryptographically secure hash function; it was designed to protect against accidental errors, not malicious attacks.

### generator
This code can generate a random 16-digit credit card number following the `Luhn algorithm` for validity, a 3-digit `CVV`*, and a random valid expiry date at least two years in the future.

*The Card Verification Value (`CVV`), also known as the Card Verification Code (CVC) or Card Security Code (CSC), is a security feature used to verify that the person making the purchase actually possesses the credit card. It's a three or four-digit number typically found on the back of the card (on the signature strip for Visa, MasterCard, and Discover, and on the front for American Express).

The `CVV` is not directly associated with the credit card number itself. Instead, it's a separate security code generated by the credit card issuer (bank or financial institution) based on certain algorithms and rules. It's used as an extra layer of security to prevent fraudulent transactions, especially in scenarios where the physical card is not present (such as online transactions).

When a transaction is made, the `CVV` is usually required along with the credit card number and expiration date. The merchant then verifies this `CVV` with the issuing bank to ensure that it matches the one associated with the card on file. If the `CVV` doesn't match, the transaction may be declined.

In the context of generating a dummy credit card number, the `CVV` is generated randomly, as it's not directly tied to the credit card number itself. It's simply a security measure included with the card details for verification purposes.

### validator
This code can check the validity of a credit card number (rather it was generated or in practical usage) according to the calculation in `Luhn algorithm`.