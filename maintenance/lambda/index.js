exports.handler = async function () {
  const body = `
    <!DOCTYPE html>
    <html>
      <head>
        <title>Maintenance</title>
      </head>
      <body>
        <h1 style="text-align: center; padding: 20px;">Maintenance in progress</h1>
        <p style="text-align: center;">I'm playing around with the domain configuration. Please check back later!</p>
      </body>
    </html>
  `;
  return {
    statusCode: 200,
    headers: { "Content-Type": "text/html" },
    body,
  };
};
