# microsoft_language_portal

Script to download terminology and style guides for selected languages from [Microsoft Language Portal](https://www.microsoft.com/en-us/language)

*Marta Bartnicka*


> The site will be removed on June 30th, 2023. You can download the existing terminology by clicking this link until then. International Style guides will be available on the Microsoft Learn Portal starting July 1st, 2023.  
After the change, [the UI strings] will only be available with a Visual Studio subscription.


1. `pip install -r requirements.txt`
2. Update list of languages - use the names that [Microsoft](https://www.microsoft.com/en-us/language/) uses, for example: 
```
    languages = ['Arabic','German','Polish']
```
3. `python microsoft_terminology_and_style.py`
4. Find tbx glossaries and pdf style guides downloaded to subfolder and renamed per language
