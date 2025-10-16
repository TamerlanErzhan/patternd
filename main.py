class UserProfile:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def update(self, **kwargs):
        return UserProfile(
            kwargs.get("name", self.name),
            kwargs.get("email", self.email),
            kwargs.get("role", self.role)
        )

    def __repr__(self):
        return f"UserProfile(name='{self.name}', email='{self.email}', role='{self.role}')"


user = UserProfile("Tamer", "Tamer@example.com", "admin")
new_user = user.update(role="editor")
print(user)
print(new_user)


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, prop):
        return Vector2D(self.x + prop.x, self.y + prop.y)

    def scale(self, factor):
        return Vector2D(self.x * factor, self.y * factor)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


v1 = Vector2D(2, 3)
v2 = Vector2D(1, 4)
print(v1.add(v2))
print(v1.scale(2))


class FrozenInvoice:
    def __init__(self, price, quantity):
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @property
    def total(self):
        return self._price * self._quantity

    def __repr__(self):
        return f"FrozenInvoice(price={self.price}, quantity={self.quantity}, total={self.total})"


invoice = FrozenInvoice(500, 3)
print(invoice.price)
print(invoice.quantity)
print(invoice.total)
