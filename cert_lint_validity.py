import subprocess
import os

def pem_format(file_path):
    try:
        with open(file_path, 'r') as f:
            first_line = f.readline()
            return "BEGIN CERTIFICATE" in first_line
    except Exception:
        return False

def lint_certificate(cert_path):
    if not os.path.isfile(cert_path):
        raise FileNotFoundError("Certificate file not found.")

    try:
        result = subprocess.run(
            ["zlint", "-summary", cert_path],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error running zlint:", e.stderr)
        return None

def display_summary(text_output):
    print("\n📋 ZLint Summary Report:\n")
    print(text_output)

def show_certificate_details(cert_path):
    try:
        result = subprocess.run(
            ["openssl", "x509", "-in", cert_path, "-text", "-noout"],
            capture_output=True, text=True, check=True
        )
        print("\n📄 Certificate Details:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error showing certificate details:", e.stderr)

if __name__ == "__main__":
    cert_file = input("Enter the path to the certificate file (.cer, .pem, etc.): ").strip()
    if not pem_format(cert_file):
        print("❌ Only PEM format certificates are supported.")
        print('👉 To convert a DER (.cer/.der) certificate to PEM, use:')
        print('   openssl x509 -inform DER -in "your_cert.cer" -out "converted_cert.pem" -outform PEM')
    else:
        summary = lint_certificate(cert_file)
        if summary:
            display_summary(summary)
        show_certificate_details(cert_file)
