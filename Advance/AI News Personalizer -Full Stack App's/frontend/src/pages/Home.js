import React, { useEffect, useState } from "react";
import { getNews } from "../services/api";
import NewsList from "../components/NewsList";
import Loader from "../components/Loader";

const Home = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchNews = async () => {
    try {
      const data = await getNews();
      console.log("API DATA:", data); // 👈 add this for debug
      setArticles(data.results || []);
    } catch (err) {
      console.error("Error:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNews();
  }, []);

  return (
    <div style={{ maxWidth: "800px", margin: "20px auto" }}>
      {loading ? <Loader /> : <NewsList articles={articles} />}
    </div>
  );
};

export default Home;