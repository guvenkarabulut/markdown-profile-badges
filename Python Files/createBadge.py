from selenium import webdriver
from selenium.webdriver.common.by import By
import os


driver = webdriver.Chrome()
driver.get("https://simpleicons.org/")

# Search for the grid
grid = driver.find_element(By.CLASS_NAME, "grid")

dosya = open("allBrandInSimpleIcons.txt", "w")

# Get all icons
icons = grid.find_elements(By.TAG_NAME, "li")
for(icon) in icons:
    dosya.write(icon.find_element(By.TAG_NAME, "h2").text)
    dosya.write("\n")

dosya.close()
driver.quit()
