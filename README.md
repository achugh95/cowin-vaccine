## Cowin Vaccine Slot
This script helps in checking the available slots for the entered age-group and a particular district. You can refer to 
`district_mapping.csv` for the list of districts and their ids. If there are any slots available for the desired age 
group and district id, a pop up alert is shown.

Please note that this script has to be triggered manually and will work until stopped.

### Prerequisites

Run the following commands to install the required packages:

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### Run the script


After setting the desired values of age_group and district_id in vaccine.py while calling check_slots. Run the file as:

`python3 vaccine.py`
