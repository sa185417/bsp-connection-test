# bsp-connection-test
This proves out the ability to keep the connection to BSP apigee servers alive with a simple GET request to the /bsp-network-connectivity endpoint.

To run it without the keepalive requests:
`python3 ./bsp-test.py`

To run it with the keepalive requests, just add keepalive as the first argument
`python3 ./bsp-test.py keepalive`
