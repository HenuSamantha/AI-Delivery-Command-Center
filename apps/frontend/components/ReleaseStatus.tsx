interface ReleaseStatusProps {
  status: string;
}

export default function ReleaseStatus({
  status,
}: ReleaseStatusProps) {

    return (
      <div className="bg-gray-900 p-6 rounded-2xl border-2 border-yellow-500 h-64">
        <h2 className="text-lg font-semibold mb-2">
          Release Status
        </h2>
  
        <div className="flex items-center gap-3">
          <div className="w-4 h-4 rounded-full bg-yellow-400"></div>
  
          <span className="text-2xl font-bold text-yellow-400 whitespace-nowrap">
            {status}
          </span>
        </div>
      </div>
    );
  }