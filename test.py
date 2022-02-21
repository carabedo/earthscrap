from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/fernando/gits/hypermap/chromedriver")
driver.get("https://earth.google.com/web/")



# desde la full xpath cambiar las // por shadowroot, despues (tag#id)
##/html/body/earth-app//paper-drawer-panel/div/earth-toolbar//earth-gm2-icon-button[2]
##earth-app//earth-toolbar//earth-gm2-icon-button[2]
search=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-toolbar').shadowRoot.querySelector('earth-gm2-icon-button#search')")

search.click()

##/html/body/earth-app//paper-drawer-panel/div/earth-drawer//neon-animated-pages/earth-search//app-header-layout/app-header/earth-omnibox//div/iron-input/input
## solo shadowroots
##earth-app//earth-drawer//earth-search//earth-omnibox//div/iron-input/input

search_text=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-drawer').shadowRoot.querySelector('earth-search').shadowRoot.querySelector('earth-omnibox').shadowRoot.querySelector('input#omnibox-input')")

search_text.send_keys(latlon[i])

search_text.send_keys(Keys.RETURN)

##/html/body/earth-app//paper-drawer-panel/div/earth-knowledge-card//earth-card-stack/earth-normal-card[3]//aside/app-toolbar/earth-gm2-icon-button[2]
##earth-app//earth-knowledge-card//earth-normal-card[3]//earth-gm2-icon-button[2]
## los indices se peuden reemplazar con id, mirando la consola

close=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-knowledge-card').shadowRoot.querySelector('earth-normal-card#top-card').shadowRoot.querySelector('earth-gm2-icon-button#close')")
close.click()


##/html/body/earth-app//paper-drawer-panel/div/div/div[2]/earth-zoom-buttons//div/earth-gm2-icon-button[1]

##earth-app//earth-zoom-buttons//earth-gm2-icon-button#zoom-out

zoom=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-zoom-buttons').shadowRoot.querySelector('earth-gm2-icon-button#zoom-out')")

zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click()


driver.save_screenshot(str[i]+'.png')

##/html/body/earth-app//paper-drawer-panel/div/earth-drawer//neon-animated-pages/earth-search//app-header-layout/app-header/earth-omnibox//div/div/earth-gm2-icon-button[1]

##earth-app//earth-drawer//earth-search//earth-omnibox//earth-gm2-icon-button#clear-button

clear_text=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-drawer').shadowRoot.querySelector('earth-search').shadowRoot.querySelector('earth-omnibox').shadowRoot.querySelector('earth-gm2-icon-button#clear-button')")

clear_text.click()


time.sleep(5)
for i,x in enumerate(latlons):
    search.click()
    time.sleep(1)
    try:
        clear_text=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-drawer').shadowRoot.querySelector('earth-search').shadowRoot.querySelector('earth-omnibox').shadowRoot.querySelector('earth-gm2-icon-button#clear-button')")
        clear_text.click()
    except:
        pass  
    search_text=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-drawer').shadowRoot.querySelector('earth-search').shadowRoot.querySelector('earth-omnibox').shadowRoot.querySelector('input#omnibox-input')")  
    search_text.send_keys(x)
    search_text.send_keys(Keys.RETURN)
    time.sleep(2)
    close=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-knowledge-card').shadowRoot.querySelector('earth-normal-card#top-card').shadowRoot.querySelector('earth-gm2-icon-button#close')")
    close.click()
    time.sleep(1)
    zoom=driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-zoom-buttons').shadowRoot.querySelector('earth-gm2-icon-button#zoom-out')")

    zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click();time.sleep(0.2);zoom.click()

    driver.save_screenshot(str(i)+'.png')
    time.sleep(0.5)





