import axios from 'axios';

const baseURL =
  window.location.hostname === 'localhost'
    ? 'http://localhost:3000/api'
    : 'http://api-gateway-web:3000/api';

export default axios.create({ baseURL });
