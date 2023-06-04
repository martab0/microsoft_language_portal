# microsoft_language_portal

Script to download terminology and style guides for selected languages from [Microsoft Language Portal](https://www.microsoft.com/en-us/language)


1. `pip install -r requirements.txt`
2. Update list of languages - use the names that [Microsoft](https://www.microsoft.com/en-us/language/) uses: 
```
    languages = ['Arabic','German','Polish']
```
3. `python microsoft_terminology_and_style.py`
4. Find tbx glossaries and pdf style guides downloaded to subfolder and renamed per language