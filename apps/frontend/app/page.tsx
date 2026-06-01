"use client";
import MetricCard from "../components/MetricCard";
import ActivityFeed from "../components/ActivityFeed";
import ReleaseStatus from "../components/ReleaseStatus";
import SummaryPanel from "../components/SummaryPanel";
import ExecutiveRecommendation from "../components/ExecutiveRecommendation";
import { useState, useEffect } from "react";
import ConnectedSources from "../components/ConnectedSources";


export default function HomePage() {

  const [updates, setUpdates] = useState("");
  const [summary, setSummary] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [deliveryContext, setDeliveryContext] = useState<any>(null);
  
  useEffect(() => {
    fetch("http://127.0.0.1:8000/delivery-context")
      .then((res) => res.json())
      .then((data) => setDeliveryContext(data));
  }, []);

  const blockedCount = deliveryContext
  ? deliveryContext.jira_tickets.filter(
      (ticket: any) => ticket.status === "Blocked"
    ).length
  : 0;

const riskCount = deliveryContext
  ? deliveryContext.jira_tickets.filter(
      (ticket: any) =>
        ticket.status === "Blocked" ||
        ticket.status === "In Progress"
    ).length
  : 0;

  const generateSummary = async () => {

    setLoading(true);

    try {

      const response = await fetch("http://127.0.0.1:8000/generate-summary", {
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

        <div className="grid grid-cols-1 md:grid-cols-5 gap-6 mb-8">

        <MetricCard
          title="Sprint Health"
          value={summary ? `${summary.delivery_health_score}%` : "92%"}
          color="text-green-400"
         />

       <MetricCard
        title="Open Risks"
        value={riskCount.toString()}
        color="text-yellow-400"
        />

      <MetricCard
        title="Blocked"
        value={blockedCount.toString()}
        color="text-red-400"
        />
      
      <MetricCard
        title="AI Confidence"
        value={summary ? `${summary.ai_confidence}%` : "87%"}
        color="text-blue-400"
        />

     <ReleaseStatus
        status={summary ? summary.release_readiness : "At Risk"}
      />
        </div>
		
        {deliveryContext && (
  <ConnectedSources
    jiraTickets={deliveryContext.jira_tickets}
    slackMessages={deliveryContext.slack_messages}
  />
)}

      <ActivityFeed
        activities={
          summary
            ? [
                "AI summary generated",
                `${summary.blockers.length} blockers identified`,
                `${summary.risks.length} risks detected`,
                `Release status: ${summary.release_readiness}`,
              ]
            : [
                "Waiting for sprint analysis...",
              ]
  }
/>
    
    {summary && (
      <ExecutiveRecommendation
        recommendation={summary.executive_recommendation}
      />
    )}

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

        {summary && <SummaryPanel summary={summary} />}

      </div>
    </main>
  );
}