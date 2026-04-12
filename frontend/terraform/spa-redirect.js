// eslint-disable-next-line no-unused-vars
function handler(event) {
  var request = event.request;
  var uri = request.uri;
  if (!uri.includes(".")) {
    request.uri = "/index.html";
  }
  return request;
}
