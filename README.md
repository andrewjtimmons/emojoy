#Emojoy
A quick and easy way to bulk upload custom emoji to slack.

Comes with more cat emoji because cats.

###Requirements
1. Python 2.7.X: [download](https://www.python.org/downloads/)
2. Selenium: pip install selenium
3. Chromedriver:  brew install chromedriver or [download](https://sites.google.com/a/chromium.org/chromedriver/downloads)
4. Admin access to your slack account.

###Usage
1.  Complete the requirements above and download this repo.
2.  (Optional) Add any custom emoji you want to the imgs directory or another dir.
3.  From a terminal in the repo directory run `python emojoy.py`.
4.  Follow the prompts for teamname, directory (use imgs for cats), email, and password.
5.  Watch the emoji upload like magic.

###Notes
Software is provided under the [MIT Liscense](https://opensource.org/licenses/MIT).  Emoji liscensed as per the emoji sources section.

This software asks for your password using the python [getpass library.](# https://docs.python.org/2/library/getpass.html
)  This program only takes your password and puts in it a browser, which then sends it to slack.  This program does not store your password or send it to any third parties. 

###Emoji sources
Emoji one images provided free by [Emoji One.](http://emojione.com/)

Mozilla emoji provided by Mozilla.  Here is their [github](https://github.com/mozilla/fxemoji/blob/gh-pages/LICENSE.md) and here is a link to the [apache liscense](http://www.apache.org/licenses/LICENSE-2.0) for these emoji.

