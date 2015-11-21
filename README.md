# Purpose:
Create an aggregate and lightweight format of the Trans-Pacific Partnership for easy readability and parsing.

# Included:
`TTP.txt` - All 30 chapters of TPP in plain text  
`TTP.json` - All 30 chapters of TPP in JSON format  
`TTP_scrape.py` - Python script used to scrape the data

# JSON format
The the text of each chapter is broken down by line:
```
{“Chapter”: 
	{“text”: [“chapter_line”, “chapter_line”],
	 “title”: “chapter_title”,
	 “url”: “chapter_url”
	}
}
```
