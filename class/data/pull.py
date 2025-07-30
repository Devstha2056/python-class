import requests
from bs4 import BeautifulSoup
import csv
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

def get_contact_details(school_url):
    try:
        response = requests.get(school_url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Failed to retrieve {school_url} (status: {response.status_code})")
            return None, None

        soup = BeautifulSoup(response.text, "html.parser")

        # This depends on the actual page structure, but
        # I'll give you a generic example to look for phone and email

        phone = None
        email = None

        # Example: Look for phone inside some element or with label "Phone"
        # This part you need to adapt based on the page HTML structure.

        # Find phone by searching for text patterns or specific classes/ids:
        phone_candidates = soup.find_all(string=lambda text: text and ("phone" in text.lower() or "contact" in text.lower()))
        for candidate in phone_candidates:
            # Try to extract phone numbers (very generic)
            # For example, get text nearby or parent element text
            parent_text = candidate.parent.get_text(separator=" ", strip=True)
            if any(char.isdigit() for char in parent_text):
                phone = parent_text
                break
        
        # Or try a simpler way — find phone in a span or div with some class, e.g., "phone"
        if not phone:
            phone_tag = soup.find(class_="phone")
            if phone_tag:
                phone = phone_tag.get_text(strip=True)

        # For email, look for mailto links
        mailto = soup.select_one('a[href^=mailto]')
        if mailto:
            email = mailto['href'].replace('mailto:', '').strip()

        return phone, email

    except Exception as e:
        print(f"Error while scraping {school_url}: {e}")
        return None, None

def update_csv_with_contacts(input_csv, output_csv):
    updated_schools = []
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            link = row.get("link")
            if link:
                print(f"Scraping: {link}")
                phone, email = get_contact_details(link)
                row["phone"] = phone or "Not found"
                row["email"] = email or "Not found"
                # To be gentle on the server, pause between requests
                time.sleep(1)
            else:
                row["phone"] = "No link"
                row["email"] = "No link"
            updated_schools.append(row)

    # Write updated data
    keys = updated_schools[0].keys() if updated_schools else ["name", "address", "link", "phone", "email"]
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(updated_schools)

    print(f"Updated CSV saved to {output_csv}")

if __name__ == "__main__":
    update_csv_with_contacts("schools_list.csv", "schools_list_with_contacts.csv")
