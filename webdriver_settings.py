from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("disable-infobars")
options.add_argument("--window-size=1920,1080")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--js-flags=-max-old-space-size=8196")
options.add_argument("--disable-gpu")
options.add_argument("--disable-web-security")
options.add_argument("--dns-prefetch-disable")

capabilities = options.to_capabilities()
capabilities["acceptSslCerts"] = True
capabilities["acceptInsecureCerts"] = True
