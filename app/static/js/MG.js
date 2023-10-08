var nt = 1000; // Number of time steps
var dt = 0.1; // Time step size
var tdelay = 2; // Time delay
var x = []; // Array to store x(t) values
var xd = []; // Array to store x(t - tdelay) values
var xd2 = []; // Array to store x(t - 2 * tdelay) values
var n = 9.65;
var g = 1;
var B = 10;

// Initial condition: x(0) = 0
x[0] = 0.5;
for (var i = 1; i < tdelay / dt + 1; i++) {
    x[i] = 0.5;
}

function compute() {
    for (var i = tdelay / dt; i < nt; i++) {
        var idelay = i - tdelay / dt; // Calculate delayed index
        
        // Compute x'(t) using the given differential equation
        var dx = (B * x[idelay]) / (1 + Math.pow(x[idelay], n)) - g * x[i - 1];
        
        // Use Euler method to update x(t) based on x'(t)
        x[i] = x[i - 1] + dx * dt;
    }
}

compute();

for (var i = 1; i < nt - tdelay / dt; i++) {
    xd[i] = x[i + tdelay / dt];
}
for (var i = 1; i < nt - 2 * (tdelay / dt); i++) {
    xd2[i] = x[i + 2 * (tdelay / dt)];
}

Plotly.newPlot('MG', [{
    x: x,
    y: xd,
    z: xd2,
    mode: 'markers',
    marker: {
		size: 2,
    },
    type: 'scatter3d',
}], {
    xaxis: {
        range: [-5, 5],
        showticklabels: false,
        zeroline: false
    },
    yaxis: {
        range: [-5, 5],
        showticklabels: false,
        zeroline: false
    },
    zaxis: {
        range: [-5, 5],
        showticklabels: false,
        zeroline: false
    },
    plot_bgcolor: '#F3F4F6',
    paper_bgcolor: '#F3F4F6',
})
/*
function update() {
    compute();

    Plotly.animate('MG', {
        data: [{
            x: x,
            y: v,
        }]
    }, {
        transition: {
            duration: 0
        },
        frame: {
            duration: 0,
            redraw: false
        }
    });

    requestAnimationFrame(update);
}

requestAnimationFrame(update);
*/