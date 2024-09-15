from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define your Google Drive API credentials and scope
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = r'C:\Users\******.json'

# Load the service account credentials from the specified file
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Google Drive API service
service = build('drive', 'v3', credentials=credentials)

# Function to generate a shareable link for a given file ID
def get_shareable_link(file_id):
    # Return the shareable link format for the Google Drive file
    link = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"
    return link

# Function to list files in a specified Google Drive folder
def list_files_in_folder(folder_id, max_pages=1, page_size=100):
    # Query to search for files in the specified folder, excluding subfolders
    query = f"'{folder_id}' in parents and mimeType != 'application/vnd.google-apps.folder'"
    page_token = None  # To manage pagination
    page_count = 0  # Track the number of pages processed
    file_number = 1  # Initialize file numbering for display

    # Loop through pages until the max number of pages is reached
    while page_count < max_pages:
        # Request the list of files in the folder
        response = service.files().list(
            q=query,
            pageSize=page_size,
            fields="nextPageToken, files(id, name)",  # Request file ID and name
            pageToken=page_token
        ).execute()

        # Get the list of files from the response
        items = response.get('files', [])
        if not items:
            print('No files found.')
            break
        
        # Loop through each file in the folder and print its name and shareable link
        for item in items:
            print(f"{file_number}. File: {item['name']}")
            link = get_shareable_link(item['id'])
            print(f"Shareable link: {link}")
            file_number += 1  # Increment the file number for display

        # Get the next page token to continue listing files if available
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break  # Exit if no more pages are available
        
        page_count += 1  # Increment the page count

# Enter the target folder ID and specify the number of pages to retrieve
folder_id = '********'  # Google Drive folder ID
list_files_in_folder(folder_id, max_pages=1, page_size=100)  # Example: get 1 page with up to 100 files
