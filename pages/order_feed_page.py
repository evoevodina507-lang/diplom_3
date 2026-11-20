from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    def get_total_orders(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER).strip())

    def get_today_orders(self):
        return int(self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER).strip())
        
    def get_in_progress_order_number(self):
        return self.get_text(OrderFeedLocators.IN_PROGRESS_ORDER).replace("#", "").strip()