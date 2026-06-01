type ExecutiveRecommendationProps = {
    recommendation: string;
  };
  
  export default function ExecutiveRecommendation({
    recommendation,
  }: ExecutiveRecommendationProps) {
    return (
      <div className="bg-gray-900 p-6 rounded-2xl border border-blue-500 mb-8">
        <h2 className="text-2xl font-semibold mb-3">
          Executive Recommendation
        </h2>
  
        <p className="text-gray-300">
          {recommendation}
        </p>
      </div>
    );
  }