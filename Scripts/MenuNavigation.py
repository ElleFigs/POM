from Pages.HomePage import *

class MenuNavigation_Script():

    def __init__(self, driver):
        self.driver = driver

    def changeZones(self, zoneName, tenant):
        navigation = HomePage(self.driver)
        navigation.OpenEnvironment()
        navigation.typeNewEnvironment(zoneName)
        print('typed in zone name')
        navigation.typeNewTenant(tenant)
        print('typed in tenant name')
        navigation.selectAutoTestTenant()