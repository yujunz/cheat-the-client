# Demo script for presentation "Cheat The Client"

Replacing `openstack` with `mitmproxy` in request and reponse

## Cheat Sheet

### simple replacement

```
python -m SimpleHTTPServer
mitmdump -dd -s "./replace.py openstack mitmproxy"

curl -s http://localhost:8000/openstack-logo.png |imgcat
curl -s --proxy http://localhost:8080 http://localhost:8000/openstack-logo.png |imgcat

curl -s http://localhost:8000/clouds.json | ack --passthru 'openstack|mitmproxy'
curl -s --proxy http://localhost:8080 http://localhost:8000/clouds.json | ack --passthru 'openstack|mitmproxy'
```

### nova list multiplier

```
nova list
export http_proxy=localhost:8080
mitmdump -dd -s "multiply.py 5"
nova list
```
