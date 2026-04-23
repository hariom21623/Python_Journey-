import React, { useState } from "react";
import API from "../api/api";
import { useNavigate } from "react-router-dom";

import { TextField, Button, Container, Typography } from "@mui/material";

function Login() {
  const [form, setForm] = useState({ email: "", password: "" });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await API.post("/auth/login", form);

      localStorage.setItem("token", res.data.access_token);
      localStorage.setItem("refresh", res.data.refresh_token);
      localStorage.setItem(
        "ai",
        JSON.stringify(res.data.ai_security || {})
      );

      navigate("/dashboard");
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" sx={{ mt: 5 }}>
        Login
      </Typography>

      <form onSubmit={handleSubmit}>
        <TextField
          fullWidth
          margin="normal"
          label="Email"
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
        />

        <TextField
          fullWidth
          margin="normal"
          label="Password"
          type="password"
          onChange={(e) =>
            setForm({ ...form, password: e.target.value })
          }
        />

        <Button type="submit" variant="contained" fullWidth>
          Login
        </Button>
      </form>
    </Container>
  );
}

export default Login;