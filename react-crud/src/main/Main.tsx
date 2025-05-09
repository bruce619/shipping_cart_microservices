import React from "react";

const Main = () => {
    return (
      <div className="album py-5 bg-body-tertiary">
        <div className="container">
          {/* Header */}
          <div className="pb-4">
            <h1 className="display-5 fw-bold">Album Example</h1>
            <p className="col-lg-8 fs-4">A simple photo gallery showcasing images in a responsive grid.</p>
            <button className="btn btn-primary btn-lg" type="button">View More</button>
          </div>
          {/* Card Grid */}
          <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            {[...Array(6)].map((_, index) => (
              <div className="col" key={index}>
                <div className="card shadow-sm">
                  <img src={`https://via.placeholder.com/400x300?text=Image+${index + 1}`} className="bd-placeholder-img card-img-top" width="100%" height="225" alt={`Image ${index + 1}`} />
                  <div className="card-body">
                    <h5 className="card-title">Image {index + 1}</h5>
                    <p className="card-text">This is a sample description for image {index + 1} in the album.</p>
                    <div className="d-flex justify-content-between align-items-center">
                      <div className="btn-group">
                        <button type="button" className="btn btn-sm btn-outline-secondary">View</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }

export default Main;