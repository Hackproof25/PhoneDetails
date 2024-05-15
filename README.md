
# Phone Details Lookup

This Python script allows you to look up details for a phone number, including country, carrier, location, time zone, and additional information using the Truecaller API.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)
- `phonenumbers` library (install using `pip install phonenumbers`)
- You can also install requirements by

```bash
pip install -r requirements.txt

## Usage

1. Clone the repository or download the `phone_details_lookup.py` file.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using Python:

```bash
python phone_details_lookup.py
```

4. Follow the prompts to enter the country code and phone number for which you want to look up details.
5. The script will display the phone details such as country, carrier, location, time zone, and more.
6. After each result, you will be asked if you want to continue or quit.

## Note

- You need to have a valid Truecaller API key to fetch additional details such as name, father's name, and live location.
- Replace `"Your-Truecaller-API-Key"` in the script with your actual Truecaller API key.
- Make sure to handle errors and exceptions appropriately, especially when accessing external APIs like Truecaller.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
```

Replace `"Your-Truecaller-API-Key"` with your actual API key.
