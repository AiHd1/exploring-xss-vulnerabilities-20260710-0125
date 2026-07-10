def save_results(results, file_path):
    """
    Save the scan results to a file.

    :param results: List of scan results.
    :param file_path: Path to the file where results will be saved.
    "try:
        with open(file_path, 'w') as file:
            for result in results:
                file.write(result + '\n')
        logging.info(f"Results saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while saving results: {e}")