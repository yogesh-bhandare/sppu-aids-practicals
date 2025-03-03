// Create collection and insert data
db.customers.insertMany([
    {
        customer_id: 1,
        name: "John Doe",
        age: 28,
        city: "New York",
        purchase_date: new Date("2024-09-12"),
        purchase_amount: 150.50,
        purchased_product: "Laptop"
    },
    {
        customer_id: 2,
        name: "Jane Smith",
        age: 32,
        city: "Los Angeles",
        purchase_date: new Date("2024-09-15"),
        purchase_amount: 80.99,
        purchased_product: "Smartphone"
    },
    {
        customer_id: 3,
        name: "Mike Johnson",
        age: 45,
        city: "Chicago",
        purchase_date: new Date("2024-09-18"),
        purchase_amount: 200.75,
        purchased_product: "TV"
    },
    {
        customer_id: 4,
        name: "Sara Davis",
        age: 23,
        city: "New York",
        purchase_date: new Date("2024-09-20"),
        purchase_amount: 300.50,
        purchased_product: "Laptop"
    }
]);

// Aggregation Queries
// Total Purchase Amount by City
db.customers.aggregate([
    {
        $group: {
            _id: "$city",
            total_purchase: { $sum: "$purchase_amount" },
            avg_purchase: { $avg: "$purchase_amount" }
        }
    },
    {
        $sort: { total_purchase: -1 } 
    }
]);

// Total Number of Purchases by Product
db.customers.aggregate([
    {
        $group: {
            _id: "$purchased_product",
            total_purchases: { $sum: 1 }
        }
    },
    {
        $sort: { total_purchases: -1 }
    }
]);


// Average Purchase Amount by Age Group
db.customers.aggregate([
    {
        $bucket: {
            groupBy: "$age",
            boundaries: [20, 30, 40, 50], 
            default: "Others",
            output: {
                avg_purchase_amount: { $avg: "$purchase_amount" }
            }
        }
    }
]);

// Indexing
// Index on 'city' field
db.customers.createIndex({ city: 1 });

// Compound index on 'city' and 'purchase_date' fields
db.customers.createIndex({ city: 1, purchase_date: -1 });

db.customers.find({ city: "New York" }).sort({ purchase_date: -1 });

// Map-Reduce Operation
var mapFunction = function() {
    emit(this.city, this.purchase_amount);
};

var reduceFunction = function(city, amounts) {
    return Array.sum(amounts);
};

db.customers.mapReduce(
    mapFunction,
    reduceFunction,
    {
        out: "total_purchases_by_city"
    }
);

// View Results
db.total_purchases_by_city.find().pretty();
