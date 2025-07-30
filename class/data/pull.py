from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure headless Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the school listing URL
url = "https://nepalschoolmela.com/edufair/listing-schools"
driver.get(url)
time.sleep(5)  # Wait for JavaScript to load content

# Scroll to bottom (optional - to load more if lazy loaded)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Output file path
output_file = "school_data.txt"

# Open file for writing
with open(output_file, "w", encoding="utf-8") as file:
    # Locate each school card (update class names as per actual site)
    schools = driver.find_elements(By.CLASS_NAME, "school-card")  # Update this if needed

    for school in schools:
        try:
            name = school.find_element(By.CLASS_NAME, "school-name").text
            address = school.find_element(By.CLASS_NAME, "school-address").text
            contact = school.find_element(By.CLASS_NAME, "school-contact").text
            email = school.find_element(By.CLASS_NAME, "school-email").text

            # Write to file
            file.write(f"Name: {name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Contact: {contact}\n")
            file.write(f"Email: {email}\n")
            file.write("-" * 40 + "\n")

        except Exception as e:
            continue  # skip if data is missing

driver.quit()
print(f"✅ Data saved to {output_file}")
