import React, { useEffect, useState } from "react";
import API from "../api/api";

import {
  Container,
  Grid,
  Card,
  CardContent,
  Typography,
  Button,
} from "@mui/material";

import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

ChartJS.register(BarElement, CategoryScale, LinearScale);

function Dashboard() {
  const [history, setHistory] = useState([]);
  const [ai, setAi] = useState(null);

  useEffect(() => {
    fetchHistory();
    loadAI();
  }, []);

  const loadAI = () => {
    try {
      const data = localStorage.getItem("ai");
      if (data && data !== "undefined") {
        setAi(JSON.parse(data));
      }
    } catch {}
  };

  const fetchHistory = async () => {
    const res = await API.get("/user/login-history");
    setHistory(res.data);
  };

  const logout = () => {
    localStorage.clear();
    window.location.href = "/";
  };

  const chartData = {
    labels: history.map((h) =>
      new Date(h.timestamp).toLocaleDateString()
    ),
    datasets: [{ label: "Logins", data: history.map(() => 1) }],
  };

  return (
    <Container>
      <Typography variant="h4" sx={{ mt: 3 }}>
        Dashboard
      </Typography>

      <Grid container spacing={3}>
        {/* AI */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography>AI Security</Typography>
              <Typography>
                Risk: {ai?.risk || "Unknown"}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        {/* Chart */}
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Bar data={chartData} />
            </CardContent>
          </Card>
        </Grid>

        {/* Map */}
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography>Login Locations</Typography>

              <MapContainer
                center={[20.5937, 78.9629]}
                zoom={4}
                style={{ height: "400px" }}
              >
                <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

                {history.map(
                  (item) =>
                    item.lat &&
                    item.lon && (
                      <Marker
                        key={item.id}
                        position={[item.lat, item.lon]}
                      >
                        <Popup>
                          {item.city} <br />
                          {item.ip_address}
                        </Popup>
                      </Marker>
                    )
                )}
              </MapContainer>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      <Button onClick={logout} color="error" variant="contained">
        Logout
      </Button>
    </Container>
  );
}

export default Dashboard;