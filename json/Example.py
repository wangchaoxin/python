import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())

# Compact encoding:
json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))

# Pretty printing:
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
# Decoding JSON:
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
json.loads('"\\"foo\\bar"')
io = StringIO('["streaming API"]')
json.load(io)