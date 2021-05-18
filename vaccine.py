import json
import time
import tkinter
from _datetime import datetime
from tkinter import messagebox

import requests


def get_current_date():
    return datetime.now().date().strftime("%d-%m-%Y")


def get_api_results(district_id):
    curr_date = get_current_date()
    print(f"Checking on: {curr_date} for district_id: {district_id}")
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict"
    params = {
        "district_id": district_id,
        "date": curr_date
    }
    # Faking as browser request
    browser_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/56.0.2924.76\
                        Safari/537.36'
    }
    api_response = requests.get(url=url, params=params, headers=browser_headers)
    return json.loads(api_response.text)


def show_popup_alert(center, session):
    # This code is to hide the main tkinter window
    root = tkinter.Tk()
    root.withdraw()

    # Message Box
    messagebox.showinfo("SLOT AVAILABLE", f"Slots Available: {session['available_capacity']} \n {center['name']}")


def check_slots(age_group, district_id):
    response = get_api_results(district_id)
    # print(response)
    required_centers = 0
    available_for_booking = 0
    for k, v in response.items():
        if k == "centers":
            for center in v:
                center_sessions = center.get("sessions")
                if center_sessions and len(center_sessions) > 0:
                    for session in center_sessions:
                        if session.get('min_age_limit') == age_group:
                            required_centers += 1
                            print("---")
                            print(session['date'], center['name'])
                            if session.get("available_capacity") > 0:
                                available_for_booking += 1
                                print("**** Available *****")
                                print(f"{session['date']} | {session['vaccine']} \
                                | Slots:{session['available_capacity']}")
                                print(f"{center['name']} | {center['address']} | {center['district_name']} | "
                                      f"{center['state_name']} | {center['block_name']} | {center['pincode']}")

                                # NOTE: Additional functions like notifications can be called here
                                show_popup_alert(center=center, session=session)
            print(f"\n\nTotal {age_group}+ centers on portal: {required_centers}")
            print(f"Available for booking: {available_for_booking}\n")

    # Rate limiter - 100 per 5 minutes
    time.sleep(10)


while True:
    check_slots(age_group=18, district_id=195)  # Check district_mapping.csv for district_ids
