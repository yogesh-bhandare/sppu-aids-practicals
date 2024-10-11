// MongoDB Bookstore Collection Script

// 1. Create (Insert)

// Insert a single book
db.bookstore.insertOne({
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    price: 15.99,
    category: "Fiction",
    published_date: new Date("1925-04-10")
});

// Insert multiple books
db.bookstore.insertMany([
    {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        price: 10.99,
        category: "Classic",
        published_date: new Date("1960-07-11")
    },
    {
        title: "1984",
        author: "George Orwell",
        price: 12.99,
        category: "Dystopian",
        published_date: new Date("1949-06-08")
    },
    {
        title: "Moby Dick",
        author: "Herman Melville",
        price: 18.50,
        category: "Adventure",
        published_date: new Date("1851-11-14")
    }
]);

// 2. Read (Find)

// Find all books
db.bookstore.find().pretty();

// Find a specific book by title
db.bookstore.find({ title: "The Great Gatsby" }).pretty();

// Find books priced above $12
db.bookstore.find({ price: { $gt: 12 } }).pretty();

// Find books in the "Fiction" category or priced below $11
db.bookstore.find({
    $or: [
        { category: "Fiction" },
        { price: { $lt: 11 } }
    ]
}).pretty();

// 3. Update

// Update the price of a specific book
db.bookstore.updateOne(
    { title: "The Great Gatsby" },
    { $set: { price: 17.99 } }
);

// Update the category for all books in the "Dystopian" category
db.bookstore.updateMany(
    { category: "Dystopian" },
    { $set: { category: "Science Fiction" } }
);

// 4. Delete

// Delete a specific book by title
db.bookstore.deleteOne({ title: "1984" });

// Delete all books in the "Classic" category
db.bookstore.deleteMany({ category: "Classic" });

// 5. Find Books with Multiple Conditions

db.bookstore.find({
    $or: [
        { category: "Fiction" },
        { price: { $gt: 15 } }
    ]
}).pretty();

// 6. Count Books in a Specific Category

const count = db.bookstore.countDocuments({ category: "Fiction" });
print("Number of books in Fiction:", count);

// 7. Using Projection to Limit Returned Fields

db.bookstore.find({}, { title: 1, author: 1, _id: 0 }).pretty();
