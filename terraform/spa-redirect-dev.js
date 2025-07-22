const PREFIX = "/dev";
function handler(event) {
  var request = event.request;
  var uri = request.uri;
  if (!uri.startsWith("/assets/")) {
    if (!uri.includes(".")) {
      request.uri = `${PREFIX}/index.html`;
    } else {
      request.uri = PREFIX + uri;
    }
  }
  return request;
}
