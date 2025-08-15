# Psion Time Machine

Psion Time Capsule is a web app that lets users explore archived Psion-related websites from the late '90s and early 2000s. Built from URLs found on old CD-ROMs, it offers a glimpse into the personal homepages of developers and uncovers forgotten apps from the early days of mobile computing.

# Crawling URLs on software archive : 

01-scanurl.py : This Python script is designed to scan a directory tree (including .txt files and .zip archives containing .txt files), extract all URLs found within those files, filter out unwanted URLs, and save the cleaned list of URLs to an output text file.

- 'TEXT_EXTENSIONS' = {'.txt'} can be set to multiple file extensions
- input_directory = Path(r"path/to/folder") # Put the folder structure to be scanned here
- output_urls_file = Path(r"path/to/psion_url.txt") # outputs all URLs

# URLs filtering to specific key words :

02-filterpsioncontent.py : This script is designed to analyze a list of URLs and identify which ones are related to Psion—a historic brand of mobile computing devices.

It does this by:

- Reading URLs from a text file.
- Visiting each website and checking if the page content contains keywords like "psion" or "epoc".
- Saving the matching URLs to a new file.
- Logging any URLs that failed to load (due to network issues or timeouts) for future retry.