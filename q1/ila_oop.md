# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory Problem

### 1. Encapsulation
Encapsulation can be used in the sari-sari store inventory system to bundle a products' related behavior and data into a single product class. This involves wrapping private attributes like __name and __stock with public methods such as update_stock(). Applying this concept improves program organization by protecting data from accidental corruption and ensuring that all modifications go through a safe, controlled method. 

### 2. Abstraction
Abstraction can be used to simplify complex inventory management process by showing only important and essential details to the cashier or owner. It involves creating management classes or interfaces that hide the underlying stock calculations, reciept printing, and database queries. This improves program design by reducing the complexity of the code and letting its users to interact through a clean and straighforward system.

### 3. Inheritance
Inheritance can be used to create a hierarchical product structure where a generl product class serves as a parrent for specialized inventory types. This involves sharing common attributes like name and price while allowing subclasses like perishableproduct to introduce unique properties such as expiration_date. Aplying this concept eliminates code duplication and makes the inventory system much easier to expand aas the store introduces new products.

### 4. Polymorphism
Polymorphism can be used to allow different types of prouducts to respond to the same method call in ways specific to their category. For instance, both regularproduct and perishable product classes can implement their own version of a calculate_discount() method to handle clearance rules or whole sale price deductions differently. This improves deisgn flexibility by letting the inventory system process diverse items uniformly through a single, shared interface.

## Reflection
For me, among the four pillars of OOP, the most useful in improving the sari-sari store inventory system would be Encapsulation. By bundling product data and restricting direct access to critical attributes like stock quantities and prices, it prevents accidental corruption of data during bulk sale transactions. This ensures that every invetory upgrade goes through validated methods, maintaning reliability and data integrity across the entire store management system.
