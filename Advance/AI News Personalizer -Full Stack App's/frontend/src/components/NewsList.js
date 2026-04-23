import React from "react";
import NewsCard from "./NewsCard";

const NewsList = ({ articles }) => {
  return (
    <div>
      {articles.map((article, i) => (
        <NewsCard key={i} article={article} />
      ))}
    </div>
  );
};

export default NewsList;