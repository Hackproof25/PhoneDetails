import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import NumberParseException


def get_phone_details():
    print("""\033[95m
    
    
    _____  _                        _____       _        _ _       _                 _                
   |  __ \| |                      |  __ \     | |      (_| |     | |               | |               
   | |__) | |__   ___  _ __   ___  | |  | | ___| |_ __ _ _| |___  | |     ___   ___ | | ___   _ _ __  
   |  ___/| '_ \ / _ \| '_ \ / _ \ | |  | |/ _ | __/ _` | | / __| | |    / _ \ / _ \| |/ | | | | '_ \ 
   | |    | | | | (_) | | | |  __/ | |__| |  __| || (_| | | \__ \ | |___| (_) | (_) |   <| |_| | |_) |
   |_|    |_| |_|\___/|_| |_|\___| |_____/ \___|\__\__,_|_|_|___/ |______\___/ \___/|_|\_\\__,_| .__/ 
                                                                                               | |    
                                                                                               |_|    

    
    \033[0m""")  # Print in magenta color

    while True:
        country_code = input("\033[92mEnter country code (e.g., +1 for USA), or type 'exit' to quit: \033[0m")
        if country_code.lower() == 'exit':
            break

        phone_number = input("\033[92mEnter mobile number: \033[0m")
        full_number = f"{country_code}{phone_number}"

        try:
            parsed_number = phonenumbers.parse(full_number, None)

            # Get country and carrier information
            country = geocoder.description_for_number(parsed_number, "en")
            provider = carrier.name_for_number(parsed_number, "en")

            # Get location information
            location = geocoder.description_for_number(parsed_number, "en")

            # Get time zone information
            time_zones = timezone.time_zones_for_number(parsed_number)
            time_zone = time_zones[0] if time_zones else "Unknown"

            # Get name and other details using Truecaller API
            truecaller_api_url = f"https://api4.truecaller.com/v1/key/{country_code[1:]}/{phone_number}"
            headers = {
                "Authorization": "Your-Truecaller-API-Key",
                "Accept": "application/json"
            }
            response = requests.get(truecaller_api_url, headers=headers)
            data = response.json()

            name = data.get("name", "Unknown")
            father_name = data.get("fathers", {}).get("name", "Unknown")
            live_location = data.get("location", {}).get("city", "Unknown")

            print("\033[93mPhone Details:\033[0m")
            print(f"\033[94mCountry:\033[0m {country}")
            print(f"\033[94mCarrier:\033[0m {provider}")
            print(f"\033[94mLocation:\033[0m {location}")
            print(f"\033[94mTime Zone:\033[0m {time_zone}")
            print(f"\033[94mName:\033[0m {name}")
            print(f"\033[94mFather's Name:\033[0m {father_name}")
            print(f"\033[94mLive Location:\033[0m {live_location}")

            # Ask user if they want to quit
            exit_choice = input("\033[92mDo you want to quit? (y/n): \033[0m")
            if exit_choice.lower() == 'y':
                break
        except NumberParseException as e:
            print(f"\033[91mError parsing phone number:\033[0m {e}")
        except Exception as e:
            print(f"\033[91mError accessing Truecaller API:\033[0m {e}")


if __name__ == "__main__":
    get_phone_details()
