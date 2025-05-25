import React, {SyntheticEvent, useState} from "react";
import Wrapper from "./Wrapper";
import { Navigate } from "react-router-dom";


const ProductsCreate = () => {
    const [title, setTitle] = useState("");
    const [image, setImage] = useState("");
    const [redirect, setRedirect] = useState(false);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        
        await fetch('http://localhost:8000/api/v1/products', {
            method: 'POST',
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
                    <input type="text" className="form-control" id="title" name="title" value={title}
                        onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" id="image" name="image" value={image}
                        onChange={e => setImage(e.target.value)}
                    />
                </div>

                <button className="btn btn-outline-secondary">Save</button>
            </form>
       </Wrapper>
    );
}

export default ProductsCreate;