# claimxmr

A custodial service that lets you easily distribute Monero to newbees and others.

1. Visit the website,
2. create a new link,
3. pay Monero to the subaddress,
4. send the link to the recipient.

## Installation

1. Create a virtual environment

   ```
   python -m venv venv
   ```

2. Activate the virtual environment

   ```
   source venv/bin/activate
   ```

3. Install cherrypy, requests and qrcode

   ```
   pip install cherrypy qrcode requests
   ```

4. In a terminal start the Monero RPC with these flags:

   ```
   ./monero-wallet-rpc --stagenet --rpc-bind-port 18082 --wallet-file stagenetclaim --prompt-for-password --rpc-login test:test
   ```

5. Start the claimxmr server (and visit localhost:8080)
   ```
   python server.py
   ```

## ATTENTION

The code is very cringe. I'm still a beginner and this is the first version.
