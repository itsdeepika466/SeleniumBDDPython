from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C://Users//10708565//Downloads//Driver//chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
#self
self=driver.find_element(By.XPATH,"//a[contains(text(),'Nimbus Project')]/self::a").text
print(self)
#parent
parent=driver.find_element(By.XPATH,"//a[contains(text(),'Nimbus Project')]/parent::td").text
print(parent)
#ancestor
ancestor=driver.find_element(By.XPATH,"//a[contains(text(),'Nimbus Project')]/ancestor::tr").text
print(ancestor)
#child
child=driver.find_element(By.XPATH,"//a[contains(text(),'Nimbus Project')]/ancestor::tr/child::td[3]").text
print(child)
#descendants
descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Nimbus Project')]/ancestor::tr/descendant::*")
print(len(descendants))
el=len(descendants)
for el in descendants:
    print(el.text)
#following
following=driver.find_element(By.XPATH,"//a[contains(text(),'Nimbus Project')]/ancestor::tr/following::tr[1]")
print(following.text)
#followingsibling
followingsibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Nimbus Project')]/ancestor::tr/following-sibling::*")
print(len(followingsibling))
#preceding
preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Nimbus Project')]/ancestor::tr/preceding::*")
print(len(preceding))
#precedingsibling
precedingsibling=driver.find_element(By.XPATH,"//a[contains(text(),'Nimbus Project')]/ancestor::tr/preceding-sibling::tr[1]")
print(precedingsibling.text)

driver.close()

