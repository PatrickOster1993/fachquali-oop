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

    def addProduct(self):
        """
        Adds a new product to the inventory.
        """
        currentId = self.model.currentId
        name, price, quantity = self.view.getInput()
        product = Product(
            productId=currentId,
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

    def start(self):
        """
        Calls the show()-Mehtod within the view instance for displaying the form.
        """
        self.view.show()