import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Box, 
  Typography, 
  Paper, 
  Grid,
  Card,
  CardContent,
  Alert,
  CircularProgress
} from '@mui/material';
import { 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer 
} from 'recharts';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function App() {
  const [ftrtActual, setFtrtActual] = useState(null);
  const [prediccion, setPrediccion] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [actualRes, prediccionRes] = await Promise.all([
          axios.get(`${API_URL}/ftrt/actual`),
          axios.get(`${API_URL}/ftrt/prediccion/30`)
        ]);

        setFtrtActual(actualRes.data);
        setPrediccion(prediccionRes.data);
        setLoading(false);
      } catch (err) {
        setError('Error al cargar datos FTRT');
        setLoading(false);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 3600000); // Actualizar cada hora
    return () => clearInterval(interval);
  }, []);

  if (loading) return (
    <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
      <CircularProgress />
    </Box>
  );

  if (error) return (
    <Box m={2}>
      <Alert severity="error">{error}</Alert>
    </Box>
  );

  return (
    <Container maxWidth="xl">
      <Box my={4}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          Monitor FTRT - Predicción Solar
        </Typography>

        {/* Panel de Estado Actual */}
        <Grid container spacing={3} mb={4}>
          <Grid item xs={12} md={6}>
            <Paper elevation={3}>
              <Box p={3}>
                <Typography variant="h5" gutterBottom>
                  Estado FTRT Actual
                </Typography>
                {ftrtActual && (
                  <>
                    <Typography variant="h4" color="primary">
                      {ftrtActual.ftrt_valor.toFixed(3)}
                    </Typography>
                    <Alert 
                      severity={ftrtActual.alerta ? "warning" : "info"}
                      sx={{ mt: 2 }}
                    >
                      Nivel: {ftrtActual.nivel_riesgo}
                    </Alert>
                  </>
                )}
              </Box>
            </Paper>
          </Grid>

          {/* Contribuciones Planetarias */}
          <Grid item xs={12} md={6}>
            <Paper elevation={3}>
              <Box p={3}>
                <Typography variant="h5" gutterBottom>
                  Contribuciones Planetarias
                </Typography>
                {ftrtActual && (
                  <Grid container spacing={1}>
                    {Object.entries(ftrtActual.contribuciones_planetarias)
                      .sort(([,a], [,b]) => b - a)
                      .map(([planeta, valor]) => (
                        <Grid item xs={6} key={planeta}>
                          <Card>
                            <CardContent>
                              <Typography variant="subtitle1">
                                {planeta.charAt(0).toUpperCase() + planeta.slice(1)}
                              </Typography>
                              <Typography variant="h6" color="primary">
                                {(valor * 100).toFixed(1)}%
                              </Typography>
                            </CardContent>
                          </Card>
                        </Grid>
                    ))}
                  </Grid>
                )}
              </Box>
            </Paper>
          </Grid>
        </Grid>

        {/* Gráfico de Predicción */}
        <Paper elevation={3}>
          <Box p={3}>
            <Typography variant="h5" gutterBottom>
              Predicción FTRT - Próximos 30 días
            </Typography>
            {prediccion && (
              <Box height={400}>
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart
                    data={prediccion.valores_diarios}
                    margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis 
                      dataKey="fecha" 
                      tickFormatter={(date) => new Date(date).toLocaleDateString()}
                    />
                    <YAxis />
                    <Tooltip 
                      labelFormatter={(date) => new Date(date).toLocaleDateString()}
                      formatter={(value) => [value.toFixed(3), "FTRT"]}
                    />
                    <Line 
                      type="monotone" 
                      dataKey="ftrt" 
                      stroke="#8884d8" 
                      activeDot={{ r: 8 }} 
                    />
                  </LineChart>
                </ResponsiveContainer>
              </Box>
            )}
          </Box>
        </Paper>

        {/* Alertas */}
        {prediccion && prediccion.alertas.length > 0 && (
          <Box mt={4}>
            <Typography variant="h5" gutterBottom>
              Alertas Detectadas
            </Typography>
            <Grid container spacing={2}>
              {prediccion.alertas.map((alerta, index) => (
                <Grid item xs={12} sm={6} md={4} key={index}>
                  <Alert 
                    severity={alerta.nivel === 'EXTREMO' ? 'error' : 'warning'}
                    variant="filled"
                  >
                    <Typography variant="subtitle1">
                      {new Date(alerta.fecha).toLocaleDateString()}
                    </Typography>
                    <Typography variant="body2">
                      FTRT: {alerta.ftrt.toFixed(3)} - Nivel: {alerta.nivel}
                    </Typography>
                  </Alert>
                </Grid>
              ))}
            </Grid>
          </Box>
        )}
      </Box>
    </Container>
  );
}

export default App;