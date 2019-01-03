from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys 
from unittest import skip


class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		## an empty list item. She hits Enter on the emtoy input box.

		# The home page refreshes, adn there ian error message saying
		## that list itmes cannot be blank.

		# She tries again with some text fo trht itme, which now works.

		# Perversely, show no decides to submit a second blank list itme.

		# She receives a similar warning on the list page

		# And she can corret it by filling some text in 
		self.fail('write me!')


