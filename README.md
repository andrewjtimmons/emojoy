#Emojoy
A quick and easy way to bulk upload [custom emoji to slack.](https://get.slack.help/hc/en-us/articles/206870177-Creating-custom-emoji)

Comes with more cat emoji because cats.

<img src="imgs/cat_face_with_tears_of_joy_emoji_one.png" width=33 height=33 />
<img src="imgs/cat_face_with_tears_of_joy_mozilla.png" width=33 height=33 />
<img src="imgs/cat_face_with_wry_smile_emoji_one.png" width=33 height=33 />
<img src="imgs/cat_face_with_wry_smile_mozilla.png" width=33 height=33 />
<img src="imgs/crying_cat_face_emoji_one.png" width=33 height=33 />
<img src="imgs/crying_cat_face_mozilla.png" width=33 height=33 />
<img src="imgs/grinning_cat_face_with_smiling_eyes_emoji_one.png" width=33 height=33 />
<img src="imgs/grinning_cat_face_with_smiling_eyes_mozilla.png" width=33 height=33 />
<img src="imgs/kissing_cat_face_with_closed_eyes_emoji_one.png" width=33 height=33 />
<img src="imgs/kissing_cat_face_with_closed_eyes_mozilla.png" width=33 height=33 />
<img src="imgs/pouting_cat_face_emoji_one.png" width=33 height=33 />
<img src="imgs/pouting_cat_face_mozilla.png" width=33 height=33 />
<img src="imgs/smiling_cat_face_with_heart_shaped_eyes_emoji_one.png" width=33 height=33 />
<img src="imgs/smiling_cat_face_with_heart_shaped_eyes_mozilla.png" width=33 height=33 />
<img src="imgs/smiling_cat_face_with_open_mouth_emoji_one.png" width=33 height=33 />
<img src="imgs/smiling_cat_face_with_open_mouth_mozilla.png" width=33 height=33 />
<img src="imgs/weary_cat_face_emoji_one.png" width=33 height=33 />
<img src="imgs/weary_cat_face_mozilla.png" width=33 height=33 />

###Requirements
1. Python 2.7.X: [download](https://www.python.org/downloads/)
2. Selenium: `pip install selenium`
3. Chromedriver:  `brew install chromedriver` or [download](https://sites.google.com/a/chromium.org/chromedriver/downloads)

###Usage
1.  Satisfy the requirements above and download this repo.
2.  (Optional) Add any custom emoji you want to the imgs directory or another dir.
3.  From a terminal in the repo directory run `python emojoy.py`.
4.  Follow the prompts for teamname, directory (use `imgs` for the cats in this repo), email, and password.
5.  Watch the emoji upload like magic, or go pet a real cat.  You earned it.

###Notes
Software is provided under the [MIT Liscense](https://opensource.org/licenses/MIT).  Emoji liscensed as per the emoji sources section.

This software asks for your password using the python [getpass library.](# https://docs.python.org/2/library/getpass.html
)  This program only takes your password and puts in it a browser, which then sends it to slack.  This program does not store your password or send it to any third parties.  But don't believe me, read the code!

I only tested this on Mac.  If you have trouble with Windows or Linux and find a solution feel free to put in a pull request.

###Emoji sources
Emoji one images provided free by [Emoji One.](http://emojione.com/)

Mozilla emoji provided by Mozilla.  Here is their [github](https://github.com/mozilla/fxemoji/blob/gh-pages/LICENSE.md) and here is a link to the [apache liscense](http://www.apache.org/licenses/LICENSE-2.0) for these emoji.

