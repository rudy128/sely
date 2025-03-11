# Installation
## Office365 Pro Plus Installation and Activation

- Step 1:- Install O365ProPlusRetail 'Offline Installer' from [here](https://gravesoft.dev/office_c2r_links)

- Step 2:- Copy paste this command in PowerShell
```
irm https://get.activated.win | iex
```
(Reference Taken from [here](https://massgrave.dev/#method_1_-_powershell))

- Step 3:- You will see the activation options.
- - Choose [1] HWID for Windows activation.
- - Choose [2] Ohook for Office activation.

All links have been gathered from this [reddit post](https://www.reddit.com/r/Piracy/comments/1814gmp/guide_how_to_pirate_microsoft_office_properly/)
## Script Installation
```
python -m venv venv
pip install selenium pyautogui openpyxl supabase us pywin32 python-dotenv supabase pytz
```

# Run script for Automation
Open excel.py and email.py separately 
```
python excel.py
python email.py
```