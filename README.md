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

4. If needed, [download the Monero CLI and RPC](https://www.getmonero.org/downloads/) for your operating system

5. Create a new stagenet wallet in the newly downloaded Moneor directory (name it 'stagenetclaim' for consistency)

   ```
   ./monero-wallet-cli --stagenet
   ```

6. In a terminal start Monero RPC (make sure to adjust flags such as --wallet-file or --stagenet)

   ```
   ./monero-wallet-rpc --stagenet --rpc-bind-port 18082 --wallet-file stagenetclaim --prompt-for-password --rpc-login test:test --daemon-host stagenet.community.xmr.to --trusted-daemon
   ```

7. Start the claimxmr server (and visit localhost:8080)

   ```
   python server.py
   ```

## ATTENTION

The code is very cringe. I'm still a beginner and this is the first version.
