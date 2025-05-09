import React from 'react';
import './App.css';
import Nav from './components/Nav';
import Menu from './components/Menu';
import Products from './admin/Products';
import Main from './main/Main';
import { BrowserRouter, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">
          {/* Navbar Component */}
          <Nav />

          {/* Main Layout */}
          <div className="container-fluid">
            <div className="row">
              {/* Sidebar */}
              <Menu />

              {/* Main Content */}
              <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                <h2>Dashboard</h2>

                <div className="row">
                  <div className="col-md-4">
                    <div className="card">
                      <div className="card-body">
                        <h5 className="card-title">Sales</h5>
                        <p className="card-text">$12,345</p>
                      </div>
                    </div>
                  </div>
                  {/* More cards */}
                </div>

                <BrowserRouter>
                  <Routes>
                    <Route path="/"  Component={Main} />
                    <Route path="/admin/products" Component={Products} />
                  </Routes>
                </BrowserRouter>


              </main>
            </div>
          </div>
        </div>
      );
}

export default App;
