from dataclasses import dataclass


class Product:
    product: str
    price: float
    description: str
    units: str = "kg"
    allergen: bool = False

    @property
    def __post_init__(self):
        if self.price <= 0:
            return ValueError("Price should be above 0")


PRODUCTS = {
    "morka": Product("Morka", 1.49, "Darzove"),
    "miltai": Product("Miltai", 1.99, "Bakaleja"),
    "cukrus": Product("Cukrus", 0.99, "Bakaleja"),
    "kiausinis": Product("Kiausinis", 0.1, "Bakaleja", units="vnt", allergen=True),
    "pienas": Product("Pienas", 0.89, "Pieno produktai", allergen=True),
}
