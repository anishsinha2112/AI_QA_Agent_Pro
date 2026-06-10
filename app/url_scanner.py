import requests
from bs4 import BeautifulSoup

def scan_website(url):
    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")
        buttons = soup.find_all("button")
        links = soup.find_all("a")
        inputs = soup.find_all("input")

        result = {
            "forms": len(forms),
            "buttons": len(buttons),
            "links": len(links),
            "inputs": len(inputs)
        }

        return result

    except Exception as e:
        return {"error": str(e)}