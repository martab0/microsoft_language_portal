# microsoft_language_portal

Script to download terminology and style guides for selected languages from [Microsoft Language Portal](https://www.microsoft.com/en-us/language)

*Marta Bartnicka*


> The site will be removed on June 30th, 2023. You can download the existing terminology by clicking this link until then. International Style guides will be available on the Microsoft Learn Portal starting July 1st, 2023.  
After the change, [the UI strings] will only be available with a Visual Studio subscription.


1. `pip install -r requirements.txt`
2. Update list of languages - use the names that Microsoft uses, and they can differ for [terminology](https://www.microsoft.com/language/Terminology) and for [style guides](https://www.microsoft.com/language/StyleGuides), for example: 
```
    terminology_languages = ['Arabic', 'Chinese Simp.', 'Chinese Trad. (HK, SAR)', 'Chinese Trad. (Taiwan)', 'French', 'French (Canada)', 'German', 'Italian', 'Japanese', 'Korean', 'Norwegian (Bokmål)', 'Norwegian (Nynorsk)', 'Polish', 'Portuguese (Brazil)', 'Portuguese (Portugal)', 'Russian', 'Spanish', 'Spanish (Mexico)', 'Ukrainian']
    
    styleguides_languages = ['Arabic', 'Chinese (Simplified)', 'Chinese (Traditional)', 'French (Canada)', 'French (France)', 'German', 'Italian', 'Japanese', 'Korean', 'Norwegian Bokmål', 'Norwegian Nynorsk', 'Polish', 'Russian', 'Portuguese (Brazil)', 'Portuguese (Portugal)', 'Spanish (Neutral)', 'Spanish (Mexico)', 'Spanish (Spain)', 'Spanish (US)', 'Ukrainian']
```
3. `python microsoft_terminology_and_style.py`
4. Find tbx glossaries and pdf style guides downloaded to subfolder and renamed per language
