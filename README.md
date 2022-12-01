
# Ozain Parser
Simple function to parse USFM files in **chapter-verse structure**.
This function removes all formatting markdowns and preserves only text of file.
The text will be organized in a dict, with chapter -> verse levels and remove all others markdowns.
Some metadata (file_encoding, usfm_version etc) will be returned in the dict.

## Example
Get the 9º verse of chapter 137 in Psalms.txt file.
- **from ozain.main import parser**
- **psalms = parser("Psalms.txt")**
- **psalms[137][9]**

Will return:
> **Happy is the one who takes your babies and smashes them against the rocks!**

    USFM is a standard markdown for digital versions of the Bible in different languages.
    Organized by United Bible Societies, the USFM format is an attempt to unify the digital format for Bible texts in a single markdown.

    for more information, see: https://paratext.org/usfm/
    THis Lib is recommended for simplified versions (usfm-s)

