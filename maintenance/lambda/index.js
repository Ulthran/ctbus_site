exports.handler = async function () {
  const body = `
    <!DOCTYPE html>
    <html>
      <head>
        <title>Maintenance</title>
      </head>
      <body>
        <h1>Maintenance in progress</h1>
      </body>
    </html>
  `;
  return {
    statusCode: 200,
    headers: { "Content-Type": "text/html" },
    body,
  };
};
