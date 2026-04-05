import axios from "axios";

const API = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
});

export const getNews = async () => {
  const res = await API.get("/news/");
  return res.data;
};