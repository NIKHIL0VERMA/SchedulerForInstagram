
# Scheduler For Instagram

Recently, I found about the meta business suit.<br>

I'm hardworking guys but not a labour :sweat_smile: I get distracted easily that's why Meta Business Suit work like charm 'cause it let me schedule posts.<br>

It let me schedule post but for that I need to schedule each post by myself, so I just automate the whole process :grin::grin::grin:<br>

An automation for bulk uploading posts on **IG** aka **Instagram**

#### Tested with
- OS - Windows 10 
- Browser - Chromium
- IDE - Pycharm with venv

#### Libraries used
- [WebBot](https://github.com/nateshmbhat/webbot) for browser control
- [Selenium](https://www.selenium.dev/)~3.141.0 (For compatibility)
- [AutoIT](https://www.autoitscript.com/site/) for uploading file


### Features
- Schedule 1 photo each day
- Auto delete scheduled photo
- One time login
- Cookies re-use

### Need to Add
- Add support for other formats
- Time configurable
- Different tags for each post
- Config for IG stories & videos

### Limitation
- Time fixed at `11:00:AM`
- Works only in India

### Overcomes
- Change time in [scheduler.py](scheduler.py)
- Change `web.click('फ़ोटो जोड़ें')` to corresponding elements' text

### How to use

#### Install
- Checkout main branch using your favourite IDE
- Install [requirements](requirements.txt)

#### Config script
- Add photos to [toInstaPost](toInstaPost) folder
- Fill your tags for post in [this](toInstaPost/tags.txt) file
- Add your username and password of Instagram in [this](toInstaPost/user.txt) file

##### Run
- Run [main.py](main.py)
- Input no. of days to skip

### Contribution
Anyone can contribute but be sure your pull should
- Add feature
- Fix any bug
- Have comments for me/others

Pretty basic :wink:

### Support
- [@STUGRAMMING](https://www.instagram.com/stugramming/) for memes
- [Play Store](https://play.google.com/store/apps/dev?id=5011720043750659265)