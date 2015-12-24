import requests as r
import json, time

venue   = 'EFCBEX'
stock   = 'HYYM'
payload = {
    'account'   : 'ERB50094442',
    'price'     : 4800,
    'qty'       : 10 * 1000,
    'direction' : 'buy',
    'orderType' : 'limit'
}

total_purchase_limit = (100 * 1000)
total_asked = 0

api_base   = 'https://api.stockfighter.io/ob/api'
api_params = '/venues/%s/stocks/%s/orders' % (venue, stock)
api_url    = '%s%s' % (api_base, api_params)

headers = { 'X-Starfighter-Authorization': 'e5cd0f210845cb14e02bfa4d72027bad8602d5ac' }

i = 0

while total_asked < total_purchase_limit:
    response = r.post(api_url, headers=headers, data=json.dumps(payload))
    if ( json.loads(response.text)['ok'] is not True ):
        print("There was an error: \n%s\n" % json.loads(response.text)['error'] )
        break
    total_asked = total_asked + payload['qty']
    i += 1
    print('Iteration %s completed. Asked for %s thus far.' % (i, total_asked))
    time.sleep(1)

print("END:")
print('payload: %s' % payload)
print("response.text: %s" % response.text)