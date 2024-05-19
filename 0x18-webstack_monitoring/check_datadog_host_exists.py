from datadog import initialize, api

options = {
    'api_key': '54a797bf3be5a7ea6d004816f5a602c7',
    'app_key': '90a0ec4c7c2f4d2d4db031d8228b22eff212064e'
    }

initialize(**options)

host_name = 'XX-web-01'
result = api.Hosts.search(q=host_name)

if result['total_returned'] > 0:
    print("Host exists")
else:
    print("Host does not exist")

