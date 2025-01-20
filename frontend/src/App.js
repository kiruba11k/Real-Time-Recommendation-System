import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [userId, setUserId] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleUserIdChange = (event) => {
    setUserId(event.target.value);
  };

  const handleRecommendClick = async () => {
    if (userId) {
      setLoading(true);
      try {
        const response = await axios.get(`http://127.0.0.1:5000/recommend?user_id=${userId}`);
        setRecommendations(response.data.recommendations);
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      } finally {
        setLoading(false);
      }
    } else {
      alert('Please enter a valid user ID');
    }
  };

  return (
    <div className="App">
      <h1>Product Recommendation System</h1>
      <div className="input-container">
        <input
          type="number"
          placeholder="Enter User ID"
          value={userId}
          onChange={handleUserIdChange}
        />
        <button onClick={handleRecommendClick} disabled={loading}>
          {loading ? 'Loading...' : 'Get Recommendations'}
        </button>
      </div>
      <div className="recommendations">
        {recommendations.length > 0 && (
          <div>
            <h2>Recommended Products</h2>
            <ul>
              {recommendations.map((product) => (
                <li key={product.product_id}>
                  <h3>{product.product_name}</h3>
                  <p>{product.description}</p>
                  <p><strong>Category:</strong> {product.category}</p>
                  <p><strong>Price:</strong> ${product.price}</p>
                </li>
              ))}
            </ul>
          </div>
        )}
        {recommendations.length === 0 && !loading && (
          <p>No recommendations to show. Enter a valid user ID to get recommendations.</p>
        )}
      </div>
    </div>
  );
}

export default App;
