type ActivityFeedProps = {
  activities: string[];
};

export default function ActivityFeed({
  activities,
}: ActivityFeedProps) {
  return (
    <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800 mb-8">
      <h2 className="text-2xl font-semibold mb-4">
        Recent Activity
      </h2>

      <div className="space-y-3">
        {activities.map((activity, index) => (
          <div
            key={index}
            className="text-gray-300"
          >
            • {activity}
          </div>
        ))}
      </div>
    </div>
  );
}