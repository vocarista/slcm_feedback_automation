from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
import time

print("🚀 Starting script...")

path = "path/to/your/chromedriver-win64/chromedriver.exe"

service = webdriver.chrome.service.Service(path)
service.start()

print("✅ Chrome service started.")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://mujslcm.jaipur.manipal.edu")
driver.implicitly_wait(10)

print("🧑‍💻 Waiting for manual login...")
input("👉 Press Enter after you've logged in manually...")

driver.get("https://mujslcm.jaipur.manipal.edu/Student/Survey/FeedbackList")
print("📄 Opened Feedback List Page.")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#kt_ViewTable > tbody > tr")))
    rows = driver.find_elements(By.CSS_SELECTOR, "#kt_ViewTable > tbody > tr")
    n = len(rows)
    print(f"📊 Found {n} feedback rows.")
except:
    print("❌ Feedback table not found.")
    driver.quit()
    exit()

for i in range(n):
    print(f"\n➡️ Processing feedback row {i + 1} of {n}")

    driver.get("https://mujslcm.jaipur.manipal.edu/Student/Survey/FeedbackList")

    try:
        wait = WebDriverWait(driver, 10)
        link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#kt_ViewTable > tbody > tr:nth-child({i + 1}) > td:nth-child(5) > a')))
        print("🔗 Feedback link found and clickable.")
        link.click()
    except:
        print(f"❌ Could not click feedback link for row {i + 1}")
        continue

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btnSubmit")))
        print("✅ Feedback form loaded.")
    except:
        print("❌ Feedback form did not load.")
        continue

    for j in range(10):
        try:
            buttons = driver.find_elements(By.CSS_SELECTOR, f"#dtPart{j} > tbody > tr > td > label:nth-child(7) > input")
            if buttons:
                print(f"🟢 Clicking {len(buttons)} buttons in dtPart{j}")
            for btn in buttons:
                btn.click()
        except Exception as e:
            print(f"⚠️ Skipping dtPart{j} due to error: {e}")
            continue

    for idx in [1, 2]:
        try:
            select_input = driver.find_element(By.CSS_SELECTOR, f"#dtPartYes{idx}")
            select = Select(select_input)
            select.select_by_index(1)
            print(f"📌 Selected option 1 in dropdown dtPartYes{idx}")
        except:
            print(f"⚠️ Could not select dropdown dtPartYes{idx}")

    try:
        submit_btn = driver.find_element(By.CSS_SELECTOR, "#btnSubmit")
        submit_btn.click()
        print("✅ Submitted feedback.")
    except:
        print("❌ Couldn't click submit button.")

    time.sleep(1)

print("\n🏁 Script completed.")
