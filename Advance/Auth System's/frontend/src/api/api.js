import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// ✅ attach access token
API.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");
  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }
  return req;
});

// 🔄 refresh token logic
API.interceptors.response.use(
  (res) => res,
  async (err) => {
    if (err.response?.status === 401) {
      try {
        const refresh = localStorage.getItem("refresh");

        const res = await axios.post(
          "http://127.0.0.1:8000/auth/refresh",
          { token: refresh }
        );

        localStorage.setItem("token", res.data.access_token);

        err.config.headers.Authorization = `Bearer ${res.data.access_token}`;
        return axios(err.config);
      } catch {
        localStorage.clear();
        window.location.href = "/";
      }
    }
    return Promise.reject(err);
  }
);

export default API;