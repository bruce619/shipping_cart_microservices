import React from "react";

const Products = () => {
    return (
        <table className="table">
            <thead>
            <tr>
                <th>Order ID</th>
                <th>Customer</th>
                <th>Date</th>
                <th>Status</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>001</td>
                <td>John Doe</td>
                <td>2025-05-01</td>
                <td>Delivered</td>
            </tr>
            {/* More rows */}
            </tbody>
        </table> 
    );
};

export default Products;