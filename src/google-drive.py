import gspread
from oauth2client.service_account import ServiceAccountCredentials

file = './client_secret.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(file, scope)

gc = gspread.authorize(credentials)

nba_sheet = gc.open("nba_sheets").sheet1

list_of_hashes = nba_sheet.get_all_records()
print(list_of_hashes)
