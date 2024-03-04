# LatticeStreamCrypt

LatticeStreamCrypt is a quantum-resistant hybrid encryption system designed to secure communications in the post-quantum era. It combines the power of Kyber, a lattice-based key encapsulation mechanism, with the efficiency of BLAKE3 hash function for stream cipher encryption, offering a robust solution against both classical and quantum computing threats.

## Features

- **Quantum-Resistant Key Exchange**: Utilizes the Kyber algorithm for secure key exchange, ensuring forward secrecy and resistance against quantum computing attacks.
- **Efficient Encryption**: Incorporates BLAKE3 for fast and secure symmetric encryption, providing high throughput and low latency for streaming data.
- **Hybrid Approach**: Leverages the strengths of both post-quantum and symmetric cryptography, offering a comprehensive security solution.

### Installation

```bash
git clone https://github.com/afkaf/LatticeStreamCrypt-Hybrid-Kyber.git
```

## Required DLL

This project requires the `kyberk2so.dll` that is included in the repo for convenience. It is a C-shared library compiled for 64-bit Windows systems. To compile it yourself you'll need Go installed and a C compiler. For Windows users navigate to the kyberk2so folder in the project directory using your terminal and enter these commands:
```bash 
go mod init kyberk2so

go get -u github.com/symbolicsoft/kyber-k2so

go build -o kyberk2so.dll -buildmode=c-shared kyberk2so.go
```
After building the dll, place it in the same directory as `kyberk2so.py` and `LatticeSteamCrypt.py`.

### Prerequisites

- Python 3.6
- Numpy
- blake3

### Usage

```python
from LatticeStreamCrypt import create_keypair, encrypt, decrypt

private_key, public_key = create_keypair()

data = b'Hello, quantum world!'

encrypted_data = encrypt(data, public_key)
decrypted_data = decrypt(encrypted_data, private_key)

assert data == decrypted_data, "Decryption failed!"
```

## Built With

- [Kyber-K2SO](https://github.com/symbolicsoft/kyber-k2so) - The Go language Kyber implementation used for quantum-resistant key exchange.
- [BLAKE3](https://github.com/BLAKE3-team/BLAKE3) - The cryptographic hash function used for efficient stream cipher encryption.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The `kyberk2so.dll` is built using the [Kyber-K2SO Go library by Symbolic Software](https://github.com/symbolicsoft/kyber-k2so), published under the MIT License. This project owes its gratitude to the creators of Kyber-K2SO for their pioneering work in post-quantum cryptography.
