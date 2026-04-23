import React from "react";

const NewsCard = ({ article }) => {
    const ai = typeof article.ai === "object" ? article.ai : {};

    const summary = ai.summary || "";
    const bullets = ai.bullet_points || [];
    const why = ai.why_it_matters || "";
    const tone = ai.tone || "";

    return (
        <div style={styles.card}>
            <h2 style={styles.title}>{article.title}</h2>

            {/* Summary */}
            {summary && <p style={styles.summary}>{summary}</p>}

            {/* Bullet Points */}
            {bullets.length > 0 && (
                <ul style={styles.list}>
                    {bullets.map((point, i) => (
                        <li key={i}>{point}</li>
                    ))}
                </ul>
            )}

            {/* Why it matters */}
            {why && (
                <div style={styles.box}>
                    <strong>Why it matters:</strong>
                    <p>{why}</p>
                </div>
            )}

            {/* Tone */}
            {tone && (
                <p style={styles.tone}>Tone: {tone}</p>
            )}

            {/* Link */}
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
    title: {
        marginBottom: "10px",
    },
    summary: {
        marginBottom: "10px",
        color: "#333",
    },
    list: {
        paddingLeft: "20px",
        marginBottom: "10px",
    },
    box: {
        background: "#eef",
        padding: "10px",
        borderRadius: "5px",
        marginBottom: "10px",
    },
    tone: {
        fontSize: "12px",
        color: "gray",
        marginBottom: "10px",
    },
};

export default NewsCard;