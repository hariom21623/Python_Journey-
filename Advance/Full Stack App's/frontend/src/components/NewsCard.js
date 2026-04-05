import React from "react";

const NewsCard = ({ article }) => {
    return (
        <div style={styles.card}>
            <h2>{article.title}</h2>

            {/* Show AI text directly */}
            <p>{article.ai.summary}</p>

            <a href={article.url} target="_blank" rel="noreferrer">
                Read full →
            </a>
        </div>
    );
};

const styles = {
    card: {
        background: "#fff",
        padding: "15px",
        marginBottom: "15px",
        borderRadius: "10px",
        boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
    },
};

export default NewsCard;