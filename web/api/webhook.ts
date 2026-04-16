// Inside the 'checkout.session.completed' block
if (event.type === 'checkout.session.completed') {
  const session = event.data.object as Stripe.Checkout.Session;
  
  // 1. Mark project as PAID in database
  // 2. Trigger Producer to ZIP all high-res assets
  // 3. Email the client their "Vault Key"
  console.log(`RELEASE ASSETS: Payment verified for ${session.customer_details?.email}`);
  
  await fetch(`${process.env.BACKEND_URL}/api/release-assets`, {
    method: 'POST',
    headers: { 'x-api-key': process.env.MASTER_API_KEY! },
    body: JSON.stringify({ email: session.customer_details?.email })
  });
}
