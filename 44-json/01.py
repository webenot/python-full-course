import json

json_str = '{"id":235,"brand":"Nike","qty":84,"status":{"isForSale":true}}'

sneakers = json.loads(json_str)
print(sneakers)
print(type(sneakers))
print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])
print(json.dumps(sneakers, indent=2))
