from django.shortcuts import render
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def home(request):
    return render(request, 'home.html')

def analyze_reviews(request):
    if request.method == "POST":
        product_url = request.POST.get("product_url")  # Get URL from input
        if not product_url:
            return JsonResponse({"error": "No URL provided"}, status=400)

        # 🚀 Perform analysis here (For now, return the URL)
        return render(request, "analyze.html", {"product_url": product_url})

    return render(request, "home.html")  # If accessed via GET, return home page
def scrape_amazon(url):
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        elements = driver.find_elements(By.CSS_SELECTOR, ".review-text-content span")
        
        reviews = []
        for elem in elements:
            text = elem.text.strip()
            reviews.append(text)

        driver.quit()
        return reviews
    except Exception as e:
        driver.quit()
        return [f"Error: {str(e)}"]
