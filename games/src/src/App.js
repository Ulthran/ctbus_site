const { useState } = React;

const styles = {
  page: {
    fontFamily: "Inter, system-ui, -apple-system, sans-serif",
    margin: 0,
    padding: "32px 24px",
    minHeight: "100vh",
    background: "linear-gradient(135deg, #0a101f 0%, #0f162a 50%, #1b1f3a 100%)",
    color: "#f5f7fb",
  },
  hero: {
    textAlign: "center",
    marginBottom: 32,
  },
  env: {
    display: "inline-block",
    padding: "4px 10px",
    borderRadius: 999,
    backgroundColor: "rgba(255,255,255,0.08)",
    fontSize: 12,
    letterSpacing: 0.4,
    color: "#c5c9d6",
    marginBottom: 10,
  },
  title: {
    fontSize: 40,
    margin: "0 0 8px",
    letterSpacing: -0.5,
  },
  subtitle: {
    margin: 0,
    color: "#d1d5e2",
    maxWidth: 520,
    display: "inline-block",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
    gap: 16,
    marginTop: 24,
  },
  card: {
    backgroundColor: "rgba(255,255,255,0.06)",
    borderRadius: 16,
    padding: 16,
    boxShadow: "0 10px 25px rgba(0,0,0,0.25)",
    border: "1px solid rgba(255,255,255,0.08)",
  },
  cardTitle: {
    margin: "0 0 6px",
    fontSize: 18,
  },
  cardCopy: {
    margin: 0,
    color: "#c5c9d6",
  },
};

function GameCard({ title, description }) {
  const h = React.createElement;

  return h(
    "div",
    { style: styles.card },
    h("h2", { style: styles.cardTitle }, title),
    h("p", { style: styles.cardCopy }, description)
  );
}

export function App() {
  const h = React.createElement;
  const [games] = useState([
    { title: "Guess the Number", description: "A quick number guessing warm-up game." },
    { title: "Tile Taps", description: "Tap as many tiles as you can before the timer runs out." },
    { title: "Pathfinder", description: "Find a route across the grid without hitting any traps." },
  ]);

  return h(
    "main",
    { style: styles.page },
    h(
      "header",
      { style: styles.hero },
      h("p", { style: styles.env }, "Environment: ENV_NAME"),
      h("h1", { style: styles.title }, "CTBus Games"),
      h(
        "p",
        { style: styles.subtitle },
        "Small experiments and playgrounds for browser-based games."
      )
    ),
    h(
      "section",
      { style: styles.grid },
      games.map((game) =>
        h(GameCard, {
          key: game.title,
          title: game.title,
          description: game.description,
        })
      )
    )
  );
}
