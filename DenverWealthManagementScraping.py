import datetime
import requests
import json
import time
import os
from tqdm import tqdm

def fetch_posts(t1_str, t2_str, base_url, search_terms):
    url_params = {
        'count': 100,
        'sortBy': 'DATE',
        'startDate': t1_str,
        'endDate': t2_str,
        'searchTerm': ' OR '.join(search_terms),
        'language': 'EN'
    }
    full_post_data = []

    # Make the initial request to get the total number of posts for pagination
    response = requests.get(base_url, params=url_params)
    data = response.json()
    total_posts = data.get('result', {}).get('hitCount', 0)

    # Iterate through pages of results
    for page in tqdm(range(0, int(total_posts / url_params['count']) + 1)):
        url_params['offset'] = page * url_params['count']
        response = requests.get(base_url, params=url_params)
        data = response.json()
        posts = data.get('result', {}).get('posts', [])

        # Replace the section here with your requested modification
        for post in posts:
            post_data = {
                'username': post.get('creator', {}).get('name', 'N/A'),
                'message': post.get('message', 'N/A'),
                'link': post.get('link', 'N/A')
            }
            full_post_data.append(post_data)

    return full_post_data

def main():
    base_url = "https://api.crowdtangle.com/posts/search?token="Enter_CT_KEY_HERE"  # Placeholder token
    
    search_terms = [
    "denver wealth management",
    "denver luxury real estate",
    "denver real estate investment",
    "denver commercial real estate",
    "denver residential real estate",
    "denver business owner",
    "denver small business success",
    "denver entrepreneurship",
    "denver startup founder",
    "denver venture capital",
    "denver angel investor",
    "denver private equity",
    "denver investment portfolio",
    "denver business expansion",
    "denver industry leader",
    "denver executive level",
    "denver corporate governance",
    "denver board member",
    "denver business acquisition",
    "denver mergers and acquisitions",
    "denver wealth creation",
    "denver financial independence",
    "denver asset management",
    "denver estate planning",
    "denver family office",
    "denver private banking",
    "denver real estate developer",
    "denver luxury property",
    "denver high-end investment",
    "denver luxury lifestyle",
    "denver upscale neighborhood",
    "denver luxury amenities",
    "denver luxury brands",
    "denver luxury travel",
    "denver high-end dining",
    "denver luxury fashion",
    "denver exclusive club membership",
    "denver innovative business",
    "denver disruptive technology",
    "denver startup ecosystem",
    "denver emerging markets",
    "denver global business",
    "denver industry insights",
    "denver entrepreneurial mindset",
    "denver creative solutions",
    "denver innovative strategies",
    "denver cutting-edge technology",
    "denver startups",
    "denver startup culture",
    "denver innovation hub",
    "denver tech startups",
    "denver startup accelerator",
    "denver innovation trends",
    "denver forward-thinking",
    "denver entrepreneurial spirit",
    "denver business innovation",
    "denver innovative products",
    "denver innovative services",
    "denver innovation in business",
    "denver innovation management",
    "denver innovation consulting",
    "denver business development",
    "denver business strategy",
    "denver business growth",
    "denver strategic planning",
    "denver market analysis",
    "denver competitive analysis",
    "denver market research",
    "denver industry trends",
    "denver business intelligence",
    "denver customer acquisition",
    "denver customer retention",
    "denver branding strategy",
    "denver marketing campaigns",
    "denver digital marketing",
    "denver social media marketing",
    "denver content marketing",
    "denver email marketing",
    "denver sales strategies",
    "denver sales funnel",
    "denver lead generation",
    "denver customer experience",
    "denver customer satisfaction",
    "denver product development",
    "denver product launch",
    "denver product management",
    "denver supply chain management",
    "denver operations management",
    "denver project management",
    "denver financial management",
    "denver budgeting",
    "denver cost management",
    "denver financial analysis",
    "denver risk management",
    "denver investment strategies",
    "denver portfolio management",
    "denver asset allocation",
    "denver entrepreneurial finance",
    "denver startup funding",
    "denver business loans",
    "denver venture funding",
    "denver private equity funding",
    "denver angel investment",
    "denver crowdfunding",
    "denver cash flow management",
    "denver tax planning",
    "denver legal compliance",
    "denver human resources management",
    "denver talent acquisition",
    "denver employee training",
    "denver workplace culture",
    "denver employee engagement",
    "denver leadership development",
    "denver succession planning",
    "denver business coaching",
    "denver management consulting",
    "denver executive coaching",
    "denver business networking",
    "denver professional associations",
    "denver industry conferences",
    "denver trade shows",
    "denver business partnerships",
    "denver strategic alliances",
    "denver joint ventures",
    "denver franchising",
    "denver business innovation",
    "denver innovation management",
    "denver technology adoption",
    "denver digital transformation",
    "denver cloud computing",
    "denver artificial intelligence",
    "denver machine learning",
    "denver data analytics",
    "denver cybersecurity",
    "denver blockchain technology",
    "denver internet of things",
    "denver e-commerce",
    "denver online retail",
    "denver mobile apps",
    "denver web development",
    "denver customer relationship management",
    "denver enterprise resource planning",
    "denver business automation",
    "denver supply chain automation",
    "denver industry 4.0",
    "denver sustainability in business",
    "denver green initiatives",
    "denver corporate social responsibility",
    "denver ethical business practices",
    "denver environmental impact",
    "denver social impact",
    "denver community engagement",
    "denver diversity and inclusion",
    "denver workplace wellness",
    "denver employee benefits",
    "denver remote work",
    "denver flexible work arrangements",
    "denver work-life balance",
    "denver company culture",
    "denver organizational development",
    "denver change management",
    "denver crisis management",
    "denver business continuity",
    "denver risk mitigation",
    "denver regulatory compliance",
    "denver business ethics",
    "denver industry standards",
    "denver business awards",
    "denver customer testimonials",
    "denver case studies",
    "denver best practices",
    "denver thought leadership",
    "denver industry expert",
    "denver business mentorship",
    "denver executive leadership",
    "denver business success stories",
    "denver industry disruptor",
    "denver market leader",
    "denver business excellence",
    "denver business"
]

    output_directory = "./API_Responses/DenverFinancialAcquisition"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    full_data = []
    post_count=0
    year, month = 2024, 2
    start_day, end_day = 20, 20  # Adjust end_day as needed

    for day in range(start_day, end_day + 1):
        t1 = datetime.datetime(year, month, day, 0, 0, 0).strftime("%Y-%m-%dT%H:%M:%S")
        t2 = datetime.datetime(year, month, day, 23, 59, 59).strftime("%Y-%m-%dT%H:%M:%S")
        print(f"Fetching posts for {t1} to {t2}")
        session_posts = fetch_posts(t1, t2, base_url, search_terms)
        full_data.extend(session_posts)
        time.sleep(10)  # To respect API rate limits

    # Save the collected posts to one file
    output_file_path = os.path.join(output_directory, 'DenverWealthManagement.json')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(full_data, file, ensure_ascii=False, indent=4)
    
    print(f"Saved {len(full_data)} posts to {output_file_path}")
    print(f"Total number of posts fetched: {post_count}")
if __name__ == "__main__":
    main()
