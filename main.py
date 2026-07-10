import argparse
import logging
import requests
from core.scanner import XSSScanner
from utils.payloads import load_payloads
from utils.output import save_results

def setup_logging(verbose):
    """Set up logging configuration."
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Main function to parse arguments and run the XSS scanner."""
    parser = argparse.ArgumentParser(description='XSS Vulnerability Explorer')
    parser.add_argument('-u', '--url', required=True, help='The target URL to test for XSS vulnerabilities.')
    parser.add_argument('-p', '--payloads', default='utils/default_payloads.txt', help='Path to a file containing custom payloads (one per line).')
    parser.add_argument('-o', '--output', help='Path to a file where the results will be saved.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging.')
    args = parser.parse_args()

    setup_logging(args.verbose)

    try:
        payloads = load_payloads(args.payloads)
        scanner = XSSScanner(args.url, payloads)
        results = scanner.scan()
        if args.output:
            save_results(results, args.output)
        else:
            for result in results:
                print(result)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()