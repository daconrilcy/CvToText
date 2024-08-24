def csv_reader(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Exception: {e}")
        return ''