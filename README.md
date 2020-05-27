# monopoly
Monopoly ticket extractor

This is my first useful python code inspired by real life problem. 

This code is designed to speed up the process of entering codes that come with monopoly game tickets. This game is played at leading grocery stores and chain restaraunts like McDonalds. Customers receive tickets for purchasing groceries and have to manually enter a 16 digit code on shopplaywin.com for each ticket. 

It works by running a for loop through your designated folder holding photos of your monopoly tickets. Text is extracted from each image, regex looks for 16 digit pattern of ****-****-****-**** in the text, if pattern is found then it is added to code_list. After all images processed, selenium opens up firefox, navigates through buttons using css_selectors mostly, selenium enters login information and then loops through code_list, entering each code one at a time and submitting it to claim the potential prize. 

Make sure to take a clean photo, pytesseract is sensitive. 

Make sure to change your image directory, and also enter your login information if you want to use the code to login to shopplaywin using firefox. 

I had about a 75% success rate pulling text, finding the code and entering it automatically using this code.
