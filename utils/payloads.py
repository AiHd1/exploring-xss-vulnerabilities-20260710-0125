def load_payloads(file_path):
    """
    Load XSS payloads from a file.

    :param file_path: Path to the file containing payloads.
    :return: A list of payloads.
    "try:
        with open(file_path, 'r') as file:
            payloads = file.readlines()
        return [payload.strip() for payload in payloads if payload.strip()]
    except FileNotFoundError:
        logging.error(f"Payload file not found: {file_path}")
        return []
    except Exception as e:
        logging.error(f"An error occurred while reading the payload file: {e}")
        return []