1. Put a URL on the clipboard.
2. Insert a Yubikey with CCID on. (This is why the script is called ykgodot:
first it waits for a URL then it waits for a Yubikey. So much waiting.)
3. [pass](http://www.passwordstore.org/) will be called automatically to copy
the password for the domain of the URL. We use [tldextract](https://github.com/john-kurkowski/tldextract)
to find the domain.
4. On Linux (tested) and Mac OS X (untested) a notification will appear about the successful copying.

Optionally, install the [copy url](https://chrome.google.com/webstore/detail/copy-url/mkhnbhdofgaendegcgbmndipmijhbili?hl=en) extension into Chrome.

pip can install both pyperclip and tldextract. No other dependencies.
