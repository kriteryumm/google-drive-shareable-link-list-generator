# Google Drive Shareable Link List Generator
Project interacts with the Google Drive API to list files in a specified folder and generate shareable links for each file. Using service account credentials, it allows for easy access to Google Drive contents programmatically. This tool is useful for automating file management tasks, particularly for generating and sharing links to files stored in a Google Drive folder.

## Additional information for the code:
### max_pages: 
Specifies the maximum number of pages to retrieve. This parameter controls how many pages the loop can process.

### page_size: 
Specifies the number of files on each page. The maximum pageSize in Google Drive API can be 1000, so it is set to 100 here.

### page_token: 
The token used to retrieve the next page. If there is a next page, this token is used to move to the new page.

This code processes up to a certain number of pages to get the share links of the files. If you want to get all the files, you can keep the max_pages value high or process all the pages by setting it to None.
 

## The output of the code : 

<img width="561" alt="google-drive-link-list-result" src="https://github.com/user-attachments/assets/79021387-b65a-40d3-8a76-73450b1f7e1a">
