from model.inventory_manager_model import InventoryManager
from model.product_model import Product
from view.product_form_view import ProductFormView

class MainController:

    """
    The MainController class acts as the central controller of the application.

    It connects the view (ProductFormView) with the model (InventoryManager)
    and handles user interactions, such as adding or removing products.

    Attributes:
        inventory_manager (InventoryManager): Manages the inventory of products.
        view (ProductFormView): The graphical user interface for product management.

    Methods:
        __init__(): Initializes the MainController instance.
        addProduct(): Adds a new product to the inventory.
        removeProduct(): Removes a product from the inventory by its ID.
        start(): Starts the GUI
    """
    
    def __init__(self):
        self.model = InventoryManager()
        self.view = ProductFormView()

        self.view.submitButton.clicked.connect(self.addProduct)
        self.view.deleteButton.clicked.connect(self.removeProduct)

    def addProduct(self):
        """
        Adds a new product to the inventory.
        """
        name, price, quantity = self.view.getInput()
        product = Product(
            name = name,
            price = price,
            quantity= quantity
            )
        self.model.addProduct(product)
        products = self.model.products
        self.view.updateProductList(products)
        self.view.clearInputs()

    def removeProduct(self):
        """
        Removes a product from the inventory by its ID.
        """
        selected_items = self.view.productList.selectedItems()
        for item in selected_items:
            self.view.productList.takeItem(self.view.productList.row(item))
            # f"ID: {product.productId} | Name: {product.name} | Preis: {product.price} | Menge: {product.quantity}"
            selected_id = int(item.text().split(' | ')[0].split(' ')[1])
            print(f"Selected ID: {selected_id}")
            self.model.removeProduct(selected_id)

    def start(self):
        """
        Updates the view for loaded product data and calls the show()-Mehtod within the view instance for displaying the form.
        """
        self.view.updateProductList(self.model.products)
        self.view.show()