#!/usr/bin/env node
const fs = require("fs");
const http = require("http");
const path = require("path");

const args = process.argv.slice(2);
const providedPortIndex = args.findIndex(
  (arg) => arg === "--port" || arg === "-p"
);
const requestedPort =
  providedPortIndex >= 0 && args[providedPortIndex + 1]
    ? Number(args[providedPortIndex + 1])
    : Number(process.env.PORT || 4173);
const port =
  Number.isFinite(requestedPort) && requestedPort > 0 ? requestedPort : 4173;
const contentRoot = path.resolve(__dirname, "src");
const assetsRoot = path.resolve(__dirname, "../assets/files");
const assetsBaseUrl =
  process.env.ASSETS_BASE_URL || `http://localhost:${port}/assets`;
const envName = process.env.ENV_NAME || "local";

const MIME_TYPES = {
  ".html": "text/html",
  ".js": "application/javascript",
  ".css": "text/css",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
};

const TEXT_EXTENSIONS = new Set([".html", ".js", ".css", ".json", ".svg"]);

const placeholderValues = {
  ASSETS_BASE_URL: assetsBaseUrl,
  ENV_NAME: envName,
};

function isPathInsideBase(base, target) {
  const relative = path.relative(base, target);
  return !relative.startsWith("..") && !path.isAbsolute(relative);
}

function replacePlaceholders(content) {
  let next = content;
  for (const [key, value] of Object.entries(placeholderValues)) {
    next = next.replaceAll(key, value);
  }
  return next;
}

async function fileExists(filePath) {
  try {
    const stats = await fs.promises.stat(filePath);
    return stats.isFile();
  } catch (error) {
    return false;
  }
}

async function serveFile(res, absolutePath, shouldReplace) {
  const ext = path.extname(absolutePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || "application/octet-stream";
  try {
    if (shouldReplace) {
      const raw = await fs.promises.readFile(absolutePath, "utf8");
      const content = replacePlaceholders(raw);
      res.writeHead(200, { "Content-Type": contentType });
      res.end(content);
      return;
    }

    const buffer = await fs.promises.readFile(absolutePath);
    res.writeHead(200, { "Content-Type": contentType });
    res.end(buffer);
  } catch (error) {
    res.writeHead(500, { "Content-Type": "text/plain" });
    res.end("Internal server error");
  }
}

async function serveAsset(res, pathname) {
  const assetPath = path.join(assetsRoot, pathname.replace("/assets", ""));
  const normalized = path.normalize(assetPath);
  if (
    !isPathInsideBase(assetsRoot, normalized) ||
    !(await fileExists(normalized))
  ) {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not found");
    return;
  }
  const ext = path.extname(normalized).toLowerCase();
  await serveFile(res, normalized, TEXT_EXTENSIONS.has(ext));
}

async function serveContent(res, pathname) {
  const targetPath = path.join(contentRoot, pathname);
  const normalized = path.normalize(targetPath);
  const hasExtension = path.extname(pathname) !== "";

  if (!isPathInsideBase(contentRoot, normalized)) {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not found");
    return;
  }

  if (hasExtension) {
    if (await fileExists(normalized)) {
      const ext = path.extname(normalized).toLowerCase();
      await serveFile(res, normalized, TEXT_EXTENSIONS.has(ext));
      return;
    }

    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not found");
    return;
  }

  const fallback = path.join(contentRoot, "index.html");
  await serveFile(res, fallback, true);
}

const server = http.createServer(async (req, res) => {
  const { pathname } = new URL(req.url, `http://localhost:${port}`);

  if (pathname.startsWith("/assets")) {
    await serveAsset(res, pathname);
    return;
  }

  await serveContent(res, decodeURIComponent(pathname));
});

server.listen(port, () => {
  console.log(`Games dev server running at http://localhost:${port}`);
  console.log(`Serving content from: ${contentRoot}`);
  console.log(`Assets base URL: ${assetsBaseUrl}`);
  console.log(`Environment name: ${envName}`);
});
