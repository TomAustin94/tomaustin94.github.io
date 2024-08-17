import feedparser
import datetime

def fetch_medium_posts():
    feed_url = "https://medium.com/@TomTalksIT/feed"
    feed = feedparser.parse(feed_url)
    
    markdown_content = "\n\n"

    
    for entry in feed.entries[:5]:  # Get the 5 most recent posts
        title = entry.title
        link = entry.link
        published = datetime.datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
        published_formatted = published.strftime("%B %d, %Y")
        
        markdown_content += f"## [{title}]({link})\n"
        markdown_content += f"*Published on: {published_formatted}*\n\n"
        
        # Add a brief excerpt if available
        if 'summary' in entry:
            summary = entry.summary.split('<p>')[1].split('</p>')[0]  # Extract text from HTML
            markdown_content += f"{summary[:150]}...\n\n"
        
        markdown_content += "---\n\n"
    
    return markdown_content

def update_markdown_file(content):
    with open('medium-feed.md', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    content = fetch_medium_posts()
    update_markdown_file(content)
