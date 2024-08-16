


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import time
import csv

# List of links to open
# List of links to open
links = [
    "https://www.iimb.ac.in/user/214/deepti-ganapathy",
    "https://www.iimb.ac.in/user/232/swati-bandi",
    "https://www.iimb.ac.in/user/254/rusha-das",
    "https://www.iimb.ac.in/user/93/deepak-malghan",
    "https://www.iimb.ac.in/user/105/arnab-mukherji",
    "https://www.iimb.ac.in/user/134/soham-sahoo",
    "https://www.iimb.ac.in/user/148/anil-b-suraj",
    "https://www.iimb.ac.in/user/213/allen-p-ugargol",
    "https://www.iimb.ac.in/user/146/m-s-sriram",
    "https://www.iimb.ac.in/user/149/hema-swaminathan",
    "https://www.iimb.ac.in/user/82/rajalaxmi-kamath",
    "https://www.iimb.ac.in/user/221/arpit-shah",
    "https://www.iimb.ac.in/user/225/reshma-chirayil-chandrasekharan",
    "https://www.iimb.ac.in/user/244/anand-deo",
    "https://www.iimb.ac.in/user/180/ananth-krishnamurthy",
    "https://www.iimb.ac.in/user/110/rajluxmi-v-murthy",
    "https://www.iimb.ac.in/user/253/arjun-ramachandra",
    "https://www.iimb.ac.in/user/138/trilochan-sastry",
    "https://www.iimb.ac.in/user/65/shubhabrata-das",
    "https://www.iimb.ac.in/user/68/jitamitra-desai",
    "https://www.iimb.ac.in/user/196/soudeep-deb",
    "https://www.iimb.ac.in/user/70/u-dinesh-kumar",
    "https://www.iimb.ac.in/user/73/pulak-ghosh",
    "https://www.iimb.ac.in/user/215/sarvesh-bandhu",
    "https://www.iimb.ac.in/user/53/ritwik-banerjee",
    "https://www.iimb.ac.in/user/169/kunal-dasgupta",
    "https://www.iimb.ac.in/user/69/anubha-dhasmana",
    "https://www.iimb.ac.in/user/76/subhashish-gupta",
    "https://www.iimb.ac.in/user/236/sanket-patil",
    "https://www.iimb.ac.in/user/58/manaswini-bhalla",
    "https://www.iimb.ac.in/user/203/gaurav-jakhu",
    "https://www.iimb.ac.in/user/66/tirthatanmoy-das",
    "https://www.iimb.ac.in/user/249/akhil-ilango",
    "https://www.iimb.ac.in/user/108/srinivasan-murali",
    "https://www.iimb.ac.in/user/242/aditya-shrinivas",
    "https://www.iimb.ac.in/user/147/chetan-subramanian",
    "https://www.iimb.ac.in/user/57/suresh-bhagavatula",
    "https://www.iimb.ac.in/user/79/srivardhini-k-jha",
    "https://www.iimb.ac.in/user/208/ludvig-levasseur",
    "https://www.iimb.ac.in/user/95/dalhia-mani",
    "https://www.iimb.ac.in/user/224/ramya-k-murthy",
    "https://www.iimb.ac.in/user/137/saras-d-sarasvathy",
    "https://www.iimb.ac.in/user/251/jaideep-sarkar",
    "https://www.iimb.ac.in/user/245/athira-a",
    "https://www.iimb.ac.in/user/246/venu-madhav-tatiparti",
    "https://www.iimb.ac.in/user/49/abhinav-anand",
    "https://www.iimb.ac.in/user/207/debojyoti-das",
    "https://www.iimb.ac.in/user/231/anirudh-dhawan",
    "https://www.iimb.ac.in/user/199/varun-jindal",
    "https://www.iimb.ac.in/user/114/m-s-narasimhan",
    "https://www.iimb.ac.in/user/119/venkatesh-panchapagesan",
    "https://www.iimb.ac.in/user/212/kannan-raghunandan",
    "https://www.iimb.ac.in/user/129/srinivasan-rangan",
    "https://www.iimb.ac.in/user/252/sumit-saurav",
    "https://www.iimb.ac.in/user/144/padmini-srinivasan",
    "https://www.iimb.ac.in/user/150/ashok-thampy",
    "https://www.iimb.ac.in/user/250/nitin-vishen",
    "https://www.iimb.ac.in/user/50/v-ravi-anshuman",
    "https://www.iimb.ac.in/user/56/sankarshan-basu",
    "https://www.iimb.ac.in/user/78/m-jayadev",
    "https://www.iimb.ac.in/user/111/shashidhar-murthy",
    "https://www.iimb.ac.in/user/133/g-sabarinathan",
    "https://www.iimb.ac.in/user/52/rajendra-k-bandi",
    "https://www.iimb.ac.in/user/206/shankhadeep-banerjee",
    "https://www.iimb.ac.in/user/67/rahul-de",
    "https://www.iimb.ac.in/user/153/shankar-venkatagiri",
    "https://www.iimb.ac.in/user/235/spurthy-dharanikota",
    "https://www.iimb.ac.in/user/83/nagasimha-balakrishna-kanagal",
    "https://www.iimb.ac.in/user/234/mayank-nagpal",
    "https://www.iimb.ac.in/user/122/srinivas-prakhya",
    "https://www.iimb.ac.in/user/139/g-shainesh",
    "https://www.iimb.ac.in/user/100/y-l-r-moorthi",
    "https://www.iimb.ac.in/user/64/gopal-das",
    "https://www.iimb.ac.in/user/80/sreelata-jonnalagedda",
    "https://www.iimb.ac.in/user/240/malika",
    "https://www.iimb.ac.in/user/98/ashis-mishra",
    "https://www.iimb.ac.in/user/222/arpita-pandey",
    "https://www.iimb.ac.in/user/202/debolina-dutta",
    "https://www.iimb.ac.in/user/228/sushanta-kumar-mishra",
    "https://www.iimb.ac.in/user/142/e-s-srinivas",
    "https://www.iimb.ac.in/user/145/vasanthi-srinivasan",
    "https://www.iimb.ac.in/user/106/sourav-mukherji",
    "https://www.iimb.ac.in/user/219/apurva-sanaria",
    "https://www.iimb.ac.in/user/86/mukta-kulkarni",
    "https://www.iimb.ac.in/user/162/gopal-mahapatra",
    "https://www.iimb.ac.in/user/102/kanchan-mukherjee",
    "https://www.iimb.ac.in/user/117/abhoy-k-ojha",
    "https://www.iimb.ac.in/user/255/surendra-babu-talluri",
    "https://www.iimb.ac.in/user/191/tarun-jain",
    "https://www.iimb.ac.in/user/91/b-mahadevan",
    "https://www.iimb.ac.in/user/136/haritha-saranga",
    "https://www.iimb.ac.in/user/157/nishant-kumar-verma",
    "https://www.iimb.ac.in/user/77/jishnu-hazra",
    "https://www.iimb.ac.in/user/92/siddharth-mahajan",
    "https://www.iimb.ac.in/user/233/ms-shalique",
    "https://www.iimb.ac.in/user/84/d-krishna-sundar",
    "https://www.iimb.ac.in/user/135/amar-sapra",
    "https://www.iimb.ac.in/user/151/rajeev-r-tripathi",
    "https://www.iimb.ac.in/user/81/p-d-jose",
    "https://www.iimb.ac.in/user/241/shailendra-kumar",
    "https://www.iimb.ac.in/user/118/rejie-george-pallathitta",
    "https://www.iimb.ac.in/user/156/sai-yayavaram",
    "https://www.iimb.ac.in/user/190/sai-chittaranjan-kalubandi",
    "https://www.iimb.ac.in/user/186/nilam-kaushik",
    "https://www.iimb.ac.in/user/85/rishikesha-t-krishnan",
    "https://www.iimb.ac.in/user/230/shubha-patvardhan",
    "https://www.iimb.ac.in/user/209/deepak-chandrashekar",
    "https://www.iimb.ac.in/user/121/ganesh-n-prabhu",
    "https://www.iimb.ac.in/user/125/prateek-raj",
    "https://www.iimb.ac.in/user/143/r-srinivasan",
    "https://www.iimb.ac.in/user/187/vijay-venkataraman",
    "https://www.iimb.ac.in/user/243/sandeep-yadav"
]


# Set up Chrome options
chrome_options = Options()

# Create a new Chrome browser instance
driver = webdriver.Chrome(options=chrome_options)

# Function to extract emails from the page source
def extract_emails_from_page():
    page_source = driver.page_source
    # Regular expression to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, page_source)
    return emails

# Function to extract name from the page source
def extract_name_from_page():
    try:
        # Assuming the name is within an element with class 'profile-name'
        name_element = driver.find_element(By.CLASS_NAME, 'profile-name')
        name = name_element.text
    except:
        name = "Unknown"
    return name

all_data = []

# Loop through the links
for link in links:
    # Open the link in the current tab
    driver.get(link)
    
    # Wait for the page to load
    time.sleep(0.0001)
    
    # Extract emails from the page
    emails = extract_emails_from_page()
    
    # Extract name from the page
    name = extract_name_from_page()
    
    for email in emails:
        all_data.append((name, email))

# Save the extracted data to a CSV file named after the institute
csv_filename = 'iimbangalore_emails.csv'
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Email'])
    for name, email in all_data:
        writer.writerow([name, email])

# Close the browser
driver.quit()