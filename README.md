# Python Ransomware

## Prerequisites

To run this ransomware, follow these steps:

1. Launch the server file first, which sets up listening.
2. Next, launch the client file.
3. Make sure you have Cryptodome installed. If you're using the script dedicated to Ubuntu, also check for the installation of Cryptography.

## Operation

This ransomware is a demonstration for educational purposes only and is by no means intended for malicious use.

1. **Launch the Server**

   - When you launch the server, a pair of private and public keys is created.
   - The public key is sent immediately after a connection, while the private key requires an action from the client (simulating the payment of the ransom).

2. **Launch the Client**

   - Once the client script is launched, a connection is established with the server on port 3000.
   - The client receives the public key and encrypts the files in the current directory. It is possible to move up and encrypt other files.
   - Encryption is done with the public key.

3. **Wait for the Countdown to Finish**

   - **CAUTION!** If you close the countdown window before the timer finishes (10 seconds in this quick example), decryption will not occur, and your files will remain encrypted.
   - Failure to comply with this instruction will result in being blocked.

4. **Once the Countdown is Complete**

   - The script will prompt you to enter something. Enter "pay" to decrypt your files.
   - Once you enter "pay" (simulating payment of the ransom), the private key is sent from the server to the client, allowing for file decryption.

## Summary, Attention:

1. Launch the server.
2. Launch the client.
3. Wait for the countdown to finish and close the window.
4. Enter "pay".

## Issues Encountered

Depending on the operating system, various problems may arise:

- On Ubuntu, use "from cryptography.hazmat.primitives.asymmetric import rsa" or "from cryptography.fernet import Fernet". Personally, I have implemented the second option, which uses symmetric encryption.
- On Debian, the RSA module is available from Crypto.PublicKey.
- On Kali, it is advisable to import the RSA module using Cryptodome.PublicKey, as here asymmetric encryption is used, and the encryption key differs from the decryption key.


