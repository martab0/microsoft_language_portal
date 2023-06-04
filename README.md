# microsoft_language_portal

Script to download terminology for selected languages from [Microsoft Language Portal](https://www.microsoft.com/en-us/language)

**Downloading glossaries**

1. `pip install -r requirements.txt`
2. update list of languages - use the names that [Microsoft](https://www.microsoft.com/en-us/language/) uses: 
```
    languages = ['Arabic','German','Polish']
```
3. `python microsoft_terminology_and_style.py`
4. find tbx glossaries downloaded to subfolder and renamed per language

*Downloading style guides TBD*

Add "styleguides" to script if you want to see what's wrong with Style Guides :-)
```
    assets = [styleguides, terminology]
```
