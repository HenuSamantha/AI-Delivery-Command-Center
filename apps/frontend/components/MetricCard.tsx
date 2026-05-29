type MetricCardProps = {
    title: string;
    value: string;
    color?: string;
  };
  
  export default function MetricCard({
    title,
    value,
    color = "text-white",
  }: MetricCardProps) {
    return (
      <div className="bg-gray-900 p-6 rounded-2xl border border-gray-800 h-64">
        <h2 className="text-lg font-semibold mb-2">
          {title}
        </h2>
  
        <p className={`text-3xl font-bold ${color}`}>
          {value}
        </p>
      </div>
    );
  }