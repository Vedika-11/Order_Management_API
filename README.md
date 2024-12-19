# Order_Management_API
This API handles the lifecycle of daily delivery orders, including placing, modifying, and canceling orders. It features validation, accurate amount calculations, and dynamic discounts to ensure seamless operations and an optimized user experience for order management.

# Project Overview:
The Pride of Cows project is built to manage daily delivery orders for a dairy service. Within the project, an app named orders has been created to handle order-related functionalities such as placing, modifying, canceling, and calculating totals for customer orders.

# Project Structure:
The project consists of the following components:

 # Project Name: Pride of Cows
 # App Name: orders

# Models:
In the orders app, I have created the following models:

# 1.Product:
The Product model stores information about the products available for order. Each product has attributes such as name, description, price, and stock quantity.

# 2.Order:
The Order model tracks the customer orders, including order details such as customer information, ordered products, quantities, and status (e.g., placed, modified, canceled).

# 3.OrderHistory:
The OrderHistory model is used to maintain the history of order modifications or cancellations. It tracks the changes made to orders over time, including status updates and timestamps.

# Serializers:
To convert complex data types (models) into JSON format, I created a serializers.py file, where I defined serializers for each model:

# 1.ProductSerializer
# 2.OrderSerializer
# 3.OrderHistorySerializer

# Views
In the views.py file, I created four class-based views to handle the different order-related actions:

# 1.PlaceOrder:
This view allows customers to place a new order. It validates the order details, checks product availability, and creates an entry in the Order model. Additionally, it generates an entry in the OrderHistory to record the action.

# 2.ModifyOrder:
This view allows customers to modify an existing order. It checks if the order exists, validates the changes, and updates the order details accordingly. The modification is logged in the OrderHistory.

# 3.CancelOrder:
This view handles the cancellation of an order. It ensures that the order can be canceled (i.e., it hasn’t been shipped or completed yet), and updates the status of the order. The cancellation is recorded in the OrderHistory.

# 4.CalculateTotal:
This view calculates the total amount for a customer’s order, including any discounts or promotions. It considers the order’s quantity, the unit price of products, and applicable discount rules. The final amount is returned in the response.

