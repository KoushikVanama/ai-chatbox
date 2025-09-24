import { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [resp, setResp] = useState("");

  async function sendPrompt() {
    const r = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });
    const j = await r.json();
    setResp(j.text);
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h1>AI Chatbox Demo</h1>
      <textarea rows="4" cols="50"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <br />
      <button onClick={sendPrompt}>Send</button>
      <h3>Response:</h3>
      <pre>{resp}</pre>
    </div>
  );
}

export default App;
