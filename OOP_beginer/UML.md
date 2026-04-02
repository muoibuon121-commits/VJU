``` mermaid
classDiagram
    direction TB
    class Product {
        #String productId
        #String productName
        #String manufacturer
        #float price
        +showInfo()
    }
    class ElectronicProduct {
        -int warrantyMonths
        -int voltage
        -int power
        +showInfo()
    }
    class CeramicProduct {
        -String materialType
        +showInfo()
    }
    class FoodProduct {
        -String mfgDate
        -String expiryDate
        +showInfo()
    }
    class ProductManager {
        +List productList
        +addProduct(Product p)
        +showAll()
        +search(String name)
    }

    Product <|-- ElectronicProduct : Inheritance
    Product <|-- CeramicProduct : Inheritance
    Product <|-- FoodProduct : Inheritance
    ProductManager "1" o-- "0..*" Product : Aggregation
