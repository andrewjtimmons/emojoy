#Emojoy
A quick and easy way to bulk upload custom emoji to slack.

Comes with more cat emoji because cats.

<img src="imgs/cat_face_with_tears_of_joy_emoji_one.png" width=25 height=25 />


![cat_face_with_tears_of_joy_emoji_one](https://raw.githubusercontent.com/andrewjtimmons/emojoy/master/imgs/cat_face_with_tears_of_joy_emoji_one.png%20=25ximgs/cat_face_with_tears_of_joy_emoji_one.png =25x)
![cat_face_with_tears_of_joy_mozilla](imgs/cat_face_with_tears_of_joy_mozilla.png =25x)
![cat_face_with_wry_smile_emoji_one](imgs/cat_face_with_wry_smile_emoji_one.png =25x)
![cat_face_with_wry_smile_mozilla](imgs/cat_face_with_wry_smile_mozilla.png =25x)
![crying_cat_face_emoji_one](imgs/crying_cat_face_emoji_one.png =25x)
![crying_cat_face_mozilla](imgs/crying_cat_face_mozilla.png =25x)
![grinning_cat_face_with_smiling_eyes_emoji_one](imgs/grinning_cat_face_with_smiling_eyes_emoji_one.png =25x)
![grinning_cat_face_with_smiling_eyes_mozilla](imgs/grinning_cat_face_with_smiling_eyes_mozilla.png =25x)
![kissing_cat_face_with_closed_eyes_emoji_one](imgs/kissing_cat_face_with_closed_eyes_emoji_one.png =25x)
![kissing_cat_face_with_closed_eyes_mozilla](imgs/kissing_cat_face_with_closed_eyes_mozilla.png =25x)
![pouting_cat_face_emoji_one](imgs/pouting_cat_face_emoji_one.png =25x)
![pouting_cat_face_mozilla](imgs/pouting_cat_face_mozilla.png =25x)
![smiling_cat_face_with_heart_shaped_eyes_emoji_one](imgs/smiling_cat_face_with_heart_shaped_eyes_emoji_one.png =25x)
![smiling_cat_face_with_heart_shaped_eyes_mozilla](imgs/smiling_cat_face_with_heart_shaped_eyes_mozilla.png =25x)
![smiling_cat_face_with_open_mouth_mozilla](imgs/smiling_cat_face_with_open_mouth_mozilla.png =25x)
![weary_cat_face_emoji_one](imgs/weary_cat_face_emoji_one.png =25x)
![weary_cat_face_mozilla](imgs/weary_cat_face_mozilla.png =25x)
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

I only tested this on Mac.  If you have trouble with Windows or Linux and find a solution feel free to put in a pull request.

###Emoji sources
Emoji one images provided free by [Emoji One.](http://emojione.com/)

Mozilla emoji provided by Mozilla.  Here is their [github](https://github.com/mozilla/fxemoji/blob/gh-pages/LICENSE.md) and here is a link to the [apache liscense](http://www.apache.org/licenses/LICENSE-2.0) for these emoji.

