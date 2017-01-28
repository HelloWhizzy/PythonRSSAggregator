import feedparser


class WhizRssAggregator():
    feedurl = ""

    def __init__(self, paramrssurl):
        print(paramrssurl)
        self.feedurl = paramrssurl
        self.parse()

    def parse(self):
        thefeed = feedparser.parse(self.feedurl)

        print("Getting Feed Data")
        print(thefeed.feed.get("title", ""))
        print(thefeed.feed.get("link", ""))
        print(thefeed.feed.get("description", ""))
        print(thefeed.feed.get("published", ""))
        print(thefeed.feed.get("published_parsed",
                           thefeed.feed.published_parsed))

        for thefeedentry in thefeed.entries:
            print("__________")
            print(thefeedentry.get("guid", ""))
            print(thefeedentry.get("title", ""))
            print(thefeedentry.get("link", ""))
            print(thefeedentry.get("description", ""))
            print("__________")

            # Parsing Namespaces
            for thefeednamespace in thefeed.namespaces:
                if (thefeednamespace == "media"):
                    # parse for Yahoo Media
                    print("Media")
                    allmediacontent = thefeedentry.get("media_content", "")
                    for themediacontent in allmediacontent:
                        print(themediacontent["url"])
                        print(themediacontent["height"])
                        print(themediacontent["width"])


