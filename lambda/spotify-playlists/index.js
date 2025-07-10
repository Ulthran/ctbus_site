const CLIENT_ID = process.env.SPOTIFY_CLIENT_ID;
const CLIENT_SECRET = process.env.SPOTIFY_CLIENT_SECRET;

exports.handler = async function () {
  try {
    const tokenRes = await fetch("https://accounts.spotify.com/api/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization:
          "Basic " +
          Buffer.from(`${CLIENT_ID}:${CLIENT_SECRET}`).toString("base64"),
      },
      body: "grant_type=client_credentials",
    });
    const tokenData = await tokenRes.json();
    const token = tokenData.access_token;

    let url =
      "https://api.spotify.com/v1/users/charlie_bushman/playlists?limit=50";
    const playlists = [];
    while (url) {
      const res = await fetch(url, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await res.json();
      playlists.push(...(data.items || []).filter(Boolean));
      url = data.next;
    }

    const regex = /[A-Z][a-z]{2} ['‘]\d{2}/;
    const months = [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ];
    const filtered = playlists
      .filter((p) => regex.test(p.name))
      .map((p) => ({ ...p, name: p.name.replace("‘", "'") }));

    filtered.sort((a, b) => {
      const aYear = parseInt(a.name.slice(-2));
      const bYear = parseInt(b.name.slice(-2));
      if (aYear !== bYear) return bYear - aYear;
      const aMonth = months.indexOf(a.name.slice(0, 3));
      const bMonth = months.indexOf(b.name.slice(0, 3));
      return bMonth - aMonth;
    });

    const result = filtered.map((p) => ({
      name: p.name,
      url: p.external_urls?.spotify || "#",
      image: (p.images && p.images[2] && p.images[2].url) || "#",
    }));

    return {
      statusCode: 200,
      headers: { "Access-Control-Allow-Origin": "*" },
      body: JSON.stringify(result),
    };
  } catch (e) {
    console.error("Failed to fetch playlists", e);
    return { statusCode: 500, body: "error" };
  }
};
