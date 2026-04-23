import React, { useEffect, useState } from "react";
import API from "../api/api";

import {
  Container,
  Grid,
  Card,
  CardContent,
  Typography,
  // Button,
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
import Navbar from "../components/Navbar";

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
    } catch { }
  };

  const fetchHistory = async () => {
    const res = await API.get("/user/login-history");
    setHistory(res.data);
  };


  const chartData = {
    labels: history.map((h) =>
      new Date(h.timestamp).toLocaleDateString()
    ),
    datasets: [{ label: "Logins", data: history.map(() => 1) }],
  };

  return (
    <Container>
      <Navbar />
      <Typography variant="h4" sx={{ mt: 3, topMargin: "80px" }}>
        Dashboard
      </Typography>

      <Grid container spacing={3}>
        {/* AI */}
        <Grid item xs={12} md={6}>
          <Card sx={{ border: "2px solid black", height: 150, width: "500px", backgroundColor: ai?.risk === "High" ? "#ffcccc" : "#ccffcc" }}>
            <CardContent>
              <Typography variant="h5" sx={{ mt: 2, textAlign: "center" }}>
                AI Security
              </Typography>
              <Typography textAlign="center" sx={{ mt: 2 }}>
                Risk: {ai?.risk || "Unknown"}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        {/* Chart */}
        <Grid item xs={12}>
         <Card sx={{ border: "2px solid black", height: 150, width: "500px", backgroundColor: ai?.risk === "High" ? "#ffcccc" : "#ccffcc" }}>
            <CardContent>
              <Typography align="center">
                Login Activity
              </Typography>
              <Bar data={chartData} />
            </CardContent>
          </Card>
        </Grid>

        {/* Map */}
        <Grid item xs={12}>
         <Card sx={{ border: "2px solid black", backgroundColor: ai?.risk === "High" ? "#ffcccc" : "#ccffcc" }}>
            <CardContent>
              <Typography>Login Locations</Typography>

              <MapContainer
                center={[20.5937, 78.9629]}
                zoom={4}
                style={{ height: "400px", width: "1000px" }}
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

    </Container>
  );
}

export default Dashboard;