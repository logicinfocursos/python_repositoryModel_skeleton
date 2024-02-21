from typing import Optional, List

# Definição dos dados
db = {
    "products": [
        { "id": 1, "name": "product1", "categoryId": 2 },
        { "id": 2, "name": "product2", "categoryId": 1 },
        { "id": 3, "name": "product3", "categoryId": 2 },
        { "id": 4, "name": "product4", "categoryId": 1 }
    ],
    "categories": [
        { "id": 1, "name": "category1" },
        { "id": 2, "name": "category2" }
    ]
}

class Product:
    def __init__(self, id: int, name: str, categoryId: int, category: Optional["Category"] = None):
        self.id = id
        self.name = name
        self.categoryId = categoryId
        self.category = category

class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Repositories:
    def __init__(self, data: List):
        self.data = data

    def getAll(self):
        return self.data

    def getById(self, id: int):
        return next((item for item in self.data if item.id == id), None)

class ProductRepository(Repositories):
    def __init__(self):
        super().__init__([
            Product(p["id"], p["name"], p["categoryId"]) for p in db["products"]
        ])
        self.mapCategories()

    def mapCategories(self):
        categories = {c.id: c for c in [Category(c["id"], c["name"]) for c in db["categories"]]}
        for product in self.data:
            product.category = categories.get(product.categoryId)

class CategoryRepository(Repositories):
    def __init__(self):
        super().__init__([Category(c["id"], c["name"]) for c in db["categories"]])

# Exemplo de uso
def fetchData():
    # Produtos
    prodRepo = ProductRepository()

    # Método getAll
    products = prodRepo.getAll()
    print("Products:")
    for product in products:
        print(f"  ID: {product.id}, Name: {product.name}, Category ID: {product.categoryId}")

    # Método getById
    productIdToFind = 2
    productById = prodRepo.getById(productIdToFind)
    print(f"Product with id {productIdToFind}:", productById.name)

    # Categorias
    catRepo = CategoryRepository()

    # Método getAll
    categories = catRepo.getAll()
    print("\nCategories:")
    for category in categories:
        print(f"  ID: {category.id}, Name: {category.name}")

    # Método getById
    categoryIdToFind = 1
    categoryById = catRepo.getById(categoryIdToFind)
    print(f"Category with id {categoryIdToFind}:", categoryById.name)

fetchData()
