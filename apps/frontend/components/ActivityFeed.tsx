const activities = [
  "10:42 AM • QA blocker detected",
  "10:40 AM • Sprint summary generated",
  "10:35 AM • Release risk identified",
  "10:28 AM • Stakeholder approval pending",
];
  
  export default function ActivityFeed() {
    return (
      <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800 mb-8">
        <h2 className="text-2xl font-semibold mb-4">Recent Activity</h2>
  
        <div className="space-y-3">
          {activities.map((activity, index) => (
            <div
              key={index}
              className="flex items-center gap-3 text-gray-300"
            >
              <span className="h-2 w-2 rounded-full bg-blue-400" />
              <span>{activity}</span>
            </div>
          ))}
        </div>
      </div>
    );
  }