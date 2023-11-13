const n = 100;
const x = [];
const y = [];
const z = [];
const x2 = [];
const y2 = [];
const z2 = [];
const x3 = [];
const y3 = [];
const z3 = [];
const dt = 0.015;

for (let i = 0; i < n; i++) {
  x[i] = Math.random() * 2 - 15;
  y[i] = Math.random() * 2 - 15;
  z[i] = 30 + Math.random() * 10;

  x2[i] = Math.random() * 2 + 13;
  y2[i] = Math.random() * 2 + 13;
  z2[i] = 30 + Math.random() * 10;

  x3[i] = x2[i];
  y3[i] = y2[i];
  z3[i] = z2[i];
}

Plotly.newPlot('Lorenz_unlinked_2', [{
  x: [x3[0]],
  y: [z3[0]],
  mode: 'markers',
  marker: {color: '#FF0000', size: 10},
}, {
  x: x3.slice(1),
  y: z3.slice(1),
  mode: 'markers',
  marker: {color: '#0000FF', size: 3},
}], {
  title: {
    text: 'Unlinked Lorenz Attractor #2',
    font: {
      size: 18,
    },
  },
  xaxis: {
    range: [-60, 60],
    showticklabels: false,
    zeroline: false,
  },
  yaxis: {
    range: [0, 60],
    showticklabels: false,
    zeroline: false,
  },
  plot_bgcolor: '#F3F4F6',
  paper_bgcolor: '#F3F4F6',
  showlegend: false,
}, {responsive: true});

Plotly.newPlot('Lorenz', [{
  x: [x[0]],
  y: [z[0]],
  mode: 'markers',
  marker: {color: '#FF0000', size: 10},
}, {
  x: x.slice(1),
  y: z.slice(1),
  mode: 'markers',
  marker: {color: '#0000FF', size: 3},
}], {
  title: {
    text: 'Lorenz Attractor #1',
    font: {
      size: 18,
    },
  },
  xaxis: {
    range: [-40, 40],
    showticklabels: false,
    zeroline: false,
  },
  yaxis: {
    range: [0, 60],
    showticklabels: false,
    zeroline: false,
  },
  plot_bgcolor: '#F3F4F6',
  paper_bgcolor: '#F3F4F6',
  showlegend: false,
}, {responsive: true});

Plotly.newPlot('Lorenz2', [{
  x: [x2[0]],
  y: [z2[0]],
  mode: 'markers',
  marker: {color: '#FF0000', size: 10},
}, {
  x: x2.slice(1),
  y: z2.slice(1),
  mode: 'markers',
  marker: {color: '#0000FF', size: 3},
}], {
  title: {
    text: 'Linked Lorenz Attractor #2',
    font: {
      size: 18,
    },
  },
  xaxis: {
    range: [-60, 60],
    showticklabels: false,
    zeroline: false,
  },
  yaxis: {
    range: [0, 60],
    showticklabels: false,
    zeroline: false,
  },
  plot_bgcolor: '#F3F4F6',
  paper_bgcolor: '#F3F4F6',
  showlegend: false,
}, {responsive: true});

/**
 * Compute the next step of the Lorenz attractor
 */
function compute() {
  const s = 10;
  const b = 8 / 3;
  const r = 28;
  let dx; let dy; let dz;
  let xh; let yh; let zh;
  for (let i = 0; i < n; i++) {
    dx = s * (y[i] - x[i]);
    dy = x[i] * (r - z[i]) - y[i];
    dz = x[i] * y[i] - b * z[i];

    xh = x[i] + dx * dt * 0.5;
    yh = y[i] + dy * dt * 0.5;
    zh = z[i] + dz * dt * 0.5;

    dx = s * (yh - xh);
    dy = xh * (r - zh) - yh;
    dz = xh * yh - b * zh;

    x[i] += dx * dt;
    y[i] += dy * dt;
    z[i] += dz * dt;
  }
}

/**
 * Compute the next step of the Lorenz attractor 2
 */
function compute2() {
  const s = 10;
  const b = 8 / 3;
  const r = 28;
  let dx; let dy; let dz;
  let xh; let yh; let zh;
  for (let i = 0; i < n; i++) {
    dx = s * (y2[i] - x2[i]);
    dy = x2[i] * (r - z2[i]) - y2[i];
    dz = x2[i] * y2[i] - b * z2[i];

    xh = x2[i] + dx * dt * 0.5;
    yh = y2[i] + dy * dt * 0.5;
    zh = z2[i] + dz * dt * 0.5;

    dx = s * (yh - xh);
    dy = xh * (r - zh) - yh;
    dz = xh * yh - b * zh;

    x2[i] += dx * dt;
    const couplingConst = 0.03;
    y2[i] = (1 - couplingConst) * (y2[i] + dy * dt) + couplingConst * y[i];
    z2[i] += dz * dt;
  }
}

/**
 * Compute the next step of the Lorenz attractor 3
 */
function compute3() {
  const s = 10;
  const b = 8 / 3;
  const r = 28;
  let dx; let dy; let dz;
  let xh; let yh; let zh;
  for (let i = 0; i < n; i++) {
    dx = s * (y3[i] - x3[i]);
    dy = x3[i] * (r - z3[i]) - y3[i];
    dz = x3[i] * y3[i] - b * z3[i];

    xh = x3[i] + dx * dt * 0.5;
    yh = y3[i] + dy * dt * 0.5;
    zh = z3[i] + dz * dt * 0.5;

    dx = s * (yh - xh);
    dy = xh * (r - zh) - yh;
    dz = xh * yh - b * zh;

    x3[i] += dx * dt;
    y3[i] += dy * dt;
    z3[i] += dz * dt;
  }
}

/**
 * Update Lorenz attractor simulations
 */
function update() {
  compute();
  compute2();
  compute3();

  Plotly.animate('Lorenz_unlinked_2', {
    data: [{
      x: [x3[0]],
      y: [z3[0]],
    }, {
      x: x3.slice(1),
      y: z3.slice(1),
    }],
  }, {
    transition: {
      duration: 0,
    },
    frame: {
      duration: 0,
      redraw: false,
    },
  });

  Plotly.animate('Lorenz', {
    data: [{
      x: [x[0]],
      y: [z[0]],
    }, {
      x: x.slice(1),
      y: z.slice(1),
    }],
  }, {
    transition: {
      duration: 0,
    },
    frame: {
      duration: 0,
      redraw: false,
    },
  });

  Plotly.animate('Lorenz2', {
    data: [{
      x: [x2[0]],
      y: [z2[0]],
    }, {
      x: x2.slice(1),
      y: z2.slice(1),
    }],
  }, {
    transition: {
      duration: 0,
    },
    frame: {
      duration: 0,
      redraw: false,
    },
  });

  requestAnimationFrame(update);
}

requestAnimationFrame(update);
