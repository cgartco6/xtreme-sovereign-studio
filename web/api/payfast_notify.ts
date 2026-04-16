import crypto from 'crypto';

export default async function handler(req: any, res: any) {
  const data = req.body;
  const pfParamString = Object.keys(data)
    .filter(key => key !== 'signature')
    .map(key => `${key}=${encodeURIComponent(data[key]).replace(/%20/g, '+')}`)
    .join('&');

  const signature = crypto.createHash('md5').update(pfParamString).digest('hex');

  if (data.signature === signature && data.payment_status === 'COMPLETE') {
    // 1. Mark order as PAID in ZAR
    // 2. Trigger AssetFactory for PDF/ZIP generation
    console.log(`ZAR Payment Verified: R${data.amount_gross} from ${data.email_address}`);
  }
  res.status(200).send('OK');
}
