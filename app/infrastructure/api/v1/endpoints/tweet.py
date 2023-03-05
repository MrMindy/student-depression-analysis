from fastapi import APIRouter
from typing  import List

import snscrape.modules.twitter as sntwitter

router = APIRouter()


@router.get("/tweet/{text}")
def search_tweets(text: str, since: str = "", until: str = "", limit: int = 100):

    query  = ""
    tweets = []

    if text:
        query += f"{text}"

    if until:
        query += f" until:{until}"

    if since:
        query += f" since:{since}"

    #query += f" {settings.TWEETS_LANGUAGE}"
    #TODO: Check why tweets language is not working

    query  = query.strip()

    scraper = sntwitter.TwitterSearchScraper(query)

    for tweet in scraper.get_items():

        if len(tweets) == limit:
            break

        tweets.append({
            "username": tweet.user.username,
            "text": tweet.rawContent,
            "date": tweet.date
        })

    return tweets

@router.get("/tweet")
def search_users_tweets(usernames, since: str = "", until: str = "", limit: int = 100):

    usernames = usernames.split(",")
    tweets    = []

    for username in usernames:

        query  = ""
        query += f"(from:{username})"

        if until:
            query += f" until:{until}"

        if since:
            query += f" since:{since}"

        query  = query.strip()

        scraper   = sntwitter.TwitterSearchScraper(query)
        iteration = 0

        for tweet in scraper.get_items():

            if iteration == limit:
                    break

            tweets.append({
                    "username": tweet.user.username,
                    "text": tweet.rawContent,
                    "date": tweet.date
            })

            iteration += 1

    return tweets
