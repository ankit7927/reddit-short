from selenium import webdriver
from selenium.webdriver.common.by import By

# page_link = "https://www.reddit.com/r/AskReddit/comments/12dmbbk/who_is_the_worst_kind_of_person_to_be_sat_next_to/?sort=new"

class DataExtractor:
    image_path = "raw/images"
    data_path = "raw"
    driver:webdriver= None
    

    def __init__(self, driverOpt) -> None:
        if driverOpt == "1":
            self.driver = webdriver.Chrome()
        elif driverOpt == "2":
            self.driver = webdriver.Firefox()
        elif driverOpt == "3":
            self.driver = webdriver.Edge()
        else:
            raise Exception("no web driver selected")
        
        self.driver.set_window_size(980, 812)
    
    def extractData(self, page_link:str) -> dict:
        self.driver.get(page_link)
        data:dict = {}
        question = self.driver.find_element(By.XPATH, "//div[@data-testid='post-container']")
        question.screenshot(f"{self.image_path}/question.png")

        data["question"] = question.find_element(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m").text

        list_commemts:list = []
        
        comments = self.driver.find_elements(By.CLASS_NAME, "_3sf33-9rVAO_v4y0pIW_CH")
        comments_texts = self.driver.find_elements(By.CLASS_NAME, "_1qeIAgB0cPwnLhDF9XSiJM")

        for inx, ele in enumerate(comments[:4]):
            ele.screenshot(f"{self.image_path}/{inx}.png")
        
        for ele in comments_texts[:4]:
            list_commemts.append(str(ele.text))

        data["comments"] = list_commemts
        print(data)
        self.driver.close()
        return data

#test = DataExtractor()
#x = test.extractData("https://www.reddit.com/r/AskReddit/comments/12dmbbk/who_is_the_worst_kind_of_person_to_be_sat_next_to/?sort=new")
#print(x)