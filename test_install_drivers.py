from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_edge_session():
    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())

    driver = webdriver.Edge(service=service)

    driver.quit()


