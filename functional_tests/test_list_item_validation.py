from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys 
from unittest import skip


class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box.
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys(Keys.ENTER)

		# The browser intercetps the request and does not load the
		# list page
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:invalid'
		))

		# She starts typing some text fo the new itme and the error disappears
		self.get_item_input_box().send_keys('Buy milk')
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:valid'))

		# The home page refreshes, adn there ian error message saying
		# that list itmes cannot be blank.
		# self.wait_for(lambda: self.assertEqual(
		# 	self.browser.find_element_by_css_selector('#has-error').text,
		# 	"You can't have an empty list item"
		# ))

		# She tries again with some text for the item, which now works.
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')

		# Perversely, show no decides to submit a second blank list itme.
		self.get_item_input_box().send_keys(Keys.ENTER)

		# She receives a similar warning on the list page
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:invalid'
		))

		# And she can corret it by filling some text in 
		self.get_item_input_box().send_keys('Make tea')
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:valid'))
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for_row_in_list_table('2: Make tea')


