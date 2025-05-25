import React, { useEffect, useState} from "react";
import Wrapper from "./Wrapper";
import { Product } from "../interface/products";
import { Link } from "react-router-dom";


const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {

        (
            async () => {
                const response = await fetch('http://localhost:8000/api/v1/products');
                const data = await response.json();
                setProducts(data);
            }
        )();
    }, []);

    const handleDelete = async (id: number) => {
    const confirmed = window.confirm('Are you sure you want to delete this product?');
    if (!confirmed) return;

    await fetch(`http://localhost:8000/api/v1/products/${id}`, {
        method: 'DELETE',
    });

    setProducts(products.filter((p: Product) => p.id !== id));
    };

    return (
        <Wrapper>

            <div className="pt-3 pb-2 mb-3 border-bottom">
                <div className="btn-toolbar mb-2 mb-md-0">
                    <Link to='/admin/products/create' className="btn btn-sm btn-outline-secondary">Add</Link>
                </div>
            </div>

            <div className="table-responsive">
                <table className="table table-striped table-sm">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Image</th>
                        <th>Title</th>
                        <th>Likes</th>
                        <th>Action</th>
                    </tr>
                    </thead>
                    <tbody>
                        {products.map(
                            (p: Product) => {
                            return (
                                <tr key={p.id}>
                                    <td>{p.id}</td>
                                    <td><img src={p.image} height="180" /></td>
                                    <td>{p.title}</td>
                                    <td>{p.likes}</td>
                                    <td>
                                        <div className="btn-group mr-2">
                                            <Link to={`/admin/products/${p.id}/edit`} className="btn btn-sm btn-outline-primary">Edit</Link>
                                            <a href="#" className="btn btn-sm btn-outline-danger" onClick={() => handleDelete(p.id)}>Delete</a>
                                        </div>
                                    </td>
                                </tr>
                            );
                        })}
                    {/* More rows */}
                    </tbody>
                </table>
            </div>
        </Wrapper>
    );
};

export default Products;