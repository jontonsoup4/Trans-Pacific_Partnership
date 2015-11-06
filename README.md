# Purpose:
Create an aggregate and lightweight format of the Trans-Pacific Partnership for easy readability and parsing

# Included:
`TTP.txt` - All 30 chapters of in plain text
`TTP.json` - All 30 chapters in JSON format

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