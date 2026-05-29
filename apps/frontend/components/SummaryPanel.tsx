type SummaryPanelProps = {
    summary: {
      executive_summary: string;
      blockers: string[];
      risks: string[];
      action_items: string[];
    };
  };
  
  function InsightCard({
    title,
    items,
    color,
  }: {
    title: string;
    items: string[];
    color: string;
  }) {
    return (
      <div className="bg-gray-950 p-5 rounded-xl border border-gray-800">
        <h3 className={`font-semibold mb-3 ${color}`}>
          {title}
        </h3>
  
        {items.length > 0 ? (
          <ul className="space-y-2 text-gray-300">
            {items.map((item, index) => (
              <li key={index}>• {item}</li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500">No items detected</p>
        )}
      </div>
    );
  }
  
  export default function SummaryPanel({ summary }: SummaryPanelProps) {
    return (
      <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800">
        <h2 className="text-2xl font-semibold mb-4">
          AI Analysis
        </h2>
  
        <div className="bg-gray-950 p-5 rounded-xl border border-gray-800 mb-6">
          <h3 className="font-semibold text-blue-400 mb-3">
            Executive Summary
          </h3>
  
          <p className="text-gray-300 whitespace-pre-line">
            {summary.executive_summary}
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <InsightCard
            title="Blockers"
            items={summary.blockers}
            color="text-red-400"
          />
  
          <InsightCard
            title="Risks"
            items={summary.risks}
            color="text-yellow-400"
          />
  
          <InsightCard
            title="Action Items"
            items={summary.action_items}
            color="text-green-400"
          />
        </div>
      </div>
    );
  }