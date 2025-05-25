import React, {SyntheticEvent, useEffect, useState} from "react";
import Wrapper from "./Wrapper";
import { useParams, Navigate } from "react-router-dom";
import { Product } from "../interface/products";



const ProductsEdit = () => {
    const { id } = useParams() as {id: string};        // ← grab the `:id` from the URL
    const [title, setTitle] = useState("");
    const [image, setImage] = useState("");
    const [redirect, setRedirect] = useState(false);

    useEffect(() => {
        (
            async () => {
                if (!id) return;
                const response = await fetch(`http://localhost:8000/api/v1/products/${id}`);
                if (!response.ok) {
                    // handle 404 / errors here if you like
                    return;
                }
                const product: Product = await response.json();
                setTitle(product.title);
                setImage(product.image);
            }
        )();
    }, [id])

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        
        await fetch(`http://localhost:8000/api/v1/products/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title,
                image,
            }),
        });
    setRedirect(true); // trigger redirect after successful submission
    };

    if (redirect) {
        return <Navigate to="/admin/products" replace />;
    }

    return (
       <Wrapper>
            <form onSubmit={submit}>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" id="title" name="title" defaultValue={title}
                        onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" id="image" name="image" defaultValue={image}
                        onChange={e => setImage(e.target.value)}
                    />
                </div>

                <button className="btn btn-outline-secondary">Save</button>
            </form>
       </Wrapper>
    );
}

export default ProductsEdit;