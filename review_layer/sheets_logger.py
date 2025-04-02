import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetsLogger:
    def __init__(self, creds_path, sheet_name):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open(sheet_name).sheet1

    def send(self, entry):
        self.sheet.append_row(list(entry.values()))
