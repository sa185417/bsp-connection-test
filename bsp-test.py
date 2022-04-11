# This proves out the ability to keep the connection to BSP apigee servers alive with a simple
# GET request to the /bsp-network-connectivity endpoint.
#
# To run it without the keepalive requests:
#    python3 ./bsp-test.py
#
# To run it with the keepalive requests, just add keepalive as the first argument
#    python3 ./bsp-test.py keepalive

import http.client
import ssl
import time
import sys

def main():
    context = ssl.SSLContext()  # The default ssl truststore
    
    # Open up an https connection.
    conn = http.client.HTTPSConnection("api.ncr.com", context=context)
    print("Connection opened [api.ncr.com]")

    # Send an http request
    try:
        print("Sending first request")
        conn.request("GET","/bsp-network-connectivity")
        resp = conn.getresponse()
        data = resp.read()
        print(resp.status, data)

        # Test to see if we are doing the keepalive test
        if len(sys.argv) > 1 and sys.argv[1] == "keepalive":
            print("Sending messages every 60 seconds for 3 minutes")
            for i in range(3):
                time.sleep(60)
                conn.request("GET","/bsp-network-connectivity")
                resp = conn.getresponse()
                data = resp.read()
                print(resp.status, data)
        else:
            print('Sleeping for 2.5 minutes...')
            time.sleep(150) # Sleep for 2.5 minutes
        
        print('Sending final request')
        conn.request("GET","/bsp-network-connectivity")
        resp = conn.getresponse()
        data = resp.read()
        print(resp.status, data)
    finally:
        conn.close()
        print("Connection closed")

if __name__ == '__main__':
    main()