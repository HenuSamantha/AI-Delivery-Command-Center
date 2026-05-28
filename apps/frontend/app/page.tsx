"use client";

import { useState } from "react";

export default function HomePage() {

  const [updates, setUpdates] = useState("");
  const [summary, setSummary] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const generateSummary = async () => {

    setLoading(true);

    try {

      const response = await fetch("http://localhost:8000/generate-summary", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          updates,
        }),
      });

      const data = await response.json();

      setSummary(data);

    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-gray-950 text-white p-8">
      <div className="max-w-5xl mx-auto">

        <h1 className="text-5xl font-bold mb-2">
          AI Delivery Command Center
        </h1>

        <p className="text-gray-400 mb-8">
          AI-powered sprint reporting and delivery insights
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">

          <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800">
            <h2 className="text-lg font-semibold mb-2">Sprint Health</h2>
            <p className="text-3xl font-bold text-green-400">92%</p>
          </div>

          <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800">
            <h2 className="text-lg font-semibold mb-2">Open Risks</h2>
            <p className="text-3xl font-bold text-yellow-400">3</p>
          </div>

          <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800">
            <h2 className="text-lg font-semibold mb-2">Blocked Tickets</h2>
            <p className="text-3xl font-bold text-red-400">5</p>
          </div>

        </div>

        <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800 mb-8">

          <h2 className="text-2xl font-semibold mb-4">
            AI Sprint Summary
          </h2>

          <textarea
            value={updates}
            onChange={(e) => setUpdates(e.target.value)}
            className="w-full h-40 bg-gray-950 border border-gray-700 rounded-xl p-4 mb-4"
            placeholder="Paste sprint updates here..."
          />

          <button
            onClick={generateSummary}
            className="bg-blue-600 hover:bg-blue-500 px-6 py-3 rounded-xl font-semibold"
          >
            {loading ? "Generating..." : "Generate Summary"}
          </button>

        </div>

        {summary && (
          <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800">

            <h2 className="text-2xl font-semibold mb-4">
              AI Analysis
            </h2>

            <p className="mb-6 text-gray-300">
              {summary.executive_summary}
            </p>

            <div className="mb-4">
              <h3 className="font-semibold text-red-400 mb-2">
                Blockers
              </h3>

              <ul className="list-disc list-inside text-gray-300">
                {summary.blockers.map((item: string, index: number) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>

            <div className="mb-4">
              <h3 className="font-semibold text-yellow-400 mb-2">
                Risks
              </h3>

              <ul className="list-disc list-inside text-gray-300">
                {summary.risks.map((item: string, index: number) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>

            <div>
              <h3 className="font-semibold text-green-400 mb-2">
                Action Items
              </h3>

              <ul className="list-disc list-inside text-gray-300">
                {summary.action_items.map((item: string, index: number) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>

          </div>
        )}

      </div>
    </main>
  );
}