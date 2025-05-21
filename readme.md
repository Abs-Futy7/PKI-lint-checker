# Certificate Linting & Inspection Tool

This Python script helps you **lint** and **inspect** certificates using [ZLint](https://github.com/zmap/zlint) and [OpenSSL](https://www.openssl.org/). It checks if your certificate is in PEM format (by examining the file, e.g., `filename.ext`), runs ZLint for compliance checks, and displays detailed certificate information.

---


## Installation

### 1. Install Python

Ensure you have Python 3.x installed. Download from [python.org](https://www.python.org/downloads/).

### 2. Install ZLint

#### On Windows (using Chocolatey):
```sh
choco install zlint
```

#### On macOS (using Homebrew):
```sh
brew install zlint
```

#### On Linux (using Go):
```sh
go install github.com/zmap/zlint/v3/cmd/zlint@latest
# Ensure $GOPATH/bin is in your PATH
```

Or download binaries from the [ZLint releases page](https://github.com/zmap/zlint/releases).

### 3. Install OpenSSL

- **Windows**: [Download OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)
- **macOS**: `brew install openssl`
- **Linux**: `sudo apt install openssl`

---

## Usage

1. Save the script as `cert_lint.py`.
2. Run it:
    ```sh
    python cert_lint.py
    ```
3. Enter the path to your certificate file (e.g., `filename.ext`) when prompted. The script will check whether the file is already in PEM format.

---

## Example Output

```
📥 Enter the path to the certificate file (.cer, .pem, etc.): filename.ext

🔍 Checking if 'filename.ext' is in PEM format...

📋 ZLint Summary Report:

... (ZLint output) ...

📄 Certificate Details:

... (OpenSSL output) ...
```

---

## Notes

- Only **PEM** format certificates are supported.
- To convert DER to PEM:
    ```sh
    openssl x509 -inform DER -in "your_cert.cer" -out "converted_cert.pem" -outform PEM
    ```

---

## License

This script is provided under the MIT License.
