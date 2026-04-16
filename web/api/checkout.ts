import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, { apiVersion: '2023-10-16' });

export default async function handler(req: any, res: any) {
  if (req.method === 'POST') {
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      # REMOVED: shipping_address_collection
      line_items: [{
        price_data: {
          currency: 'usd',
          product_data: { 
            name: 'Xtreme Sovereign Digital Branding Kit',
            description: 'Full high-res logo set, brand guidelines, and marketing copy.'
          },
          unit_amount: 49900, // $499.00
        },
        quantity: 1,
      }],
      mode: 'payment',
      success_url: `${req.headers.origin}/vault?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${req.headers.origin}/pricing`,
    });
    res.status(200).json({ id: session.id });
  }
}
