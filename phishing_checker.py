import re 
from urllib.parse import urlparse



def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate =url if "://" in url else "http://" + url
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()

    if not host:
        return["could not identify a hostname."]

    if "@" in candidate:
        findings.append("contains an '@' symbol; inspect carefully.")

    if len(url) > 100:
        findings.append(" unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("uses an IP address instead of a  familiar domain .")

    labels =[part for part in host.split(".") if part]
    if len(labels) >=5:
        findings.append("contains many hostname segment/subdomains.")

    if  "xn--" in host:
        findings.append("contains a punnycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("uses HTTP.  HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does not prove safety.")


    return findings 
INFO_MESSAGES = ("No URL entered", "Could not identify", "No listed warning")

def has_warnings(findings):
    return not findings[0].startswith(INFO_MESSAGES)           
def main():
    print("EWB phishing URL Awareness Checker")
    print("text checks only - this program does not open URLs .")


    while True:
        raw_url = input("\nEnter a sample URL  (or type q to quit): ")


        if raw_url.strip().lower() in ("q","quit","exist"):
            print("Goodbye! stay alert online.")
            break

        print("\nResult:")
        finding = inspect_url(raw_url)
        for item in finding:
            print(" - " + item)

        if has_warnings(finding):
            print("\nREVIEW CAREFULLY:" + str(len(finding)) + " warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
            


    
           