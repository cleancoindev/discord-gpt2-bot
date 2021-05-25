# Discord GPT-2 Bot

## Dependencies:
Tensorflow-gpu v. 1.15, Python 3.7.x or earlier, gpt_2_simple, Pytorch, NLTK, discord.py

## Setup
Clone this repo. Make sure you have a few GB of space as the models can take up some room as they grow.

Using a Python 3.x version prior to 3.8, install Tensorflow-gpu 1.15 (later versions will not work with the gpt_2_simple model), pytorch, nltk and discord.py. This can be done with `pip install -r requirements.txt`.

After you've created a bot account on Discord's developer portal, it will give you a token. Make a file called `token.txt` and paste the token into the file.

Now you must train the model. There are two ways to do so.
1. You can use this [Google Colab](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) notebook to train the model on Google's servers for free.
2. You can run bot.py and the first runthrough will download the model and train on the reddit_comments.txt file. You can use your own file if desired, and I would recommend changing this BEFORE running bot.py if at all. Training will take around 20-40 minutes, but you only have to do it once.

After inviting the bot to your server, you can summon it using the &talk command, giving it a few words following the command to "think" about when formulating a response. The bot will also randomly respond to about 10% of messages.