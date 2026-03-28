# The HTTPS Protocol
In modern networks, Hypertext Transfer Protocol Secure (HTTPS) is used to securely send data between clients and servers on the web. It is a secure implementation of the previously used Hypertext Transfer Protocol (HTTP), which encrypts data while it is in transmission to protect against attacks like man-in-the-middle attacks and packet sniffing. Note that HTTPS isn't actually a separate protocol to HTTP, it is essentially just HTTP using TLS/SSL encryption.

It relies on a protocol called Transport Layer Security (TLS), which uses asymmetric key cryptography to initiate the communication and symmetric key cryptography for the actual communication. It utilises both a private key (which is held by the server) and a public key (which is provided to anyone accessing the server). Using the private key, information encrypted with the public key can be decrypted (and vice versa). This allows sensitive data to be securely transferred over the network.

For servers on the internet to enable HTTPS, they must have an SSL certificate from a trusted Certificate Authority (CA). These certificates contain a digital signature from the CA to verify that the certificate does indeed belong to that server (and it isn't being forged by some bad actor). Clients accessing these servers then validate the certificate's signature through a process known as an SSL/TLS handshake.

The SSL/TLS handshake takes place as soon as the client tries to communicate with the server. It begins with the client and server agreeing on the protocol and cipher suite (a set of algorithms to securely establish the connection). The client then authenticates the server by verifying its certificate, which is done by the server sending its certificate and the public key. The client then does some further checks on the certificate to ensure it is legitimate, including validating that the certificate was issued by a CA which the client trusts (which are typically handled by the browser). Once this is done, session keys are generated so that communication can use symmetric encryption (i.e. they use the same key for encryption and decryption) because it is faster.

<br>

# References
Cloudflare, Inc. "What is HTTPS?". Accessed: Mar. 10, 2026. [Online]. Available: https://www.cloudflare.com/en-gb/learning/ssl/what-is-https/

C. Chipeta and P. Ross. "What is HTTPS? How it Works and Why It's So Important". UpGuard, Inc. Accessed: Mar. 10, 2026. [Online]. Available: https://www.upguard.com/blog/what-is-https

Namecheap, Inc. "Understanding How SSL Encryption Works". Accessed: Mar. 10, 2026. [Online]. Available: https://www.namecheap.com/support/knowledgebase/article.aspx/10595/38/understanding-how-ssl-encryption-works/

Australian Signals Directorate. "Implementing certificates, TLS, HTTPS and opportunistic TLS". Accessed: Mar. 10, 2026. [Online]. Available: https://www.cyber.gov.au/business-government/protecting-devices-systems/hardening-systems-applications/web-hardening/implementing-certificates-tls-https-and-opportunistic-tls

Cloudflare, Inc. "What happens in a TLS handshake? | SSL handshake". Accessed: Mar. 10, 2026. [Online]. Available: https://www.cloudflare.com/en-gb/learning/ssl/what-happens-in-a-tls-handshake/