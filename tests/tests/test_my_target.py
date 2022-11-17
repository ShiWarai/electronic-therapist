import pytest
from urllib.parse import urljoin

from tests.base_test import BaseCase
from tests.utils.generators import generate_random_string, generate_random_number_string

@pytest.mark.UI
class TestMyTarget(BaseCase):

    def test_login(self):
        pass
        #self.welcome_page.login(login, password)
        #assert login in self.main_page.get_auth_username()

    def test_logout(self):
        #self.welcome_page.login(login, password)
        self.main_page.logout()
        assert "" == self.welcome_page.get_auth_username()

    def test_editing_contacts_data(self):
        #self.welcome_page.login(login, password)
        self.driver.get(urljoin(self.config['url'], 'profile', 'contacts')) # Navbar hasn't been tested yet

        fio = generate_random_string(20)
        phone_number = "+7" + generate_random_number_string(10)
        self.contacts_page.change_contacts(fio, phone_number)

        self.driver.refresh()
        assert self.contacts_page.get_fio() == fio
        assert self.contacts_page.get_phone_number() == phone_number

    tabs_test_data = [
        pytest.param('segments'),
        pytest.param('billing'),
    ]

    @pytest.mark.parametrize("tab_name", tabs_test_data)
    def test_tabs_via_navbar(self, tab_name):
        self.welcome_page.login(login, password)
        self.main_page.change_tab(tab_name)
        self.driver.switch_to.window(self.driver.window_handles[-1]) # for case of new tab
        assert tab_name in self.driver.current_url