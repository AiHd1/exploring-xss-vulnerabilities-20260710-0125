import logging
import requests

class XSSScanner:
    """Class to perform XSS scanning on a target URL with given payloads."""

    def __init__(self, url, payloads):
        """
        Initialize the XSSScanner with a target URL and a list of payloads.

        :param url: The target URL to test for XSS vulnerabilities.
        :param payloads: A list of XSS payloads to test.
        """
        self.url = url
        self.payloads = payloads

    def scan(self):
        """
        Perform the XSS scan by injecting each payload into the URL and checking the response.

        :return: A list of results indicating whether each payload was successful.
        """
        results = []
        for payload in self.payloads:
            try:
                response = requests.get(self.url, params={'input': payload})
                if payload in response.text:
                    results.append(f"Payload '{payload}' was reflected in the response.")
                else:
                    results.append(f"Payload '{payload}' was not reflected in the response.")
            except requests.RequestException as e:
                logging.error(f"Request failed for payload '{payload}': {e}")
                results.append(f"Request failed for payload '{payload}': {e}")
        return results