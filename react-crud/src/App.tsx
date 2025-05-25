import React from 'react';
import './App.css';
import Main from './main/Main';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import ProductsCreate from './admin/ProductsCreate';
import Products from './admin/Products';
import ProductsEdit from './admin/ProductsEdit';


function App() {
  return (
    <div className="App">
          
                

              {/*}
                <div className="row">
                  <div className="col-md-4">
                    <div className="card">
                      <div className="card-body">
                        <h5 className="card-title">Sales</h5>
                        <p className="card-text">$12,345</p>
                      </div>
                    </div>
                  </div>
                  
                </div>
                */}

                <BrowserRouter>
                  <Routes>
                    <Route path="/"  Component={Main} />
                    <Route path="/admin/products" Component={Products} />
                    <Route path="/admin/products/create" Component={ProductsCreate} />
                    <Route path="/admin/products/:id/edit" Component={ProductsEdit} />
                  </Routes>
                </BrowserRouter>

        </div>
      );
}

export default App;
