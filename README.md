# bsp-connection-test
This proves out the ability to keep the connection to BSP apigee servers alive with a simple GET request to the /bsp-network-connectivity endpoint.

To run it without the keepalive requests:

`python3 ./bsp-test.py`

To run it with the keepalive requests, just add keepalive as the first argument

`python3 ./bsp-test.py keepalive`


## Results
You will notice that without the keepalive requests the connection gets closed by the remote server after 120 seconds. It will look like this `http.client.RemoteDisconnected: Remote end closed connection without response`

With the keepalive, however, this does not occur.
