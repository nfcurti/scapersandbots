import praw
import discord
from discord_webhook import DiscordWebhook, DiscordEmbed


reddit = praw.Reddit(client_id='1Y_dnEC6Xrlpbw', client_secret='c2kHQgaKNxdRkLorcRrcRzuk8YYaIw', user_agent='forhireScrape')
subreddit = reddit.subreddit('forhire+slavelabour+designjobs+hireawriter+jobbit')
hot_posts = subreddit.new(limit=10)


client = discord.Client()
def post_jobs():
    try:
        for submission in subreddit.stream.submissions():
            questions = ["hiring", "task"]
            normalized_title = submission.title.lower()
            for question_phrase in questions:
                if question_phrase in normalized_title:
                    print(submission.title)
                    if question_phrase in questions[0]:
                        if submission.subreddit == "designjobs":
                            webhook_urls = ['https://discord.com/api/webhooks/793504883231293460/537FucLOsNuzmTYGlDE5Y3q3BsPUuXqQul2WT4CIYrRjvypNMSkOQTjafI-7rD33FgE8']
                            webhook = DiscordWebhook(url=webhook_urls, title='New job posting added!')
                        elif submission.subreddit == "forhire":
                            webhook_urls = ['https://discord.com/api/webhooks/793120420185505834/HPdMDjEfYh3HDR1Ogn2q_qXSEWHoH6o1cgnHyKroxmGANqtpe4Yl6un4s0Cpj28C_ClF']
                            webhook = DiscordWebhook(url=webhook_urls, title='New job posting added!')
                        elif submission.subreddit == "hireawriter":
                            webhook_urls = ['https://discord.com/api/webhooks/793507079314472992/p-gIMsIMwuN3rc2VFyjCalbSLEBNswqjC90tOpB877lDuuLBm0GYhFNGJfV6aYtoXxXO']
                            webhook = DiscordWebhook(url=webhook_urls, title='New job posting added!')
                        elif submission.subreddit == "jobbit":
                            webhook_urls = ['https://discord.com/api/webhooks/793507407761244180/8-eYhP_5bhjv9Je21vj-0wYoht4Mii5E27JQp508OO_I2RsGRZxVf8s1nbwJkCTYeGhE']
                            webhook = DiscordWebhook(url=webhook_urls, title='New job posting added!')
                        
                    elif question_phrase in questions[1]:
                        webhook_urls = ['https://discord.com/api/webhooks/793497863510294539/MgZT5cOJWwUZH5sR6RA7Fn-9WEvE02YVL61NXkVc66KTEZj7YiJPJJQm0L-kixu48LIC']
                        webhook = DiscordWebhook(url=webhook_urls, title='New job posting added!') 
                    embed = DiscordEmbed(title="Click here", description=submission.title, color=242424, url=submission.url)
                    webhook.add_embed(embed)
                    response = webhook.execute()
    except:
        post_jobs()
        
post_jobs()



            



