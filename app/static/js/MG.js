const MGnt = 1000; // Number of time steps
const MGdt = 0.1; // Time step size
const MGtdelay = 2; // Time delay
const MGx = []; // Array to store x(t) values
const MGxd = []; // Array to store x(t - tdelay) values
const MGxd2 = []; // Array to store x(t - 2 * tdelay) values
const MGn = 9.65;
const MGg = 1;
const MGB = 10;

// Initial condition: x(0) = 0
MGx[0] = 0.5;
for (let i = 1; i < MGtdelay / MGdt + 1; i++) {
  MGx[i] = 0.5;
}

/**
 * Compute the next step of the Mackey-Glass attractor
 */
function computeMG() {
  for (let i = MGtdelay / MGdt; i < MGnt; i++) {
    const idelay = i - MGtdelay / MGdt; // Calculate delayed index

    // Compute x'(t) using the given differential equation
    const frac = (MGB * MGx[idelay]) / (1 + Math.pow(MGx[idelay], MGn));
    const dx = frac - MGg * MGx[i - 1];

    // Use Euler method to update x(t) based on x'(t)
    MGx[i] = MGx[i - 1] + dx * MGdt;
  }
}

computeMG();

for (let i = 1; i < MGnt - MGtdelay / MGdt; i++) {
  MGxd[i] = MGx[i + MGtdelay / MGdt];
}
for (let i = 1; i < MGnt - 2 * (MGtdelay / MGdt); i++) {
  MGxd2[i] = MGx[i + 2 * (MGtdelay / MGdt)];
}

Plotly.newPlot('MG', [{
  x: MGx,
  y: MGxd,
  z: MGxd2,
  mode: 'markers',
  marker: {
    size: 2,
  },
  type: 'scatter3d',
}], {
  xaxis: {
    range: [-5, 5],
    showticklabels: false,
    zeroline: false,
  },
  yaxis: {
    range: [-5, 5],
    showticklabels: false,
    zeroline: false,
  },
  zaxis: {
    range: [-5, 5],
    showticklabels: false,
    zeroline: false,
  },
  plot_bgcolor: '#F3F4F6',
  paper_bgcolor: '#F3F4F6',
});
